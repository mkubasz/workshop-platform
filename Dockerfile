# Use the Python 3.11 image as a base
FROM python:3.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8

WORKDIR /app

COPY pyproject.toml pyproject.toml

RUN pip install hatch && \
    hatch env create && \
    hatch install

COPY . .

CMD ["hatch", "env", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
