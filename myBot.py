import discord
import asyncio
import random
from discord.ext import commands
from bs4 import BeautifulSoup
import urllib.request
import datetime

client = discord.Client()
absurb = []

def makeDiary():
    f = open('diaryData2.txt', 'r')
    readlist = f.read()
    f.close()
    global absurb
    absurb = readlist.split('$$')

def cypersRank(nickname):
    parseNick = urllib.parse.quote(nickname)
    cypersURL ='http://cyphers.nexon.com/cyphers/game/log/search/1/' + parseNick
    with urllib.request.urlopen(cypersURL) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
    
    table = soup.find_all('dd')
    nick = table[1].string.replace('\n', '')
    clan = table[5].string.replace('\n', '')
    rank = table[3].string.replace('\n', '')
    mainRP = table[2].string.replace('\n', '')
    bestRP = table[4].string.replace('\n', '')
    winlose = table[6].string.replace('\n', '')

    return [nick, clan, rank, mainRP, bestRP, winlose]

@client.event
async def on_ready():
    print('이몸 등장이올시다')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    if message.content.startswith('!망언집'):
        await message.channel.send(random.choice(list))
    
    if message.content.startswith('!사이퍼즈'):
        mes = message.content.split(" ")
        nickname = mes[1]
        cypersResult = cypersRank(nickname)

        embed = discord.Embed(
            title = '**CYPHERS**',
            description = '사이퍼즈 전적입니다',
            colour = discord.Colour.red()
        )
        embed.add_field(name='닉네임', value=cypersResult[0])
        embed.add_field(name='클랜', value=cypersResult[1])
        embed.add_field(name='랭크', value=cypersResult[2])
        embed.add_field(name='공식전 RP', value=cypersResult[3])
        embed.add_field(name='최고 RP', value=cypersResult[4])
        embed.add_field(name='승패', value=cypersResult[5])
        await message.channel.send(embed=embed)


client.run('TOKEN')
