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

    @commands.command(aliases=["si", "guildinfo"])
    async def serverinfo(self, ctx):
        server = ctx.guild

        serverRoles = ", ".join([str(r.name) for r in server.roles]
                                ).replace("@everyone", "everyone")
        if len(serverRoles) > 1024:
            roles = "Too many roles to display"

        serverEmbed = discord.Embed(
            title="**Server information**",
            description=f"**Server icons: ** [Click here]({server.icon_url})",
            color=discord.Color.from_rgb(225, 225, 225)
        )
        serverEmbed.set_author(
            name=server.name,
            icon_url=server.icon_url
        )
        serverEmbed.set_thumbnail(url=server.icon_url)
        serverEmbed.add_field(
            name="Server name: ",
            value=f"```yaml\n{server.name}```",
            inline=True
        )
        serverEmbed.add_field(
            name="**Server ID: **",
            value=f"```yaml\n{server.id}```",
            inline=True
        )
        serverEmbed.add_field(
            name="**Server Owner: **",
            value=f"```yaml\n{server.owner}```",
            inline=True
        )
        serverEmbed.add_field(
            name="**Server Region: **",
            value=f"```yaml\n{server.region}```",
            inline=True
        )
        serverEmbed.add_field(
            name="**Verification Level: **",
            value=f"```yaml\n{server.verification_level}```",
            inline=True
        )
        serverEmbed.add_field(
            name="**Server Member Count: **",
            value=f"```yaml\n{server.member_count} Users```",
            inline=True
        )
        serverEmbed.add_field(
            name="**Server Created At: **",
            value=f"```yaml\n{server.created_at}```",
        )
        serverEmbed.add_field(
            name="**Server Roles: **",
            value=serverRoles,
            inline=False
        )
        serverEmbed.set_footer(
            text="Requested by: " + ctx.author.name,
            icon_url=ctx.author.avatar_url
        )

        await ctx.reply(embed=serverEmbed)

    @commands.command(aliases=["ui"])
    async def userinfo(self, ctx, member: discord.Member = None):
        user = ctx.author if member is None else member

        userRoles = ", ".join([str(r.name) for r in user.roles]).replace(
            "@everyone", "everyone")
        hypesquad_class = str(user.public_flags.all()).replace(
            '[<UserFlags.', '').replace('>]', '').replace('_', ' ').replace(':', '').title()
        hypesquad_class = ''.join(
            [i for i in hypesquad_class if not i.isdigit()])
        if len(userRoles) > 1024:
            roles = "Too many roles to display"

        if hypesquad_class == "[]":
            hypesquad_class = "```yaml\nNone```"
        if user.activity is None:
            activity = "None"
        userEmbed = discord.Embed(
            title="**User information**",
            description=f"**User icons: ** [Click here]({user.avatar_url})",
            color=discord.Color.from_rgb(225, 225, 225)
        )
        userEmbed.set_author(
            name=user.name,
            icon_url=user.avatar_url
        )
        userEmbed.set_thumbnail(url=user.avatar_url)
        userEmbed.add_field(
            name="User name: ",
            value=f"```yaml\n{user.name}```",
            inline=True
        )
        userEmbed.add_field(
            name="**User Discriminator: **",
            value=f"```yaml\n{user.discriminator}```",
            inline=True
        )
        userEmbed.add_field(
            name="**User ID: **",
            value=f"```yaml\n{user.id}```",
            inline=True
        )
        userEmbed.add_field(
            name="Badges: ",
            value=hypesquad_class,
            inline=True
        )
        userEmbed.add_field(
            name="**User Status: **",
            value=f"```yaml\n{user.status}```",
            inline=True
        )
        userEmbed.add_field(
            name="**User Activity: **",
            value=f"```yaml\n{user.activity}```",
            inline=True
        )
        userEmbed.add_field(
            name="**User Created At: **",
            value=f"```yaml\n{user.created_at}```",
            inline=False
        )
        if ctx.guild is not None:
            userEmbed.add_field(
                name="**User Joined At: **",
                value=f"```yaml\n{user.joined_at}```",
                inline=False
            )

        userEmbed.add_field(
            name="**User Roles: **",
            value=userRoles,
            inline=False
        )
        userEmbed.set_footer(
            text="Requested by: " + ctx.author.name,
            icon_url=ctx.author.avatar_url
        )

        await ctx.reply(embed=userEmbed)


def setup(client):
    client.add_cog(Info(client))
