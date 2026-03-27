# Code Review Assistant API

An AI-powered code review API built with FastAPI and Groq LLaMA.

## What it does
Accepts a code snippet and returns a structured AI review including issues, severity levels, and improvement suggestions.

## Tech Stack
- FastAPI
- Pydantic
- Groq LLaMA AI
- Uvicorn

## Run locally

1. Clone the repo
2. Install dependencies:
pip install -r requirements.txt
3. Create .env file:
GROQ_API_KEY=your_key_here
4. Start the server:
uvicorn main:app --reload
5. Visit http://127.0.0.1:8000/docs

## Example

POST /review/
{
  "code": "def add(a,b): return a+b",
  "language": "python"
}

Response:
{
  "language": "python",
  "summary": "Concise but lacks documentation",
  "issues": [...],
  "overall_score": 6,
  "status": "success"
}


## Live Demo
https://code-review-api-ynul.onrender.com/docs