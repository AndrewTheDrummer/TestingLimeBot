import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class Poll(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 10, BucketType.user)
    async def poll(self, ctx, *, poll): 
        #Poll format: ;poll Should x be allowed to join? | :Zero:=Yes :One:=No
        poll = poll.split(" | ")
        pollmessage = poll[0]
        poll = poll[1].split(" ")
        reactions = []
        for i in poll: 
            a = i.split("=")
            pollmessage += f"\n{a[0]} {a[1]}"
            reactions.append(f"{a[0]}")
        reactto = await ctx.send(pollmessage)
        for i in reactions:
            await reactto.add_reaction(i)
        
def setup(client):
    client.add_cog(Poll(client))
