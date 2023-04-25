FROM python:3.8-slim

VOLUME ["/app"]

WORKDIR /app

RUN pip install discord.py

CMD ["python", "/app/bot.py"]

# docker build --no-cache --tag kleinundhilflos_bot .
# docker image tag kleinundhilflos_bot kleinundhilflos/discord_bot
# docker push kleinundhilflos/discord_bot

# docker run -v C:/Users/chf/Documents/GitHub/discord_bot:/config kleinundhilflos_bot