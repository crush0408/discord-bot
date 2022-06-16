# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
from asyncio import events
from email import message
from pydoc import describe
from random import randint
from turtle import color, title
import discord, asyncio
from discord.utils import get
from discord.ext import commands
from discord import DMChannel
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
    
    await client.process_commands(message) # 메세지 중 명령어가 있을 경우 처리해주는 코드

@client.command()
async def 도움말(ctx):
    embed = discord.Embed(title="도움말",describe=f"명령어들", color=0x0080FF)
    embed.add_field(name="테스트하기",value=f"형식 : {client.command_prefix}테스트",inline=True)
    embed.add_field(name="집합시키기",value=f"형식 : {client.command_prefix}집합",inline=False)
    embed.add_field(name="랜텀 팀",value=f"형식 : {client.command_prefix}랜덤 a b",inline=False)
    await ctx.send(embed = embed)
    return

@client.command()
async def 랜덤(ctx, member1="", member2=""):
    embed = discord.Embed(title="랜덤",describe=f"결과", color=0x0080FF)
    randomList = [member1,member2]
    if(randint(0,1) == 0):
        embed.add_field(name="결과",value=f"1팀 : {member1}\n2팀 :{member2}",inline=False)
    else:
        embed.add_field(name="결과",value=f"1팀 : {member2}\n2팀 :{member1}",inline=False)
    await ctx.send(embed = embed)
    return

@client.command()
async def 팀(ctx):
    embed = discord.Embed(title="팀 추첨 결과",describe=f"결과", color=0x0080FF)
    
    embed.add_field(name="1팀",value=f"[TANKER]김범주\n [BRAIN]이민형\n [SUB TANKER]유지호\n [NORMAL]김홍열",inline=False)
    embed.add_field(name="2팀",value=f"[TANKER]김건범\n [BRAIN]이상백\n [SUB TANKER]박광현\n [NORMAL]이승혁",inline=False)
    await ctx.send(embed = embed)
    return
    
@client.command()
async def 집합(ctx):
    await ctx.channel.send ("모여라 !! @everyone")
    return ctx


client.run(TOKEN)