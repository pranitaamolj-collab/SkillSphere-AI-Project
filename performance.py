def get_dashboard_data(skills, missing_skills, careers):

    data = {
        "Detected Skills": len(skills),
        "Missing Skills": len(missing_skills),
        "Career Options": len(careers)
    }

    return data