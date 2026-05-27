# AI Model Serving Project 🚀

A Full Stack AI Application built using:

- FastAPI
- Hugging Face Transformers
- React + Vite
- Raw CSS

This project demonstrates serving multiple AI models using FastAPI APIs and connecting them with a modern React frontend.

---

# 📌 Features

✅ Sentiment Analysis  
✅ Text Generation  
✅ Question Answering  
✅ Text Translation  
✅ Grammar Correction  
✅ FastAPI Backend  
✅ React Frontend  
✅ Hugging Face Models  
✅ REST API Integration  
✅ Beautiful Responsive UI  

---

# 🛠️ Tech Stack

## Frontend
- React
- Vite
- Axios
- CSS

## Backend
- FastAPI
- Transformers
- PyTorch
- Pydantic

---

# 📂 Project Structure

```bash
ai-model-serving-project/

│

├── backend/
│   ├── app.py
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── App.css
│   │
│   ├── package.json
│   ├── vite.config.js
│
└── README.md
```

---

# 🤖 AI Models Used

| Task | Model |
|------|------|
| Sentiment Analysis | distilbert-base-uncased-finetuned-sst-2-english |
| Question Answering | distilbert-base-cased-distilled-squad |
| Text Generation | google/flan-t5-small |
| Translation | Helsinki-NLP/opus-mt-en-hi |
| Grammar Correction | vennify/t5-base-grammar-correction |

---

# ⚙️ Backend Setup

## Step 1 — Go to Backend Folder

```bash
cd backend
```

---

## Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 3 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Step 4 — Install Requirements

```bash
pip install -r requirements.txt
```

---

## Step 5 — Run FastAPI Server

```bash
uvicorn app:app --reload
```

---

## Step 6 — Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# 💻 Frontend Setup

## Step 1 — Go to Frontend Folder

```bash
cd frontend
```

---

## Step 2 — Install Dependencies

```bash
npm install
```

---

## Step 3 — Install Axios

```bash
npm install axios
```

---

## Step 4 — Run Frontend

```bash
npm run dev
```

---

## Step 5 — Open Frontend

```text
http://localhost:5173
```

---

# 🌐 API Endpoints

| Endpoint | Method | Description |
|------|------|------|
| `/sentiment` | POST | Sentiment Analysis |
| `/generate` | POST | Text Generation |
| `/qa` | POST | Question Answering |
| `/translate` | POST | Text Translation |
| `/grammar` | POST | Grammar Correction |

---

# 📸 Sample Output

## Sentiment Analysis

Input:
```text
I love artificial intelligence
```

Output:
```text
POSITIVE
```

---

# 🚀 Deployment

## Frontend Deployment
- Vercel

## Backend Deployment
- Render

---

# 👩‍💻 Author

Dhaneshwari Bhatia

---

# ⭐ Conclusion

This project demonstrates:
- Full Stack AI Development
- Model Serving using FastAPI
- Hugging Face Integration
- React API Integration
- End-to-End Deployment

```
