# Commander Cody
'''
General purpose bot based on Shulk
'''
# By Sage, Josh, and Harrison

#Imports--------------------
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
import random
import csv
from csv_files import csv_editor
#--------------------

# Bot Tokens-------------------------
# https://discordapp.com/oauth2/authorize?client_id=578925926046498827&scope=bot&permissions=999999
#TOKEN ="NTc4NjEwMTI0NzI2MzM3NTQ3.XN2GuA.2aejkyAmJ7o6ovPtZTWuzIlboAs" # Shulk Bot
TOKEN ="NTgxMTM3NzM5MDg1MzgxNjMy.XOa4uQ.VklM6dv5PeyrvzpQ-eJLJcw9tK8" # Shulk Test Bot
#TOKEN ="NTc4OTI1OTI2MDQ2NDk4ODI3.XN6uFw.xV3I_hgem9e6bikdYDII-HDD9q8" # Commander Cody Test Bot
#--------------------

Client = discord.Client()
bot = commands.Bot(command_prefix='s.')
bot_name = "Test Shulk Bot"
USER_CSV = csv_editor.csv_editor(0)
Prof_CSV = csv_editor.csv_editor(1)

def update_user_csv(ctx, user):          # CSV file updater function
    if user is None:
        user = ctx.message.author
    return USER_CSV.update(user)

@bot.event                          # Ready Check If Bot Is Online
async def on_ready():
    print("Bot is running")
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))

@bot.command(pass_context=True)
async def hello(ctx, user: discord.Member = None):
    await ctx.channel.send(update_user_csv(ctx,user))

'''@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice_channel
    await bot.connect(channel)

@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()

@bot.command(pass_context=True)
async def play(ctx, arg, user: discord.Member = None):
    await ctx.channel.send("This doesn't work yet")'''

# NEEDS TESTING--------------------
'''@bot.event
async def on_message(message):      # CSV file updater
    user = message.author
    temp = CSV.update(user.name,user.id)'''
#--------------------

bot.run(TOKEN)