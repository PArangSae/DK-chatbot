import discord
import time
import asyncio
import datetime
from random import *

client = discord.Client()
guild_list = client.guilds

@client.event
async def on_ready():
    print("{0:=^10}".format("켜지는중"))
    game = discord.Game("구름이 일어날려고 ")
    await client.change_presence(status=discord.Status.idle, activity=game)
    await asyncio.sleep(5)
    print("{0:=^10}".format("봇이켜짐"))
    print(client.user.id)
    game = discord.Game("봇 개발중 또는 점검을 진행")
    await client.change_presence(status=discord.Status.dnd, activity=game)
#상태
    while True:
        game = discord.Game("Cloud 봇 도움말 //help")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f"{len(client.users)} 명과 함께 ")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f"{len(client.guilds)} 개의 서버와 함께")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game("Version - M.B[1.4]")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)

@client.event
async def on_message(message):
#사용자확인
    if message.author.bot:
        return
    if message.content == ("//가입") or message.content == ("//join"):
        embed = discord.Embed(title = "Cloud 가입불가", description = "Cloud봇에 가입 할 수 있는 시간이 아닙니다. 오후 5시 경 다시 시도해주시기 바랍니다.", color = 0xff0000)
        me = await message.channel.send(embed = embed)
        i = 0
        return
    
#변수
    mchat = message.content
    nick = (f'{message.author}')
    nickid = message.author.id
    f = "구름아 "
    i = 1
    p = 0

#개발자
    if message.content.startswith("/,"):
        if message.author.id == 706788425352740887:
            if message.content.startswith("/,clear"):
                if message.content.startswith("/,clear"):
                    cu = mchat[8:]
                else:
                    cu = mchat[5:]
                await message.channel.purge(limit=int(cu))

            if message.content.startswith("/,dm"):
                try:
                    Dmm = mchat[5:].split("/")
                    dMm = client.get_user(int(Dmm[0]))
                    dmM = str(Dmm[1])
                    await dMm.send(dmM)
                    await message.channel.send("`전송완료`")
                except ValueError:
                    await message.channel.send("`전송실패`")
            
            if message.content.startswith("/,text"):
                await message.channel.send("`다음과 같습니다 = " + mchat + "`")

            if message.content.startswith("/,test"):
                if mchat == message.content:
                    await message.channel.send("`다음과 같습니다 = True`")
                else:
                    await message.channel.send("`다음과 같습니다 = False`")

