
import discord
import asyncpraw
import random
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="~", intents=intents)

# Accessing Reddit's API, this stuff is supposed to be secret. This isn't used in the bot as of now but I can add it later.
reddit = asyncpraw.Reddit(client_id='insertclientid',
                          client_secret='insertclientsecret',
                          user_agent='insertuseragent')


@bot.command()
async def pet(ctx):
    await ctx.channel.send("https://tenor.com/view/doggo-petting-pet-nuzzle-dog-gif-7701760")
    await ctx.channel.send("Thanks for petting me! Now do it again. Now. ")


@bot.command()
async def sleep(ctx):
    randomNumber = random.randint(1, 2)
    if randomNumber == 1:
        await ctx.channel.send("I'm too tired to do anything, let's just sleep in the sun.")
    else:
        await ctx.channel.send("https://tenor.com/view/dog-wagging-tail-cute-still-waiting-bored-gif-16453890")
        await ctx.channel.send("Let's go play outside instead, I'm bored. ")


@bot.command()
async def play(ctx):
    await ctx.channel.send("Let's go outside and throw sticks around! It'll be fun.")

@bot.command()
async def doatrick(ctx):
    randomTrick = random.randint(1, 3)
    if randomTrick == 1:
        await ctx.channel.send("*rolls around*")
        await ctx.channel.send("https://tenor.com/view/puppy-cute-dog-gif-4946551")
    elif randomTrick == 2:
        await ctx.channel.send("*Sits down*")
        await ctx.channel.send("https://tenor.com/view/cute-puppy-dog-sit-down-pet-gif-17693977")
    else:
        await ctx.channel.send("*huh?*")
        await ctx.channel.send("https://tenor.com/view/happymonday-cute-puppy-dog-cute-dog-gif-14228361")

@bot.command()
async def rolldice(ctx):
    randomTrick = random.randint(1, 6)
    if randomTrick == 1:
        await ctx.channel.send("**You rolled 1!**")
    elif randomTrick == 2:
        await ctx.channel.send("**You rolled 2!**")
    elif randomTrick == 3:
        await ctx.channel.send("**You rolled 3!**")
    elif randomTrick == 4:
        await ctx.channel.send("**You rolled 4!**")
    elif randomTrick == 5:
        await ctx.channel.send("**You rolled 5!**")
    else:
        await ctx.channel.send("**You rolled 6! This is your lucky day!**")
        
@bot.command()
async def treat(ctx):
    await ctx.channel.send("https://tenor.com/view/dog-treat-snack-scooby-gif-12847347")
    await ctx.channel.send("Ooo a treat! Thank you! Another one.")

@bot.event
async def on_ready():
    game = discord.Game("with my owner")
    await bot.change_presence(status=discord.Status.online, activity=game)

bot.run('insertsecrettokenhere')
