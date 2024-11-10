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
        if len(response) > 4096:
            response = response[:4092] + '....'
        embed = discord.Embed(
            color=config.color,
            description=response,
            title=f'Query : {prompt}',
            timestamp=datetime.datetime.now()
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.set_footer(text='generated with gooogle gemini', icon_url=config.Media.google)
        try:
            await ctx.reply(embed=embed)
        except:
            await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(GeminiCog(bot))