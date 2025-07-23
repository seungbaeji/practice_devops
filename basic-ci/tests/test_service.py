from unittest.mock import Mock, patch

import pytest

from basic_ci.datamodel import User, UserDict
from basic_ci.service import fetch_user_data, filter_active_users, validate_users


# ---- 테스트 입력/출력 데이터 ----
validate_users_inputs: list[list[UserDict]] = [
    [  # 케이스 1
        {"id": 1, "name": "Alice", "is_active": True},
        {"id": None, "name": "Bob", "is_active": False},  # invalid
        {"id": 2, "name": "Charlie", "is_active": True},
    ],
    [  # 케이스 2
        {"id": -1, "name": "Alice", "is_active": True},  # invalid id
        {"id": 3, "name": "", "is_active": True},  # invalid name
    ],
]

validate_users_expected: list[list[str]] = [
    ["Alice", "Charlie"],  # 케이스 1 결과
    [],  # 케이스 2 결과
]


# ---- 유틸리티 함수 ----
def mock_requests_get(mock_data: list[UserDict]) -> Mock:
    """
    Returns a mocked requests.get response with the given JSON data.
    """
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_data
    return mock_response


test_inputs = list(zip(validate_users_inputs, validate_users_expected))


# ---- 테스트 케이스 ----
@pytest.mark.parametrize("users_data, expected_valid_names", test_inputs)
def test_validate_users(
    users_data: list[UserDict], expected_valid_names: list[str]
) -> None:
    """
    Tests that validate_users filters invalid data correctly.
    """
    valid_users: list[User] = validate_users(users_data)
    assert [u.name for u in valid_users] == expected_valid_names


def test_filter_active_users() -> None:
    """
    Tests that filter_active_users returns only active users.
    """
    users: list[User] = [
        User(id=1, name="Alice", is_active=True),
        User(id=2, name="Bob", is_active=False),
    ]
    result: list[User] = filter_active_users(users)
    assert [u.name for u in result] == ["Alice"]


def test_fetch_and_validate_users() -> None:
    """
    Tests the combined fetch, validate, and filter steps.
    """
    mock_data: list[UserDict] = validate_users_inputs[0]  # 첫 번째 케이스 재사용

    with patch("requests.get", return_value=mock_requests_get(mock_data)):
        users_data: list[UserDict] = fetch_user_data("http://example.com/api/users")
        valid_users: list[User] = validate_users(users_data)
        active_users: list[User] = filter_active_users(valid_users)

        assert [u.name for u in active_users] == ["Alice", "Charlie"]
