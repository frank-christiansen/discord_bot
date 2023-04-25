FROM python:3.8-slim

WORKDIR /app

COPY bot.py /app/bot.py

VOLUME ["/config"]

RUN pip install discord.py

CMD ["python", "/app/bot.py"]

# docker build --no-cache --tag kleinundhilflos_bot .
# docker image tag kleinundhilflos_bot kleinundhilflos/discord_bot
# docker push kleinundhilflos/discord_bot