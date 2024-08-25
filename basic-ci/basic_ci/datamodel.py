from __future__ import annotations

from typing import Any, Optional, TypedDict

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(..., ge=1)
    name: str = Field(..., min_length=1)
    is_active: bool


class UserDict(TypedDict):
    id: int
    name: Optional[str]
    is_active: Optional[bool]
