import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix = "!")

responses - ["Unsure Mortal", "Absolutely not", "perhaps this is likely", "The future is bright", "I see grand things for you, young one",
"Not in this lifetime", "Never Mortal", "This could be", "Unclear human...ask once more", "Yes", "No", "Possible, but not in this reality"]

@bot.event
async def on_ready():
    print("Logged in as;")
    print(bot.user.name)
    print(bot.user.id)

@bot.command(aliases=["8b", "8ball", "eightb", "eb"])
async def eightball():
    await bot.say("I will reach through the vail for your answer...")
    await asyncio.sleep(2)
    await bot.say("I almost have it aquired...")
    await asuncio.sleep(2)
    await bot.say(random.choice(response))


bot.run("Enter Your Personal Discor key here")
