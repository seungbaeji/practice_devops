FROM python:3.11-slim-buster AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry poetry-plugin-export
RUN poetry export -f requirements.txt \
    --output requirements.txt \
    --without-hashes \
    && pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim-buster AS release

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

WORKDIR /app

COPY ./basic_ci .
COPY ./main.py .

ENTRYPOINT ["python", "main.py"]
