FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir flask-meld==0.13.1 --no-deps && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--debugger"]
