import discord
from discord.ext import commands
import json
from discord.flags import Intents

with open('setting.json','r',encoding='utf-8') as file:
    data = json.load(file)

Intents = discord.Intents.all()
Intents.members = True

bot = commands.Bot(command_prefix='!',intents=Intents)

@bot.event
async def on_ready():
    print("Bot is Online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(data['Welcome_Channel']))
    await channel.send(f"{member} join!")


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(data['Leave_Channel']))
    await channel.send(f"{member} leave!")

@bot.command(pass_context=True) #括號內為權限許可
async def ping(ctx):
    await ctx.send(bot.latency)

bot.run(data['token'])
