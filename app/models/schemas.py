from pydantic import BaseModel

class GPTResult(BaseModel):
    verdict: str
    score: int
    explanation: str
