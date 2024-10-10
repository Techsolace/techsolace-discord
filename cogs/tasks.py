import discord
from discord.ext import commands, tasks

class Tasks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @tasks.loop(seconds=180)
    async def update_server_stats(self):
        guild = self.bot.get_guild(1237816968443334740)
        if guild is not None:
            channel = guild.get_channel(1292620756630507560)
            await channel.edit(name=f"members : {guild.member_count}")

async def setup(bot):
    bot.add_cog(Tasks(bot))