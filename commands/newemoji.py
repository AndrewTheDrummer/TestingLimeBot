import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

class NewEmoji(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_emojis=True)
    async def newemoji(self, ctx, emojiname): 
        image = await ctx.message.attachments[0].read()
        newemote = await ctx.guild.create_custom_emoji(name=emojiname, image=image)
        await ctx.send(f"Created a new emoji! {str(newemote)}")
        
def setup(client):
    client.add_cog(NewEmoji(client))
