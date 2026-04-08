import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Leaf Pigmentation Analyzer", layout="centered")

st.title("🌿 Advanced Leaf Analyzer")

def analyze_leaf(image):
    img = np.array(image)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    # Color masks
    green = cv2.inRange(hsv, (25, 40, 40), (85, 255, 255))
    yellow = cv2.inRange(hsv, (15, 40, 40), (35, 255, 255))
    brown = cv2.inRange(hsv, (5, 40, 40), (20, 255, 255))

    g = np.sum(green > 0)
    y = np.sum(yellow > 0)
    b = np.sum(brown > 0)

    total = g + y + b + 1

    g_per = (g / total) * 100
    y_per = (y / total) * 100
    b_per = (b / total) * 100

    # 🌿 Health Logic
    if g_per > 60:
        health = "Healthy ✅"
    elif y_per > 30:
        health = "Nutrient Deficiency ⚠️"
    elif b_per > 20:
        health = "Diseased ❌"
    else:
        health = "Moderate Condition ⚠️"

    # 🦠 Disease Prediction
    if b_per > 25:
        disease = "Possible Fungal Infection"
    elif y_per > 35:
        disease = "Nitrogen Deficiency"
    else:
        disease = "No Major Disease Detected"

    # 🌱 Leaf Age Estimation
    if g_per > 70 and y_per < 10:
        age = "Young Leaf 🌱"
    elif g_per > 50:
        age = "Mature Leaf 🍃"
    else:
        age = "Old Leaf 🍂"

    return g_per, y_per, b_per, health, disease, age


# Upload
file = st.file_uploader("📤 Upload Leaf Image")

if file:
    image = Image.open(file)
    st.image(image, caption="Uploaded Leaf", use_column_width=True)

    g, y, b, health, disease, age = analyze_leaf(image)

    st.subheader("📊 Pigmentation Analysis")
    st.write(f"🟢 Green: {g:.2f}%")
    st.write(f"🟡 Yellow: {y:.2f}%")
    st.write(f"🟤 Brown: {b:.2f}%")

    st.subheader("🌿 Health Status")
    st.success(health)

    st.subheader("🦠 Disease Prediction")
    st.warning(disease)

    st.subheader("🌱 Leaf Age Estimation")
    st.info(age)
