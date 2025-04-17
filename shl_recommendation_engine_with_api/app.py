import streamlit as st
import pandas as pd

st.title("SHL Assessment Recommendation Engine")

catalog = pd.read_csv("product_catalog.csv")

role = st.text_input("Enter your role:")
skills = st.text_input("Enter your skills (comma-separated):")

def recommend(role, skills):
    role = role.lower()
    skills = [skill.strip().lower() for skill in skills.split(",")]

    def match(row):
        role_match = role in row["target_roles"].lower()
        skill_match = any(skill in row["skills_tested"].lower() for skill in skills)
        return role_match or skill_match

    recommendations = catalog[catalog.apply(match, axis=1)]
    return recommendations[["assessment_name", "target_roles", "skills_tested"]]

if st.button("Get Recommendations"):
    if role and skills:
        result = recommend(role, skills)
        st.write(result)
    else:
        st.warning("Please enter both role and skills.")
