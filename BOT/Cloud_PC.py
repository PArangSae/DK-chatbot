import discord
import time
import asyncio
import datetime
import json
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
    game = discord.Game("봇 점검을 진행")
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
        game = discord.Game("Version - PC[1.7]")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)

@client.event
async def on_message(message):
#사용자확인
    if message.author.bot:
        return
    if message.content == ("//가입") or message.content == ("//join"):
        with open("user.json") as json_file:
            json_data = json.load(json_file)
        if str(message.author.id) in json_data:
            embed = discord.Embed(title = "Cloud 가입실패", description = "Cloud 에 이미 가입되셨습니다..", color = 0xff0000)
            me = await message.channel.send(embed = embed)
            return
        else:
            nicke = (f'{message.author}')
            uid = nicke.split("#")
            with open("user.json") as json_file:
                json_data = json.load(json_file)
            json_data[str(message.author.id)] = str(uid[1])
            with open("user.json", 'w', encoding='utf-8') as make_file:
                json.dump(json_data, make_file, indent="\t")
            with open("money.json") as json_file:
                json_data = json.load(json_file)
            json_data[str(message.author.id)] = str(0)
            with open("money.json", 'w', encoding='utf-8') as make_file:
                json.dump(json_data, make_file, indent="\t")
            with open("attendance_check.json") as json_file:
                json_data = json.load(json_file)
            json_data[str(message.author.id)] = str(0)
            with open("attendance_check.json", 'w', encoding='utf-8') as make_file:
                json.dump(json_data, make_file, indent="\t")
            with open("attendance_check_level.json") as json_file:
                json_data = json.load(json_file)
            json_data[str(message.author.id)] = str(0)
            with open("attendance_check_level.json", 'w', encoding='utf-8') as make_file:
                json.dump(json_data, make_file, indent="\t")
            with open("lottery.json") as json_file:
                json_data = json.load(json_file)
            json_data[str(message.author.id)] = str(0)
            with open("lottery.json", 'w', encoding='utf-8') as make_file:
                json.dump(json_data, make_file, indent="\t")
            embed = discord.Embed(title = "Cloud 가입", description = "Cloud봇에 가입 하였습니다", color = 0x0097ff)
            embed.add_field(name = "지침서", value = "Cloud에 가입을 하면 Cloud의 기능 및 서비스를 이용하실 수 있습니다.\n가입을 하지 않을경우 Cloud 의 서비스를 제공받을 수 없습니다.\n가입취소를 원하시는 경우 문의를 보내주시기 바랍니다.", inline = False)
            embed.add_field(name = "Cloud 에서 제공하는 서비스", value = "돈 시스템, 명령어, 대화, 게임, 등")
            embed.add_field(name = "Cloud 에서 수집하는 항목", value = "사용자의 ID, 사용자의 이름, 사용자의 채팅")
            embed.add_field(name = "Cloud 에서 수집하지 않는 항목", value = "사용자의 토큰, 사용자의 이메일, 사용자의 IP, 사용자의 비밀번호")
            embed.add_field(name = "Cloud 이용 규칙", value = "```1. 봇을 도배나 테러의 목적으로 사용할경우 영구 밴 처리됩니다.\n2. 봇에 과부화를 주어 봇 테러를 가할 경우 경고가 지급됩니다.\n3. 봇으로 남에게 피해를 주는 행동은 삼가주시기 바랍니다.```")
            me = await message.channel.send(embed = embed)
            return
    if message.content.startswith("//") or message.content.startswith("/.") or message.content.startswith("구름아"):
        with open("user.json") as json_file:
            json_data = json.load(json_file)
        if str(message.author.id) not in json_data:
            embed = discord.Embed(color = 0xff0000)
            embed.add_field(name = "Cloud 봇에 가입되지 않으셨습니다..", value = "'//가입' 또는 '//join' 을 이용하여 Cloud봇에 가입해주세요!!")
            await message.channel.send(embed = embed)
            return
        else:
            with open ("temporary_suspension.json") as json_file:
                json_data = json.load(json_file)
            if str(message.author.id) in json_data:
                author = client.get_user(int(message.author.id))
                await author.send("현재 사용자의 계정이 **임시** 차단 당하셨습니다! 앞으로 일정기간동안 Cloud의 모든서비스를 이용할 수 없습니다!")
                return
            else:
                pass
            with open ("permanent_stop.json") as json_file:
                json_data = json.load(json_file)
            if str(message.author.id) in json_data:
                author = client.get_user(int(message.author.id))
                await author.send("현재 사용자의 계정이 **영구** 차단 당하셨습니다! 이제부터 영구적으로 Cloud의 모든서비스를 이용할 수 없습니다!")
                return
            else:
                pass

