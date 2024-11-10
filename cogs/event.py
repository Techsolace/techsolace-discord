import config
import discord
import random
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_member_join")
    async def on_member_join(self, member: discord.Member):
        welcome_channel = self.bot.get_channel(1305282955886989342)
        channel = self.bot.get_channel(1305285670192939128)
        emotes = member.guild.emojis
        embed = discord.Embed(
            color=config.color,
            title=f'Welcome to {member.guild.name}!',
            description=
            f'> 📕 Read the [Rules]({config.Links.rules})\n'
            f'> 📢 Meet new people [Roles]({config.Links.chat})\n'
            f'> 🎉 Keep an eye in the [Updates]({config.Links.annc})\n'
        )
        embed.set_author(
            name=member.name,
            icon_url=member.avatar.url
        )
        embed.set_image(
            url=config.Media.welcome_banner
        )
        if emotes:
            emote = random.choice(emotes)
            await channel.send(f"{emote} Hey {member.mention}, Welcome to {member.guild.name}.")
        else:
            await channel.send(f"👋 Hey {member.mention}, Welcome to {member.guild.name}.")
        await welcome_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Events(bot))