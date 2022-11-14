import json

import discord
from discord.ext import commands

file = open("config.json", "r")
config = json.load(file)

bot = commands.Bot(config["prefix"], intents=discord.Intents.all())


@bot.event
async def on__ready():
    print("BOT IS ONLINE")


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention} pong!")


@bot.command(name="foo")
async def ping(ctx: commands.context):
    await ctx.send(embed=discord.Embed(title=f"{ctx.message.content}"))


bot.run(config["token"])
