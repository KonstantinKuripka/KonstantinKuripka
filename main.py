import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
@bot.command()
async def color(ctx,color):
    if color.lower()=='синий':
         await ctx.send('Бумага')
    elif color.lower()=='оранжевый':
         await ctx.send('Незагрязненные пластмассовые изделия')
    elif color.lower()=='зеленый':
         await ctx.send('Стекло')
    elif color.lower()=='коричневый':
         await ctx.send('Пищевые отходы')
    else:
          await ctx.send('Бака такого цвета нет в базе данных')
         


@bot.command()
async def mycor(ctx,rem):
     products=['бумага','металл','стекла','одежда и обувь','электроника','пластик']
     if rem.lower() in products:
          await ctx.send('Данный материал можно сдать на переработку')
          return 
     await ctx.send('Данный материал либо нельзя сдать на переработку, либо его нет в базе данных')
          
     

@bot.command()
async def razl(ctx,myc):
     products1={'газеты и книги':'2 года', 'шерстяные изделия':'1 год','пищевые отходы':'2-4 недели', 'пластик':'100 лет','стекло':'более 1000 лет'}
     if myc.lower() not in products1:
          await ctx.send('Не можем распознать Ваше сообщение')
          return
     await ctx.send(products1[myc.lower()])











bot.run('MTIwMTg5NTQxNDk2Njc4NDAxMA.GxMOfu.tL9zDjw7ETkMnecO3fFRLKp9aCXzTIvWDbhNu4')






























