import streamlit as st

from utils.skill_gap import (
    find_missing_skills
)


if not st.session_state.get(
    "resume_uploaded",
    False
):

    st.warning(
        "⚠️ Please upload your resume first."
    )

    st.stop()


st.title("🧠 Skill Gap Analysis")

st.write(
    "Your skill gaps are automatically calculated from your resume."
)


st.divider()


career = st.selectbox(
    "Select Target Career",
    st.session_state.careers
)


matched, missing = find_missing_skills(
    st.session_state.skills,
    career
)


col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "✅ Your Skills"
    )

    for skill in matched:

        st.success(
            f"✓ {skill}"
        )


with col2:

    st.subheader(
        "📚 Skills to Improve"
    )

    for skill in missing:

        st.error(
            f"✗ {skill}"
        )


st.divider()


total = len(matched) + len(missing)


if total > 0:

    percentage = int(
        (len(matched) / total) * 100
    )

    st.subheader(
        "📊 Skill Match"
    )

    st.progress(
        percentage / 100
    )

    st.write(
        f"Your skill match for "
        f"**{career}** is **{percentage}%**."
    )