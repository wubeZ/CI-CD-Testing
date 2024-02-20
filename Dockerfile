FROM python:3.11-slim

WORKDIR /app

COPY requirements.py .

RUN pip install -r requirements.py

COPY . .

CMD ["python3", "fizzbuzz.py"]