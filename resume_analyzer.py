import PyPDF2
import requests
import json
import re


# =========================================================
# PDF TEXT EXTRACTION
# =========================================================

def extract_text(uploaded_file):
    """
    Extract text from an uploaded PDF resume.
    """

    text = ""

    try:
        reader = PyPDF2.PdfReader(uploaded_file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print("PDF extraction error:", e)

    return text


# =========================================================
# AI SKILL EXTRACTION USING OLLAMA
# =========================================================

def extract_skills_with_ai(text):
    """
    Extract skills from resume using Ollama Llama 3.1.
    If Ollama is unavailable, fallback detection is used.
    """

    if not text or not text.strip():
        return []

    prompt = f"""
You are an expert resume analyzer.

Read the following resume carefully.

Identify ALL technical skills, software skills,
programming languages, frameworks, libraries,
tools, databases, platforms and professional skills
explicitly mentioned in the resume.

Do NOT invent skills.

Return ONLY valid JSON in this format:

{{
    "skills": [
        "Python",
        "SQL",
        "Git"
    ]
}}

Resume:

{text}
"""

    try:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.1",
                "prompt": prompt,
                "stream": False,
                "format": "json"
            },
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        ai_text = result.get(
            "response",
            ""
        )

        if not ai_text:
            raise ValueError("Empty response from Ollama")

        data = json.loads(ai_text)

        skills = data.get(
            "skills",
            []
        )

        # Clean skills
        cleaned_skills = []

        for skill in skills:

            if not isinstance(
                skill,
                str
            ):
                continue

            skill = skill.strip()

            if skill and skill not in cleaned_skills:

                cleaned_skills.append(
                    skill
                )

        return cleaned_skills

    except Exception as e:

        print(
            "AI skill extraction error:",
            e
        )

        # Use fallback detection
        return fallback_skill_detection(text)


# =========================================================
# FALLBACK SKILL DETECTION
# =========================================================

def fallback_skill_detection(text):
    """
    Used when Ollama is unavailable or AI extraction fails.
    """

    known_skills = [

        # Programming Languages
        "Python",
        "Java",
        "C",
        "C++",
        "C#",
        "JavaScript",
        "TypeScript",
        "PHP",
        "R",

        # Web Development
        "HTML",
        "CSS",
        "React",
        "Angular",
        "Vue",
        "Node.js",
        "Express",
        "Django",
        "Flask",
        "FastAPI",

        # Databases
        "SQL",
        "MySQL",
        "MongoDB",
        "PostgreSQL",
        "SQLite",
        "Oracle",

        # AI / ML
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing",
        "NLP",
        "Computer Vision",
        "Generative AI",

        # Python Libraries
        "Pandas",
        "NumPy",
        "Matplotlib",
        "Seaborn",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
        "Keras",
        "OpenCV",

        # Tools
        "Git",
        "GitHub",
        "Docker",
        "Postman",
        "Jupyter",
        "Streamlit",

        # Cloud
        "AWS",
        "Azure",
        "Google Cloud",

        # Data / BI
        "Excel",
        "Power BI",
        "Tableau",

        # APIs
        "REST API",
        "API",

        # Marketing / Other
        "SEO",
        "Digital Marketing",
        "Google Ads",
        "Canva",
        "WordPress",

        # Professional Skills
        "Communication",
        "Leadership",
        "Teamwork",
        "Problem Solving",
        "Critical Thinking",
        "Time Management"
    ]

    text_lower = text.lower()

    detected = []

    for skill in known_skills:

        pattern = re.escape(
            skill.lower()
        )

        if re.search(
            r"(?<!\w)"
            + pattern +
            r"(?!\w)",
            text_lower
        ):

            detected.append(
                skill
            )

    return detected


# =========================================================
# MAIN SKILL DETECTION FUNCTION
# =========================================================

def find_skills(text):
    """
    Main function used by app.py.

    First tries AI-based skill extraction.
    If AI is unavailable, fallback detection is used.
    """

    return extract_skills_with_ai(text)