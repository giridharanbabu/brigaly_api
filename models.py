from pydantic import BaseModel
from typing import List


class ReviewRequest(BaseModel):
    title: str
    content: str
    type: str




class ReviewResponse(BaseModel):
    clarity_score: float
    structure_score: float
    grammar_score: float
    tone: str
    tone_match: bool

    plagiarism_risk_score: float
    plagiarism_notes: List[str]

    misleading_claims: List[str]
    exaggerated_statements: List[str]
    unverified_statements: List[str]

    education_alignment_score: float
    audience_relevance_score: float

    improvement_suggestions: List[str]
    suggested_headline: str
    suggested_summary: str
    suggested_tags: List[str]

    rewritten_sample: str

    class Config:
        extra = "ignore"