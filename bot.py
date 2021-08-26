from discord.ext import commands
from discord.shard import EventItem

bot=commands.Bot(command_prefix='!')

@bot.event
async def onready():
    print(">>Bot is Onlien<<")

bot.run('ODgwMzM1MzY2MDk4NDE5Nzgy.YScyMw.Aw7TmiK-4K-GWxg5SHsMBX1xdLQ')