FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install -y git

RUN git clone https://github.com/frank-christiansen/discord_bot.git

WORKDIR /app/discord_bot

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]

# docker build --tag kleinundhilflos_bot .
# docker image tag kleinundhilflos_bot kleinundhilflos/discord_bot
# docker push kleinundhilflos/discord_bot