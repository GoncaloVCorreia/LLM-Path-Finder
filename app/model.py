from pydantic import BaseModel, Field

class FileSearchResult(BaseModel):
    score: int = Field(description="Confidence score from 0 to 100")
    path: str = Field(description="Full path of the relevant file or folder")
    justification: str = Field(description="Why this matches the query")
