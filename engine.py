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
#--------------------

Client = discord.Client()
bot = commands.Bot(command_prefix=']]')
bot_name = "Commander Cody"

chat_filter = ["OWO","UWU", "EWE", "0W0", "()W()", "()//()"]

@bot.event                          # Ready Check If Bot Is Online
async def on_ready():
    print("Sector is Clear - Bot")
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))

'''
@bot.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            await message.delete()
            await message.channel.send("NO DEGENERACY")
'''

@bot.command(pass_context=True)
async def hellothere(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    await ctx.channel.send("General " + user.name + ".")

@bot.command(pass_context=True)
async def filteradd(ctx, arg, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    if(user.top_role.permissions.manage_messages == True or user.top_role.permissions.administrator == True):
        chat_filter.append(arg.upper())
        print(chat_filter)
        await ctx.channel.send("Added " + str(arg) + " to the chat filter.")
    else:
        await ctx.channel.send("Mind tricks don't work on me.")

@bot.command(pass_context=True)
async def filterdelete(ctx, arg, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    if(user.top_role.permissions.manage_messages == True or user.top_role.permissions.administrator == True):
        chat_filter.remove(arg.upper())
        print(chat_filter)
        await ctx.channel.send("Removed " + str(arg) + " from the chat filter.")
    else:
        await ctx.channel.send("Mind tricks don't work on me.")

@bot.command(pass_context=True)
async def chatfilter(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    if(user.top_role.permissions.manage_messages == True or user.top_role.permissions.administrator == True):
        await ctx.channel.send(chat_filter)
    else:
        await ctx.channel.send("Mind tricks don't work on me.")
    

# Bot Token-------------------------
# https://discordapp.com/oauth2/authorize?client_id=578925926046498827&scope=bot&permissions=999999
#bot.run("NTc4NjEwMTI0NzI2MzM3NTQ3.XN2GuA.2aejkyAmJ7o6ovPtZTWuzIlboAs") # Shulk Bot
#bot.run("NTgxMTM3NzM5MDg1MzgxNjMy.XOa4uQ.VklM6dv5PeyrvzpQ-eJLJcw9tK8") # Shulk Test Bot
bot.run("NTc4OTI1OTI2MDQ2NDk4ODI3.XN6uFw.xV3I_hgem9e6bikdYDII-HDD9q8") # Commander Cody Test Bot
#--------------------