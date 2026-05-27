from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

# ======================================================
# CREATE FASTAPI APPLICATION
# ======================================================

app = FastAPI()

# ======================================================
# ENABLE CORS
# This allows React frontend to connect with FastAPI
# ======================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================================================
# LOAD HUGGING FACE MODELS
# Models are loaded only once when server starts
# ======================================================

# 1. Sentiment Analysis Model
sentiment_pipeline = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# 2. Text Summarization Model
summarizer_pipeline = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

# 3. Question Answering Model
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

# 4. Text Generation Model
generator_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

# 5. Translation Model
translator_pipeline = pipeline(
    "translation",
    model="Helsinki-NLP/opus-mt-en-hi"
)

# 6. Grammar Correction Model
grammar_pipeline = pipeline(
    "text2text-generation",
    model="vennify/t5-base-grammar-correction"
)

# ======================================================
# INPUT DATA MODELS
# Pydantic models validate incoming API data
# ======================================================

# Used for APIs that require only text input
class TextInput(BaseModel):
    text: str

# Used for Question Answering API
class QAInput(BaseModel):
    question: str
    context: str

# ======================================================
# HOME ROUTE
# ======================================================

@app.get("/")
def home():

    return {
        "message": "AI Model Serving API is Running Successfully"
    }

# ======================================================
# 1. SENTIMENT ANALYSIS API
# ======================================================

@app.post("/sentiment")
def sentiment_analysis(data: TextInput):

    result = sentiment_pipeline(data.text)

    return {
        "task": "Sentiment Analysis",
        "input": data.text,
        "prediction": result
    }

# ======================================================
# 2. TEXT SUMMARIZATION API
# ======================================================

@app.post("/summarize")
def summarize_text(data: TextInput):

    result = summarizer_pipeline(
        data.text,
        max_length=80,
        min_length=20,
        do_sample=False
    )

    return {
        "task": "Text Summarization",
        "input": data.text,
        "summary": result
    }

# ======================================================
# 3. QUESTION ANSWERING API
# ======================================================

@app.post("/qa")
def question_answering(data: QAInput):

    result = qa_pipeline(
        question=data.question,
        context=data.context
    )

    return {
        "task": "Question Answering",
        "question": data.question,
        "context": data.context,
        "answer": result
    }

# ======================================================
# 4. TEXT GENERATION API
# ======================================================

@app.post("/generate")
def generate_text(data: TextInput):

    prompt = f"Write a creative short story about: {data.text}"

    result = generator_pipeline(
        prompt,
        max_length=150,
        do_sample=True,
        temperature=0.9
    )

    generated_story = result[0]['generated_text']

    return {
        "output": generated_story
    }

# ======================================================
# 5. TEXT TRANSLATION API
# ======================================================

@app.post("/translate")
def translate_text(data: TextInput):

    result = translator_pipeline(data.text)

    return {
        "task": "Text Translation",
        "input": data.text,
        "translated_text": result
    }

# ======================================================
# 6. GRAMMAR CORRECTION API
# ======================================================

@app.post("/grammar")
def grammar_correction(data: TextInput):

    input_text = "grammar: " + data.text

    result = grammar_pipeline(
        input_text,
        max_length=100
    )

    return {
        "task": "Grammar Correction",
        "input": data.text,
        "corrected_text": result
    }