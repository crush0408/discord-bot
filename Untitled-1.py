# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio
from discord.utils import get
from discord.ext import commands
import os;

os.environ['DISCORD_BOT_TOKEN'] = "OTg1ODQ5MTI5NTgwMjU3Mjkw.G9RJwW.vh4hBjWdDHvey6_wp7zMevDyYd8ywLTsbDTIUE"
TOKEN = os.environ.get('DISCORD_BOT_TOKEN')

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨 Unity Start
    await client.change_presence(status=discord.Status.online, activity=discord.Game("개발"))


@client.event
async def on_message(message):
    message_context = message.content
    if(message_context.find("테스트") >= 0):
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))
    if(message_context.find("집합") >= 0):
        await message.channel.send ("모여라 !! @everyone")
    #my_name = discord.utils.get(message.guild.members , name= "이상백")
    #await message.channel.send ("{} 안녕 !!".format(my_name.mention))
    
    


client.run(TOKEN)