import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Lonely Wolf is on baby')

@bot.command()
async def howl(ctx):
    await ctx.send('auuuuuuuuuu')

bot.run('MTE1MzQ2NzU4NzE5MjE2NDM2Mg.GRKyDn.b2EWTBHVJOye8kmj_iTlY0kxKXoneM8ER5N2mo')