# SHL Assessment Recommendation Engine

## Files:
- `app.py`: Streamlit UI
- `main.py`: CLI tool
- `api.py`: Flask API for JSON querying
- `product_catalog.csv`: Sample product catalog
- `sample_input.json`: Sample request for API
- `requirements.txt`: Install dependencies

## How to Run:
### 1. Run CLI:
```
python main.py
```

### 2. Run Streamlit App:
```
streamlit run app.py
```

### 3. Run Flask API:
```
python api.py
```

Send POST request to `http://127.0.0.1:5000/recommend` with JSON input like in `sample_input.json`.
