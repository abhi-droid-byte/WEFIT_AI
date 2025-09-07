import requests
import streamlit as st
from utils.fitness_utils import (
    calculate_bmr, calculate_calories, generate_diet_plan,
    load_workout_data, get_detailed_workout
)

st.set_page_config(page_title="WeFitAI", layout="centered")
st.title("Welcome to WeFitAI - Your Personalized Fitness Trainer")

st.sidebar.header("🧍 Your Info")

age = st.sidebar.number_input("Age", 18, 80, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", 100, 250, 170)
weight = st.sidebar.number_input("Weight (kg)", 30, 200, 70)
activity = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"])

goal = st.sidebar.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
equipment = st.sidebar.selectbox("Available Equipment", ["Home", "Gym"])
diet_type = st.sidebar.radio("Diet Preference", ["Veg", "Non-Veg"])
fitness_level = st.sidebar.selectbox("Experience Level", ["Beginner", "Advanced"])

if st.sidebar.button("Generate Plan"):
    bmr = calculate_bmr(weight, height, age, gender)
    calories = calculate_calories(bmr, activity)
    diet_plan = generate_diet_plan(calories, diet_type=diet_type.lower())

    workout_data = load_workout_data()
    workout_plan = get_detailed_workout(goal, equipment, workout_data, fitness_level)

    st.subheader("🍽️ Diet Plan")
    st.markdown(f"**Total Calories:** {calories} kcal/day")

    for meal, details in diet_plan.items():
        st.markdown(f"**{meal.capitalize()}**")
        st.markdown(f"- {details['food']} ({details['calories']} kcal)")
        st.markdown("---")

    st.subheader("💪 Workout Plan")
    if workout_plan:
        for day, exercises in workout_plan.items():
            st.markdown(f"**{day}**")
            for ex in exercises:
                st.markdown(f"• {ex}")
            st.markdown("---")
    else:
        st.warning("⚠️ No workout plan found for the selected options.")


'''import os

# ==============================
# Calorie Estimator (from Image)
# ==============================
st.subheader("📸 Food Calorie & Macros Estimator")

uploaded_image = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded_image and st.button("Analyze Food Image"):
    url = "https://calorieninjas.p.rapidapi.com/v1/imagetext"

    files = {"image": uploaded_image.getvalue()}
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY", "YOUR_API_KEY_HERE"),
        "X-RapidAPI-Host": "calorieninjas.p.rapidapi.com"
    }

    with st.spinner("🔍 Analyzing your food..."):
        response = requests.post(url, headers=headers, files=files)

        if response.status_code == 200:
            result = response.json()
            if "items" in result and len(result["items"]) > 0:
                st.success("✅ Food detected!")
                for item in result["items"]:
                    st.markdown(f"🍽 **Food:** {item['name']}")
                    st.markdown(f"- Calories: {item['calories']} kcal")
                    st.markdown(f"- Protein: {item['protein_g']} g")
                    st.markdown(f"- Carbs: {item['carbohydrates_total_g']} g")
                    st.markdown(f"- Fat: {item['fat_total_g']} g")
                    st.markdown("---")
            else:
                st.warning("⚠️ No recognizable food found. Try another image.")
        else:
            st.error(f"❌ API Error: {response.text}")'''
