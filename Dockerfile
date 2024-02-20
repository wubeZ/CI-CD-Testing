FROM python:3.11-slim

WORKDIR /app

COPY requirements.py .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "fizzbuzz.py"]