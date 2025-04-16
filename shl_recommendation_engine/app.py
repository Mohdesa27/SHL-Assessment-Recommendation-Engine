import streamlit as st
import pandas as pd
import json

# Load the product catalog
@st.cache_data
def load_catalog():
    return pd.read_csv("product_catalog.csv")

# Recommendation logic
def recommend_assessments(user_input, catalog):
    role = user_input["role"].lower()
    skills = [skill.lower() for skill in user_input["skills"]]

    def match(row):
        role_match = role in row["target_roles"].lower()
        skill_match = any(skill in row["skills_tested"].lower() for skill in skills)
        return role_match or skill_match

    recommendations = catalog[catalog.apply(match, axis=1)]
    return recommendations[["assessment_name", "target_roles", "skills_tested"]]

# Streamlit UI
def main():
    st.title("🔍 SHL Assessment Recommendation Engine")
    st.write("Get assessment suggestions based on your role and skills.")

    role = st.text_input("Enter your job role (e.g., Software Engineer):")
    experience = st.number_input("Years of experience:", min_value=0, step=1)
    skills_input = st.text_input("Enter your skills (comma separated):")

    if st.button("Recommend Assessments"):
        if role and skills_input:
            skills = [skill.strip() for skill in skills_input.split(",")]
            user_input = {"role": role, "experience": experience, "skills": skills}
            catalog = load_catalog()
            results = recommend_assessments(user_input, catalog)

            if not results.empty:
                st.success("✅ Recommended Assessments:")
                st.dataframe(results)
            else:
                st.warning("❌ No matching assessments found.")
        else:
            st.error("Please enter both role and skills.")

if __name__ == "__main__":
    main()
