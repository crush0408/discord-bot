# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
from pydoc import describe
from turtle import color, title
import discord, asyncio
from discord.utils import get
from discord.ext import commands
import os;

os.environ['DISCORD_BOT_TOKEN'] = "OTg1ODQ5MTI5NTgwMjU3Mjkw.G9RJwW.vh4hBjWdDHvey6_wp7zMevDyYd8ywLTsbDTIUE"
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix='~')

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨 Unity Start
    await client.change_presence(status=discord.Status.online, activity=discord.Game("~도움말"))


@client.event
async def on_message(message):
    message_context = message.content
    if(message_context.find("테스트") >= 0):
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))
    if(message_context.find("집합") >= 0):
        await message.channel.send ("모여라 !! @everyone")
    await client.process_commands(message) # 메세지 중 명령어가 있을 경우 처리해주는 코드

@client.command()
async def 도움말(ctx):
    embed = discord.Embed(title="도움말",describe=f"명령어들", color=0x0080FF)
    embed.add_field(name="~테스트",value=f"형식 : {client.command_prefix}테스트",inline=True)
    embed.add_field(name="~집합",value=f"형식 : {client.command_prefix}집합",inline=False)
    await ctx.send(embed = embed)
    return

    
@client.command()
@commands.dm_only()
async def on_message(message):
    await message.author.send ("말 걸지 말아주세요 !!")

    




client.run(TOKEN)