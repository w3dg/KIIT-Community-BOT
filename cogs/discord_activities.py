from ast import Pass
import discord
from discord.ext import commands


class DiscordActivities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def activites():
        Pass


async def setup(client):
    await client.add_cog(DiscordActivities(client))
