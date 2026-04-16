import streamlit as st
import requests

st.set_page_config(page_title="Clinical Trial Matcher", layout="centered")

st.title("🧠 AI Clinical Trial Matcher")

st.write("Enter patient details or upload voice to find matching clinical trials")

# Option selection
option = st.radio("Choose Input Method", ["Text Input", "Voice Input"])

# ---------------- TEXT INPUT ----------------
if option == "Text Input":
    text = st.text_area("Enter patient details:")

    if st.button("Find Trials"):
        if text:
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/match/text",
                    params={"text": text}
                )
                data = response.json()

                st.success("Results Found ✅")

                for trial in data:
                    st.subheader(f"🧪 {trial['trial']}")
                    st.write(f"📊 Score: {trial['score']:.2f}")

                    if "explanation" in trial:
                        st.write("🔍 Explanation:")
                        for exp in trial["explanation"]:
                            st.write(f"- {exp}")

                    st.markdown("---")

            except:
                st.error("❌ Backend not running!")

        else:
            st.warning("⚠️ Please enter patient details")

# ---------------- VOICE INPUT ----------------
elif option == "Voice Input":
    file = st.file_uploader("Upload .wav file", type=["wav"])

    if st.button("Match Voice"):
        if file:
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/match/voice",
                    files={"file": file}
                )
                data = response.json()

                st.success("Results Found ✅")

                for trial in data:
                    st.subheader(f"🧪 {trial['trial']}")
                    st.write(f"📊 Score: {trial['score']:.2f}")
                    st.markdown("---")

            except:
                st.error("❌ Backend not running!")

        else:
            st.warning("⚠️ Please upload a file")