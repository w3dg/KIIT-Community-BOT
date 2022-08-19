import discord
from discord.ext import commands

import random


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        pingImage = [
            "https://cdn.discordapp.com/attachments/892794857905602560/892794900863660062/63e1657a8a6249a2fc9c062b17f27ce0.gif",
            "https://cdn.discordapp.com/attachments/892794857905602560/892795017104613376/dc87c9ea90b4b7d02a0cbe5de256d385.gif",
            "https://cdn.discordapp.com/attachments/892794857905602560/892795143093108806/a665463e60ef772c82286e4ee6a15353.gif",
            "https://cdn.discordapp.com/attachments/892794857905602560/892795222986207293/4a3a4f44524556704c29879feeba0c23.gif",
            "https://cdn.discordapp.com/attachments/892794857905602560/892795292573913098/534d38d35eb761ad11e43fe378c3de29.gif",
            "https://cdn.discordapp.com/attachments/892794857905602560/892795346172928080/c17166b2af1a743b149e1eb0f3203db4.gif",
            "https://cdn.discordapp.com/attachments/892794857905602560/892795432797872188/6619fe492c713eb3051ab7568181dbdd.gif"
        ]
        randomPingImage = pingImage[int(len(pingImage) * random.random())]

        pingEmbed = discord.Embed(
            title="🏓 Pong!",
            description="The bot has responded!",
            color=discord.Color.green()
        )
        pingEmbed.set_thumbnail(url=randomPingImage)
        pingEmbed.add_field(
            name="Latency: ",
            value=f"{round(self.client.latency * 1000)}ms"
        )
        pingEmbed.set_footer(text="Requested by: " + ctx.author.name)

        await ctx.reply(embed=pingEmbed)


def setup(client):
    client.add_cog(Info(client))
