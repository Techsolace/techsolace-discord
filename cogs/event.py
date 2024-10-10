import config
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

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        premium_channel = self.bot.get_channel(1248447678187049065)
        if before.guild.premium_subscriber_role in after.roles:
            emotes = after.guild.emojis
            emote = random.choice(emotes)
            embed = discord.Embed(
                color=config.color,
                description=f'{after.guild.name} currently has {len(after.guild.premium_subscribers)} boosters!,\n{len(after.guild.premium_tier)} boost level! and\n{len(after.guild.premium_subscription_count)} total boosts!'
            )
            embed.set_author(
                name=after.name,
                icon_url=after.avatar.url
            )
            embed.set_footer(text=f"{after.name} just boosted the server!")
            await premium_channel.send(f"{emote} Thankyou, {after.mention} for boosting {after.guild.name}", embed=embed)

async def setup(bot):
    await bot.add_cog(Events(bot))