# Shulk Bot
'''
General purpose bot based on Shulk
'''
# By Sage, Josh, and Harrison

#Imports--------------------
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
#--------------------

bot = commands.Bot(command_prefix='\\')
bot_name = "Shulk"

# Bot Token
# https://discordapp.com/oauth2/authorize?client_id=578610124726337547&scope=bot&permissions=999999
bot.run("NTc4NjEwMTI0NzI2MzM3NTQ3.XN2GuA.2aejkyAmJ7o6ovPtZTWuzIlboAs")