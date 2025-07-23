# CI/CD 실습 프로젝트

이 프로젝트는 **CI/CD 실습**을 목적으로 작성되었으며,
Poetry로 관리된 Python 패키지를 **Docker 이미지로 빌드하고 GHCR에 푸시하는 과정**을 다룹니다.

---

## 1. Poetry 설치 및 패키지 설치

### 1-1. Poetry 설치

Poetry를 설치하려면 다음 명령어 중 하나를 실행하세요:

```bash
curl -sSL https://install.python-poetry.org | python3 -
# 또는
pip install poetry
```

설치 확인:

```bash
poetry --version
```

### 1-2. 프로젝트 의존성 설치

`pyproject.toml`에 정의된 의존성을 설치하려면:

```bash
poetry install
```

테스트용 패키지만 설치하려면:

```bash
poetry install --only dev
```

현재 프로젝트 설치 없이, 테스트용 패키지만 설치하려면:

```bash
poetry install --only dev --no-root
```

---

## 2. 테스트 실행

`pytest`를 사용하여 테스트를 실행할 수 있습니다:

```bash
poetry run pytest
```

---

## 3. 프로젝트 빌드 (패키징)

Poetry를 이용해 패키지를 `.whl` 및 `.tar.gz` 파일로 빌드할 수 있습니다:

```bash
poetry build
poetry build -f wheel  # wheel만 생성
poetry build -f sdist  # sdist만 생성
```

빌드된 아티팩트는 `dist/` 폴더에 생성됩니다.

---

## 4. Docker 빌드 및 실행

Dockerfile을 기반으로 이미지를 빌드하고 실행할 수 있습니다.

### 4-1. Docker 이미지 빌드

```bash
docker build -t basic-ci:latest .
```

### 4-2. Docker 컨테이너 실행

```bash
docker run --rm -it basic-ci:latest
```

---

## 5. GHCR로 Docker 이미지 푸시

### 5-1. GHCR 로그인

```bash
export GITHUB_TOKEN=<your-pat-token>
echo $GITHUB_TOKEN | docker login ghcr.io -u <github-username> --password-stdin
```

* **`GITHUB_TOKEN`** 또는 \*\*Personal Access Token(PAT)\*\*은 `write:packages` 권한이 필요합니다.

### 5-2. GHCR에 태그 및 푸시

```bash
docker tag basic-ci:latest ghcr.io/<github-username>/<repo-name>:latest
docker push ghcr.io/<github-username>/<repo-name>:latest
```

### 5-3. 예시

```bash
docker build -t ghcr.io/my-org/basic-ci:latest .
docker push ghcr.io/my-org/basic-ci:latest
```

---

## 6. GitHub Actions를 활용한 CI/CD

GitHub Actions를 사용하여 **패키지 빌드 → 패키지 테스트 → Docker 이미지 빌드 → GHCR 푸시** 과정을 자동화할 수 있습니다.
수동 실행 명령어는 다음과 같습니다:

```bash
# 패키지 빌드
poetry build
poetry run pip install dist/*.whl

# 패키지 테스트
poetry install --only dev --no-root
poetry run pytest

# Docker 이미지 빌드
docker build -t ghcr.io/<github-username>/<repo-name>:latest .

# GHCR 푸시
docker push ghcr.io/<github-username>/<repo-name>:latest
```

---
