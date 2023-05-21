# This Bot requires the 'members' privileged intents

import discord
import os

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.emoji = discord.PartialEmoji(name='👍')
        self.message_to_role = {
            # message_id: role_id,
            1090166907556085891: 1085330636392366130, # Valorant
            1090184934112632873: 1086363791291334737, # Rust
            1090654473061413055: 1090653083895341228, # Among Us
            1091415883236257946: 1091386165589975101, # Call of Duty
            1091418092535549993: 1091386409543290970, # Apex Legends
            1091420519687008326: 1091386471023390871, # Minecraft
            1091422509758427207: 1091386565097431141, # Schach
            1091425383359983706: 1091386618478338119, # Pummelparty
            1091427331358326834: 1091386693275353190, # League of Legends
            1093167919799742654: 1093167182369796188, # Warframe
            1092374453977104445: 1092372910020239412, # Sea of Thieves
            1094259588041289778: 1094257982432362506, # Diablo
            1100390082613100555: 1100388624622694450, # Overwatch
        }

    # Rollen hinzufuegen
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        if payload.message_id in self.message_to_role:
            guild = self.get_guild(payload.guild_id)
            if not guild is None:
                if payload.emoji == self.emoji:
                    role = guild.get_role(self.message_to_role[payload.message_id])
                    if not role is None:
                        try:
                            await payload.member.add_roles(role)
                        except discord.HTTPException:
                            pass

    # Rollen entfernen
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        if payload.message_id in self.message_to_role:
            guild = self.get_guild(payload.guild_id)
            if not guild is None:
                if payload.emoji == self.emoji:
                    role = guild.get_role(self.message_to_role[payload.message_id])
                    if not role is None:
                        member = guild.get_member(payload.user_id)
                        if not member is None:
                            try:
                                await member.remove_roles(role)
                            except discord.HTTPException:
                                pass

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents, activity=discord.Activity(name="mit Bob", type=1))

client.run(os.getenv("TOKEN"))