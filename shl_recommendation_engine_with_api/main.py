import pandas as pd

def recommend_assessments(role, skills):
    catalog = pd.read_csv("product_catalog.csv")
    role = role.lower()
    skills = [skill.lower() for skill in skills]

    def match(row):
        role_match = role in row["target_roles"].lower()
        skill_match = any(skill in row["skills_tested"].lower() for skill in skills)
        return role_match or skill_match

    recommendations = catalog[catalog.apply(match, axis=1)]
    return recommendations[["assessment_name", "target_roles", "skills_tested"]]

if __name__ == "__main__":
    role_input = input("Enter the role: ")
    skills_input = input("Enter skills (comma-separated): ").split(",")
    result = recommend_assessments(role_input, skills_input)
    print(result)
