# Shulk Bot
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
#--------------------

bot = commands.Bot(command_prefix='S.')
bot_name = "Shulk"

@bot.event                          # Ready Check If Bot Is Online
async def on_ready():
    print("Test Shulk Bot is Running")
    print("I am running on " + bot.user.name)
    print("With the ID: " + bot.user.id)

# Bot Token-------------------------
# https://discordapp.com/oauth2/authorize?client_id=578610124726337547&scope=bot&permissions=999999
bot.run("NTc4NjEwMTI0NzI2MzM3NTQ3.XN2GuA.2aejkyAmJ7o6ovPtZTWuzIlboAs") # Shulk Bot
#bot.run("NTgxMTM3NzM5MDg1MzgxNjMy.XOa4uQ.VklM6dv5PeyrvzpQ-eJLJcw9tK8") # Shulk Test Bot
#bot.run("NTc4OTI1OTI2MDQ2NDk4ODI3.XN6uFw.xV3I_hgem9e6bikdYDII-HDD9q8") # Commander Cody Test Bot
#--------------------