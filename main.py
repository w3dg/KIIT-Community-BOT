import os
import discord
from discord.ext import commands, tasks
from requests import get
import json

client = commands.Bot(command_prefix=",")

@client.event
async def on_ready():
  auto_meme.start()
  print("we have logged in as {0.user}".format(client))

@client.command()
async def hi(ctx):
   await ctx.reply("hi")

  
@tasks.loop(seconds=3600)
async def auto_meme():
    c=986350107496677456
    channel = client.get_channel(c)
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await channel.send(embed=meme)

@client.command()
async def meme(ctx):
    content = get("https://meme-api.herokuapp.com/gimme").text
    data = json.loads(content,)
    meme = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")
    await ctx.reply(embed=meme)


from keep_alive import keep_alive
keep_alive()
my_secret = os.environ['Token']
client.run(my_secret)