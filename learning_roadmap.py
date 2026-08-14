def get_learning_roadmap(missing_skills):

    roadmap_data = {

        "Git": {
            "level": "Beginner",
            "reason": "Git helps you manage code versions.",
            "practice": "Learn add, commit, push, pull and GitHub."
        },

        "Pandas": {
            "level": "Beginner",
            "reason": "Pandas is useful for data analysis.",
            "practice": "Practice DataFrames, CSV files and data filtering."
        },

        "NumPy": {
            "level": "Beginner",
            "reason": "NumPy is useful for numerical computing.",
            "practice": "Practice arrays, indexing and mathematical operations."
        },

        "OpenCV": {
            "level": "Intermediate",
            "reason": "OpenCV is useful for computer vision.",
            "practice": "Practice image reading, resizing and edge detection."
        },

        "TensorFlow": {
            "level": "Intermediate",
            "reason": "TensorFlow is useful for deep learning.",
            "practice": "Learn tensors, models, training and evaluation."
        },

        "SQL": {
            "level": "Beginner",
            "reason": "SQL is important for database operations.",
            "practice": "Practice SELECT, WHERE, JOIN and GROUP BY."
        }
    }

    roadmap = []

    for missing_skill in missing_skills:

        skill_name = str(missing_skill).strip()

        details = roadmap_data.get(
            skill_name,
            {
                "level": "Beginner",
                "reason": f"Learning {skill_name} can improve your technical skills.",
                "practice": f"Learn the basics of {skill_name} and build a small project."
            }
        )

        roadmap.append(
            {
                "skill": skill_name,
                "level": details["level"],
                "reason": details["reason"],
                "practice": details["practice"]
            }
        )

    return roadmap