FROM python:3.9-slim-bookworm
RUN apt update && apt -y upgrade
COPY . .
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /app

CMD ["python", "main.py"]

