import discord, logging, json
import os
import asyncio

from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="_")
bot.remove_command("help")
bot.load_extension("jishaku")

# Cyclone Version 000 Codename GlobalCyclone


@bot.event
async def on_ready():
    print("Запуск клиента бота")
    print("Токен бота запущен и вошел в клиент")
    print(bot.user.name)
    print("------------------------")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="_help"))

@bot.command(aliases = ["h"])
async def help(ctx,):
    emb = discord.Embed(title = f"Команды бота Cyclone", description = f"**Основные команды** \n`_help` `_stat` `_server` `_invite` \n**Модерация** \n`_ban` `_clear` \n**Развлечения** \n`_cat` `_coinflip` \n**Утилиты** \n`_ping` `_emoji` `_avatar`", colour = discord.Color.blue())
    await ctx.send(embed = emb)





@bot.command(aliases = ["em"])
async def emoji(ctx, emoji: discord.Emoji):
     emb = discord.Embed(title = f"{emoji.name}", colour = discord.Color.blue())
     emb.set_image(url = emoji.url)
     await ctx.send(embed = emb)


@bot.command(aliases = ["ava"])
async def avatar(ctx, *, avamember: discord.Member):   #аватар упомянутого пользователя
    emb = discord.Embed(title = f"Аватар {avamember.name}", colour = discord.Color.blue())
    emb.set_image(url = avamember.avatar_url)
    await ctx.send(embed = emb)

@bot.command(aliases = ["i", "in", "add"])
async def invite(ctx):
    emb = discord.Embed(title = "Добавления бота на сервер", description = "На держи ссылку на [инвайт бота](https://discord.com/api/oauth2/authorize?client_id=621674194341462016&permissions=8&scope=bot)", colour = discord.Color.blue())
    await ctx.send(embed = emb)


@bot.command(aliases = ["s"])
async def say(ctx, *, arg):
    await ctx.send(arg)






@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"Укажите причину и пользователя")
    else:
        messageok = f"Вы забанены на {ctx.guild.name} по причине {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)




@bot.command()
@commands.has_permissions(kick_members = True)
async def clear(ctx):
    val = str(ctx.message.content)
    val = int(val[6:])
    cleared = f"<:c_yes:777506231195533312> Удалено {val} Сообщений"
    await ctx.channel.purge(limit = val)
    await ctx.send(cleared)





# тут должна быть команда, но я не мог придумать её




bot.run("NjIxNjc0MTk0MzQxNDYyMDE2.XXoxNg.sVI0OHOLPNjquq3kryZcpeTK8CE")