#변수
    mchat = message.content
    nick = (f'{message.author}')
    nickid = message.author.id
    i = 1
    p = 0

#개발자 
    if message.content.startswith("/,"):
        if message.author.id == 706788425352740887:
            f = "/,"
            if message.content.startswith(f + "clear"):
                if message.content.startswith(f + "clear"):
                    cu = mchat[8:]
                else:
                    cu = mchat[5:]
                await message.channel.purge(limit=int(cu))

            if message.content.startswith(f + "server"):
                serverCount = len(client.guilds)
                embed = discord.Embed(title = "서버수업데이트됨", description = (""), color = 0x0097ff)
                embed.add_field(title = "현재 서버수", value = "")

            if message.content.startswith(f + "dm"):
                try:
                    Dmm = mchat[5:].split("|")
                    dMm = client.get_user(int(Dmm[0]))
                    dmM = str(Dmm[1])
                    await dMm.send(dmM)
                    await message.channel.send("`전송완료`")
                except ValueError:
                    await message.channel.send("`전송실패`")

            if message.content.startswith(f + "text"):
                await message.channel.send("`다음과 같습니다 = " + mchat + "`")

            if message.content.startswith(f + "test"):
                if mchat == message.content:
                    await message.channel.send("`다음과 같습니다 = True`")
                else:
                    await message.channel.send("`다음과 같습니다 = False`")
            
            if message.content.startswith(f + "kick"):
                us = message.content[7:].split("|")
                with open("temporary_suspension.json") as json_file:
                    json_data = json.load(json_file)
                json_data[str(us[0])] = str(us[1])
                with open("temporary_suspension.json", 'w', encoding='utf-8') as make_file:
                    json.dump(json_data, make_file, indent="\t")
                return

            if message.content.startswith(f + "money"):
                us = message.content[8:].split("|")
                with open("money.json") as json_file:
                    json_data = json.load(json_file)
                json_data[str(us[0])] = str(us[1])
                with open("money.json", 'w', encoding='utf-8') as make_file:
                    json.dump(json_data, make_file, indent="\t")
                return

            if message.content.startswith(f + "ban"):
                us = message.content[7:].split("|")
                with open("permanent_stop.json") as json_file:
                    json_data = json.load(json_file)
                json_data[str(us[0])] = str(us[1])
                with open("permanent_stop.json", 'w', encoding='utf-8') as make_file:
                    json.dump(json_data, make_file, indent="\t")
                return

            if message.content.startswith(f + "print_id"):
                iol = message.content[11:]
                with open ("temporary_suspension.json") as json_file:
                    json_data = json.load(json_file)
                if str(iol) in json_data:
                    await message.channel.send(json_data[str(iol)])
                else:
                    with open ("permanent_stop.json") as json_file:
                        json_data = json.load(json_file)
                    if str(iol) in json_data:
                        await message.channel.send(json_data[str(iol)])
                    else:
                        await message.channel.send("`해당하는 사용자 없음`")

