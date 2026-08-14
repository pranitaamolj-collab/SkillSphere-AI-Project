import streamlit as st


if not st.session_state.get(
    "resume_uploaded",
    False
):

    st.warning(
        "⚠️ Please upload your resume first."
    )

    st.stop()


st.title("🎯 Career Recommendation")

st.write(
    "Career recommendations generated from your resume."
)


st.divider()


for index, career in enumerate(
    st.session_state.careers,
    start=1
):

    st.subheader(
        f"{index}. 💼 {career}"
    )

    st.write(
        "This career matches the skills "
        "detected in your resume."
    )

    st.divider()