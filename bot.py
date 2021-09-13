import discord
from discord.ext import commands
from discord.flags import Intents

Intents = discord.intents.all()
intents = Intents.members = True

bot = commands.Bot(command_prefix='[',intents=intents)

@bot.event
async def on_ready():
    print("Bot is Online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(881521268690673674)
    await channel.send(f"{member}join!")


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(881521330321768468)
    await channel.send(f"{member}leave!")

bot.run("ODgwMzM1MzY2MDk4NDE5Nzgy.YScyMw.jPgdFHn3SHgremPd9k_ecTk19OU")
