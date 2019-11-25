#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import discord
import asyncio
import random
from discord.ext import commands
from datetime import datetime, date, time

from myBot import *

client = discord.Client()
conch = []
hello = ['왜?', '무슨일?', '하이!', '응!', '짜잔!', '왜 불렀어?', '꺄!', '어엉?', '칫', '뭐']

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
            title='**판 사 요 정 등 장**',
            description='이거슨 판사 요정 커맨드 리스트',
            colour=discord.Colour.green()
        )
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.add_field(name='!망언, !diary', value='판사 역대 망언 출력해줌. 숫자 같이 입력하면 해당 번호 망언 나옴.')
        embed.add_field(name='!망언검색 (이름/내용) (검색어)', value='망언 검색해줌. 몇번인지 나옴.')
        embed.add_field(name='!선택', value='선택 장애인들이 넘치는 동아리를 위한 멋진 커맨드. 띄어쓰기로 나눠서 이것저것 입력하면 하나 골라줌.')
        embed.add_field(name='!타키, !taki', value='오늘의 타키쿤은?')
        embed.add_field(name='!채림, !채릠, !chaerim', value='오늘의 채림쓰는?')
        embed.add_field(name='!소라고둥, 소라고둥님, 마법의소라고둥님, 마법의 소라고둥님', value='위대하신 소라고둥님의 말을 들을 수 있다.')
        embed.add_field(name='!전역일', value='군인님들 본명 OOO 입력하면 몇일 남았는지 알려줌. 추가되고 싶은 사람은 쥔장한테 ㄱㄱ')
        embed.add_field(name='!날씨, !오늘날씨', value='오늘날씨 알려줌. 지역 같이 입력하면 됨.')
        embed.add_field(name='!내일날씨', value='내일날씨 알려줌. 지역 같이 입력하면 됨.')
        embed.add_field(name='!사이퍼즈 (닉네임)', value='전적 알려줌.')
        embed.add_field(name='!사이퍼즈 공식 (닉네임)', value='전적이랑 공식전 최근에 한거 결과 알려줌.')
        embed.add_field(name='!사이퍼즈 일반 (닉네임)', value='전적이랑 일반전 최근에 한거 결과 알려줌.')
        embed.add_field(name='!기억', value='/로 구분해서 기억함. A/B 입력하면 A 에 B가 대응')
        embed.add_field(name='!삭제', value='기억 삭제함. A 입력하면 A에 대응하는 걸 잊음')
        embed.add_field(name='!말해 or 요정아', value='기억한거 말함. A 입력하면 대응하는 B 출력')
        embed.add_field(name='!리스트', value='기억 리스트 나옴. A->B')
        embed.add_field(name='!한영, !영한, !한일, !일한', value='번역함. 네이버 파파고 제공')
        embed.add_field(name='!재정, !새롬, !이룸', value='오늘 밥 뭔지 알려줌.')
        embed.add_field(name='!운세, !fortune', value='아주 간단한 오늘의 운세')
        embed.add_field(name='!요정수치, !fairy', value='그때그때 요정수치')
        embed.add_field(name='!주사위, !dice, ㅈㅅㅇ (굴릴 횟수)D(몇면체) + ...', value='주사위 굴림. 총합도 알려줌.')
        embed.add_field(name='!모두모여', value='뒷문장 추가해서 전체멘션')
        embed.set_footer(text='강원대 판화사랑 동아리 컴정 15학번 과잠선배 제작')
        await message.channel.send(embed=embed)

    if message.content.startswith('!!공지'):
        mes = message.content.replace('!!공지', '').strip().split("/")
        member = message.author
        embed = discord.Embed(
            title='{}'.format(mes[0]),
            description='{}'.format(mes[1]),
            colour=discord.Colour.blurple()
        )
        embed.set_footer(text='{0}이(가) 모두에게 전달중'.format(member.name),
            icon_url=member.avatar_url)
        await client.get_channel('TEXT_CHANNEL_ID').send(embed=embed)

    if message.content.startswith('!망언') or message.content.startswith('!diary'):
        if message.content.startswith('!망언검색'):
            mes = message.content.split(" ")
            if mes[1] in '이름':
                numList = absurbFindName(mes[2])
                numStr = ''
                for i in numList:
                    numStr = numStr + str(i) + ' '
                embed = discord.Embed(
                    title='{0}이(가) 이름에 포함된 망언은...'.format(mes[2]),
                    description=numStr,
                    colour=random.randint(0, 0xffffff)
                )
                await message.channel.send(embed=embed)
            elif mes[1] in '내용':
                numList = absurbFindAbsurb(mes[2])
                numStr = ''
                for i in numList:
                    numStr = numStr + str(i) + ' '
                embed = discord.Embed(
                    title='{0}이(가) 내용에 포함된 망언은...'.format(mes[2]),
                    description=numStr,
                    colour=random.randint(0, 0xffffff)
                )
                await message.channel.send(embed=embed)
        elif message.content.startswith('!망언추가'):
            mes = message.content.replace('!망언추가', '').strip().split('/')
            absurb = addAbsurb(mes[0], mes[1], mes[2])
            embed = discord.Embed(
                title='{0}. {1}'.format(absurb['number'], absurb['absurb']),
                description='- ***{0}***, *{1}*'.format(absurb['name'], absurb['description']),
                colour=random.randint(0, 0xffffff)
            )
            await message.channel.send(embed=embed)
        elif message.content.startswith('!망언수정'):
            mes = message.content.replace('!망언수정', '').strip().split('/')
            absurb = changeAbsurb(mes[1], mes[2], mes[3], int(mes[0]))
            embed = discord.Embed(
                title='{0}. {1}'.format(absurb['number'], absurb['absurb']),
                description='- ***{0}***, *{1}*'.format(absurb['name'], absurb['description']),
                colour=random.randint(0, 0xffffff)
            )
            await message.channel.send(embed=embed)
        else:
            mes = message.content.split(" ")
            if len(mes) == 2:
                absurb = absurbDiary(int(mes[1]))
            else:
                absurb = absurbDiary(0)
            embed = discord.Embed(
                title='{0}. {1}'.format(absurb['number'], absurb['absurb']),
                description='- ***{0}***, *{1}*'.format(absurb['name'], absurb['description']),
                colour=random.randint(0, 0xffffff)
            )
            await message.channel.send(embed=embed)
    
    if message.content.startswith('!타키') or message.content.startswith('!taki'):
        await message.channel.send(makeTaki())

    if message.content.startswith('!채림') or message.content.startswith('!채릠') or message.content.startswith('!chaerim'):
        await message.channel.send(makeChaerim())

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
            title='**CYPHERS**',
            description='사이퍼즈 전적입니다',
            colour=discord.Colour.red(),
        )
        if len(log) <= 4:
            embed.set_thumbnail(
                url='http://static.cyphers.co.kr/img/event/logo_bar.gif')
            embed.add_field(name='닉네임', value=log[0])
            embed.add_field(name='급수', value=log[1])
            embed.add_field(name='클랜', value=log[2])
            embed.add_field(name='승패 RP 등등', value='이번 시즌 공식전 기록이 없는 거시와요')
            await message.channel.send(embed=embed)

        else:
            embed.set_thumbnail(
                url='http://static.cyphers.co.kr/img/event/logo_bar.gif')
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
                title='**가장 최근 경기 결과**',
                url=nickURL,
                description='가장 최근에 플레이한 경기의 결과입니다.',
                colour=discord.Colour.red()
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

    if message.content.startswith('!오늘날씨') or message.content.startswith('!날씨'):
        mes = message.content.replace('!오늘날씨', '').replace('!날씨', '').strip()
        today = todayWeather(mes)
        embed = discord.Embed(
                title='**날씨! 오늘! 날씨!**',
                description=today[0]+'의 오늘 날씨!',
                colour=discord.Colour.blue()
            )
        embed.add_field(name='현재 기온', value=today[1]+'도')
        embed.add_field(name='상태', value=today[2])
        embed.add_field(name='최저최고기온', value=today[3])
        embed.add_field(name='체감온도', value=today[4])
        embed.add_field(name='미세먼지', value=today[5])
        embed.set_footer(text='네이버 날씨 제공')
        await message.channel.send(embed=embed)

    if message.content.startswith('!내일날씨'):
        mes = message.content.replace('!내일날씨', '').strip()
        tomorr = tomorrowWeather(mes)
        embed = discord.Embed(
                title='**날씨! 내일! 날씨!**',
                description=tomorr[0]+'의 내일 날씨!',
                colour=discord.Colour.blue()
            )
        embed.add_field(name='내일 오전', value=tomorr[1]+'도')
        embed.add_field(name='상태', value=tomorr[2])
        embed.add_field(name='미세먼지', value=tomorr[3])
        embed.add_field(name='내일 오후', value=tomorr[4]+'도')
        embed.add_field(name='상태', value=tomorr[5])
        embed.add_field(name='미세먼지', value=tomorr[6])
        embed.set_footer(text='네이버 날씨 제공')
        await message.channel.send(embed=embed)
    
    if message.content.startswith('!기억'):
        mes = message.content.replace('!기억', '')
        mesTemp = setString(mes)
        if mesTemp[0] == '' or mesTemp[1] == '':
            await message.channel.send('기억할 문장이 이상한 거 같은데...제대로 가르쳐줘!')
        else:
            result = setMemory(mesTemp[0], mesTemp[1])
            await message.channel.send(result)
    
    if message.content.startswith('!삭제'):
        mes = message.content.replace('!삭제', '').strip()
        result = deleteMemory(mes)
        await message.channel.send(result)
    
    if message.content.startswith('!말해'):
        mes = message.content.replace('!말해', '').strip()
        result = findMemory(mes)
        await message.channel.send(result)

    if message.content.startswith('요정아'):
        mes = message.content.replace('요정아', '').strip()
        if mes == '':
            await message.channel.send(random.choice(hello))
        else :
            result = findMemory(mes)
            await message.channel.send(result)
    
    if message.content.startswith('!리스트'):
        memoryDataList = printMemory()
        printListStr = "```"
        for i in memoryDataList:
            printListStr = printListStr + i + '\n'
        printListStr = printListStr + "```"
        await message.channel.send('내 머리속을 보고 싶어하다니...변태...')
        await message.channel.send(printListStr)

    if message.content.startswith('!한일'):
        mes = message.content.replace('!한일', '').strip()
        transText = translate('ko', 'ja', mes)
        embed = discord.Embed(
            title=transText,
            description=mes,
            colour=discord.Colour.purple()
        )
        embed.set_footer(text='Translated by.네이버 파파고')
        await message.channel.send(embed=embed)
    
    if message.content.startswith('!일한'):
        mes = message.content.replace('!일한', '').strip()
        transText = translate('ja', 'ko', mes)
        embed = discord.Embed(
            title=transText,
            description=mes,
            colour=discord.Colour.purple()
        )   
        embed.set_footer(text='Translated by.네이버 파파고')
        await message.channel.send(embed=embed)

    if message.content.startswith('!한영'):
        mes = message.content.replace('!한영', '').strip()
        transText = translate('ko', 'en', mes)
        embed = discord.Embed(
            title=transText,
            description=mes,
            colour=discord.Colour.purple()
        )   
        embed.set_footer(text='Translated by.네이버 파파고')
        await message.channel.send(embed=embed)

    if message.content.startswith('!영한'):
        mes = message.content.replace('!영한', '').strip()
        transText = translate('en', 'ko', mes)
        embed = discord.Embed(
            title=transText,
            description=mes,
            colour=discord.Colour.purple()
        )   
        embed.set_footer(text='Translated by.네이버 파파고')
        await message.channel.send(embed=embed)

    if message.content.startswith('!재정') or message.content.startswith('!새롬') or message.content.startswith('!이룸'):
        dietTable = makeDietTable(message.content.replace('!', '').strip(), datetime.today().weekday())
        embed = discord.Embed(
            title = '식 단 표',
            description = '{0}의 오늘의 식단표'.format(message.content.replace('!', '').strip()),
            colour=discord.Colour.blue()
        )
        embed.add_field(name='아침', value = dietTable[0])
        embed.add_field(name='점심', value = dietTable[1])
        embed.add_field(name='저녁', value = dietTable[2])
        await message.channel.send(embed=embed)
    
    if message.content.startswith('!모두모여'):
        mes = message.content.replace('!모두모여', '').strip()
        await message.channel.send('@everyone ' + mes)

    if message.content.startswith('!운세') or message.content.startswith('!fortune'):
        await message.channel.send(makeFortune(message.author.display_name))

    if message.content.startswith('!fairy') or message.content.startswith('!요정수치'):
        await message.channel.send('{0}의 동방 요정수치는 무려 >>>{1}<<<씩이나 된다구?'.format(message.author.display_name, random.randint(1, 9999)))

    if message.content.startswith('!dice') or message.content.startswith('!주사위') or message.content.startswith("ㅈㅅㅇ"):
        mes = message.content.replace("!dice", "").replace("!주사위", "").replace("ㅈㅅㅇ", "").strip().upper().split('+')
        result = 0
        embed = discord.Embed(
            title = '주사위 결과',
            description = '입력한 주사위의 결과와 합입니다',
            color = random.randint(0, 0xffffff)
        )
        for i in mes:
            tmpDice = i.split('D')
            diceResult = dice(int(tmpDice[0]), int(tmpDice[1]))
            embed.add_field(name='{0}주사위'.format(i), value=diceResult)
            embed.add_field(name='{0}주사위의 합'.format(i), value=sum(diceResult))
            result = result + sum(diceResult)
        embed.add_field(name='주사위 총 합', value='{}'.format(result))
        await message.channel.send(embed=embed)

conch = makeConch(conch)
client.run('NjE4NzQ1MDU4MTYxODUyNDI2.XduPpw.umIWw4Z_lrJbDOa4v8Ja6FHrZKQ')
