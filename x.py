# -*- coding: utf-8 -*-
from Linephu.linepy import *
from datetime import datetime
from time import sleep
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,atexit
from time import strftime
#==============================================================================#
botStart = time.time()

cl = LINE("","")
cl.log("Auth Token : " + str(cl.authToken))
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))

#ki = LINE()
#ki.log("Auth Token : " + str(ki.authToken))

#k1 = LINE()
#k1.log("Auth Token : " + str(k1.authToken))

#k2 = LINE()
#k2.log("Auth Token : " + str(k2.authToken))

clMID = cl.profile.mid
#AMID = ki.profile.mid
#BMID = k1.profile.mid
#CMID = k2.profile.mid

#KAC = [cl,ki,k1,k2]
#Bots = [clMID,AMID,BMID,CMID]

clProfile = cl.getProfile()
#kiProfile = ki.getProfile()
#k1Profile = k1.getProfile()
#k2Profile = k2.getProfile()
lineSettings = cl.getSettings()
#kiSettings = ki.getSettings()
#k1Settings = k1.getSettings()
#k2Settings = k2.getSettings()

oepoll = OEPoll(cl)
#oepoll1 = OEPoll(ki)
#oepoll2 = OEPoll(k1)
#oepoll3 = OEPoll(k2)
#==============================================================================#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
banOpen = codecs.open("ban.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)
ban = json.load(banOpen)

msg_dict = {}
bl = [""]

#==============================================================================#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = ban
        f = codecs.open('ban.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """▹Help 查看指令◃

▶ 狀態 ◀
▹ Restart 重新啟動◃
▹ Save 儲存設定◃
▹ Runtime 運作時間◃
▹ Sp 速度◃
▹ Set 設定◃
▹ About關於本帳◃
▶ 設置 ◀
▹ AutoAdd On/Off 自動加入◃
▹ AutoJoin On/Off 自動進群◃
▹ AutoLeave On/Off 離開副本◃
▹ AutoRead On/Off 自動已讀◃
▹ Share On/Off 公開/私人◃
▹ ReRead On/Off 查詢收回◃
▹ Getmid On/Off 取得mid◃
▹ Detect On/Off 標註偵測◃
▹ Timeline On/Off 文章網址預覽◃
▶ 我的狀態 ◀
▹ Me 我的連結◃
▹ MyMid 我的mid◃
▹ MyName 我的名字◃
▹ MyBio 個簽◃
▹ MyPicture 我的頭貼◃
▹ MyCover 我的封面◃
▹ Contact @ 標註取得連結◃
▹ Mid @ 標註查mid◃
▹ Name @ 查看名字◃
▶ 黑名單 ◀
▹ Ban @ 加入黑單◃
▹ Unban @ 取消黑單◃
▹ Ban: MID 加入黑單◃
▹ Unban: MID 取消黑單◃
▹ Banlist 查看黑單◃
▹ CleanBan 清空黑單◃
▹ Nkban 踢除黑單◃
▶ 群組設置 ◀
▹ GroupCreator創群者◃
▹ GroupId 群組ID◃
▹ GroupName 群組名稱◃
▹ GroupPicture 群組圖片◃
▹ GroupLink 群組網址◃
▹ Link「On/Off」網址開啟/關閉◃
▹ GroupList所有群組列表◃
▹ GroupMemberList 成員名單◃
▹ GroupInfo 群組資料◃
▹ Gn (文字) 更改群名◃
▹ Nk @ 單、多踢◃
▹ Zk 踢出0字元◃
▹ 秘密指令 翻群◃
▹ Cl 取消所有邀請◃
▹ Ri @ 來回機票◃
▶ 特別 ◀
▹ Tagall 標註全體◃
▹ Zc 發送0字元友資◃
▹ Setread 已讀點設置◃
▹ Cancelread 取消偵測◃
▹ Checkread 已讀偵測◃
▹ Gbc: 群組廣播◃
▹ Fbc: 好友廣播◃
▹ Text 打字傳文字圖 ◃(限制15黑底白字)
▹ 日期 顯示年月日時◃
▶ 權限 ◀
▹ Adminadd @ 新增權限◃
▹ Admindel @ 刪除權限◃
▹ Adminlist 查看權限表◃
▶ Invite ◀
▹ Botsadd @ 加入自動邀請◃
▹ Botsdel @ 取消自動邀請◃
▹ Botslist 自動邀請表◃
▹ Join 自動邀請◃ """
    return helpMessage
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']

def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))

admin =['u45c1325c7db7d1685360dcc008aebea9','u62bb8efa5e3c81bc4a1b381dbe521987',"u1607998a55d0f8b002c81c8989c127ea","u0959a5e5a9f0c9d1b159bf6b3f7a0c0d","ua2d7992361ba087ff41d752880ce9b4e","u1b4efb3e7d4d534e7876e66e3fe7473a","u0fd57663c0e31db13dd2e67c3b35d354","ub7fb57dce0c0a711731d9253e51f423a","ub0ee919a78a61d7ef01c918a21cbd607","u19d1dd35b38c9992f5a7f5d232f3f651","u1a14273ba4d7018ec26faf95170016be","u57d28bd09220d08c2aa212d567cbe6c1","u01f63b77f34fc15d6ce7d378e50ab223","u57d28114668175f36844be3960755b37","u77f067a5a66bed55b99afd73bc5b1f88","u0ae76d135672bd9a5cf45b11d9b05fc7","u81cee47b13e8bc02702ae65f41e804f0","ub50e202ef2354ca67782327e53e6686a","uf0e4f46cbd5e986010e63b96a13d2e38","u387316a2564f5fbcbf7f31628d4e7929","u8f43bdb97e35e3f3931d8a37c5324bbd","u1c8154e29befa015ee9af6bd303e530e","u6614e3118c50b0398257e6066ad5b26a","u1b8a1af44216b87b9a394290f1d1ac54","udc76a02edad2cc6418e2738b2f8fc74b","u30967a29dd7fed99e2256c0b800206cf",clMID]
owners = ["ub7fb57dce0c0a711731d9253e51f423a",'u62bb8efa5e3c81bc4a1b381dbe521987',"u0ae76d135672bd9a5cf45b11d9b05fc7"]
#if clMID not in owners:
#    python = sys.executable
#    os.execl(python, python, *sys.argv)
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "歡迎加入好友>0<".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            if clMID in op.param3:
                group = cl.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25 or op.type == 26:
            K0 = admin
            msg = op.message
            if settings["share"] == True:
                K0 = msg._from
            else:
                K0 = admin
#        if op.type == 25 :
#            if msg.toType ==2:
#                g = cl.getGroup(op.message.to)
#                print ("sended:".format(str(g.name)) + str(msg.text))
#            else:
#                print ("sended:" + str(msg.text))
#        if op.type == 26:
#            msg =op.message
#            pop = cl.getContact(msg._from)
#            print ("replay:"+pop.displayName + ":" + str(msg.text))
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
            if sender in K0 or sender in owners:
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to,"u45c1325c7db7d1685360dcc008aebea9")
                elif text.lower() == 'bye1':
                    cl.sendMessage(to,"再見了TwT")
                    cl.leaveGroup(msg.to)
#==============================================================================#
                elif text.lower() == 'sp':
                    start = time.time()
                    cl.sendMessage(to, "七辣洩洪中...")
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'洩洪速度\n'+format(str(elapsed_time)) + " Second...")
                elif text.lower() == 'save':
                    backupData()
                    cl.sendMessage(to,"儲存設定成功!")
                elif text.lower() == 'restart':
                    cl.sendMessage(to, "重新啟動中...")
                    cl.sendMessage(to, "重啟成功>w<")
                    restartBot()
                    cl.sendMessage(to, "已完成")
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "系統已運作 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner ="u45c1325c7db7d1685360dcc008aebea9"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "►[ 關於使用者 ]◄"
                        ret_ += "\n▸ 使用者名稱 : {}".format(contact.displayName)
                        ret_ += "\n▸ 群組數 : {}".format(str(len(grouplist)))
                        ret_ += "\n▸ 好友數 : {}".format(str(len(contactlist)))
                        ret_ += "\n▸ 已封鎖 : {}".format(str(len(blockedlist)))
                        ret_ += "\n►[ 關於本bot ]◄"
                        ret_ += "\n▸ 版本 : 最新"
                        ret_ += "\n▸ 製作者 : {}".format(creator.displayName)
                        ret_ += "\n►[ 感謝您的使用 ]◄"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "►[ 狀態 ]◄"
                        if settings["autoAdd"] == True: ret_ += "\n▸ Auto Add ✅"
                        else: ret_ += "\n▸ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n▸ Auto Join ✅"
                        else: ret_ += "\n▸ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n▸ Auto Leave ✅"
                        else: ret_ += "\n▸ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n▸ Auto Read ✅"
                        else: ret_ += "\n▸ Auto Read ❌"
                        if settings["detectMention"] ==True: ret_+="\n▸ DetectMention ✅"
                        else: ret_ += "\n▸ DetectMention ❌"
                        if settings["reread"] ==True: ret_+="\n▸ Reread ✅"
                        else: ret_ += "\n▸ Reread ❌"
                        if settings["share"] ==True: ret_+="\n▸ Share ✅"
                        else: ret_ += "\n▸ Share ❌"
                        ret_ += "\n►[ Finish ]◄"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入開啟")
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入關閉")
                elif text.lower() == 'autojoin on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動進群開啟")
                elif text.lower() == 'autojoin off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動進群關閉")
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "離開副本開啟")
                elif text.lower() == 'autojoin off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "離開副本關閉")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀開啟")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀關閉")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to,"查看收回開啟")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to,"查看收回關閉")
                elif text.lower() == 'share on':
                    settings["share"] = True
                    cl.sendMessage(to, "已開啟分享")
                elif text.lower() == 'share off':
                    settings["share"] = False
                    cl.sendMessage(to, "已關閉分享")
                elif text.lower() == 'detect on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "已開啟標註偵測")
                elif text.lower() == 'detect off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "已關閉標註偵測")
                elif text.lower() == 'qrprotect on':
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "網址保護開啟")
                elif text.lower() == 'getmid on':
                    settings["getmid"] = True
                    cl.sendMessage(to, "mid獲取開啟")
                elif text.lower() == 'getmid off':
                    settings["getmid"] = False
                    cl.sendMessage(to, "mid獲取關閉")
                elif text.lower() == 'timeline on':
                    settings["timeline"] = True
                    cl.sendMessage(to, "文章預覽開啟")
                elif text.lower() == 'timeline off':
                    settings["timeline"] = False
                    cl.sendMessage(to, "文章預覽關閉")
#==============================================================================#
                elif text.startswith("Text "):
                    sep = text.split(" ")
                    textnya = text.replace(sep[0] + " ","")	
                    urlnya = "http://chart.apis.google.com/chart?chs=1000x70&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"		
                    cl.sendImageWithURL(msg.to, urlnya)
                elif msg.text.lower().startswith("adminadd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.append(str(inkey))
                    cl.sendMessage(to, "恭喜您已獲得權限>3<")
                elif msg.text.lower().startswith("admindel "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.remove(str(inkey))
                    cl.sendMessage(to, "抱歉><您的權限已被移除")
                elif text.lower() == 'adminlist':
                    if admin == []:
                        cl.sendMessage(to,"無擁有權限者!")
                    else:
                        mc = "►[ Admin List ]◄"
                        for mi_d in admin:
                            mc += "\n▸ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n►[ Finish ]◄")
                elif msg.text.lower().startswith("invite "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    G = cl.getGroup
                    cl.inviteIntoGroup(to,targets)
                elif ("Say " in msg.text):
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        cl.sendMessage(to,x[1])
                elif msg.text.lower().startswith("tag "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    x = text.split(' ',2)
                    c = int(x[2])
                    for c in range(c):
                        sendMessageWithMention(to, inkey)
                elif msg.text.lower().startswith("botsadd "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].append(str(inkey))
                    cl.sendMessage(to, "已加入分機！")
                elif msg.text.lower().startswith("botsdel "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    ban["bots"].remove(str(inkey))
                    cl.sendMessage(to, "已取消分機！")
                elif text.lower() == 'botslist':
                    if ban["bots"] == []:
                        cl.sendMessage(to,"無分機!")
                    else:
                        mc = "►[ Inviter List ]◄"
                        for mi_d in ban["bots"]:
                            mc += "\n▸ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(to,mc + "\n►[ Finish ]◄")
                elif text.lower() == 'join':
                    if msg.toType == 2:
                        G = cl.getGroup
                        cl.inviteIntoGroup(to,ban["bots"])
                elif msg.text.lower().startswith("ii "):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    cl.createGroup("fuck",[inkey])
                    cl.leaveGroup(op.param1)
                elif text.lower() == '日期':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = timeNow.strftime('%Y') + "/" + bln + "/" + timeNow.strftime('%d') + (" 【") + hasil + ("】 ") + "\n時間 : " + timeNow.strftime('%H:%M:%S')
                    cl.sendMessage(msg.to, readTime)
#==============================================================================#
                elif text.lower() == 'me':
                    if msg.toType == 2 or msg.toType == 1:
                        sendMessageWithMention(to, sender)
                        cl.sendContact(to, sender)
                    else:
                        cl.sendContact(to,sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[Name]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = cl.getContact(sender)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 名字 ]\n" + contact.displayName)
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 個簽 ]\n" + contact.statusMessage)
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == 'groupid':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = cl.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[群組名稱 : ]\n" + gid.name)
                elif text.lower() == 'grouplink':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "Grouplink未開啟 {}openlink".format(str(settings["keyCommand"])))
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "開啟成功")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "關閉成功")
                elif text.lower() == 'groupinfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "不明"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "無"
                    else:
                        gQr = "開啟"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "►[ Group Info ]◄"
                    ret_ += "\n▸ 群組名稱 : {}".format(str(group.name))
                    ret_ += "\n▸ 群組 Id : {}".format(group.id)
                    ret_ += "\n▸ 創建者 : {}".format(str(gCreator))
                    ret_ += "\n▸ 群組人數 : {}".format(str(len(group.members)))
                    ret_ += "\n▸ 邀請中 : {}".format(gPending)
                    ret_ += "\n▸ 網址狀態 : {}".format(gQr)
                    ret_ += "\n▸ 群組網址 : {}".format(gTicket)
                    ret_ += "\n►[ Finish ]◄"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "►[ 成員名單 ]◄"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n▸ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n►[ 全部成員共 {} 人]◄".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = cl.groups
                        ret_ = "►[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n▸ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n►[ Total {} Groups ]◄".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("nk "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.sendMessage(to,"恭喜你獲得日本東京單程機票~")
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendMessage(to,"Error")
                
                elif "Zk" in msg.text:
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass

                elif msg.text.lower().startswith("ri "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.sendMessage(to,"恭喜你獲得日本東京來回機票~")
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.inviteIntoGroup(to,[target])
                        except:
                            cl.sendMessage(to,"Error")
                elif text.lower() == '堅強翻群030':
                    if msg.toType == 2:
                        print ("[ 19 ] KICK ALL MEMBER")
                        _name = msg.text.replace("堅強翻群030","")
                        gs = cl.getGroup(msg.to)
                        cl.sendMessage(msg.to,"低速半垢正在幹大事www\n"+"https://line.me/ti/p/S6ogSalsg4")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendMessage(msg.to,"Not Found")
                        else:
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendMessage(msg.to,"")
                elif ("Gn " in msg.text):
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"It can't be used besides the group.")
                elif text.lower() == 'cl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendMessage(msg.to,"☆月滅骑士团...垃圾の取消☆")
                elif "Inv:" in msg.text:
                    midd = msg.text.replace("Inv:","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif msg.text in ["Fl"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"「 朋友列表 」\n"+ap+"人數 : "+str(len(anl)))
#==============================================================================#
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//20
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*20 : (a+1)*20]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            sendMessageWithMention(to,target)
                elif text.lower() == 'zm':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for mi_d in targets:
                           cl.sendContect(to,mi_d)
                elif text.lower() == 'setread':
                    cl.sendMessage(msg.to, "已讀點設置成功")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif text.lower() == "cancelread":
                    cl.sendMessage(to, "已讀點已刪除")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                        del wait2['setTime'][msg.to]
                    except:
                        pass
                elif msg.text in ["checkread","Checkread"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "[已讀順序]%s\n\n[已讀的人]:\n%s\n查詢時間:[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入setread")

#==============================================================================#
                elif msg.text.lower().startswith("ban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            ban["blacklist"][target] = True
                            cl.sendMessage(msg.to,"已加入黑單!")
                            break
                        except:
                            cl.sendMessage(msg.to,"添加失敗 !")
                            break
                elif "Ban:" in msg.text:
                    mmtext = text.replace("Ban:","")
                    try:
                        ban["blacklist"][mmtext] = True
                        cl.sendMessage(msg.to,"已加入黑單!")
                    except:
                        cl.sendMessage(msg.to,"添加失敗 !")
                elif msg.text.lower().startswith("unban "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del ban["blacklist"][target]
                            cl.sendMessage(msg.to,"刪除成功 !")
                            break
                        except:
                            cl.sendMessage(msg.to,"刪除失敗 !")
                            break
                elif "Unban:" in msg.text:
                    mmtext = text.replace("Unban:","")
                    try:
                        del ban["blacklist"][mmtext]
                        cl.sendMessage(msg.to,"刪除成功!")
                    except:
                        cl.sendMessage(msg.to,"刪除失敗 !")
                elif text.lower() == 'banlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "►[ Black List ]◄"
                        for mi_d in ban["blacklist"]:
                            mc += "\n▸ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n►[ Finish ]◄")
                elif text.lower() == 'nkban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                    for tag in ban["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendMessage(msg.to,"此群組無黑名單成員>w<")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendMessage(msg.to,"黑名單都滾www")
                elif text.lower() == 'cleanban':
                    for mi_d in ban["blacklist"]:
                        ban["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'banmidlist':
                    if ban["blacklist"] == {}:
                        cl.sendMessage(msg.to,"無黑單成員!")
                    else:
                        mc = "◤ Black List ◥"
                        for mi_d in ban["blacklist"]:
                            mc += "\n▸ "+mi_d
                        cl.sendMessage(to,mc + "\n◣ ◢")


#==============================================================================#
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif "Copy " in msg.text:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            X = contact.displayName
                            profile = cl.getProfile()
                            profile.displayName = X
                            cl.updateProfile(profile)
                            cl.sendMessage(to, "正在處理中，請稍後...")
                            Y = contact.statusMessage
                            lol = cl.getProfile()
                            lol.statusMessage = Y
                            cl.updateProfile(lol)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            P = contact.pictureStatus
                            cl.updateProfilePicture(P)
                        except Exception as e:
                            cl.sendMessage(to, "拷貝完成!")
            if text.lower() == 'cc9487':
                if sender in ['u45c1325c7db7d1685360dcc008aebea9']:
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
                else:
                    pass
#==============================================================================#
            if msg.contentType == 13:
                if settings["getmid"] == True:
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"[mid]:\n" + msg.contentMetadata["mid"])
                    else:
                        cl.sendMessage(msg.to,"[mid]:\n" + msg.contentMetadata["mid"])
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "文章網址：\n" + msg.contentMetadata["postEndUrl"]
                  #  detail = cl.downloadFileURL(to,msg,msg.contentMetadata["postEndUrl"])
                    cl.sendMessage(msg.to,msg.text)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in ban["mimic"]["target"] and ban["mimic"]["status"] == True and ban["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    sendMessageWithMention(to, contact.mid)
                                    cl.sendMessage(to, "大哥/大姊 對不起>w<沒ㄐㄐ是我的錯><別揍我www")
                                break
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                    elif msg.contentType == 7:
                        stk_id = msg.contentMetadata['STKID']
                        msg_dict[msg.id] = {"text":"貼圖id:"+str(stk_id),"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)

#==============================================================================#
        if op.type == 65:
            print ("[ 65 ] REREAD")
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            timeNow = datetime.now()
                            timE = datetime.strftime(timeNow,"%y-%m-%d %H:%M:%S")
                            try:
                                strt = int(3)
                                akh = int(3)
                                akh = akh + 8
                                aa = """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(msg_dict[msg_id]["from"])+"},"""
                                aa = (aa[:int(len(aa)-1)])
                                cl.sendMessage(at, "收回訊息者 @wanping ", contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
                            except Exception as e:
                                print(str(e))
                            cl.sendMessage(at,"[收回訊息者]\n%s\n[訊息內容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            cl.sendMessage(at,"發送時間: \n"+strftime("%y-%m-%d %H:%M:%S \n")+"收回時間: \n"+timE)
                            
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print (e)
#==============================================================================#

        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[※]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[※]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
