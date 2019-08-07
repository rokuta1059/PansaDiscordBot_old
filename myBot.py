#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import discord
import asyncio
import random
from discord.ext import commands
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime, date, time

client = discord.Client()
absurb = []
conch = []

def makeDiary():
    f = open('diaryData.txt', 'r', encoding="utf8")
    readlist = f.read()
    f.close()
    global absurb
    absurb = readlist.split('$$')
    
def makeConch():
    f = open('magicConch.txt', 'r', encoding="utf8")
    readlist = f.read()
    f.close()
    global conch
    conch = readlist.split('\n')

def cypersRank(nickname):
    parseNick = urllib.parse.quote(nickname)
    if game == "공식":
        cypersURL ='http://cyphers.nexon.com/cyphers/game/record/search/1/' + parseNick + '/1'
    else:
        cypersURL ='http://cyphers.nexon.com/cyphers/game/record/search/2/' + parseNick + '/2'
    with urllib.request.urlopen(cypersURL) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
    
    a = []
    battle = []
    img = []
    
    for firstTable in soup.find_all("div", "info info1"):
        for firstValue in firstTable.find_all("td"):
            a.append(firstValue.get_text())

    for secondTable in soup.find_all("div", "info info2"):
        for secondValue in secondTable.find_all("td"):
            a.append(secondValue.get_text())
    
    for battleTable in soup.find_all("li", "show"):
        for battleResult in battleTable.find_all("td"):
            battle.append(battleResult.get_text().replace('\n', '').replace('\r', '').replace('\t', ''))

        for battleResult in battleTable.find_all("td", "char"):
            for imgList in battleResult.find_all("img"):
                img.append(imgList.get("src"))

    return cypersURL, a, battle, img

def getMillDate(name):
    f = open('militaryDate.txt', 'r', encoding="utf8")
    mill = []
    findName = False
    while True:
        line = f.readline()
        if line.find(name) != -1:
            mill = line.replace('\n', '').split(' ')
            findName = True
            break
        if not line: break
    f.close()

    if findName:
        milldate = list(map(int, mill[1].split('.')))
        now = datetime.now()
        findDate = datetime(milldate[0], milldate[1], milldate[2]) - now
        return "{0}쿤의 전역일은 {1}일 남았답니다~".format(mill[0], findDate.days)
    else:
        return "{0}쿤은 군인이 아닌거 같아요~".format(name)

@client.event
async def on_ready():
    print('이몸 등장이올시다')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='동아리방 먼지와 함께 뒹굴뒹굴', type=1))

@client.event
async def on_message(message):
    
    if message.content.startswith('!도움'):
        embed = discord.Embed(
            title = '**판 사 요 정 등 장**',
            description = '이거슨 판사 요정 커맨드 리스트',
            colour = discord.Colour.green(),
        )
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.add_field(name='!망언집', value='판사 역대 망언 출력해줌. 숫자 같이 입력하면 해당 번호 망언 나옴.')
        embed.add_field(name='!선택', value='선택 장애인들이 넘치는 동아리를 위한 멋진 커맨드. 띄어쓰기로 나눠서 이것저것 입력하면 하나 골라줌.')
        embed.add_field(name='!소라고둥', value='소라고둥님 마법의소라고둥님 마법의 소라고둥님 다 됨. 위대하신 소라고둥님의 말을 들을 수 있다.')
        embed.add_field(name='!전역일', value='군인님들 본명 OOO 입력하면 몇일 남았는지 알려줌. 추가되고 싶은 사람은 쥔장한테 ㄱㄱ')
        embed.add_field(name='!사이퍼즈 (닉네임)', value='전적 알려줌.')
        embed.add_field(name='!사이퍼즈 공식 (닉네임)', value='전적이랑 공식전 최근에 한거 결과 알려줌.')
        embed.add_field(name='!사이퍼즈 일반 (닉네임)', value='전적이랑 일반전 최근에 한거 결과 알려줌.')
        embed.set_footer(text='강원대 판화사랑 동아리 컴정 15학번 과잠선배 제작')
        await message.channel.send(embed=embed)

    if message.content.startswith('!망언집'):
        mes = message.content.split(" ")
        if len(mes) == 2:
            await message.channel.send(absurb[int(mes[1])-1])
        else:
            await message.channel.send(random.choice(absurb))
            
    if message.content.startswith('!선택'):
        mes = message.content.split(" ")
        del mes[0]
        await message.channel.send(random.choice(mes))
        
    if message.content.startswith('!소라고둥') or message.content.startswith('소라고둥님') or message.content.startswith('마법의소라고둥님') or message.content.startswith('마법의 소라고둥님'):
        await message.channel.send(random.choice(conch))
    
    if message.content.startswith('!전역일'):
        mes = message.content.split(" ")
        await message.channel.send(getMillDate(mes[1]))
    
    if message.content.startswith('!사이퍼즈'):
        mes = message.content.split(" ")
        if mes[1] == '일반' or mes[1] == '공식':
            nickname = mes[2]
            nickURL, log, battleResult, imgURL = cypersRank(nickname, mes[1])
        else:
            nickname = mes[1]
            nickURL, log, battleResult, imgURL = cypersRank(nickname, '')

        embed = discord.Embed(
            title = '**CYPHERS**',
            description = '사이퍼즈 전적입니다',
            colour = discord.Colour.red(),
        )
        embed.set_thumbnail(url='http://static.cyphers.co.kr/img/event/logo_bar.gif')
        embed.add_field(name='닉네임', value=log[0])
        embed.add_field(name='급수', value=log[1])
        embed.add_field(name='클랜', value=log[2])
        embed.add_field(name='승패', value=log[3])
        embed.add_field(name='공식전 RP', value=log[4])
        embed.add_field(name='최고 RP', value=log[5])
        embed.add_field(name='티어', value=log[6])
        await message.channel.send(embed=embed)

        if mes[1] == '일반' or mes[1] == '공식':
            embed = discord.Embed(
                title = '**가장 최근 경기 결과**',
                url = nickURL,
                description = '가장 최근에 플레이한 경기의 결과입니다.',
                colour = discord.Colour.red()
            )
            embed.set_thumbnail(url=imgURL[0])
            embed.add_field(name='플레이 시간 및 결과', value=battleResult[0])
            embed.add_field(name='캐릭터', value=battleResult[1])
            embed.add_field(name='레벨', value=battleResult[2])
            embed.add_field(name='킬', value=battleResult[3])
            embed.add_field(name='데스', value=battleResult[4])
            embed.add_field(name='도움', value=battleResult[5])
            embed.add_field(name='공격량', value=battleResult[6])
            embed.add_field(name='피해량', value=battleResult[7])
            embed.add_field(name='전투참여', value=battleResult[8])
            embed.add_field(name='시야확보', value=battleResult[9])
            await message.channel.send(embed=embed)


makeDiary()
makeConch()
client.run('TOKEN')
