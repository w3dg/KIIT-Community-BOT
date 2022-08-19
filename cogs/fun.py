import datetime
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import requests
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['d'])
    async def dare(self, ctx, member: discord.Member = None):
        user = ctx.author if member is None else member

        if user.id == self.client.user.id:
            await ctx.send("I can't do that")
        elif user.id == ctx.author.id:
            await ctx.send("You can't do that")
        else:
            url = "https://raw.githubusercontent.com/losier/Kiri/master/Data/TextData/Dare.json"
            response = requests.get(url)
            data = response.json()
            random_data = data[random.randint(0, len(data) - 1)]

            dare_embed = discord.Embed(
                title=f"{user.name}'s dare",
                description=f"{user.mention} Here is a dare for you from {ctx.author.name}\n\n*{random_data}*",
                color=discord.Color.blue()
            )
            dare_embed.set_thumbnail(
                url="https://media.tenor.com/images/3408860a5f846d39283b01e5d6b5712d/tenor.gif")
            dare_embed.timestamp = datetime.datetime.utcnow()

            await ctx.reply(embed=dare_embed)

    @commands.command(aliases=['t'])
    async def truth(self, ctx, member: discord.Member = None):
        user = ctx.author if member is None else member

        if user.id == self.client.user.id:
            await ctx.send("I can't do that")
        elif user.id == ctx.author.id:
            await ctx.send("You can't do that")
        else:
            url = "https://raw.githubusercontent.com/losier/Kiri/master/Data/TextData/Truth.json"
            response = requests.get(url)
            data = response.json()
            random_data = data[random.randint(0, len(data) - 1)]

            truth_embed = discord.Embed(
                title=f"{user.name}'s dare",
                description=f"{user.mention}, {ctx.author.name} wanted to know that:\n\n*{random_data}*",
                color=discord.Color.blue()
            )
            truth_embed.set_thumbnail(
                url="https://media.tenor.com/images/b2f04c9d19c4378840741fcdcd41fc5f/tenor.gif")
            truth_embed.timestamp = datetime.datetime.utcnow()

            await ctx.reply(embed=truth_embed)

    @commands.command()
    async def topic(self, ctx):
        url = "https://raw.githubusercontent.com/losier/Kiri/master/Data/TextData/Topic.json"
        response = requests.get(url)
        data = response.json()
        random_data = data[random.randint(0, len(data) - 1)]

        topic_embed = discord.Embed(
            title="🥠Topic",
            description=f"*{random_data}*",
            color=discord.Color.blue()
        )
        topic_embed.timestamp = datetime.datetime.utcnow()

        await ctx.reply(embed=topic_embed)

    @commands.command()
    async def nickname(self, ctx, member: discord.Member = None):
        pass


def setup(client):
    client.add_cog(Fun(client))
