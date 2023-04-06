FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY bot.py bot.py

CMD ["python3", "bot.py"]

# docker build --tag kleinundhilflos_bot .
# docker image tag kleinundhilflos_bot kleinundhilflos/discord_bot
# docker push kleinundhilflos/discord_bot