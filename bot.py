import discord
import os
from discord.ext import commands

import runtimeHandler

# prefix
client = commands.Bot(command_prefix="-")

# on ready event


@client.event
async def on_ready():
    print("{0.user} is ready!".format(client))

# Error handler


@client.event
async def on_command_errot(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing required argument")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Missing permissions")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("Bot missing permissions")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Check failure")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Command on cooldown")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("Command invoke error")
    elif isinstance(error, commands.CommandError):
        await ctx.send("Command error")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Missing permissions")
    elif isinstance(error, commands.NotOwner):
        await ctx.send("Not owner")
    elif isinstance(error, commands.MissingAnyRole):
        await ctx.send("Missing any role")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("Missing role")
    elif isinstance(error, commands.NSFWChannelRequired):
        await ctx.send("NSFW channel required")
    elif isinstance(error, commands.PrivateMessageOnly):
        await ctx.send("Private message only")
    elif isinstance(error, commands.NoPrivateMessage):
        await ctx.send("No private message")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Bad argument")
    elif isinstance(error, commands.ConversionError):
        await ctx.send("Conversion error")
    elif isinstance(error, commands.UserInputError):
        await ctx.send("User input error")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


# runtimeHandler()
# my_secret = os.environ['Token']
# client.run()

client.run("")
