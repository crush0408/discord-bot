# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
from asyncio import events
from email import message
from pydoc import describe
from random import randint, random
from turtle import color, title
import discord, asyncio
from discord.utils import get
from discord.ext import commands
from discord import DMChannel
import riot
import os;

os.environ['DISCORD_BOT_TOKEN'] = "OTg1ODQ5MTI5NTgwMjU3Mjkw.G9RJwW.vh4hBjWdDHvey6_wp7zMevDyYd8ywLTsbDTIUE"
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix='~')

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨 Unity Start
    await client.change_presence(status=discord.Status.online, activity=discord.Game("~도움말"))


@client.event
async def on_message(message):
    await client.process_commands(message) # 메세지 중 명령어가 있을 경우 처리해주는 코드

@client.command()
async def 도움말(ctx):
    embed = discord.Embed(title="도움말",describe=f"명령어들", color=0x0080FF)
    embed.add_field(name="집합시키기",value=f"형식 : {client.command_prefix}집합 보내고싶은 메세지",inline=False)
    embed.add_field(name="랜텀 뽑기",value=f"형식 : {client.command_prefix}랜덤 a b",inline=False)
    embed.add_field(name="롤 정보 보기",value=f"형식 : {client.command_prefix}롤 소환사이름",inline=False)
    await ctx.send(embed = embed)
    return

@client.command()
async def 랜덤(ctx, member1, member2):
    embed = discord.Embed(title="랜덤",describe=f"결과", color=0x0080FF)
    if(randint(0,1) == 0):
        embed.add_field(name="결과",value=f"{member1}",inline=False)
    else:
        embed.add_field(name="결과",value=f"{member2}",inline=False)
    
    await ctx.send(embed = embed)
    return


    
@client.command()
async def 집합(ctx, *args):
    message = ' '.join(args)
    await ctx.channel.send ("모여라 !! @everyone,\n" + message)
    return ctx

@client.command()
async def 롤(ctx, *args):
    summonerName = ' '.join(args)
    embed = discord.Embed(title="소환사 정보",describe=f"소환사 정보 검색 결과", color=0x0080FF)
    summer_ID = riot.get_SummonerId(summonerName)
    list = riot.get_RankInfo(summer_ID)
    
    embed.add_field(name="닉네임",value=f"소환사 닉네임 : {list['summonerName']}",inline=False)
    embed.add_field(name="티어",value=f"소환사 티어 : {list['tier']} {list['rank']}" + f" {list['leaguePoints']}LP",inline=False)
    embed.add_field(name="승률",value=f"승률 : {(list['wins'] / (list['wins'] + list['losses'])) * 100:.2f}퍼센트 (승:{list['wins']}/패:{list['losses']}) ",inline=False)
    
    await ctx.send(embed = embed)
    return



client.run(TOKEN)