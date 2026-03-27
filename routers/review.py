from fastapi import APIRouter, HTTPException
from models.schemas import CodeReviewRequest, CodeReviewResponse
from services.llm_service import review_code_with_llm

router = APIRouter(prefix="/review", tags=["Code Review"])

@router.post("/", response_model=CodeReviewResponse)
def review_code(request: CodeReviewRequest):
    
    if len(request.code.strip()) == 0:
        raise HTTPException(status_code=400, detail="Code cannot be empty")
    
    if len(request.code) > 5000:
        raise HTTPException(status_code=400, detail="Code too long - max 5000 characters")
    
    try:
        result = review_code_with_llm(
            code=request.code,
            language=request.language.value,
            context=request.context
        )
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Review failed: {str(e)}")