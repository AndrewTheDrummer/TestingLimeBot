import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get

class Moderation(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user : discord.Member, *, reason=None): 
        if ctx.author.top_role.position > user.top_role.position: 
            await user.send(f"You have been kicked from **{ctx.guild.name}**\nReason:`{reason}`")
            await user.kick(reason=reason)
            await ctx.send(f"**{user.name}** has been kicked by **{ctx.author.name}**\nReason:`{reason}`")
        else: 
            await ctx.send("You don't have permission to use that command")
            
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user : discord.Member, *, reason=None): 
        if ctx.author.top_role.position > user.top_role.position: 
            try:
                await user.send(f"You have been banned from **{ctx.guild.name}**\nReason:`{reason}`")
            except:
                pass
            await user.ban(reason=reason)
            await ctx.send(f"**{user.name}** has been banned by **{ctx.author.name}**\nReason:`{reason}`")
        else: 
            await ctx.send("You don't have permission to use that command")        
        
        
def setup(client):
    client.add_cog(Moderation(client))
