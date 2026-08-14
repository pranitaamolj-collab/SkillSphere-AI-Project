import streamlit as st
import random


# =========================================================
# CHECK RESUME
# =========================================================

if not st.session_state.get("resume_uploaded", False):

    st.warning(
        "⚠️ Please upload and analyze your resume first."
    )

    st.stop()


# =========================================================
# PAGE TITLE
# =========================================================

st.title("🎤 AI Interview MCQ Test")

st.write(
    "Your questions are generated according to the "
    "skills detected from your resume."
)

st.divider()


# =========================================================
# GET RESUME SKILLS
# =========================================================

skills = st.session_state.get("skills", [])

user_skills = [
    str(skill).strip().lower()
    for skill in skills
]


if not user_skills:

    st.warning(
        "⚠️ No skills were detected from your resume."
    )

    st.stop()


st.info(
    "🧠 Skills detected from your resume: "
    + ", ".join(skills)
)

st.divider()


# =========================================================
# QUESTION BANK
# =========================================================

QUESTION_BANK = {

    # =====================================================
    # PYTHON
    # =====================================================

    "python": [

        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "A. function",
                "B. def",
                "C. define",
                "D. fun"
            ],
            "answer": "B. def"
        },

        {
            "question": "Which data type is immutable in Python?",
            "options": [
                "A. List",
                "B. Dictionary",
                "C. Tuple",
                "D. Set"
            ],
            "answer": "C. Tuple"
        },

        {
            "question": "Which symbol is used for comments in Python?",
            "options": [
                "A. //",
                "B. #",
                "C. <!-- -->",
                "D. /* */"
            ],
            "answer": "B. #"
        },

        {
            "question": "Which library is commonly used for data analysis in Python?",
            "options": [
                "A. Pandas",
                "B. Flask",
                "C. Tkinter",
                "D. Turtle"
            ],
            "answer": "A. Pandas"
        },

        {
            "question": "Which function is used to display output in Python?",
            "options": [
                "A. display()",
                "B. output()",
                "C. print()",
                "D. show()"
            ],
            "answer": "C. print()"
        },

        {
            "question": "Which keyword is used to create a loop over a sequence?",
            "options": [
                "A. repeat",
                "B. for",
                "C. loop",
                "D. iterate"
            ],
            "answer": "B. for"
        }

    ],


    # =====================================================
    # SQL
    # =====================================================

    "sql": [

        {
            "question": "Which SQL command is used to retrieve data?",
            "options": [
                "A. INSERT",
                "B. SELECT",
                "C. DELETE",
                "D. UPDATE"
            ],
            "answer": "B. SELECT"
        },

        {
            "question": "Which key uniquely identifies each row in a table?",
            "options": [
                "A. Foreign Key",
                "B. Primary Key",
                "C. Normal Key",
                "D. Secondary Key"
            ],
            "answer": "B. Primary Key"
        },

        {
            "question": "Which clause is used to filter records?",
            "options": [
                "A. ORDER BY",
                "B. WHERE",
                "C. GROUP BY",
                "D. SELECT"
            ],
            "answer": "B. WHERE"
        },

        {
            "question": "Which command is used to add new records?",
            "options": [
                "A. ADD",
                "B. INSERT",
                "C. CREATE",
                "D. APPEND"
            ],
            "answer": "B. INSERT"
        },

        {
            "question": "Which command removes a table completely?",
            "options": [
                "A. DELETE",
                "B. REMOVE",
                "C. DROP",
                "D. CLEAR"
            ],
            "answer": "C. DROP"
        },

        {
            "question": "Which function counts the number of records?",
            "options": [
                "A. TOTAL()",
                "B. COUNT()",
                "C. NUMBER()",
                "D. SUM()"
            ],
            "answer": "B. COUNT()"
        }

    ],


    # =====================================================
    # MACHINE LEARNING
    # =====================================================

    "machine learning": [

        {
            "question": "Which is a supervised learning algorithm?",
            "options": [
                "A. Linear Regression",
                "B. K-Means",
                "C. PCA",
                "D. Apriori"
            ],
            "answer": "A. Linear Regression"
        },

        {
            "question": "What is overfitting?",
            "options": [
                "A. Model performs poorly on training data",
                "B. Model memorizes training data",
                "C. Model has no parameters",
                "D. Model has no features"
            ],
            "answer": "B. Model memorizes training data"
        },

        {
            "question": "Which algorithm is commonly used for classification?",
            "options": [
                "A. Logistic Regression",
                "B. K-Means",
                "C. PCA",
                "D. Apriori"
            ],
            "answer": "A. Logistic Regression"
        },

        {
            "question": "Which algorithm is used for clustering?",
            "options": [
                "A. Linear Regression",
                "B. K-Means",
                "C. Logistic Regression",
                "D. Decision Tree"
            ],
            "answer": "B. K-Means"
        },

        {
            "question": "What is the purpose of training data?",
            "options": [
                "A. To train the model",
                "B. To delete the model",
                "C. To create a database",
                "D. To display charts"
            ],
            "answer": "A. To train the model"
        }

    ],


    # =====================================================
    # PANDAS
    # =====================================================

    "pandas": [

        {
            "question": "Which function reads a CSV file in Pandas?",
            "options": [
                "A. pd.open()",
                "B. pd.read_csv()",
                "C. pd.csv()",
                "D. pd.load()"
            ],
            "answer": "B. pd.read_csv()"
        },

        {
            "question": "What is a Pandas DataFrame?",
            "options": [
                "A. A 2D labeled data structure",
                "B. A Python loop",
                "C. A database",
                "D. A machine learning model"
            ],
            "answer": "A. A 2D labeled data structure"
        },

        {
            "question": "Which function displays the first rows of a DataFrame?",
            "options": [
                "A. first()",
                "B. head()",
                "C. top()",
                "D. start()"
            ],
            "answer": "B. head()"
        },

        {
            "question": "Which function is used to remove missing values?",
            "options": [
                "A. remove()",
                "B. delete()",
                "C. dropna()",
                "D. clearna()"
            ],
            "answer": "C. dropna()"
        }

    ],


    # =====================================================
    # NUMPY
    # =====================================================

    "numpy": [

        {
            "question": "What is NumPy mainly used for?",
            "options": [
                "A. Numerical computing",
                "B. Web development",
                "C. Database management",
                "D. UI design"
            ],
            "answer": "A. Numerical computing"
        },

        {
            "question": "Which object is commonly used in NumPy?",
            "options": [
                "A. ndarray",
                "B. DataFrame",
                "C. Cursor",
                "D. Query"
            ],
            "answer": "A. ndarray"
        },

        {
            "question": "Which function creates an array in NumPy?",
            "options": [
                "A. np.array()",
                "B. np.create()",
                "C. np.list()",
                "D. np.make()"
            ],
            "answer": "A. np.array()"
        },

        {
            "question": "Which function creates an array filled with zeros?",
            "options": [
                "A. np.empty()",
                "B. np.zeros()",
                "C. np.null()",
                "D. np.none()"
            ],
            "answer": "B. np.zeros()"
        }

    ],


    # =====================================================
    # POWER BI
    # =====================================================

    "power bi": [

        {
            "question": "What is Power BI mainly used for?",
            "options": [
                "A. Data visualization and business intelligence",
                "B. Video editing",
                "C. Game development",
                "D. Operating systems"
            ],
            "answer": "A. Data visualization and business intelligence"
        },

        {
            "question": "Which language is commonly used for calculations in Power BI?",
            "options": [
                "A. HTML",
                "B. DAX",
                "C. CSS",
                "D. PHP"
            ],
            "answer": "B. DAX"
        },

        {
            "question": "What can a Power BI dashboard contain?",
            "options": [
                "A. Visualizations",
                "B. Only text",
                "C. Only code",
                "D. Only images"
            ],
            "answer": "A. Visualizations"
        },

        {
            "question": "Power BI is developed by which company?",
            "options": [
                "A. Google",
                "B. Microsoft",
                "C. Apple",
                "D. Amazon"
            ],
            "answer": "B. Microsoft"
        }

    ],


    # =====================================================
    # EXCEL
    # =====================================================

    "excel": [

        {
            "question": "Which software is used for spreadsheet analysis?",
            "options": [
                "A. Microsoft Excel",
                "B. Microsoft Paint",
                "C. Notepad",
                "D. PowerPoint"
            ],
            "answer": "A. Microsoft Excel"
        },

        {
            "question": "Which Excel function calculates the average?",
            "options": [
                "A. SUM()",
                "B. COUNT()",
                "C. AVERAGE()",
                "D. TOTAL()"
            ],
            "answer": "C. AVERAGE()"
        },

        {
            "question": "Which Excel function adds numbers?",
            "options": [
                "A. SUM()",
                "B. ADD()",
                "C. PLUS()",
                "D. TOTALS()"
            ],
            "answer": "A. SUM()"
        },

        {
            "question": "What is an Excel cell?",
            "options": [
                "A. Intersection of a row and column",
                "B. A complete worksheet",
                "C. A chart",
                "D. A formula"
            ],
            "answer": "A. Intersection of a row and column"
        }

    ],


    # =====================================================
    # HTML
    # =====================================================

    "html": [

        {
            "question": "What does HTML stand for?",
            "options": [
                "A. Hyper Text Markup Language",
                "B. High Text Machine Language",
                "C. Hyperlink Text Management Language",
                "D. Home Tool Markup Language"
            ],
            "answer": "A. Hyper Text Markup Language"
        },

        {
            "question": "Which tag creates a hyperlink?",
            "options": [
                "A. <p>",
                "B. <a>",
                "C. <h1>",
                "D. <link>"
            ],
            "answer": "B. <a>"
        },

        {
            "question": "Which tag is used for the largest heading?",
            "options": [
                "A. <h6>",
                "B. <heading>",
                "C. <h1>",
                "D. <head>"
            ],
            "answer": "C. <h1>"
        }

    ],


    # =====================================================
    # JAVASCRIPT
    # =====================================================

    "javascript": [

        {
            "question": "Which keyword can declare a variable in JavaScript?",
            "options": [
                "A. var",
                "B. integer",
                "C. variable",
                "D. define"
            ],
            "answer": "A. var"
        },

        {
            "question": "Which language is mainly used to add interactivity to web pages?",
            "options": [
                "A. SQL",
                "B. JavaScript",
                "C. Excel",
                "D. XML"
            ],
            "answer": "B. JavaScript"
        },

        {
            "question": "Which symbol is commonly used for strict equality?",
            "options": [
                "A. =",
                "B. ==",
                "C. ===",
                "D. !==="
            ],
            "answer": "C. ==="
        }

    ],


    # =====================================================
    # JAVA
    # =====================================================

    "java": [

        {
            "question": "Which keyword is used to create an object in Java?",
            "options": [
                "A. create",
                "B. object",
                "C. new",
                "D. make"
            ],
            "answer": "C. new"
        },

        {
            "question": "Which keyword is used to define a class?",
            "options": [
                "A. class",
                "B. object",
                "C. define",
                "D. structure"
            ],
            "answer": "A. class"
        },

        {
            "question": "Which method is the entry point of a Java program?",
            "options": [
                "A. start()",
                "B. main()",
                "C. run()",
                "D. execute()"
            ],
            "answer": "B. main()"
        }

    ]

}


