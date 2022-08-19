from turtle import title
import discord
from discord.ext import commands

import requests


class Utill(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setMemeChannel(self, ctx, channel: discord.TextChannel):
        # need to find a db for this commmand
        pass

    @commands.command()
    async def meme(self, ctx):
        meme_url = "https://meme-api.herokuapp.com/gimme"
        req_meme = requests.get(meme_url)
        postLink = req_meme.json()['postLink']
        image_url = req_meme.json()['url']
        author = req_meme.json()['author']
        meme_title = req_meme.json()['title']

        meme_embed = discord.Embed(
            title="😂 Meme",
            url=postLink,
            color=discord.Color.from_rgb(66, 135, 245),
            description=f"{meme_title} by {author}"
        )
        meme_embed.set_image(url=image_url)
        meme_embed.set_footer(
            text=f"Requested by: {ctx.author.name}")

        if req_meme.status_code == 200:
            await ctx.reply(embed=meme_embed)
        else:
            await ctx.reply("Something went wrong", delete_after=5)

    @commands.command()
    async def dankmeme(self, ctx):
        dank_meme_url = "https://v2.jokeapi.dev/joke/Dark"
        request_dank = requests.get(dank_meme_url)

        if request_dank.status_code == 200:
            first_line = request_dank.json()['setup']
            last_line = request_dank.json()['delivery']

            await ctx.reply(first_line + '\n' + last_line)
        else:
            await ctx.reply("Some error occured\nPlease try again...", delete_after=5)


def setup(client):
    client.add_cog(Utill(client))
