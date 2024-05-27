FROM python:3.9-slim-bookworm
RUN apt update && apt -y upgrade
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r ./requirements.txt


CMD ["python", "main.py"]

