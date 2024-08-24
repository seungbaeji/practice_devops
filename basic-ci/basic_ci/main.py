from __future__ import annotations

from typing import Any, Optional, TypedDict

import requests
from pydantic import BaseModel, Field, ValidationError


class User(BaseModel):
    id: int = Field(..., ge=1)
    name: str = Field(..., min_length=1)
    is_active: bool


class UserDict(TypedDict):
    id: int
    name: Optional[str]
    is_active: Optional[bool]


def fetch_user_data(url: str) -> list[UserDict]:
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch data: {response.status_code}")

    users_data: list[UserDict] = response.json()  # 불완전한 데이터를 받을 수 있음
    return users_data


def validate_users(users: list[UserDict]) -> list[User]:
    valid_users = []

    for user_data in users:
        try:
            user = User(**user_data)
            valid_users.append(user)
        except ValidationError as e:
            print(f"Invalid user data skipped: {e}")

    return valid_users


def filter_active_users(users: list[User]) -> list[User]:
    return [user for user in users if user.is_active]