# =========================================================
# FIND QUESTIONS FOR RESUME SKILLS
# =========================================================

available_questions = []

for skill in user_skills:

    if skill in QUESTION_BANK:

        for question in QUESTION_BANK[skill]:

            # Save skill name with question
            question_copy = question.copy()

            question_copy["skill"] = skill

            available_questions.append(
                question_copy
            )


# =========================================================
# REMOVE DUPLICATES
# =========================================================

unique_questions = []

seen = set()

for question in available_questions:

    question_text = question["question"]

    if question_text not in seen:

        unique_questions.append(
            question
        )

        seen.add(
            question_text
        )


available_questions = unique_questions


# =========================================================
# CHECK QUESTIONS
# =========================================================

if not available_questions:

    st.warning(
        "⚠️ No MCQ questions are available for "
        "the skills detected in your resume."
    )

    st.write("Detected skills:")

    for skill in skills:

        st.write(
            f"• {skill}"
        )

    st.stop()


# =========================================================
# CREATE RANDOM TEST
# =========================================================

# Maximum 10 questions

number_of_questions = min(
    10,
    len(available_questions)
)


# Generate test only once

if (
    "interview_questions" not in st.session_state
    or st.session_state.get("interview_skills") != user_skills
):

    st.session_state.interview_questions = random.sample(
        available_questions,
        number_of_questions
    )

    st.session_state.interview_skills = user_skills

    # Reset previous result
    st.session_state.quiz_score = 0
    st.session_state.quiz_total = 0
    st.session_state.quiz_completed = False


