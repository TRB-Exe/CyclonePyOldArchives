import discord, logging, json
import os
import asyncio

from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="_")
bot.remove_command("help")
bot.load_extension("jishaku")

# Бета версия бота 001 кодовое имя WHelp

@bot.event
async def on_ready():
    print("Запуск клиента бота")
    print("Токен бота запущен и вошел в клиент")
    print(bot.user.name)
    print("------------------------")



@bot.command(aliases = ["h"])
async def help(ctx,):
    emb = discord.Embed(title = f"Команды бота Cyclone", description = f"**Статусы команд** \n🔘 Работает \n🔴 Временно недоступна и не работает \n**Основные команды** \n🔘 `_help` \n🔴 `_stat` \n🔴 \n🔴 `_server` \n🔴 `_invite` \n**Модерация** \n🔘 `_ban` \n🔴 `_clear` \n**Развлечения** \n🔘`_cat` \n🔴 `_coinflip` \n**Утилиты** \n🔴 `_ping` \n🔘 `_emoji` \n🔘`_avatar`", colour = discord.Color.red())
    await ctx.send(embed = emb)

@bot.command(aliases = ["em"])
async def emoji(ctx, emoji: discord.Emoji):
     emb = discord.Embed(title = f"Эмодзи {emoji.name}", colour = discord.Color.blue())
     emb.set_image(url = emoji.url)
     await ctx.send(embed = emb)

@bot.command()
async def stat(ctx):
    emb = discord.Embed(title = "CycloneStatus", description = "Времмено недоступно", colour = discord.Color.blue())
    await ctx.send(embed = emb)

@bot.command(aliases = ["ava"])
async def avatar(ctx, *, avamember: discord.Member):   #аватар упомянутого пользователя
    emb = discord.Embed(title = f"Аватар {avamember.name}", colour = discord.Color.blue())
    emb.set_image(url = avamember.avatar_url)
    await ctx.send(embed = emb)

@bot.command(aliases = ["i", "in", "add"])
async def invite(ctx):
    emb = discord.Embed(title = "🛠️ Временно недоступно", description = "Извини, но бота временно нельзя добавлять на сервера.", colour = discord.Color.blue())
    await ctx.send(embed = emb)



bot.run("YOURTOKEN")

@bot.command()
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send("введите причину")
    else:
        lsmessban = f"Вы были забанен на {ctx.guild.name} по причине: {reason}"
        await member.send(lsmessban)
        await member.ban(reason=reason)
