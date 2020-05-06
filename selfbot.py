import discord							#Loading libraries
from discord.ext import commands


#Next all the lines as in the usual discord.py bot
client = commands.Bot(command_prefix="😄", self_bot=True) #The Emoji will be a prefix. We must specify self_bot=True
owner = "327753433811517441" #Your id, you do not need to specify because the team except you in any case, no one can
client.remove_command('help') #Delete the standard help command


#Then we do everything as in the bot discord.py, commands, events

#EXAMPLE <3
@client.event
async def on_ready():
    print("started")

@client.command()
async def clear(ctx, amount = 0):
	await ctx.channel.purge(limit=amount)


@client.command(name='rl')
async def restart_cmd(ctx):
    '''Перезагрузка бота.'''
    await ctx.send("> `restarted`")
    await ctx.message.delete()
    import os, sys
    os.execl(sys.executable, sys.executable, * sys.argv)
	
@client.command()
async def emb(ctx, cntnt):
    emd = discord.Embed(colour= 0x19ff19, title= "title", url="https://discord.gg/Rc7s3j3")
    emd.set_author(name= "• iAviCii •")
    emd.add_field(name= " ᠌ ᠌ ᠌᠌ ᠌ ᠌ ᠌ ᠌ ᠌ ", value=f'```{cntnt}```')
    emd.set_footer(text= "• iAviCii •", icon_url= "https://i.pinimg.com/originals/85/24/6b/85246bdc4a9e75abada664514153d921.png")
    await ctx.send(embed=emd)
    await ctx.message.delete()


#Specifying your user's token in Discord
client.run("YOUR TOKEN", bot=False) #Be sure to specify bot=False
