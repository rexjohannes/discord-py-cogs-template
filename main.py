import discord
import asyncio
from discord.ext import commands, tasks
from itertools import cycle
import os

description = '''Bot by rexjohannes98#3966'''
bot = commands.Bot(command_prefix=commands.when_mentioned_or"!", description=description)
status = cycle(["My", "Cool", "Presence.", "Here", "you", "can", "add", "more!"])

@bot.event
async def on_ready():
    change_status.start()
#    await bot.change_presence(activity=discord.Game("GAME"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.utils.oauth_url(bot.user.id))

@tasks.loop(seconds=120)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing Argument!")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not Found!")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don´t have Permssions to do that!")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("The Bot hasn`t the missing Permission!")
    if isinstance(error, commands.NotOwner):
        await ctx.send("This Command is only for my Lord!")

        
bot.remove_command('help')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loding {extension}...")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloading {extension}...")

@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Reloding {extension}...")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")
  
  
bot.run('TOKEN')
