FROM python:3.11-slim

ENV PYTHONPATH=/app:/app/src

WORKDIR /app

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY src ./src
COPY README.md ./README.md

EXPOSE 7860
EXPOSE 11434

CMD ["python", "src/main.py"]