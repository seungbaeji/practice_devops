import time

from basic_ci.service import fetch_user_data, filter_active_users, validate_users


def main():
    url = "http://example.com/api/users"

    while True:
        # 1. 사용자 데이터를 가져옴
        try:
            users_data = fetch_user_data(url)
        except RuntimeError as e:
            print(f"Error fetching user data: {e}")
            time.sleep(60)  # 실패 시 1분 대기 후 다시 시도
            continue

        # 2. 데이터를 검증하여 유효한 사용자만 필터링
        valid_users = validate_users(users_data)

        # 3. 활성화된 사용자만 필터링
        active_users = filter_active_users(valid_users)

        # 4. 결과 출력
        print("Active Users:")
        for user in active_users:
            print(f"ID: {user.id}, Name: {user.name}, Active: {user.is_active}")

        # 5. 일정 시간 대기 (예: 5분)
        time.sleep(300)  # 300초(5분)마다 다시 실행


if __name__ == "__main__":
    main()
