import pandas as pd
import json

# Step 1: Load product catalog
catalog = pd.read_csv("product_catalog.csv")

# Step 2: Load user input
with open("sample_input.json", "r") as f:
    user_input = json.load(f)

# Step 3: Recommendation logic
def recommend_assessments(user_input, catalog):
    role = user_input["role"].lower()
    skills = [skill.lower() for skill in user_input["skills"]]

    def match(row):
        role_match = role in row["target_roles"].lower()
        skill_match = any(skill in row["skills_tested"].lower() for skill in skills)
        return role_match or skill_match

    recommendations = catalog[catalog.apply(match, axis=1)]
    return recommendations[["assessment_name", "target_roles", "skills_tested"]]

# Step 4: Get recommendations
recommended = recommend_assessments(user_input, catalog)

# Step 5: Show result
if not recommended.empty:
    print("\n✅ Recommended Assessments:\n")
    print(recommended.to_string(index=False))
else:
    print("❌ No matching assessments found.")
