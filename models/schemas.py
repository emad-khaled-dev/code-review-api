from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Language(str, Enum):
    python = "python"
    javascript = "javascript"
    typescript = "typescript"
    java = "java"
    other = "other"

class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class CodeReviewRequest(BaseModel):
    code: str
    language: Language = Language.python
    context: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "code": "def add(a,b): return a+b",
                "language": "python",
                "context": "This is a utility function"
            }
        }

class Issue(BaseModel):
    line: Optional[int] = None
    severity: Severity
    message: str
    suggestion: str

class CodeReviewResponse(BaseModel):
    language: str
    summary: str
    issues: list[Issue]
    overall_score: int
    status: str