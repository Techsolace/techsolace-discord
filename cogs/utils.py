import discord
from discord.ext import commands


class UtilCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"🏓 Pong : {round(self.bot.latency * 1000)} ms")


async def setup(bot):
    await bot.add_cog(UtilCommands(bot))