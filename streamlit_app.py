import streamlit as st

st.set_page_config(
    page_title="TrustMed AI",
    layout="centered"
)

st.title("🩺 TrustMed AI")

st.subheader("Explainable Healthcare AI System")

st.write(
    "Upload a Chest X-ray image for AI-based pneumonia analysis."
)

uploaded_file = st.file_uploader(
    "Upload Chest X-ray",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded X-ray",
        use_container_width=True
    )

    st.success("✅ Image Uploaded Successfully")
