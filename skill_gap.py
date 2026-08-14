CAREER_SKILLS = {

    "AI / ML Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "SQL",
        "Statistics"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Pandas",
        "Excel",
        "Power BI",
        "Statistics"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git"
    ],

    "Software Developer": [
        "Python",
        "Java",
        "SQL",
        "Git",
        "Data Structures"
    ]
}


def find_missing_skills(
    current_skills,
    career
):

    required = CAREER_SKILLS.get(
        career,
        []
    )

    current = [
        skill.lower()
        for skill in current_skills
    ]

    missing = []

    matched = []

    for skill in required:

        if skill.lower() in current:

            matched.append(skill)

        else:

            missing.append(skill)

    return matched, missing


def get_required_skills(career):

    return CAREER_SKILLS.get(
        career,
        []
    )