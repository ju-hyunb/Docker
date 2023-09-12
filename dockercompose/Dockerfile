FROM python:3.9.17-slim

WORKDIR /app

COPY requirements.txt ./
COPY web_crawler.py /app

CMD ["python", "web_crawler.py"]