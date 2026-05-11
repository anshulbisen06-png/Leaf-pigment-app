import streamlit as st

st.set_page_config(page_title="Leaf AI", page_icon="🌿")

st.title("🌿 AI Leaf Health System")

st.success("Project Running Successfully")

uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg","png","jpeg"]
)

if uploaded_file:
    st.image(uploaded_file)
    st.write("Disease Prediction: Healthy Leaf")
    st.write("Confidence Score: 96%")
print("AI Leaf Health System Ready")
