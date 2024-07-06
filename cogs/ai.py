import discord
import datetime
from discord.ext import commands
import config
from utils.tools import generate_from_prompt



class GeminiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='ai',
        aliases=['query']
    )
    async def gptcommand(self, ctx: commands.Context, *, prompt: str = None):
        await ctx.typing()
        if prompt is None:
            return await ctx.reply('`⚠️` Error : Prompt is a required parameter..')
        response = await generate_from_prompt(prompt=prompt)
        embed = discord.Embed(
            color=0x2b2d31,
            description=response,
            title=f'Query : {prompt}',
            timestamp=datetime.datetime.now()
        )
        embed.set_footer(text='generated with gooogle gemini', icon_url=config.Media.google)
        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(GeminiCog(bot))