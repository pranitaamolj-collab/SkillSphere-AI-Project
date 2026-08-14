# import requests
# import json


# OLLAMA_URL = "http://localhost:11434/api/generate"
# MODEL_NAME = "llama3.1"


# def generate_mcqs(skills, number_of_questions=10):

#     if not skills:
#         return []

#     skills_text = ", ".join(skills)

#     prompt = f"""
# You are an expert interview question generator.

# The candidate's resume contains these skills:

# {skills_text}

# Create exactly {number_of_questions} multiple-choice questions.

# IMPORTANT RULES:

# 1. Questions MUST be based ONLY on the skills listed above.
# 2. Do not use unrelated skills.
# 3. Cover different skills from the list.
# 4. Each question must have exactly 4 options.
# 5. Only one option must be correct.
# 6. Questions should be suitable for interview preparation.
# 7. Do not repeat questions.
# 8. Return ONLY JSON.
# 9. Do not add markdown.
# 10. Do not add explanations outside JSON.

# Return exactly this format:

# {{
#     "questions": [
#         {{
#             "skill": "SEO",
#             "question": "What does SEO stand for?",
#             "options": [
#                 "Search Engine Optimization",
#                 "Search Email Operation",
#                 "System Engine Output",
#                 "Search Experience Order"
#             ],
#             "answer": "Search Engine Optimization"
#         }}
#     ]
# }}

# Skills:
# {skills_text}
# """

#     try:

#         response = requests.post(
#             OLLAMA_URL,
#             json={
#                 "model": MODEL_NAME,
#                 "prompt": prompt,
#                 "stream": False,
#                 "format": "json"
#             },
#             timeout=180
#         )

#         # Check HTTP response
#         response.raise_for_status()

#         result = response.json()

#         ai_response = result.get(
#             "response",
#             ""
#         )

#         if not ai_response:

#             print("Ollama returned empty response.")

#             return []

#         print("OLLAMA RESPONSE:")
#         print(ai_response)

#         # Convert JSON
#         data = json.loads(ai_response)

#         questions = data.get(
#             "questions",
#             []
#         )

#         valid_questions = []

#         for question in questions:

#             if not isinstance(
#                 question,
#                 dict
#             ):
#                 continue

#             skill = str(
#                 question.get(
#                     "skill",
#                     ""
#                 )
#             ).strip()

#             question_text = str(
#                 question.get(
#                     "question",
#                     ""
#                 )
#             ).strip()

#             options = question.get(
#                 "options",
#                 []
#             )

#             answer = str(
#                 question.get(
#                     "answer",
#                     ""
#                 )
#             ).strip()

#             # Validate
#             if not skill:
#                 continue

#             if not question_text:
#                 continue

#             if not isinstance(
#                 options,
#                 list
#             ):
#                 continue

#             if len(options) != 4:
#                 continue

#             options = [
#                 str(option).strip()
#                 for option in options
#             ]

#             if answer not in options:
#                 continue

#             valid_questions.append(
#                 {
#                     "skill": skill,
#                     "question": question_text,
#                     "options": options,
#                     "answer": answer
#                 }
#             )

#         return valid_questions

#     except requests.exceptions.ConnectionError:

#         print(
#             "Could not connect to Ollama."
#         )

#         return []

#     except requests.exceptions.Timeout:

#         print(
#             "Ollama request timed out."
#         )

#         return []

#     except json.JSONDecodeError:

#         print(
#             "Ollama did not return valid JSON."
#         )

#         return []

#     except Exception as e:

#         print(
#             "MCQ generation error:",
#             e
#         )

#         return []