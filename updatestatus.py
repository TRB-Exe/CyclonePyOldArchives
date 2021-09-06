import discord, logging, json
import os
import asyncio
import random

from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="_")
bot.remove_command("help")
bot.load_extension("jishaku")


@bot.event
async def on_ready():
    print("Запуск клиента бота")
    print("Токен бота запущен и вошел в клиент")
    print(bot.user.name)
    print("------------------------")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="🕔 Обновление бота. Подождите..."))






bot.run("")
