# Com Com Bot
'''
General purpose bot based on Communism
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

bot = commands.Bot(command_prefix='c.')
bot_name = "Com-Com"

@bot.event                          # Ready Check If Bot Is Online
async def on_ready():
    print("Test Com-Com is Running")
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))

@bot.command(pass_context=True)
async def capitalism(ctx, user: discord.Member = None):
    await ctx.channel.send("CAPITALIST PIG!")

@bot.command(pass_context=True)
async def stalinstats(ctx, user: discord.Member = None):
    embed = discord.Embed(title="Joseph Stalin", description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value="64625", inline=True)
    embed.add_field(name="Offense", value="52795", inline=True)
    embed.add_field(name="Defense", value="57953", inline=True)
    embed.add_field(name="Field Effect - Anti-Capitalist", value="'Capitalist' Class enemies' Offense and Defense -90%; 'Communist' Class allies' damage doubled against 'Capitalist' Class enemies", inline=True)
    embed.add_field(name="Field Effect - Disappearing Act", value="Defeated 'Capitalist' Class enemies are permanently removed from battle", inline=False)
    embed.add_field(name="Classes", value="Communist; Supreme Leader; Dictator")
    embed.set_footer(text="The OG supreme communist ruler.")
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def kimstats(ctx, user: discord.Member = None):
    embed = discord.Embed(title="Kim Jong-Un", description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value="42685", inline=True)
    embed.add_field(name="Offense", value="37894", inline=True)
    embed.add_field(name="Defense", value="22685", inline=True)
    embed.add_field(name="Field Effect - The Supreme Leader", value="'Communist' Class enemies obey Kim Jong-Un; 'Supreme Leader' and 'Dictator' Class enemies are unaffected", inline=True)
    embed.add_field(name="Field Effect - Self-Confidence", value="If Kim Jong-Un defeats a 'Capitalist' Class enemy, he recovers 25% Health lost", inline=False)
    embed.add_field(name="Classes", value="Communist; Supreme Leader; Dictator")
    embed.set_footer(text="All hail.")
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def drumpfstats(ctx, user: discord.Member = None):
    embed = discord.Embed(title="General Drumpf", description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value="14673", inline=True)
    embed.add_field(name="Offense", value="52798", inline=True)
    embed.add_field(name="Defense", value="94363", inline=True)
    embed.add_field(name="Field Effect - 'Murica", value="'Capitalist' Class allies' Offense +25%", inline=True)
    embed.add_field(name="Field Effect - It's Just Capitalism", value="When HP is below 50%, Offense +5000 and 'Capitalist' Class allies' Offense and Defense -30%", inline=False)
    embed.add_field(name="Classes", value="Capitalist; Supreme Leader; Dictator; Degeneracy")
    embed.set_footer(text="Making America degenerate again.")
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def unclestats(ctx, user: discord.Member = None):
    embed = discord.Embed(title="Uncle Sam", description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value="63157", inline=True)
    embed.add_field(name="Offense", value="36798", inline=True)
    embed.add_field(name="Defense", value="75736", inline=True)
    embed.add_field(name="Field Effect - Stars and Stripes", value="'Capitalist' Class allies ignore 'Communist' Class enemies' Offense increases", inline=True)
    embed.add_field(name="Field Effect - Lighting the Fuse", value="Offense +100% when there are no allies remaining", inline=False)
    embed.add_field(name="Classes", value="Capitalist")
    embed.set_footer(text="Stars, stripes, and fireworks. 'Murica.")
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def lordstats(ctx, user: discord.Member = None):
    embed = discord.Embed(title="Moon Lord", description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value="90426", inline=True)
    embed.add_field(name="Offense", value="84783", inline=True)
    embed.add_field(name="Defense", value="36734", inline=True)
    embed.add_field(name="Field Effect - Celestial Entity", value="Ignores enemies' Defense increases", inline=True)
    embed.add_field(name="Field Effect - Moon Leech Clots", value="Health recovered by 500 whenever an enemy is attacked", inline=False)
    embed.add_field(name="Classes", value="God; Video Game")
    embed.set_footer(text="Impending doom approaches.")
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def communism(ctx, user: discord.Member = None):
    await ctx.channel.send("best government")

@bot.command(pass_context=True)
async def backslash(ctx, user: discord.Member = None):
    await ctx.channel.send("Wrong bot.")

@bot.command(pass_context=True)
async def woodstats(ctx, user: discord.Member = None):
    embed = discord.Embed(title="Wood Man", description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value="78353", inline=True)
    embed.add_field(name="Offense", value="35784", inline=True)
    embed.add_field(name="Defense", value="62136", inline=True)
    embed.add_field(name="Field Effect - Robotic Armor", value="Ignores enemies' Offense increases", inline=True)
    embed.add_field(name="Field Effect - Leaf Shield", value="Enemies attacking Wood Man receive 500 damage", inline=False)
    embed.add_field(name="Classes", value="Video Game")
    embed.set_footer(text="doot doot doot.")
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def shulkstats(ctx, user: discord.Member = None):
    embed = discord.Embed(title="Shulk", description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value="41313", inline=True)
    embed.add_field(name="Offense", value="67834", inline=True)
    embed.add_field(name="Defense", value="53323", inline=True)
    embed.add_field(name="Field Effect - Monado Arts", value="Offense +25% after receiving attack; only activates once", inline=True)
    embed.add_field(name="Field Effect - Back Slash", value="Unleashes a wicked Back Slash when attacking, ignoring enemies' Defense increases and dealing +5000 damage to 'Video Game' Class enemies", inline=False)
    embed.add_field(name="Classes", value="Seems Familiar; Video Game")
    embed.set_footer(text="He's really feeling it.")
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def copperstats(ctx, user: discord.Member = None):
    embed = discord.Embed(title="Copper Comrade", description="Stats at Level 1000", color=0xfffa20)
    embed.add_field(name="Health", value="44462", inline=True)
    embed.add_field(name="Offense", value="45734", inline=True)
    embed.add_field(name="Defense", value="101835", inline=True)
    embed.add_field(name="Field Effect - Go Forth, Comrades!", value="'Communist' Class allies' Offense +50%", inline=True)
    embed.add_field(name="Field Effect - Overwhelming Copper Defenses", value="Ignores the Field Effects of 'Capitalist' Class enemies", inline=False)
    embed.add_field(name="Classes", value="Communist; Chastiser")
    embed.set_footer(text="Red and yellow make brown, and copper is brown. Therefore, Copper Comrade is yellow and red.")
    await ctx.channel.send(embed=embed)

# Bot Token-------------------------
# https://discordapp.com/oauth2/authorize?client_id=585846042193428480&scope=bot&permissions=999999
#bot.run("NTc4NjEwMTI0NzI2MzM3NTQ3.XN2GuA.2aejkyAmJ7o6ovPtZTWuzIlboAs") # Shulk Bot
#bot.run("NTgxMTM3NzM5MDg1MzgxNjMy.XOa4uQ.VklM6dv5PeyrvzpQ-eJLJcw9tK8") # Shulk Test Bot
#bot.run("NTc4OTI1OTI2MDQ2NDk4ODI3.XN6uFw.xV3I_hgem9e6bikdYDII-HDD9q8") # Commander Cody Test Bot
bot.run("NTg1ODQ2MDQyMTkzNDI4NDgw.XPfbPw.K5XqvDwiU4-erIKN40Qco6G4V1c") # Com-Com Test Bot
#--------------------

    