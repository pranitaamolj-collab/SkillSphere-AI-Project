import streamlit as st

from database import create_table
from auth import register_user, login_user

from resume_analyzer import extract_text, find_skills
from resume_score import calculate_resume_score
from career import recommend_career


# =========================================================
# DATABASE
# =========================================================

create_table()


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SkillSphere AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SESSION STATE INITIALIZATION
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "resume_uploaded" not in st.session_state:
    st.session_state.resume_uploaded = False

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "skills" not in st.session_state:
    st.session_state.skills = []

if "resume_score" not in st.session_state:
    st.session_state.resume_score = 0

if "careers" not in st.session_state:
    st.session_state.careers = []

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0

if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False


# =========================================================
# LOGIN / REGISTER
# =========================================================

if not st.session_state.logged_in:

    # Hide sidebar on login page
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🚀 SkillSphere AI")

    st.subheader(
        "AI-Powered Resume & Career Development Platform"
    )

    st.write(
        "Upload your resume and discover your skills, "
        "career opportunities and interview performance."
    )

    st.divider()

    login_tab, register_tab = st.tabs(
        ["🔐 Login", "📝 Register"]
    )


    # =====================================================
    # LOGIN
    # =====================================================

    with login_tab:

        st.subheader("🔐 Login to SkillSphere AI")

        email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):

            if not email or not password:

                st.warning(
                    "⚠️ Please enter email and password."
                )

            else:

                user = login_user(
                    email,
                    password
                )

                if user:

                    st.session_state.logged_in = True
                    st.session_state.user = user

                    st.success(
                        "✅ Login successful!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "❌ Invalid email or password."
                    )


    # =====================================================
    # REGISTER
    # =====================================================

    with register_tab:

        st.subheader("📝 Create New Account")

        name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
            key="register_name"
        )

        email = st.text_input(
            "Email",
            placeholder="Enter your email",
            key="register_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Re-enter your password",
            key="register_confirm_password"
        )

        if st.button(
            "📝 Register",
            use_container_width=True
        ):

            if not name or not email or not password:

                st.warning(
                    "⚠️ Please fill all required fields."
                )

            elif password != confirm_password:

                st.error(
                    "❌ Passwords do not match."
                )

            else:

                result = register_user(
                    name,
                    email,
                    password
                )

                if result:

                    st.success(
                        "🎉 Registration successful!"
                    )

                    st.info(
                        "👉 Now open the Login tab and login."
                    )

                else:

                    st.error(
                        "❌ This email is already registered."
                    )


# =========================================================
# MAIN APP
# =========================================================

else:

    # Show sidebar after login

    st.sidebar.title("🚀 SkillSphere AI")

    user = st.session_state.user


    # =====================================================
    # USER INFORMATION
    # =====================================================

    if user:

        try:

            st.sidebar.success(
                f"👋 Welcome, {user[1]}"
            )

            st.sidebar.caption(
                f"📧 {user[2]}"
            )

        except Exception:

            st.sidebar.success(
                "👋 Welcome!"
            )


    st.sidebar.divider()


    # =====================================================
    # LOGOUT
    # =====================================================

    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.user = None

        st.session_state.resume_uploaded = False
        st.session_state.resume_text = ""
        st.session_state.skills = []
        st.session_state.resume_score = 0
        st.session_state.careers = []

        st.session_state.quiz_score = 0
        st.session_state.quiz_total = 0
        st.session_state.quiz_completed = False

        st.rerun()


    # =====================================================
    # MAIN HOME PAGE
    # =====================================================

    st.title("📄 Upload Your Resume")

    st.write(
        "Upload your PDF resume to start your "
        "personalized SkillSphere AI journey."
    )

    st.divider()


    # =====================================================
    # RESUME UPLOAD
    # =====================================================

    uploaded_file = st.file_uploader(
        "Choose your Resume",
        type=["pdf"],
        help="Upload your resume in PDF format."
    )


    if uploaded_file:

        st.success(
            f"📄 Resume selected: {uploaded_file.name}"
        )


        # =================================================
        # ANALYZE BUTTON
        # =================================================

        if st.button(
            "🔍 Analyze Resume",
            use_container_width=True
        ):

            try:

                # -----------------------------------------
                # Extract resume text
                # -----------------------------------------

                resume_text = extract_text(
                    uploaded_file
                )


                # -----------------------------------------
                # Find skills
                # -----------------------------------------

                detected_skills = find_skills(
                    resume_text
                )


                # -----------------------------------------
                # Resume score
                # -----------------------------------------

                resume_score = calculate_resume_score(
                    detected_skills
                )


                # -----------------------------------------
                # Career recommendation
                # -----------------------------------------

                recommended_careers = recommend_career(
                    detected_skills
                )


                # -----------------------------------------
                # SAVE DATA
                # -----------------------------------------

                st.session_state.resume_uploaded = True

                st.session_state.resume_text = resume_text

                st.session_state.skills = detected_skills

                st.session_state.resume_score = resume_score

                st.session_state.careers = recommended_careers


                # Reset old quiz result
                st.session_state.quiz_score = 0
                st.session_state.quiz_total = 0
                st.session_state.quiz_completed = False


                # -----------------------------------------
                # SUCCESS
                # -----------------------------------------

                st.success(
                    "🎉 Resume analyzed successfully!"
                )

                st.info(
                    "✅ Your resume data is now ready. "
                    "Use the sidebar pages to explore your results."
                )


            except Exception as e:

                st.error(
                    "❌ Resume analysis failed."
                )

                st.exception(e)


    else:

        st.info(
            "👆 Please upload your PDF resume to continue."
        )


    # =====================================================
    # AFTER RESUME UPLOAD
    # =====================================================

    if st.session_state.resume_uploaded:

        st.divider()

        st.success(
            "✅ Resume uploaded and analyzed."
        )

        st.write(
            "You can now open **Career Recommendation, "
            "Interview, Performance and Skill Analysis** "
            "from the sidebar."
        )
