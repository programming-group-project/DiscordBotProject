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
import csv
from csv_files import csv_editor
#--------------------

# Bot Tokens-------------------------
# https://discordapp.com/oauth2/authorize?client_id=578925926046498827&scope=bot&permissions=999999
#TOKEN ="NTc4NjEwMTI0NzI2MzM3NTQ3.XN2GuA.2aejkyAmJ7o6ovPtZTWuzIlboAs" # Shulk Bot
TOKEN ="NTgxMTM3NzM5MDg1MzgxNjMy.XOa4uQ.VklM6dv5PeyrvzpQ-eJLJcw9tK8" # Shulk Test Bot
#TOKEN ="NTc4OTI1OTI2MDQ2NDk4ODI3.XN6uFw.xV3I_hgem9e6bikdYDII-HDD9q8" # Commander Cody Test Bot
#--------------------

#Bot Setup-------------------------
Client = discord.Client()
bot = commands.Bot(command_prefix='S.')
bot_name = "Shulk"
USER_CSV = csv_editor.csv_editor(0)
Prof_CSV = csv_editor.csv_editor(1)
#--------------------

def update_user_csv(ctx, user):          # CSV file updater function
    if user is None:
        user = ctx.message.author
    return USER_CSV.update(user)

@bot.event                              # Ready Check if Bot has Connected
async def on_connect():
    print("Bot has connected")

@bot.event                              # Ready Check If Bot Is Online
async def on_ready():
    print("Shulk Bot is running")
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))

@bot.event                              # Ready Check if Bot has Disconnected
async def on_disconnect():
    print("Bot has disconnected")

@bot.event
async def on_member_join(member):       # Updates csv when member joins and prints who joined
    print(member.name + " has joined")
    temp = USER_CSV.update(member)

@bot.event                              # Prints who leaves
async def on_member_remove(member):
    print(member.name + " has left")

@bot.command(pass_context=True)         # Simple hello command, registers author or who is pinged
async def hello(ctx, user: discord.Member = None):
    await ctx.channel.send(update_user_csv(ctx,user))

@bot.command(pass_context=True)         # Kicks mentioned member, requires kick_members role
async def kick(ctx, user: discord.Member = None):
    command_type = "kick"
    if(ctx.message.author.top_role.permissions.kick_members == True or ctx.message.author.top_role.permissions.administrator == True):
        if(user == None):
            await ctx.channel.send("You cannot " + command_type + " nothing... ")
        elif(user.top_role.permissions.kick_members == True or user.top_role.permissions.administrator == True):
            await ctx.channel.send("You cannot " + command_type + " this person")
        else:
            await ctx.channel.send("Goodbye " + user.name)
            await user.kick()
    else:
        await ctx.channel.send("You don't have permissions for this command ")

@bot.command(pass_context=True)         # Bans mentioned member, requires ban_members role
async def ban(ctx, user: discord.Member = None):
    command_type = "ban"
    if(ctx.message.author.top_role.permissions.ban_members == True or ctx.message.author.top_role.permissions.administrator == True):
        if(user == None):
            await ctx.channel.send("You cannot " + command_type + " nothing... ")
        elif(user.top_role.permissions.ban_members == True or user.top_role.permissions.administrator == True):
            await ctx.channel.send("You cannot " + command_type + " this person")
        else:
            await ctx.channel.send("Goodbye " + user.name)
            await user.ban()
    else:
        await ctx.channel.send("You don't have permissions for this command ")

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

# Runs Bot--------------------
bot.run(TOKEN)