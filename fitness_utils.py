import os
import json
import random

# -------------------------
# Load workout data
# -------------------------
def load_workout_data():
    path = os.path.join("fit_trainer_notebook", "workouts.json")
    with open(path, "r") as f:
        return json.load(f)

# -------------------------
# Get workout plan (Beginner / Advanced)
# -------------------------
def get_detailed_workout(goal, equipment, workout_data, level="Beginner"):
    return workout_data.get(goal, {}).get(equipment, {}).get(level, {})

# -------------------------
# BMR Calculation
# -------------------------
def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

# -------------------------
# Calories Calculation
# -------------------------
def calculate_calories(bmr, activity_level):
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Super active": 1.9
    }
    return int(bmr * activity_multipliers.get(activity_level, 1.2))

# -------------------------
# Diet Plan Generator
# -------------------------
def generate_diet_plan(calories, diet_type="veg"):
    # 30% breakfast, 40% lunch, 30% dinner
    meal_split = {
        "breakfast": int(0.3 * calories),
        "lunch": int(0.4 * calories),
        "dinner": int(0.3 * calories)
    }
    
    VEG_FOODS = {
        "breakfast": ["Oats with milk", "Vegetable Upma", "Paneer sandwich"],
        "lunch": ["Dal + Rice + Veg curry", "Paneer salad + Roti", "Chole + Brown Rice"],
        "dinner": ["Mixed veg + Roti", "Palak Paneer + Rice", "Vegetable Khichdi"]
    }

    NONVEG_FOODS = {
        "breakfast": ["Omelette + Toast", "Chicken sausage + Oats", "Boiled eggs + Smoothie"],
        "lunch": ["Grilled chicken + Rice", "Fish curry + Roti", "Egg curry + Brown Rice"],
        "dinner": ["Chicken salad", "Fish + Veg stir fry", "Egg bhurji + Roti"]
    }

    food_choices = VEG_FOODS if diet_type.lower() == "veg" else NONVEG_FOODS
    
    plan = {}
    for meal in ["breakfast", "lunch", "dinner"]:
        plan[meal] = {
            "food": random.choice(food_choices[meal]),
            "calories": meal_split[meal]
        }
    
    return plan

'''def generate_workout_plan(goal):
    if goal == "Weight Loss": return ["Cardio (30 mins)", "Bodyweight Circuit", "Yoga", "HIIT"]
    elif goal == "Muscle Gain": return ["Upper Body Strength", "Leg Day", "Push Pull Split", "Core Focus"]
    else:
        return ["Mixed Cardio & Strength", "Yoga", "Pilates", "Light Jog"]
'''
