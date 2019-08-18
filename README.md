# PansaDiscordBot

## 디스코드 개인 봇 feat.동아리디코

동아리에서 자주 사용하는...아니 자주 사용할 거 같은 기능들을 디스코드를 통해 바로 활용할 수 있도록 
여러가지 기능을 넣은 디스코드 개인 봇입니다.

### myBot.py

**메인 프로그램** 파일입니다.

#### 함수

- **def makeConch()**
magicConch.txt 파일을 불러들여 소라고둥 답변 리스트를 저장합니다.

- **def absurbDiary(inputInt)**
diary.json파일을 읽어들여 inputInt에 해당하는 JSON 형식의 데이터를 반환합니다.
inputInt가 0일 경우 랜덤한 데이터를 반환합니다.

- **def cypersRank(nickname)**
넥슨에서 서비스중인 게임 **사이퍼즈**의 닉네임명을 인자로 받아와서 검색한 다음 
URL주소, 전적, 최근 경기 결과, 사용 캐릭터의 이미지 URL가 각각 저장되어있는 리스트를 반환합니다.

- **def getMillDate(name)**
이름을 인자로 받아와서 해당하는 전역일을 계산하여 문장으로 반환합니다.
이름이 검색되지 않는 경우에도 지정된 문장을 반환합니다.

- **def todayWeather(search)**
네이버에서 날씨를 검색한 후 위치, 현재 온도, 날씨 상태, 최저최고기온, 체감온도, 미세먼지가 저장된 리스트를 반환합니다.

- **def tomorrowWeather(search)**
내일 오전의 온도, 상태, 미세먼지, 내일 오후의 온도, 상태 미세먼지가 저장된 리스트를 반환합니다.

- **def setXl()**
기억을 저장할 파일을 세팅합니다.

- **def setMemory(inputData, outputData)**
기억을 저장합니다. inputData는 Key값으로 A행에, outputData는 value값으로 B행에 각각 저장됩니다

- **def deleteMemory(inputData)**
기억을 삭제합니다.

- **def setString(input)**
AAA /BBB 형태의 문장을 ['AAA', 'BBB']형태의 리스트로 변환합니다.

- **def findMemory(inputData)**
inputData에 해당하는 값을 파일에서 찾아 반환합니다.

- **def translate(source, target, text)**
네이버 파파고 번역기를 통해 문장을 번역합니다.

- **def makeTaki()**
takiTaki.xlsx 파일을 읽어들여 A행의 값 중 랜덤하게 한 문장을 출력합니다.

#### 클라이언트 함수

- **async def on_ready()**
메인 프로그램 실행 후 정상적으로 접속 시 값이 명령 프롬프트에 출력됩니다.

- **async def on_message(message)**
특정 명령어를 받게 되는 경우 어떤 작업을 할지 구현하였습니다.

  - **!도움** 커맨드 목록을 출력합니다.
  - **!망언집 {번호}, !망언 {번호}, !diary {번호}** 번호에 해당하는 망언을 출력합니다. 번호가 없을 경우 랜덤하게 출력합니다.
  - **!선택 {리스트}** 여러 항목을 읽어들인 후 랜덤하게 한 항목을 선택하여 출력합니다.
  - **!타키, !taki** 오늘의 타키군을 출력합니다.
  - **!소라고둥, 소라고둥님, 마법의소라고둥님, 마법의 소라고둥님** 저장된 답변 중 하나를 랜덤하게 출력합니다.
  - **!전역일 {이름}** 입력받은 이름을 가진 사람의 전역까지 남은 날짜를 출력합니다.
  - **!오늘날씨, !내일날씨** 네이버 날씨 검색 결과를 읽어들인 후 출력합니다.
  - **!사이퍼즈 {게임} {닉네임}** 사이퍼즈 전적을 출력합니다. {게임}항목에는 공식/일반 둘 중 하나를 입력하여 가장 최근 경기를 출력할 수 있습니다. {게임}항목이 입력되지 않은 경우 전적만 출력합니다.
  - **!기억 문장1/문장2** 문장을 기억합니다.
  - **!삭제 문장1** 문장을 삭제합니다.
  - **!말해, 요정아** 문장1을 입력시 기억한 문장2를 출력합니다.
  - **!리스트** 현재 저장된 기억들을 출력합니다.
  - **!한영, !영한, !한일, !일한** 네이버 파파고 번역기를 통해 문장을 번역합니다.
  - **!모두모여 (문장)** 채널 내의 모든 사람들을 호출합니다. 문장 입력 시 문장을 같이 출력합니다.

### diary.json

망언집 파일입니다. 실제 데이터는 많지만 테스트용임과 동시에 이름과 같은 개인정보를 포함하고 있는 경우도 있어
최소한의 데이터만 저장해 두었습니다.
- 번호: 데이터 번호입니다.
-- absurb: 망언 내용입니다.
-- name: 망언을 한 사람입니다.
-- description: 망언이 나온 상황입니다.

### militaryDate2.txt

이름과 전역일이 저장된 파일입니다.

### magicConch.txt

!소라고둥 커맨드의 답변이 저장된 파일입니다. 띄어쓰기('\n')로 구분되어 있습니다.

### memoryData.xlsx

기억이 저장되어 있는 파일입니다. A행에는 key값, B행에는 value값이 저장되어 있습니다.

### 수정 내역
- 2019.07.30 최초 업로드
- 2019.08.05 !사이퍼즈, !망언집 기능 추가 및 수정, !선택 커맨드 추가
- 2019.08.06 !전역일 커맨드 추가
- 2019.08.07 !사이퍼즈 커맨드 기능 세분화, !소라고둥, !도움 커맨드 추가
- 2019.08.09 !날씨, !기억, !말해, !삭제, !모두모여 커맨드 추가, 코드 정리
- 2019.08.12 번역 관련 커맨드 추가, !날씨 커맨드 !오늘날씨, !내일날씨로 세분화, 기타 버그 수정 
- 2019.08.19 망언집 파일 JSON으로 변경에 따른 !망언 커맨드 수정, !타키 커맨드 추가 
