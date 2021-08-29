import discord
from discord.ext import commands
from discord.shard import EventItem

intents = discord.Intents.default()
intents.members = True


bot=commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def onready():
    print(">>Bot is Onlien<<")

bot.run('ODgwMzM1MzY2MDk4NDE5Nzgy.YScyMw.Aw7TmiK-4K-GWxg5SHsMBX1xdLQ')