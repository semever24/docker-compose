# app/Dockerfile
FROM python:3.11-slim

WORKDIR /usr/src/app

# Copy only requirements first for caching
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]