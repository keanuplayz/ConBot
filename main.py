# You're going to hate me for this

# Import all required packages
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the vars as system environment variables
load_dotenv()

# Define the client
client = commands.Bot(command_prefix='&_')

# This tells d.py that this function is an event
@client.event
async def on_ready():
    print('Hi!')

# tells d.py that this is a command
@client.command()
# define command name
async def userinfo(ctx):
    # tells bot what to send
    await ctx.send(f"Username: {ctx.author.name}#{ctx.author.discriminator}")


# turn off the geckos too loud
@client.command()
async def pissbaby(ctx):
    await ctx.send('hey you little piss baby, you think youre so fucking cool? huh? you think youre so fucking tough? you talk a lotta big game for someone with such a small truck')





client.run(os.getenv('TOKEN'))
# if there's a token here and youre reading it tell me so i can fix that
