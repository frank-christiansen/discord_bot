import discord
import json
import os

# Bot-Token und Emoji konfigurieren
TOKEN = os.getenv("TOKEN")
EMOJI = discord.PartialEmoji(name='👍')

# Discord-Bot erstellen
intents = discord.Intents.default()
intents.reactions = True
bot = discord.Client(intents=intents, activity=discord.Activity(name="mit Bob", type=1))

# Config-Datei laden
with open('/config/config.json', 'r') as f:
    config = json.load(f)

# Reaction-Handler registrieren
@bot.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == EMOJI and str(reaction.message.id) in config:
        role_id = int(config[str(reaction.message.id)])
        role = discord.utils.get(user.guild.roles, id=role_id)
        if role is not None:
            await user.add_roles(role)
            print(f'Benutzer {user.name} hat die Rolle {role.name} erhalten.')

@bot.event
async def on_reaction_remove(reaction, user):
    if str(reaction.emoji) == EMOJI and str(reaction.message.id) in config:
        role_id = int(config[str(reaction.message.id)])
        role = discord.utils.get(user.guild.roles, id=role_id)
        if role is not None:
            await user.remove_roles(role)
            print(f'Benutzer {user.name} hat die Rolle {role.name} verloren.')

# Bot starten
bot.run(TOKEN)