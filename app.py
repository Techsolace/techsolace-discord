import os
import discord
import jishaku
import config
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(
    command_prefix='.',
    intents=discord.Intents.all(),
    allowed_mentions = discord.AllowedMentions(
        everyone=False,
        roles=False
    ),
    activity = discord.CustomActivity(name='.gg/techsolace | elevate your brand with our digital mastery', emoji="🎨"),
    help_command=None
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

@bot.check
async def check_owners(ctx: commands.Context):
    allowed = ["ai", "query", "ping"]
    if ctx.command.qualified_name not in allowed and ctx.author.id not in bot.owner_ids:
        embed = discord.Embed(
            color=config.color,
            description=f"`❌` {ctx.author.mention}: You cannot use this command.\nThis bot is restricted to the server owners.\nOnly limited commands are available for the users."
        )
        await ctx.reply(embed=embed)
        return False
    return True

bot.run(str(os.environ.get("TOKEN")))