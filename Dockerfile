FROM python:3.9-slim-bookworm
RUN apt update && apt -y upgrade
WORKDIR /app
COPY .env .
COPY . .
RUN pip install --no-cache-dir -r ./requirements.txt && pip install python-dotenv
LABEL maintainer="Elizaveta Taktashova"
CMD echo 'ПРОЙДИТЕ ПО ССЫЛКЕ ДЛЯ ОБЩЕНИЯ С БОТОМ https://t.me/none_gigabot' && python main.py