questions = st.session_state.interview_questions


# =========================================================
# TEST INFORMATION
# =========================================================

st.subheader("📝 Personalized MCQ Test")

st.write(
    f"Total Questions: **{len(questions)}**"
)

st.write(
    "Questions are selected according to your resume skills."
)

st.divider()


# =========================================================
# MCQ FORM
# =========================================================

with st.form("personalized_mcq_form"):

    answers = []


    for index, question in enumerate(
        questions,
        start=1
    ):

        st.markdown(
            f"### Question {index}"
        )

        st.caption(
            f"Skill: {question['skill'].title()}"
        )

        st.write(
            question["question"]
        )


        # IMPORTANT:
        # No option selected initially

        selected_answer = st.radio(
            "Select your answer:",
            question["options"],
            index=None,
            key=f"mcq_answer_{index}"
        )


        answers.append(
            selected_answer
        )


        st.divider()


    submitted = st.form_submit_button(
        "🚀 Submit Test",
        use_container_width=True
    )


# =========================================================
# SUBMIT
# =========================================================

if submitted:

    unanswered = 0
    score = 0


    # -----------------------------------------------------
    # CHECK ALL QUESTIONS
    # -----------------------------------------------------

    for index, question in enumerate(questions):

        selected_answer = answers[index]

        if selected_answer is None:

            unanswered += 1

        elif selected_answer == question["answer"]:

            score += 1


    # -----------------------------------------------------
    # UNANSWERED
    # -----------------------------------------------------

    if unanswered > 0:

        st.warning(
            f"⚠️ Please answer all questions. "
            f"{unanswered} question(s) are unanswered."
        )


    # -----------------------------------------------------
    # SUCCESS
    # -----------------------------------------------------

    else:

        total = len(questions)

        percentage = int(
            (score / total) * 100
        )


        # Save result

        st.session_state.quiz_score = score

        st.session_state.quiz_total = total

        st.session_state.quiz_completed = True


        st.success(
            "🎉 Test submitted successfully!"
        )


        st.divider()


        # =================================================
        # ANSWER REVIEW
        # =================================================

        st.subheader(
            "📋 Answer Review"
        )


        for index, question in enumerate(
            questions
        ):

            selected_answer = answers[index]

            correct_answer = question["answer"]


            st.markdown(
                f"### Question {index + 1}"
            )

            st.caption(
                f"Skill: {question['skill'].title()}"
            )

            st.write(
                question["question"]
            )


            st.write(
                f"**Your Answer:** {selected_answer}"
            )


            # ---------------------------------------------
            # CORRECT
            # ---------------------------------------------

            if selected_answer == correct_answer:

                st.success(
                    f"✅ Correct Answer: {correct_answer}"
                )


            # ---------------------------------------------
            # INCORRECT
            # ---------------------------------------------

            else:

                st.error(
                    "❌ Incorrect Answer"
                )

                st.info(
                    f"✅ Correct Answer: **{correct_answer}**"
                )


            st.divider()


        # =================================================
        # FINAL RESULT
        # =================================================

        st.subheader(
            "🏆 Your Result"
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Correct",
                score
            )


        with col2:

            st.metric(
                "Incorrect",
                total - score
            )


        with col3:

            st.metric(
                "Score",
                f"{percentage}%"
            )


        st.progress(
            percentage / 100
        )


        # =================================================
        # FEEDBACK
        # =================================================

        if percentage >= 80:

            st.success(
                "🌟 Excellent performance!"
            )

        elif percentage >= 50:

            st.info(
                "👍 Good performance! Keep practicing."
            )

        else:

            st.warning(
                "📚 Keep learning and try again."
            )