#명령어
    if message.content.startswith("//"):
    #도움말
        if message.content.startswith("//help") or message.content.startswith("//도움"):
            embed = discord.Embed(title = "도움말", description = "help", colour = 0x0097ff)
            embed.add_field(name = "기본 명령어", value = "** **", inline = False)
            embed.add_field(name = "//help, //도움, //도움말", value = "Cloud봇의 도움말을 확인할 수 있어요!")
            embed.add_field(name = "//information, //봇정보, //봇", value = "Cloud봇의 개발자와 정보를 확인할 수 있어요!")
            embed.add_field(name = "//timer, //타이머", value = "타이머를 사용할 수 있어요!")
            embed.add_field(name = "//invite, //초대", value = "봇을 초대할 수 있어요!")
            embed.add_field(name = "//ping, //핑", value = "봇의 응답지연시간을 확인할 수 있어요!")
            embed.add_field(name = "//user, //내정보, //내 정보", value = "내 정보를 확인할 수 있어요!")
            embed.add_field(name = "//count, //카운트", value = "0부터 사용자가 정한 n까지의 숫자를 순서대로 출력해요!")
            embed.add_field(name = "//inquiry, //문의", value = "Cloud봇에관해 궁금한 사항이나 버그에대해 묻거나 제보할 수 있습니다!")
            embed.add_field(name = "관리자 명령어", value = "** **", inline = False)
            embed.add_field(name = "//clear, //청소", value = "채팅을 청소할 수 있어요!")
            embed.add_field(name = "또다른 명령어", value = "** **", inline = False)
            embed.add_field(name = "구름아 도움, 구름아 도움말", value = "Cloud 의 대화목록을 살펴보세요![구름아 따라해, 구름아 폭발, 등등]")
            embed.set_footer(text = "개발:corche-2000#6718[자세한 정보는 //information, //봇정보, //봇 을 이용하세요]")
            await message.channel.send(embed = embed)
            i = 0
            return

    #정보
        if message.content.startswith("//information") or message.content.startswith("//봇"):
            embed = discord.Embed(title = "봇 정보", description = "information", colour = 0x0097ff)
            embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/752412960013418496/752710762190864434/5_2.png")
            embed.add_field(name = "봇 정보", value = "이름ㅣCloud#5522\n봇버전ㅣM.B[1.4]\n최종업데이트일ㅣ2020-10-27\n생성일자ㅣ2020-09-05", inline = False)
            embed.add_field(name = "개발 정보", value = "개발자ㅣcorche-2000#6718\n개발프로그램ㅣ**V**isual**S**tudio**C**odeㅣ1.51.0(user.setup)\n개발환경ㅣDesktop[Windows_NT x64 10.0.19041]", inline = False)
            embed.add_field(name = "실행 정보", value = "실행프로그램ㅣpydroid3\n실행환경ㅣMobile[android-10ㅣKnox-3.5ㅣmodel-SM-A202k]", inline = False)
            embed.add_field(name = "개발언어/API", value = "python[3.9 / 3.8.6]\ndiscord.py[1.5.1]", inline = False)
            embed.set_footer(text = "Cloud#5522", icon_url="https://cdn.discordapp.com/attachments/752412960013418496/752710762190864434/5_2.png")
            await message.channel.send(embed = embed)
            i = 0
            return

    #타이머
        if message.content.startswith("//timer") or message.content.startswith("//타이머"):
            try:
                if message.content.startswith("//timer"):
                    tt = mchat[8:]
                else:
                    tt = mchat[6:]
                if int(tt) > 1000000:
                    embed = discord.Embed(colour=0xff0000)
                    embed.add_field(name = "오류 - 제한", value = " \nn 에는 최대 1000000 이 들어가야 합니다", inline=True)
                    await message.channel.send(embed = embed)
                    i = 0
                    return

                if int(tt) < 1:
                    embed = discord.Embed(color=0xff0000)
                    embed.add_field(name = "오류 - 제한", value = " \nn 에는 최소 1이 들어가야 합니다.", inline=True)
                    await message.channel.send(embed = embed)
                    i = 0
                    return

                embed = discord.Embed(title="타이머 :alarm_clock:", description = " ", colour=0x0097ff)
                embed.add_field(name = "타이머가 시작되었습니다!", value = "설정된 시간은 **" + tt + "**초 입니다!")
                await message.channel.send(embed = embed)
                await asyncio.sleep(int(tt))
                msgeee = await message.channel.send("<@!" + str(nickid) +  ">")
                await msgeee.delete()
                embed = discord.Embed(title="타이머 :alarm_clock:", description = " ", colour=0x0097ff)
                embed.add_field(name = nick + "님! 타이머가 종료되었습니다!", value = "**" + tt + "**초가 끝났습니다!")
                await message.channel.send(embed = embed)
                i = 0
                return
            except ValueError:
                embed = discord.Embed(color=0xff0000)
                embed.add_field(name="오류 - 구문", value=" \n//timer n, //타이머 n", inline=True)
                await message.channel.send(embed = embed)
                i = 0
                return
        
    #초대
        if message.content.startswith("//invite") or message.content.startswith("//초대"):
            embed = discord.Embed(title = ":paperclip:Cloud봇 초대 링크", description = "[초대하기](https://discord.com/api/oauth2/authorize?client_id=752410912090095616&permissions=8&scope=bot)", colour = 0x0097ff)
            await message.channel.send(embed=embed)
            i = 0
            return

    #핑
        if message.content.startswith("//ping") or message.content.startswith("//핑"):
            try:
                if (round(client.latency*1000)) < 249:
                    embed = discord.Embed(color=0x009900)
                    embed = discord.Embed(title="🏓퐁!", description="\n현재 핑ㅣ{0}ms\n상태ㅣ정상 :green_circle:".format(round(client.latency*1000)), color=0x00ff00)
                    embed.set_footer(text="상태가 매우 좋아요!")
                    await message.channel.send(embed=embed)
                    i = 0
                    return
                elif (round(client.latency*1000)) < 400:
                    embed = discord.Embed(color=0xebeb00)
                    embed = discord.Embed(title="🏓퐁!", description="\n현재 핑ㅣ{0}ms\n상태ㅣ보통 :yellow_circle:".format(round(client.latency*1000)), color=0xebeb00)
                    embed.set_footer(text="상태가 나쁘지 않군요!")
                    await message.channel.send(embed=embed)
                    i = 0
                    return
                elif (round(client.latency*1000)) < 550:
                    embed = discord.Embed(color=0xff0000)
                    embed = discord.Embed(title="🏓퐁!", description="\n현재 핑ㅣ{0}ms\n상태ㅣ나쁨 :red_circle:".format(round(client.latency*1000)), color=0xff0000)
                    embed.set_footer(text="사용량을 줄여주세요!")
                    await message.channel.send(embed=embed)
                    i = 0
                    return
                elif (round(client.latency*1000)) > 699:
                    embed = discord.Embed(color=0xffffff)
                    embed = discord.Embed(title="🏓퐁!", description="\n현재 핑ㅣ{0}ms\n상태ㅣ위험 :warning:".format(round(client.latency*1000)), color=0xffffff)
                    embed.set_footer(text="프로그램을 종료합니다!")
                    await message.channel.send(embed=embed)
                    print("중지이유 : 높은 지연시간 [ " + str((round(client.latency*1000))) + " ]")
                    i = 0
                    while True:
                        i = 0
                    return
                else:
                    embed = discord.Embed(color=0xff0000)
                    embed = discord.Embed(name="측정오류", description="\n핑을 측정하지 못하였습니다. 다시 시도 해주세요.".format(round(client.latency*1000)), color=0xff0000)
                    embed.set_footer(text="해당오류가 계속될시 사진 캡쳐와 함께 Cloud 고객센터에 알려주시기 바랍니다.")
                    await message.channel.send(embed=embed)
                    i = 0
                    return
            except ValueError:
                embed = discord.Embed(name="오류 - 시스템", description="\n핑을 측정하지 못하였습니다. 다시 시도 해주세요.".format(round(client.latency*1000)), color=0xff0000)
                embed.set_footer(text="해당오류가 계속될시 사진 캡쳐와 함께 Cloud 고객센터에 알려주시기 바랍니다.")
                await message.channel.send(embed=embed)
                i = 0
                return

    #사용자정보
        if message.content.startswith("//user") or message.content.startswith("//내정보") or message.content.startswith("//내 정보"):
            try:
                date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
                embed = discord.Embed(color=0x0097ff)
                embed.add_field(name="이름", value=message.author.name, inline=False)
                embed.add_field(name="태그", value=idid, inline=False)
                embed.add_field(name="프로필 링크", value="[:frame_photo:프로필보기]({})".format(message.author.avatar_url), inline=False)
                embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
                embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
                embed.add_field(name="아이디", value=message.author.id, inline=False)
                embed.set_thumbnail(url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                i = 0
                return
            except ValueError:
                embed = discord.Embed(color = 0xff0000)
                embed.add_field(name="오류 - 시스템", value="사용자 정보를 확인할 수 없습니다.")
                embed.set_footer(text="해당오류가 계속될시 사진 캡쳐와 함께 Cloud 고객센터에 알려주시기 바랍니다.")
                await message.channel.send(embed=embed)
                i = 0
                return

    #순서출력
        if message.content.startswith("//count") or message.content.startswith("//카운트"):
            try:
                if message.content.startswith("//count"):
                    rr = int(mchat[8:])
                else:
                    rr = int(mchat[6:])
                if rr < 1:
                    embed = discord.Embed(colour=0xff0000)
                    embed.add_field(name = "계산오류", value = " \nn 에는 최소 1 이 들어가야 합니다", inline=True)
                    await message.channel.send(embed = embed)
                    i = 0
                    return
                if rr > 500:
                    embed = discord.Embed(colour=0xff0000)
                    embed.add_field(name = "계산오류", value = " \nn 에는 최대 500 이 들어가야 합니다", inline=True)
                    await message.channel.send(embed = embed)
                    i = 0
                    return
                rrr = 0
                rrrr = "0 "
                while True: 
                    rrr += 1
                    rrrr = str(rrrr) + str(rrr) + " "
                    if rrr == rr:
                        embed = discord.Embed(title = "숫자 순서", description = str(rrrr), color=0x0097ff)
                        await message.channel.send(embed = embed)
                        i = 0
                        return
            except ValueError:
                embed = discord.Embed(color=0xff0000)
                embed.add_field(name="오류 - 구문", value=" \n//count n, //카운트 n", inline=True)
                await message.channel.send(embed = embed)
                i = 0
                return

    #문의
        if message.content == ("//inquiry") or message.content == ("//문의"):
            embed = discord.Embed(title = "문의 이용법", description = "지금 문의를 아래에 제시된 3개의 양식대로 적어주세요.", color = 0x0097ff)
            embed.add_field(name = "Cloud에 궁금한점을 물어볼때", value = "///질문.(질문 내용)")
            embed.add_field(name = "Cloud에 대한 버그를 제보할때", value = "///버그.(버그내용).(해당 버그가 발생 하는 방법)")
            embed.add_field(name = "Cloud악성 유저를 신고할때", value = "///신고.(해당 유저의 이름).#(번호).(신고사유)")
            await message.channel.send(embed = embed)
            i = 0
            return

        if message.content.startswith("///"):
            developer = client.get_user(int(706788425352740887))
            if message.content.startswith("///질문"):
                question = message.content[6:]
                await developer.send("**질문**\n질문 : " + str(question) + "\n`Nick : " + str(nick) + "ㅣID : " + str(nickid) + "`")
                embed = discord.Embed(title = "개발자에게 질문이 전송되었습니다!!", description = "답변은 Dm으로 옵니다. 답변을 받으시려면 다음의 내용대로 설정해 주시기 바랍니다! [사용자 설정->개인정보 보호 및 보안->서버 멤버가 보내는 개인메시지 허용하기 ON]", color = 0x0097ff)
                await message.channel.send(embed=embed)
                i = 0
                return

            if message.content.startswith("///버그"):
                bug = message.content[6:].split(".")
                await developer.send("**버그**\n버그내용 : " + str(bug[0]) + "ㅣ버그방법 : " + str(bug[1]) + "\n`Nick : " + str(nick) + "ㅣID : " + str(nickid) + "`")
                embed = discord.Embed(title = "개발자에게 버그내용이 전송되었습니다!!", description = "답변은 Dm으로 옵니다. 답변을 받으시려면 다음의 내용대로 설정해 주시기 바랍니다! [사용자 설정->개인정보 보호 및 보안->서버 멤버가 보내는 개인메시지 허용하기 ON]", color = 0x0097ff)
                await message.channel.send(embed=embed)
                i = 0
                return

            if message.content.startswith("///신고"):
                report = message.content[6:].split(".")
                await developer.send("**유저신고**\n이름과 #번호 : " + str(report[0]) + str(report[1]) + "ㅣ신고사유 : " + str(report[2]) + "\n`Nick : " + str(nick) + "ㅣID : " + str(nickid) + "`")
                embed = discord.Embed(title = "개발자에게 신고가 전송되었습니다!!", description = "답변은 Dm으로 옵니다. 답변을 받으시려면 다음의 내용대로 설정해 주시기 바랍니다! [사용자 설정->개인정보 보호 및 보안->서버 멤버가 보내는 개인메시지 허용하기 ON]", color = 0x0097ff)
                await message.channel.send(embed=embed)
                i = 0
                return

    #청소[관리자]
        if message.content.startswith("//clear") or message.content.startswith("//청소"):
            if message.author.guild_permissions.manage_messages:
                try:
                    if message.content.startswith("//clear"):
                        cu = mchat[8:]
                    else:
                        cu = mchat[5:]
                    if int(cu) < 1:
                        embed = discord.Embed(color=0xff0000)
                        embed.add_field(name = "계산오류", value = " \nn 에는 최소 1이 들어가야 합니다.", colour=0x0097ff, inline=True)
                        await message.channel.send(embed = embed)
                        i = 0
                        return
                    if int(cu) > 999:
                        embed = discord.Embed(color=0xebeb00)
                        embed.add_field(name = "주의", value = " \n설정된수가 1000이상일때는 렉이 있을 수 있습니다.", colour=0x0097ff, inline=True)
                        await message.channel.send(embed = embed)
                        p = 1
                        pass
                    embed = discord.Embed(title = "청소 시작! :wastebasket:", description = cu + " 개의 메시지 청소준비..", colour=0x0097ff, inline=True)
                    await message.channel.send(embed=embed)
                    if p == 1:
                        cu = int(cu) + 2
                    else:
                        cu = int(cu) + 1
                    await message.channel.purge(limit=int(cu))
                    if p == 1:
                        cu = int(cu) - 2
                    else:
                        cu = int(cu) - 1
                        
                    embed = discord.Embed(title = "청소 완료! :sparkles:", description = str(cu) + " 개의 메시지를 청소했어요!", colour=0x0097ff, inline=True)
                    await message.channel.send(embed=embed)
                    i = 0
                    return
                except ValueError:
                    embed = discord.Embed(color=0xff0000)
                    embed.add_field(name = "오류 - 구문", value = " \n//clear n, //청소 n", inline=True)
                    await message.channel.send(embed = embed)
                    i = 0
                    return
            else:
                embed = discord.Embed(color=0xff0000)
                embed.add_field(name = "오류 - 권한", value = " \n이 작업을 수행할 권한을 가지고 있지 않습니다.", inline=True)
                await message.channel.send(embed = embed)
                i = 0
                return

    #명령어오류
        if i == 1:
            embed = discord.Embed(color = 0xff0000)
            embed.add_field(name="오류 - 구문", value=mchat + "은 존재하지 않는 명령어입니다 //help 또는 //도움, //도움말 을 사용하여 명령어 목록을 참조하시기 바랍니다")
            await message.channel.send(embed=embed)

#게임
    if message.content.startswith("/."):
            embed = discord.Embed(color = 0xff0000)
            embed.add_field(name="안내 - 현재는 게임 이용시간이 아닙니다", value="현재는 게임을 이용할 수 없습니다. 오후 5시 경 다시시도해 주시기 바랍니다.")
            await message.channel.send(embed=embed)
            return

#대화
    if message.content.startswith("구름아"):  
    #일반대화

        if message.content.startswith(f + "안녕") or message.content.startswith(f + "ㅎㅇ") or message.content.startswith(f + "반가워"):
            await message.channel.send("네 안녕하세요 " + nick + " 님! 만나서 반가워요!")
            i = 0
            return

        if message.content.startswith(f + "잘가") or message.content.startswith(f + "ㅂㅂ") or message.content.startswith(f + "나중에"):
            await message.channel.send("네 " + nick + " 님! 안녕히가세요!")
            i = 0
            return

        if message.content.startswith(f + "뭐해") or message.content.startswith(f + "뭐함") or message.content.startswith(f + "ㅁㅎ"):
            await message.channel.send("멍때리고 있었어요")
            i = 0
            return

        if message.content.startswith(f + "죽어") or message.content.startswith(f + "주거") or message.content.startswith(f + "꽥"):
            await message.channel.send("꽥!")
            i = 0
            return

        if message.content.startswith(f + "심심해") or message.content.startswith(f + "쉼쉼해"):
            await message.channel.send("아쉽게도 현재는 게임을 이용할 수 있는 시간대가 아니에요.. 오후 5시경 게임을 이용할 수 있어요!")
            i = 0
            return

        if message.content.startswith(f + "빼액") or message.content.startswith(f + "빼애"):
            await message.channel.send("빼애애ㅐ애애앵ㄱ")
            i = 0
            return

        if message.content.startswith(f + "구름") or message.content == ("구름아") or message.content.startswith(f + "구름아") or message.content.startswith(f + "?"):
            r = randint(1,3)
            if r == 1:
                await message.channel.send("저 말씀하신건가요?")
                i = 0
                return
            elif r == 2:
                await message.channel.send("네?")
                i = 0
                return
            elif r == 3:
                await message.channel.send("부르셨어요??")
                i = 0
                return

        if message.content.startswith(f + "유튜브") or message.content.startswith(f + "유튭"):
            await message.channel.send("알고리즘이 지배하는 사이트(https://www.youtube.com)")
    #수정

        if message.content.startswith(f + "여친") or message.content.startswith(f + "연애"):
            m = await message.channel.send("야이 개ㅅ")
            await asyncio.sleep(1)
            await m.edit(content="***어라?***")
            i = 0
            return
        
        if message.content.startswith(f + "치킨") or message.content.startswith(f + "피자") or message.content.startswith(f + "닭다리") or message.content.startswith(f + "햄버거"):
            m = await message.channel.send("나도줘!!!!!!!!!!!!!!!!!!!!")
            await asyncio.sleep(1)
            await m.edit(content="***우물우물***(당신은 음식을 빼앗겼다)")
            i = 0
            return
        
        if message.content.startswith(f + "멍청이"):
            m = await message.channel.send("지가 더 멍청하면서 ㅋ")
            await asyncio.sleep(1)
            await m.edit(content="***어라?***")
            i = 0
            return
        
        if message.content.startswith(f + "토큰"):
            m = await message.channel.send("내가 바보가 아닌이상 절대 못 넘겨주지 ㅋ")
            await asyncio.sleep(1)
            await m.edit(content="***어라?***")
            i = 0
            return

        if message.content.startswith(f + "바보") or message.content.startswith(f + "멍청이"):
            m = await message.channel.send("내가 바보면 니는 IQ가 금붕어다")
            await asyncio.sleep(1)
            await m.edit(content="***어라?***")
            i = 0
            return
    #밈
        if message.content.startswith(f + "죽여줘") or message.content.startswith(f + "죽여"):
            if message.content == (f + "죽여줘"):
                kill = message.content[8:]
            else:
                kill = message.content[7:]
            await message.channel.send(kill + "을(를) 제거합니닷! [푸슝~!]\n`" + nick + "님이 발사했어요!`")
            await message.channel.send("https://tenor.com/view/explode-explosion-gif-13727381")
            i = 0
            return

        if message.content.startswith(f + "관짝"):
            await message.channel.send("`" + nick + "님이 요청했어요!`")
            await message.channel.send("https://tenor.com/view/dancing-coffin-dancing-pallbearers-funeral-dance-gif-16837090")
            i = 0
            return

        if message.content.startswith(f + "춤") or message.content.startswith(f + "댄스"):
            await message.channel.send("자 갑니다!\n`" + nick + "님이 춤을 추셨어요!`")
            await message.channel.send("https://tenor.com/view/boy-gif-4641773")
            i = 0
            return

        if message.content.startswith(f + "폭발") or message.content.startswith(f + "폭팔") or message.content.startswith(f + "폭8"):
            r = randint(1,100)
            if r > 10:
                await message.channel.send("펑!\n`" + nick + "님이 터뜨리셨어요!`")
                await message.channel.send("https://media.discordapp.net/attachments/740105707923177502/740158210471755826/96c1b74cfb68ff8e.gif")
                i = 0
                return
            else:
                await message.channel.send("어라? 불발인가..?")
                i = 0
                return

    #명령어
        if message.content.startswith(f + "도움") or message.content.startswith(f + "도움말"):
            embed = discord.Embed(title = "대화 도움말", description = "talk help", colour = 0x0097ff)
            embed.add_field(name = "대화 명령어", value = "** **", inline = False)
            embed.add_field(name = "구름아 도움, 구름아 도움말", value = "Cloud대화 명령어를 확인할 수 있어요!")
            embed.add_field(name = "구름아 죽여 (대상), 구름아 죽여줘 (대상)", value = "구름이가 지정한대상에게 폭격을 가합니다!")
            embed.add_field(name = "구름아 관짝", value = "말 안해도 알죠?")
            embed.add_field(name = "구름아 춤, 구름아 댄스", value = "춤을 춰봅시다!")
            embed.add_field(name = "구름아 폭발, 구름아 폭팔, 구름아 폭8", value = "Boom!")
            embed.add_field(name = "구름아 따라해 (내용)", value = "구름이가 따라말해요!")
            embed.add_field(name = "구름아 (내용)", value = "구름이와 대화를 할 수 있어요!")
            embed.add_field(name = "구름아 확률", value = "구름이가 제공하는 랜덤의 확률을 확인할 수 있어요!")
            embed.add_field(name = "또다른 명령어", value = "** **", inline = False)
            embed.add_field(name = "//help, //도움, //도움말", value = "Cloud봇의 도움말을 확인할 수 있어요!")
            embed.set_footer(text = "개발:corche-2000#6718[자세한 정보는 //information, //봇정보, //봇 을 이용하세요]")
            await message.channel.send(embed = embed)
            i = 0
            return

        if message.content.startswith(f + "따라해"):
            mhat = mchat[8:]
            await message.channel.send(mhat + "\n`" + nick + "님이 따라말하라고 하셨어요!`")
            i = 0
            return

    #없는 대화
        if i == 1:
            p = randint(1, 3)
            if p == 1:
                await message.channel.send("` " + mchat[4:] + " `?")
            elif p == 2:
                await message.channel.send("` " + mchat[4:] + " ` 가 뭐죠??")
            elif p == 3:
                await message.channel.send("` " + mchat[4:] + " ` 는 처음듣는데요?")

#비접두사
    if message.content.startswith("?"):
        r = randint(1,100)
        if r > 49:
            await message.channel.send("??")
            i = 0
            return
        else:
            i = 0
            return

    if message.content.startswith("ㅋ"):
        r = randint(1,100)
        if r > 49:
            await message.channel.send("ㅋㅋㅋㅋㅋ")
            i = 0
            return
        else:
            i = 0
            return

    if message.content.startswith("ㄷ"):
        r = randint(1,100)
        if r > 49:
            await message.channel.send("ㄷㄷ")
            i = 0
            return
        else:
            i = 0
            return

#token
client.run("NzUyNDEwOTEyMDkwMDk1NjE2.X1XPRA.7rqHXCO3bwzKcdntNF86T_pbaiQ")