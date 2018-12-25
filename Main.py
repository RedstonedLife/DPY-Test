import discord
from discord.ext import commands
import asyncio
import os

bot = commands.Bot(command_prefix=os.environ['PREFIX'])
# Getting Environ Vars os.environ['VAR_NAME']



@bot.event
async def on_ready():
  print(bot.user.name)

  
#A SIMPLE TEST COMMAND
@bot.command(pass_context=True)
async def hi(ctx):
  await bot.say("Hello there"+" "+ctx.message.author.name)
  
  
 
bot.run(os.environ['TOKEN'])
