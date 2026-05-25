FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .

RUN useradd --system --uid 10001 weatherapi && \
    chown -R weatherapi:weatherapi /app

USER weatherapi

EXPOSE 5000

CMD ["python", "app.py"]
