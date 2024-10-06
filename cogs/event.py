import discord
import random
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_member_join")
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(1247301224534114387)
        emotes = member.guild.emojis
        if emotes:
            emote = random.choice(emotes)
            await channel.send(f"{emote} Hey {member.mention}, Welcome to {member.guild.name}.")
        else:
            await channel.send(f"👋 Hey {member.mention}, Welcome to {member.guild.name}.")

async def setup(bot):
    await bot.add_cog(Events(bot))