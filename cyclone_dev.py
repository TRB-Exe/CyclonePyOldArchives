import discord, logging, json
import os
import asyncio
import youtube_dl
import os

from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure


bot = commands.Bot(command_prefix="d_")
bot.remove_command("help")
bot.load_extension("jishaku")



@bot.event
async def on_ready():
    print("WCP.IO Cyclone")
    print("Запущено с бота:")
    print(bot.user.name)
    print("==========Консоль логов==========")
    


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="_d | Альфа версия для разработчиков"))


@bot.command(aliases = ["h", "хелп", "х"])
async def help(ctx,):
    embed = discord.Embed(title = f"Cyclone Alpha", description = f"```Внимание! Это альфа версия бота для разработчиков. Префикс бота d_```", colour = discord.Color.gold())
    embed.add_field(name = 'Основное', value= "`d_help` `d_invite` `d_about` `d_ping`", inline = True)
    embed.add_field(name = 'Модерация', value = '`d_ban` `d_kick` `d_clear`', inline = True)
    embed.add_field(name = 'Утилиты', value = '`d_say` `d_emoji` `d_avatar`', inline = True)
    embed.add_field(name = 'Для разработчиков', value = '`d_jsk`', inline = True)
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.reply(embed = embed, mention_author=False)

@bot.command(aliases = ["e", "em", "е"])
async def emoji(ctx, emoji: discord.Emoji):
     emb = discord.Embed(title = f"{emoji.name}", colour = discord.Color.gold())
     emb.set_image(url = emoji.url)
     await ctx.reply(embed = emb, mention_author=False)

@bot.command(aliases = ["ava", "аватар", "ава"])
async def avatar(ctx, *, avamember: discord.Member):   
    emb = discord.Embed(title = f"Аватар {avamember.name}", colour = discord.Color.gold())
    emb.set_image(url = avamember.avatar_url)
    await ctx.reply(embed = emb, mention_author=False)


@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)

@bot.command(aliases = ["clr"])
@commands.has_permissions(kick_members = True)
async def clear(ctx):
    val = str(ctx.message.content)
    val = int(val[6:])
    cleared = f"{val} сообщений было удалено <:T_verified:705350561498923068>"
    await ctx.channel.purge(limit = val)
    await ctx.send(cleared)

@bot.command()
async def about(ctx,):
    emb = discord.Embed(title = f"Cyclone", description = f"Cyclone - is a Minimalism Discord bot writed on Python. Our goal - make bot better! \nUsing liblaries: `discord.py, asyncio, jishaku` \nDeveloper: `trb.exe#3554` \nInvite bot: Отключено \n**Acknowledgements** \nThanks TheBACKTRACK#6666 for helping with commands (clear, help, jishaku and etc) \nThe commands bases on old cyclone bot. [old cyclone repo](https://github.com/TRB-Exe/CycloneRepoOld)", colour = discord.Color.gold())
    await ctx.reply(embed = emb, mention_author=False)


@bot.command(aliases = ["inv", "i"])
async def invite(ctx,):
    emb = discord.Embed(Title = f"Cyclone", description = f"Команда отключена", colour = discord.Color.gold())
    await ctx.reply(embed = emb, mention_author=False)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  kicked = discord.Embed(title = f"Успешно", description = f"{user} был изгнан из сервера <:T_verified:705350561498923068>", colour = discord.Color.gold())
  await ctx.reply(embed = kicked, mention_author=False)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    boned = discord.Embed(title = f"Успешно", description = f"{user} был забанен на этом сервере! <:T_verified:705350561498923068>",colour = discord.Color.gold())
    boned.set_image(url = "https://media.discordapp.net/attachments/735233347999105146/735233424222322799/tenor_1.gif")
    await ctx.reply(embed = boned, mention_author=False)




bot.run("хуекен")
