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
import embedstats
#--------------------

# Bot Tokens-------------------------
# https://discordapp.com/oauth2/authorize?client_id=578925926046498827&scope=bot&permissions=999999
TOKEN ="NTc4NjEwMTI0NzI2MzM3NTQ3.XN2GuA.2aejkyAmJ7o6ovPtZTWuzIlboAs" # Shulk Bot
#TOKEN ="NTgxMTM3NzM5MDg1MzgxNjMy.XOa4uQ.VklM6dv5PeyrvzpQ-eJLJcw9tK8" # Shulk Test Bot
#TOKEN ="NTc4OTI1OTI2MDQ2NDk4ODI3.XN6uFw.xV3I_hgem9e6bikdYDII-HDD9q8" # Commander Cody Test Bot
#TOKEN = "NTg1ODQ2MDQyMTkzNDI4NDgw.XPfbPw.K5XqvDwiU4-erIKN40Qco6G4V1c" # Com-Com Test Bot
#--------------------

# Bot Setup-------------------------
Client = discord.Client()
bot = commands.Bot(command_prefix='S.')
bot_name = "Shulk"
USER_CSV = csv_editor.csv_editor(0)
PROF_CSV = csv_editor.csv_editor(1)
#--------------------

# Josh's Stupid Things--------------------
Stalin = embedstats.embedstats(0)
Jong_Un = embedstats.embedstats(1)
Drumpf = embedstats.embedstats(2)
Sam = embedstats.embedstats(3)
Lord = embedstats.embedstats(4)
Wood = embedstats.embedstats(5)
Shulk = embedstats.embedstats(6)
Comrade = embedstats.embedstats(7)
#--------------------

# Functions--------------------
def update_user_csv(ctx, user):          # CSV file updater function
    if user is None:
        user = ctx.message.author
    return USER_CSV.update(user)
#--------------------

# Events--------------------
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

@bot.event
async def on_message(message):          # Chat Filter
    temp = USER_CSV.update(message)
    await bot.process_commands(message.author)
    contents = message.content.split(" ")
    chat_filter = PROF_CSV.read_csv()
    if(message.author.id != 578925926046498827):
        for word in contents:
            if word.upper() in chat_filter:
                await message.delete()
                await message.channel.send("NO DEGENERACY")

#--------------------

# Commands--------------------
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

@bot.command(pass_context=True)
async def filteradd(ctx, arg, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    if(user.top_role.permissions.manage_messages == True or user.top_role.permissions.administrator == True):
        await ctx.channel.send(PROF_CSV.add_profanity(arg.upper()))
    else:
        await ctx.channel.send("Mind tricks don't work on me.")

@bot.command(pass_context=True)
async def filterdelete(ctx, *, arg, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    if(user.top_role.permissions.manage_messages == True or user.top_role.permissions.administrator == True):
        await ctx.channel.send(PROF_CSV.remove_profanity(arg.upper()))
    else:
        await ctx.channel.send("Mind tricks don't work on me.")

@bot.command(pass_context=True)
async def chatfilter(ctx, user: discord.Member = None):
    if user is None:
        user = ctx.message.author
    if(user.top_role.permissions.manage_messages == True or user.top_role.permissions.administrator == True):
        await ctx.channel.send(PROF_CSV.read_csv())
    else:
        await ctx.channel.send("Mind tricks don't work on me.")

@bot.command(pass_context=True)
async def stats(ctx, arg):
    if(arg.upper() == "Stalin"):
        stat = Stalin
    elif(arg.upper() == "Kim"):
        stat = Jong_Un
    elif(arg.upper() == "Drumpf"):
        stat = Drumpf
    elif(arg.upper() == "Uncle"):
        stat = Sam
    elif(arg.upper() == "Lord"):
        stat = Lord
    elif(arg.upper() == "Wood"):
        stat = Wood
    elif(arg.upper() == "Copper"):
        stat = Shulk
    elif(arg.upper() == "Copper"):
        stat = Comrade
    else:
        stat = 0
    embed = discord.Embed(title=stat.title, description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value=str(stat.health), inline=True)
    embed.add_field(name="Offense", value=str(stat.offense), inline=True)
    embed.add_field(name="Defense", value=str(stat.defense), inline=True)
    embed.add_field(name="Field Effect - " + stat.field_effect_1_title, value=stat.field_effect_1_desc, inline=True)
    embed.add_field(name="Field Effect - " + stat.field_effect_2_title, value=stat.field_effect_2_desc, inline=False)
    embed.add_field(name="Classes", value=stat.classes)
    embed.set_footer(text=stat.footer)
    if(stat != 0):
        await ctx.channel.send(embed=embed)
    else:
        await ctx.channel.send("What you entered  doesn't exist")

#--------------------

# Voice Things--------------------
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
#--------------------

# Runs Bot--------------------
bot.run(TOKEN)