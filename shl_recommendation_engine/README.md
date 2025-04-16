# SHL Assessment Recommendation Engine

## 📌 Description
A Python-based tool that recommends SHL assessments based on job role and skills.

## 🗂️ Files
- `main.py` – Main logic
- `product_catalog.csv` – SHL product data (you can replace with real data)
- `sample_input.json` – Candidate's profile
- `README.md` – Project guide

## ▶️ How to Run
Make sure Python is installed.

```bash
python main.py
```

## 📥 Sample Input
```json
{
  "role": "Software Engineer",
  "experience": 2,
  "skills": ["coding", "problem-solving"]
}
```

## ✅ Output
```
Recommended Assessments:

assessment_name             target_roles              skills_tested
Coding Aptitude Test     Software Engineer;Developer  coding;problem-solving
Cognitive Ability Test           All               logical thinking;problem-solving
```
