import discord, logging, json
import os
import asyncio
import aiohttp

# Импорты

from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure

# Префикс токен и расширение

bot = commands.Bot(command_prefix="_")
bot.remove_command("help")
bot.load_extension("jishaku")
TOKEN = "хуекен"

# логгер который уже не работает из-за хероку

# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='log.txt', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Винда говно линукс топ | Префикс _"))
    print("Запущено с бота")
    print(bot.user.name)
    print("==========Консоль логов==========")
    

@bot.event
async def on_guild_join(guild):
    print("[Лог] Бот был добавлен на сервер:")
    print(ctx.guild.name)



@bot.command(aliases = ["h", "хелп", "х"])
async def help(ctx,):
    embed = discord.Embed(title = f"Cyclone", description = f"```Создатель бота @trb.exe#3554```", colour = discord.Color.blue())
    embed.add_field(name = 'Основное', value= "`_help` `_invite` `_about` `_news`", inline = True)
    embed.add_field(name = 'Модерация (скоро будет удалено)', value = '`_ban` `_kick` `_clear`', inline = True)
    embed.add_field(name = 'Утилиты', value = '`_say` `_emoji` `_avatar`', inline = True)
    embed.set_footer(text=ctx.author.name, icon_url = ctx.author.avatar_url)
    await ctx.reply(embed = embed, mention_author=False)

@bot.command(aliases = ["e", "em", "е"])
async def emoji(ctx, emoji: discord.Emoji):
     emb = discord.Embed(title = f"{emoji.name}", colour = discord.Color.blue())
     emb.set_image(url = emoji.url)
     await ctx.reply(embed = emb, mention_author = False)



@bot.command(aliases = ["ava", "аватар", "ава"])
async def avatar(ctx, *, avamember: discord.Member):   
    emb = discord.Embed(title = f"Аватар {avamember.name}", colour = discord.Color.blue())
    emb.set_image(url = avamember.avatar_url)
    await ctx.reply(embed = emb, mention_author=False)


@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)
#    await ctx.send(f"Команда отключена и скоро будет переделана")
# (ctx, *, arg):


@bot.command()
async def news(ctx,):
    text = discord.Embed(title = f"Новости или же changelog", description = f"23.06.21 Бот переехал на другой хост. Теперь в оффлайн так часто не будет уходить.", colour = discord.Color.blue())
    await ctx.reply(embed=text, mention_author=False)


@bot.command(aliases = ["clr"])
@commands.has_permissions(kick_members = True)
async def clear(ctx):
    val = str(ctx.message.content)
    val = int(val[6:])
    cleared = f"{val} сообщений было удалено <:T_verified:705350561498923068>"
    await ctx.channel.purge(limit = val)
    await ctx.send(cleared)
    
    
    

@clear.error
async def clear_error(ctx, error):
    if isistance(error, commands.MissingPermissions):
        fail = discord.Embed(title = f"Поздравляем, вы оформили кредит в размере error рублей", description = f"Ой не то написал в заголовке извините. \nДля выполнении команды требуются права на кик. Если у вас есть права но все равно показывается это сообщение, сообщите разработчику.", colour = discord.Color.blue())
        await ctx.reply(embed = fail, mention_author=False)
    
    
    
@bot.command()
async def about(ctx,):
    emb = discord.Embed(title = f"Cyclone", description = f"Cyclone - Это минималистичный бот написанный на Python. Наша цель - сделать бота лучше!", colour = discord.Color.blue())
    emb.add_field(name = f"Используемые библиотеки", value = f"discord.py, asyncio, jishaku", inline = True)
    emb.add_field(name = f"Разработчик бота:", value = f"`trb.exe#4200`", inline = True)
    emb.add_field(name = f"Благодарности", value = f"Спасибо The BACKTRACK#0822 за помощь с командами `clear` `jsk` `help` и т.д", inline = True)
    emb.add_field(name = f"Пригласить бота", value = f"[кликни сюда](https://discord.com/api/oauth2/authorize?client_id=815985980628664342&permissions=8&scope=bot)")
    await ctx.reply(embed = emb, mention_author=False)


@bot.command(aliases = ["inv", "i"])
async def invite(ctx,):
    emb = discord.Embed(Title = f"Cyclone", description = f"[Нажмите чтобы пригласить](https://discord.com/api/oauth2/authorize?client_id=815985980628664342&permissions=8&scope=bot)", colour = discord.Color.blue())
    await ctx.reply(embed = emb, mention_author=False)


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  kicked = discord.Embed(title = f"Успешно", description = f"{user} был изгнан из сервера <:T_verified:705350561498923068>", colour = discord.Color.blue())
  await ctx.reply(embed = kicked, mention_author=False)


@kick.error
async def kick_error(ctx, error):
    if isistance(error, commands.MissingPermissions):
        fail = discord.Embed(title = f"Поздравляем, вы оформили кредит в размере error рублей", description = f"Ой не то написал в заголовке извините. \nДля выполнении команды требуются права на кик. Если у вас есть права но все равно показывается это сообщение, сообщите разработчику.", colour = discord.Color.blue())
        await ctx.reply(embed = fail, mention_author=False)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    boned = discord.Embed(title = f"Успешно", description = f"{user} был забанен на этом сервере! <:T_verified:705350561498923068>",colour = discord.Color.blue())
    boned.set_image(url = "https://media.discordapp.net/attachments/735233347999105146/735233424222322799/tenor_1.gif")
    await ctx.reply(embed = boned, mention_author=False) 



# @bot.command()
# @commands.is_nsfw()
# async def nsfwtest(ctx):
# embid = discord.Embed(title=f"ПОРНО", description=f"Дрочите")
# async with aiohttp.ClientSession() as cs:
# async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
# res = await r.json()
# embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
# await ctx.send(embed=embid)



# @nsfwtest.error(ctx, error):
#   if isinstance(error, NSFWChannelRequired):
#   await ctx.send(f"Эта команда доступна только в nsfw каналах.")






@bot.command(aliases = ["reboot"])
@commands.is_owner()
async def shutdown(ctx):
            shutdownmsg = f"Выключение/перезагрузка бота"
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Выключение бота"))
            await ctx.send("Выключение бота")
            print("[бот ]Бот выключен")
            await ctx.bot.close()


bot.run(TOKEN)
