# This Bot requires the 'members' privileged intents

import discord

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    # # # # # # # # # # # #
    # Rollen hinzufuegen  #
    # # # # # # # # # # # #
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""

        ### VALORANT
        if payload.message_id == 1090166907556085891: # ID of the Message
            guild = self.get_guild(payload.guild_id)
            if not guild is None:
                if payload.emoji == discord.PartialEmoji(name='👍'):
                    role = guild.get_role(1085330636392366130) # ID of the role
                    if not role is None:
                        try:
                            await payload.member.add_roles(role)
                        except discord.HTTPException:
                            pass

        ### RUST
        if payload.message_id == 1090184934112632873: # ID of the Message
            guild = self.get_guild(payload.guild_id)
            if not guild is None:
                if payload.emoji == discord.PartialEmoji(name='👍'):
                    role = guild.get_role(1086363791291334737) # ID of the role
                    if not role is None:
                        try:
                            await payload.member.add_roles(role)
                        except discord.HTTPException:
                            pass



    # # # # # # # # # # #
    # Rollen entfernen  #
    # # # # # # # # # # #
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""

        ### VALORANT
        if payload.message_id == 1090166907556085891: # ID of the Message
            guild = self.get_guild(payload.guild_id)
            if not guild is None:
                if payload.emoji == discord.PartialEmoji(name='👍'):                    
                    role = guild.get_role(1085330636392366130) # ID of the Role
                    if not role is None:
                        member = guild.get_member(payload.user_id)
                        if not member is None:
                            try:
                                await member.remove_roles(role)
                            except discord.HTTPException:
                                pass

        ### RUST
        if payload.message_id == 1090184934112632873: # ID of the Message
            guild = self.get_guild(payload.guild_id)
            if not guild is None:
                if payload.emoji == discord.PartialEmoji(name='👍'):                    
                    role = guild.get_role(1086363791291334737) # ID of the Role
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

client.run('MTA4ODQ1NTI2ODc3OTcwMDMxNQ.GcIp_u.zslbIY_1T9VnNYsP3PWK_2Men-izfXPONafQoo')