#명령어
    if message.content.startswith("//"):
        f = "//"
    #도움말
        if message.content.startswith(f + "help") or message.content.startswith(f + "도움"):
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
            embed.add_field(name = "/.help, /.도움", value = "Cloud 봇의 게임기능을 이용할 수 있어요![/.출첵, /.눈송이 줘, /.내 눈송이, 등등]")
            embed.add_field(name = "구름아 도움, 구름아 도움말", value = "Cloud 의 대화목록을 살펴보세요![구름아 따라해, 구름아 폭발, 등등]")
            embed.set_footer(text = "개발:corche-2000#6718[자세한 정보는 //information, //봇정보, //봇 을 이용하세요]")
            await message.channel.send(embed = embed)
            i = 0
            return

    #정보
        if message.content.startswith(f + "information") or message.content.startswith(f + "봇"):
            embed = discord.Embed(title = "봇 정보", description = "information", colour = 0x0097ff)
            embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/752412960013418496/752710762190864434/5_2.png")
            embed.add_field(name = "봇 정보", value = "이름ㅣCloud#5522\n봇버전ㅣPC[1.7]\n최종업데이트일ㅣ2020-11-08\n생성일자ㅣ2020-09-05", inline = False)
            embed.add_field(name = "개발 정보", value = "개발자ㅣcorche-2000#6718\n개발프로그램ㅣVisualStudioCodeㅣ1.51.0(user.setup)\n개발환경ㅣDesktop[Windows_NT x64 10.0.19041]", inline = False)
            embed.add_field(name = "실행 정보", value = "실행프로그램ㅣVisualStudioCode\n실행환경ㅣDesktop[Windows_NT x64 10.0.19041]", inline = False)
            embed.add_field(name = "개발언어/API", value = "python[3.9 / 3.8.6]\ndiscord.py[1.5.1]", inline = False)
            embed.set_footer(text = "Cloud#5522", icon_url="https://cdn.discordapp.com/attachments/752412960013418496/752710762190864434/5_2.png")
            await message.channel.send(embed = embed)
            i = 0
            return

    #타이머
        if message.content.startswith(f + "timer") or message.content.startswith(f + "타이머"):
            try:
                if message.content.startswith(f + "timer"):
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
                embed.add_field(name="오류 - 구문", value=" \n//timer n, //타이머 n 또는 n 에 정수가 들어가야 합니다", inline=True)
                await message.channel.send(embed = embed)
                i = 0
                return
        
    #초대
        if message.content.startswith(f + "invite") or message.content.startswith(f + "초대"):
            embed = discord.Embed(title = ":paperclip:Cloud봇 초대 링크", description = "[초대하기](https://discord.com/api/oauth2/authorize?client_id=752410912090095616&permissions=8&scope=bot)", colour = 0x0097ff)
            await message.channel.send(embed=embed)
            i = 0
            return

    #핑
        if message.content.startswith(f + "ping") or message.content.startswith(f + "핑"):
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
                    embed = discord.Embed(name="측정오류", description="\n핑을 측정하지 못하였습니다. 다시 시도 해주세요.", color=0xff0000)
                    embed.set_footer(text="해당오류가 계속될시 사진 캡쳐와 함께 Cloud 고객센터에 알려주시기 바랍니다.")
                    await message.channel.send(embed=embed)
                    i = 0
                    return
            except ValueError:
                embed = discord.Embed(name="오류 - 시스템", description="\n핑을 측정하지 못하였습니다. 다시 시도 해주세요.", color=0xff0000)
                embed.set_footer(text="해당오류가 계속될시 사진 캡쳐와 함께 Cloud 고객센터에 알려주시기 바랍니다.")
                await message.channel.send(embed=embed)
                i = 0
                return

    #사용자정보
        if message.content.startswith(f + "user") or message.content.startswith(f + "내정보") or message.content.startswith(f + "내 정보"):
            try:
                date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
                nikke = nick.split("#")
                embed = discord.Embed(color=0x0097ff)
                embed.add_field(name="이름", value=message.author.name, inline=False)
                embed.add_field(name="태그", value="#" + str(nikke[1]), inline=False)
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
        if message.content.startswith(f + "count") or message.content.startswith(f + "카운트"):
            try:
                if message.content.startswith(f + "count"):
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
        if message.content == (f + "inquiry") or message.content == (f + "문의"):
            embed = discord.Embed(title = "문의 이용법", description = "지금 문의를 아래에 제시된 3개의 양식대로 적어주세요.", color = 0x0097ff)
            embed.add_field(name = "Cloud에 궁금한점을 물어볼때", value = "///질문 (질문 내용)")
            embed.add_field(name = "Cloud에 대한 버그를 제보할때", value = "///버그 (버그내용)|(해당 버그가 발생 하는 방법)")
            embed.add_field(name = "Cloud악성 유저를 신고할때", value = "///신고 (해당 유저의 이름)|#(번호)|(신고사유)")
            await message.channel.send(embed = embed)
            i = 0
            return

        if message.content.startswith("///"):
            f = "///"
            developer = client.get_user(int(706788425352740887))
            if message.content.startswith(f + "질문"):
                question = message.content[6:]
                await developer.send("**질문**\n질문 : " + str(question) + "\n`Nick : " + str(nick) + "ㅣID : " + str(nickid) + "`")
                embed = discord.Embed(title = "개발자에게 질문이 전송되었습니다!!", description = "답변은 Dm으로 옵니다. 답변을 받으시려면 다음의 내용대로 설정해 주시기 바랍니다! [사용자 설정->개인정보 보호 및 보안->서버 멤버가 보내는 개인메시지 허용하기 ON]", color = 0x0097ff)
                await message.channel.send(embed=embed)
                i = 0
                return

            if message.content.startswith(f + "버그"):
                bug = message.content[6:].split("|")
                await developer.send("**버그**\n버그내용 : " + str(bug[0]) + "ㅣ버그방법 : " + str(bug[1]) + "\n`Nick : " + str(nick) + "ㅣID : " + str(nickid) + "`")
                embed = discord.Embed(title = "개발자에게 버그내용이 전송되었습니다!!", description = "답변은 Dm으로 옵니다. 답변을 받으시려면 다음의 내용대로 설정해 주시기 바랍니다! [사용자 설정->개인정보 보호 및 보안->서버 멤버가 보내는 개인메시지 허용하기 ON]", color = 0x0097ff)
                await message.channel.send(embed=embed)
                i = 0
                return

            if message.content.startswith(f + "신고"):
                report = message.content[6:].split("|")
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
                    embed.add_field(name = "오류 - 구문", value = " \n//clear n, //청소 n 또는 n 에 정수가 들어가야 합니다", inline=True)
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
        f = "/."
    #도움
        if message.content.startswith(f + "도움") or message.content.startswith(f + "help"):
            embed=discord.Embed(title = "게임도움말", desctiption = "gamehelp", color = 0x0097ff)
            embed.add_field(name = "게임 명령어", value = "** **", inline = False)
            embed.add_field(name = "/.내눈송이", value = "현재 소지하고 있는 눈송이를 확인할 수 있어요!")
            embed.add_field(name = "/.눈송이줘", value = "1~5개의 눈송이를 랜덤으로 얻을 수 있어요!")
            embed.add_field(name = "/.출첵, /.ㅊㅊ", value = "출석체크를하고 눈송이를 받아보세요!")
            embed.add_field(name = "/.도박 n", value = "랜덤적인 확률로 도박에 성공하거나! 도박에 실패하거나!")
            embed.add_field(name = "/.복권 nnn-nnn", value = "복권1등을 노려보세요![복권 1개당 10눈송이]")
            embed.add_field(name = "/.순위", value = "Cloud 이용자의 순위를 확인할 수 있어요![구현중]")
            embed.add_field(name = "또다른 명령어", value = "** **", inline = False)
            embed.add_field(name = "//help, //도움, //도움말", value = "Cloud 의 명령어를 사용해보세요!")
            await message.channel.send(embed = embed)
            i = 0
            return

    #눈송이
        if message.content.startswith(f + "내눈송이") or message.content.startswith(f + "내 눈송이"):
            try:
                with open ("money.json") as json_file:
                    json_data = json.load(json_file)
                embed = discord.Embed(title = "" + nick + "님의 눈송이", description = "" + nick + "님의 눈송이는 **" + json_data[str(nickid)] + "** 개에요!", color = 0x0097ff)
                await message.channel.send(embed = embed)
                i = 0
                return
            except ValueError:
                embed = discord.Embed(color = 0xff0000)
                embed.add_field(name="오류 - 시스템", description="사용자의 눈송이를 확인중 오류가 발생하였습니다, 다시 시도해주세요.")
                embed.set_footer(text="해당오류가 계속될시 사진 캡쳐와 함께 Cloud 고객센터에 알려주시기 바랍니다.")
                await message.channel.send(embed=embed)
                i = 0
                return

    #눈송이 받기
        if message.content.startswith("/.눈송이줘") or message.content.startswith("/.눈송이 줘"):
            try:
                money = 0
            #단축
                r = randint(1,5)
                if r == 1:
                    money = 1
                elif r == 2:
                    money = 2
                elif r == 3:
                    money = 3
                elif r == 4:
                    money = 4
                else:
                    money = 5
            #코드
                with open ("money.json") as json_file:
                    json_data = json.load(json_file)
                mes = int(json_data[str(nickid)]) + money
                json_data[str(nickid)] = str(mes)
                embed = discord.Embed(title = "눈송이 받기", description = "" + nick + "님은 **" + str(money) + "** 개의 눈송이를 받으셨어요!", color = 0x0097ff)
                embed.set_footer(text = "" + nick + "님의 눈송이는 현재 " +  json_data[str(nickid)] + " 개 입니다.")
                await message.channel.send(embed = embed)
                with open("money.json", 'w', encoding='utf-8') as make_file:
                    json.dump(json_data, make_file, indent="\t")
                i = 0
                return
            except ValueError:
                embed = discord.Embed(color = 0xff0000)
                embed.add_field(name="오류 - 시스템", description="사용자에게 눈송이를 지급하는중 오류가 발생하였습니다, 다시 시도해주세요.")
                embed.set_footer(text="해당오류가 계속될시 사진 캡쳐와 함께 Cloud 고객센터에 알려주시기 바랍니다.")
                await message.channel.send(embed=embed)
                i = 0
                return

    #출석체크
        if message.content.startswith("/.출첵") or message.content.startswith("/.ㅊㅊ") or message.content.startswith("/.cc") or message.content.startswith("/.cnfcpr"):
            with open ("attendance_check.json") as json_file:
                json_data = json.load(json_file)
            uuu = json_data[str(nickid)]
            if uuu == str(1):
                embed = discord.Embed(title = "출석체크", description = "이미 출석체크를 하셨습니다", color = 0xff0000)
                await message.channel.send(embed = embed)
                i = 0
                return
            else:
                try:
                    r = randint(1,5)
                    if r == 1:
                        money = 1
                    elif r == 2:
                        money = 2
                    elif r == 3:
                        money = 3
                    elif r == 4:
                        money = 4
                    else:
                        money = 5
                    with open("money.json") as json_file:
                        json_data = json.load(json_file)
                    chch = json_data[str(nickid)]
                    json_data[str(nickid)] = str(int(chch) + money)
                    with open("money.json", 'w', encoding='utf-8') as make_file:
                        json.dump(json_data, make_file, indent="\t")
                    with open("attendance_check.json") as json_file:
                        json_data = json.load(json_file)
                    json_data[str(nickid)] = str(1)
                    with open("attendance_check.json", 'w', encoding='utf-8') as make_file:
                        json.dump(json_data, make_file, indent="\t")
                    with open("attendance_check_level.json") as json_file:
                        json_data = json.load(json_file)
                    chj = json_data[str(nickid)]
                    json_data[str(nickid)] = str(int(chj) + 1)
                    with open("attendance_check_level.json", 'w', encoding='utf-8') as make_file:
                        json.dump(json_data, make_file, indent="\t")
                    chjd = int(chj) + 1
                    embed = discord.Embed(title = "출석체크", description = "출석체크 완료!", color = 0x0097ff)
                    embed.add_field(name = "** **" + nick + "님은현재" + str(chjd) + ".LV 입니다.", value = "눈송이" + str(money) + "개가 지급되었습니다.")
                    await message.channel.send(embed = embed)
                    i = 0
                    return
                except ValueError:
                    embed = discord.Embed(color = 0xff0000)
                    embed.add_field(name="오류 - 시스템", value="출석체크를 하던중 오류가 발생하였습니다, 다시시도해주세요.")
                    embed.set_footer(text="해당오류가 계속될시 사진 캡쳐와 함께 Cloud 고객센터에 알려주시기 바랍니다.")
                    await message.channel.send(embed=embed)
                    i = 0
                    return

    #도박
        if message.content.startswith("/.도박"):
            with open ("money.json") as json_file:
                json_data = json.load(json_file)
            try:
                set = mchat[5:]
                mmmoo = int(json_data[str(nickid)])
                if set == 0:
                    embed = discord.Embed(color = 0xff0000)
                    embed.add_field(name = "오류 - 구문", value = "n 에는 0보다 큰 정수가 들어가야 합니다.")
                    await message.channel.send(embed = embed)
                    i = 0
                    return
                else:
                    pass
                if int(set) <= mmmoo:
                    pass
                else:
                    embed = discord.Embed(color = 0xff0000)
                    embed.add_field(name = "오류 - 구문", value = "적은 눈송이가 소지한 눈송이와 같거나 더 낮게 적어주세요.")
                    await message.channel.send(embed = embed)
                    i = 0
                    return
                try:
                    r = randint(0,100)
                    a = randint(0,5)
                    if  r > 50:
                        if a < 2:
                            give = int(set) * 1
                            json_data[str(nickid)] = str(int(give))
                            with open("money.json", 'w', encoding='utf-8') as make_file:
                                json.dump(json_data, make_file, indent="\t")
                            embed = discord.Embed(title = "실패..", description = "다행이도 눈송이는 않녹았네요..", color = 0xff0000)
                            await message.channel.send(embed = embed)
                            i = 0
                            return
                        elif a < 5:
                            give = int(set) * 2
                            json_data[str(nickid)] = str(int(give))
                            with open("money.json", 'w', encoding='utf-8') as make_file:
                                json.dump(json_data, make_file, indent="\t")
                            embed = discord.Embed(title = "성공!", description = "걸었던 눈송이를 2배로 돌려드립니다!", color = 0x0097ff)
                            await message.channel.send(embed = embed)
                            i = 0
                            return
                        elif a == 5:
                            give = int(set) * 3
                            json_data[str(nickid)] = str(int(give))
                            with open("money.json", 'w', encoding='utf-8') as make_file:
                                json.dump(json_data, make_file, indent="\t")
                            embed = discord.Embed(title = "잭팟!!!", description = "걸었던 눈송이를 3배로 돌려드립니다!!!", color = 0xebeb00)
                            await message.channel.send(embed = embed)
                            i = 0
                            return
                    else:
                        fakeset = int(mmmoo) - int(set)
                        json_data[str(nickid)] = str(fakeset)
                        with open("money.json", 'w', encoding='utf-8') as make_file:
                            json.dump(json_data, make_file, indent="\t")
                        embed = discord.Embed(title = "실패..", description = "걸었던 눈송이는 녹아내렸습니다..", color = 0xff0000)
                        await message.channel.send(embed = embed)
                        i = 0
                        return
                except ValueError:
                    embed = discord.Embed(color = 0xff0000)
                embed.add_field(name = "오류 - 구문", value = "n 에는 정수가 들어가야 합니다.")
                await message.channel.send(embed = embed)
                i = 0
                return
            except ValueError:
                embed = discord.Embed(color = 0xff0000)
                embed.add_field(name = "오류 - 구문", value = "n 에는 0보다 큰 정수가 들어가야 합니다.")
                await message.channel.send(embed = embed)
                i = 0
                return

    #복권
        if message.content.startswith("/.복권"):
            try:
                with open("money.json") as json_file:
                    json_data = json.load(json_file)
                money = json_data[str(nickid)]
                if 10 <= int(money):
                    mooneney = int(money) - 10
                    json_data[str(nickid)] = str(mooneney)
                    with open("money.json", 'w', encoding='utf-8') as make_file:
                        json.dump(json_data, make_file, indent="\t")
                    looeo = mchat[5:].split("-")
                    mooeo = str(looeo[0]) + str(looeo[1])
                    with open("lottery.json") as json_file:
                        json_data = json.load(json_file)
                    json_data[str(nickid)] = str(mooeo)
                    with open("lottery.json", 'w', encoding='utf-8') as make_file:
                        json.dump(json_data, make_file, indent="\t")
                    embed = discord.Embed(title = "복권구매 완료!", description = "복권 당첨은 매월 1일에 만날 수 있어요!", color = 0x0097ff)
                    await message.channel.send(embed = embed)
                    i = 0
                else:
                    embed = discord.Embed(color = 0xff0000)
                    embed.add_field(name = "눈송이 부족", value = "소지한 눈송이가 10개보다 적습니다.")
                    await message.channel.send(embed = embed)
                    i = 0
                    return
            except ValueError:
                embed = discord.Embed(color = 0xff0000)
                embed.add_field(name = "오류 - 구문", value = "n 에는 0보다 크고, 10보다 작은 정수가 들어가야 합니다.")
                await message.channel.send(embed = embed)
                i = 0
                return
                
    #랭킹


    #명령어 오류
        if i == 1:
            embed = discord.Embed(color = 0xff0000)
            embed.add_field(name="오류 - 구문", value=mchat + "은 존재하지 않는 명령어입니다 /.help 또는 /.도움, /.도움말 을 사용하여 명령어 목록을 참조하시기 바랍니다")
            await message.channel.send(embed=embed)
            return

#대화
    if message.content.startswith("구름아"):  
        f = "구름아 "
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
            await message.channel.send("아직 놀이기능이 없어요.. 이를 어쩌죠?")
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

#token
client.run("NzUyNDEwOTEyMDkwMDk1NjE2.X1XPRA.7rqHXCO3bwzKcdntNF86T_pbaiQ")