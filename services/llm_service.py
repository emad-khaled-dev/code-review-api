from groq import Groq
import json
from core.config import settings
from models.schemas import CodeReviewResponse, Issue, Severity

client = Groq(api_key=settings.groq_api_key)

def review_code_with_llm(code: str, language: str, context: str = None) -> CodeReviewResponse:
    
    prompt = f"""You are an expert code reviewer. Review the following {language} code and respond ONLY with a JSON object in this exact format, nothing else, no markdown, no backticks:

{{
    "summary": "brief overall summary of the code quality",
    "overall_score": <number from 1 to 10>,
    "issues": [
        {{
            "line": <line number or null>,
            "severity": "<low, medium, or high>",
            "message": "what the issue is",
            "suggestion": "how to fix it"
        }}
    ]
}}

Code to review:
{code}

{f'Additional context: {context}' if context else ''}

Respond with JSON only. No explanation, no markdown, no backticks, just the raw JSON object."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    response_text = response.choices[0].message.content.strip()
    
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
    
    data = json.loads(response_text)
    
    issues = [
        Issue(
            line=issue.get("line"),
            severity=Severity(issue["severity"]),
            message=issue["message"],
            suggestion=issue["suggestion"]
        )
        for issue in data.get("issues", [])
    ]
    
    return CodeReviewResponse(
        language=language,
        summary=data["summary"],
        issues=issues,
        overall_score=data["overall_score"],
        status="success"
    )