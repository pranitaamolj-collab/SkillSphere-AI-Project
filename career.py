def recommend_career(skills):

    skills_lower = [
        skill.lower()
        for skill in skills
    ]

    careers = []

    if any(
        skill in skills_lower
        for skill in [
            "python",
            "machine learning",
            "tensorflow",
            "pandas",
            "numpy"
        ]
    ):

        careers.append("AI / ML Engineer")


    if any(
        skill in skills_lower
        for skill in [
            "sql",
            "excel",
            "power bi",
            "pandas"
        ]
    ):

        careers.append("Data Analyst")


    if any(
        skill in skills_lower
        for skill in [
            "html",
            "css",
            "javascript",
            "react"
        ]
    ):

        careers.append("Web Developer")


    if any(
        skill in skills_lower
        for skill in [
            "java",
            "python",
            "c++"
        ]
    ):

        careers.append("Software Developer")


    if not careers:

        careers.append("Software Developer")


    return careers