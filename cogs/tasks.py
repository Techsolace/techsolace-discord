import discord
from discord.ext import commands, tasks

class Tasks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.update_server_stats.start()




async def setup(bot):
    await bot.add_cog(Tasks(bot))