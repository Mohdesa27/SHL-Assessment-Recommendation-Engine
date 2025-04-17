from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

catalog = pd.read_csv("product_catalog.csv")

def recommend_assessments(role, skills):
    role = role.lower()
    skills = [skill.lower() for skill in skills]

    def match(row):
        role_match = role in row["target_roles"].lower()
        skill_match = any(skill in row["skills_tested"].lower() for skill in skills)
        return role_match or skill_match

    recommendations = catalog[catalog.apply(match, axis=1)]
    return recommendations[["assessment_name", "target_roles", "skills_tested"]].to_dict(orient="records")

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    role = data.get("role", "")
    skills = data.get("skills", [])
    result = recommend_assessments(role, skills)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
