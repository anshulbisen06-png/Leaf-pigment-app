import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Leaf Pigmentation Analyzer")

st.title("🌿 Leaf Pigmentation Analyzer")

def analyze_leaf(image):
    img = np.array(image)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

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

    if g_per > 60:
        status = "Healthy ✅"
    elif y_per > 30:
        status = "Nutrient Deficiency ⚠️"
    elif b_per > 20:
        status = "Diseased ❌"
    else:
        status = "Moderate Condition ⚠️"

    return g_per, y_per, b_per, status

file = st.file_uploader("Upload Leaf Image")

if file:
    image = Image.open(file)
    st.image(image)

    g, y, b, status = analyze_leaf(image)

    st.write(f"Green: {g:.2f}%")
    st.write(f"Yellow: {y:.2f}%")
    st.write(f"Brown: {b:.2f}%")
    st.success(status)
