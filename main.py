import discord, random, json, os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

token = os.environ.get("BOT_TOKEN")
bot = commands.Bot(command_prefix=".")

# uploading commands and stuff at 10 stars and 20 followers

bot.run(token)
