from pydantic import BaseModel, Field
from typing import Optional

class BookSchema(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=2)
    # can add status and colors as well
    # pages: Optional[int] = Field(default=None, gt=0)
    # available: bool = Field(default=True)
