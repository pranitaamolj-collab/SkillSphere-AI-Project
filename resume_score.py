def calculate_resume_score(skills):

    total_possible = 10

    count = len(skills)

    score = int(
        min((count / total_possible) * 100, 100)
    )

    return score