import discord
import config
from discord.ext import commands

class ModerationCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick', aliases=['gm'])
    @commands.is_owner()
    async def kick_cmd(self, ctx: commands.Context, member: discord.Member = None, *, reason: str = None):
        if member is None:
            return await ctx.send("`⚠️` : Member is a required value.")
        if reason is None:
            reason = "no reason provided"
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(
                color=config.color,
                title=f'Kicked.',
                description=
                f'Name: {member.name}\n'
                f'ID: {member.id}\n'
                f'Reason: {reason}'
            )
            embed.set_author(name=ctx.author.name)
            try:
                await member.send(f"`🚨` You have been kicked from {ctx.guild.name}.\nReason : {reason}")
            except:
                pass
            return await ctx.reply(content=f"**Sucessfully Kicked : {member.mention}**",embed=embed)
        except Exception as e:
            return await ctx.send(f"`⚠️` Error: {e}")
        

    @commands.command(name='ban')
    @commands.is_owner()
    async def ban_cmd(self, ctx: commands.Context, member: discord.Member = None, *, reason: str = None):
        if member is None:
            return await ctx.send("`⚠️` : Member is a required value.")
        if reason is None:
            reason = "no reason provided"
        try:
            await member.ban(reason=f"banned by : {ctx.author.name} : {reason}")
            embed = discord.Embed(
                color=config.color,
                title=f'Banned.',
                description=
                f'Name: {member.name}\n'
                f'ID: {member.id}\n'
                f'Reason: {reason}'
            )
            embed.set_author(name=ctx.author.name)
            try:
                await member.send(f"`🚨` You have been banned from {ctx.guild.name}.\nReason : {reason}")
            except:
                pass
            return await ctx.reply(content=f"**Sucessfully Banned : {member.mention}**",embed=embed)
        except Exception as e:
            return await ctx.send(f"`⚠️` Error: {e}")
        
    @commands.command(name='unban')
    @commands.is_owner()
    async def unban_cmd(self, ctx: commands.Context, member_id: int):
        try:
            banned_users = await ctx.guild.bans()
            for ban_entry in banned_users:
                user = ban_entry.user
                if user.id == member_id:
                    await ctx.guild.unban(user, reason=f"unbanned by : {ctx.author.name}")
                    embed = discord.Embed(
                        color=config.color,
                        title=f'Unbanned.',
                        description=
                        f'Name: {user.name}\n'
                        f'ID: {user.id}\n'
                    )
                    embed.set_author(name=ctx.author.name)
                    return await ctx.reply(content=f"**Successfully Unbanned : {user.mention}**", embed=embed)
            return await ctx.send("`⚠️` User not found in the bans list.")
        except Exception as e:
            return await ctx.send(f"`⚠️` Error: {e}")
    

    @commands.command(
        name='purge',
        aliases=['clear']
    )
    @commands.has_permissions(manage_messages=True)
    async def clearmsgs(self, ctx: commands.Context, amount: int):
        try:
            if amount <=0:
                amount = 10
            deleted = await ctx.channel.purge(limit=amount +1, reason=f'clear command used by : {ctx.author.name}')
            return await ctx.send(f'`🗑️` : Successfully deleted {len(deleted)} messages from {ctx.channel.mention}', delete_after=5)
        except Exception as e:
            return await ctx.send(f"`⚠️` Error: {e}")



async def setup(bot):
    await bot.add_cog(ModerationCommands(bot))