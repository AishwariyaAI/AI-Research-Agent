from pydantic import BaseModel

class ResumeResponse(BaseModel):
    filename: str
    status: str