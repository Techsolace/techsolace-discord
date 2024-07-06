import os
import discord
import jishaku
from discord.ext import commands


bot = commands.Bot(
    command_prefix='.',
    intents=discord.Intents.all(),
    allowed_mentions = discord.AllowedMentions(
        everyone=False,
        roles=False
    ),
    help_command=None,
    status = discord.CustomActivity(name='.gg/techsolace', status=discord.Status.dnd)
)
bot.owner_ids = [1139950107995934863, 680820132355899622, 1148259965946052619]


@bot.event
async def on_ready():
    for files in os.listdir('./cogs'):
        if files.endswith(".py"):
            try:
                await bot.load_extension(f'cogs.{files[:-3]}')
            except Exception as e:
                print(e)
    await bot.load_extension("jishaku")
    print(f'Logged in as {bot.user.name}')

bot.run(os.environ.get("TOKEN"))