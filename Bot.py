import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = "/")
status = cycle(['Make a thing','Study coding'])







#events
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle)
    change_status.start()
    print('I am now Online!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Quack! Quack! Your Command Is Not Found!')
       

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))








#commands

@bot.command()
async def say(ctx, *, msg):
    await ctx.send(msg)
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 100)}ms')
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)
    
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason='Misbehavior'):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
    
@client.command()
@commands.has_permissions(administrator=True)
async def ban_add(ctx, member : discord.Member, *, reason='Misbehavior'):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')
    
@client.command()
@commands.has_permissions(administrator=True)
async def ban_del(ctx, *, member):
    banned_users = await ctx.guild.bans()
    mamber_name, member_discrikinator = member.split('#')
    
    for banned_entry in banned_users:
        user = banned_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
            
client.run(os.getenv('Token'))
