import discord
from discord.ext import commands


bot = discord.Bot()
TOKEN = ""


@bot.slash_command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
    
bot.run(TOKEN)
