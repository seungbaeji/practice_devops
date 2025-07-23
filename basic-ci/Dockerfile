# ---- Builder Stage ----
FROM python:3.11-slim-bookworm AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml poetry.lock ./

# poetry 설치 및 wheel 빌드
RUN pip install --no-cache-dir poetry poetry-core
COPY . .
RUN poetry build -f wheel
# 결과: /app/dist/*.whl

# ---- Release Stage (Alpine) ----
FROM python:3.11-alpine AS release

RUN apk add --no-cache \
    libpq \
    && apk add --no-cache --virtual .build-deps \
    libstdc++ \
    bash

WORKDIR /app

# 빌더에서 생성된 wheel 파일 복사
COPY --from=builder /app/dist/*.whl ./

# wheel 설치
RUN pip install --no-cache-dir ./*.whl \
    && rm ./*.whl

ENV PYTHONUNBUFFERED=1
CMD ["basic-ci"]