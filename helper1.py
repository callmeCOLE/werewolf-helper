from pyrogram import Client,filters
import time
from pyrogram.types import MessageEntity,ChatPermissions
from pyrogram.raw import functions
from pyrogram.raw.types import ChannelAdminLogEventsFilter
import random
from pyrogram.types import Message, User
from datetime import datetime
import datetime
import json
import json
import os
import re
from requests import post
from pyrogram.handlers import MessageHandler
import sqlite3 as db
con=db.connect('data.db')
c=con.cursor()
c.execute('CREATE TABLE IF NOT EXISTS points (user_id INT PRIMARY KEY, point  INT)')
con.commit()
ems = ['đŚ', 'đŻ', 'đŚ', 'đŚ', 'đ', 'đş', 'đŚ', 'đ', 'đł', 'đŹ', 'đź', 'đŚ', 'đ', 'đ˛', 'đ', 'đ', 'đˇ', 'đš', 'đş', 'đ¸', 'đź', 'đ', 'đ', 'đŞ', 'đŤ', 'â­ď¸', 'â¨', 'âĄď¸', 'đĽ', 'đ', 'âď¸', 'âď¸', 'đ', 'đ', 'đ', 'đ', 'đ', 'đ§', 'đ°', 'đ­', 'đŹ', 'đŤ', 'đż', 'đŠ', 'đŞ', 'đĽ', 'đ¸', 'đš', 'đ§', 'đž', 'â˝ď¸', 'đ', 'đ', 'âžď¸', 'đĽ', 'đž', 'đ', 'đ', 'đĽ', 'đ¸', 'đş', 'đˇ', 'đ', 'đ', 'âď¸', 'đ', 'đ¸', 'đ°', 'đź', 'đĄ', 'đŠ', 'đą', 'đť', 'đĽ', 'đ°', 'đ§¨', 'đŁ', 'đŞ', 'đ', 'âąď¸', 'đŽ', 'đŠ¸', 'đŚ ', 'đ', 'đ§¸', 'đ', 'đ', 'đŻ', 'â¤ď¸', 'đ§Ą', 'đ', 'đ', 'đ', 'đ', 'đ¤', 'đ¤', 'đ¤', 'âŁď¸', 'đ', 'đ', 'đ', 'âď¸', 'đą', 'đŁ', 'âĽď¸', 'đ', 'đĽ°', 'đĽł', 'đ¤Š', 'đ¤Ş', 'đž', 'đť', 'đ', 'đ', 'đ', 'đŠ']
next_dic={}
afki_list={}
ban_list=[]
wwbots=[854021534,175844556]
apps = {}
send_id=0
delay_each_atk = 7
delay_time = 0
id=0
Banner = {}
attacker = False
name = ''
Id = ''
Hash = ''
phhash = ''
phnum = ''
winner=None
admin_tag=0
biadaabi=0
afki_lock=9999
chl="""ŮŘ§Ř§Ř§Ř§Ů Ř§ŰŮŘŹŘ§ŘąŮđđ
ŮŘąÚŠŰ Ř˛ŮŘŻŘŞŘą ŘąŰŮž Ř¨Ř˛ŮŮ ŰÚŠ Ř§ŮŘŞŰŘ§Ř˛ Ř¨Ů ŘŞŮŘąŮŮŮŮŘŞŘ´ Ř§ŘśŘ§ŮŮ ŮŰŘ´Ů âĄď¸âď¸



Ř¨Ř¨ŰŮŰŮ ÚŠŰ Ř¨ŘąŮŘŻŮ ŮŰŘ´Ůđđ"""
starttime=0
fakebazi=0
token='1121419247:AAHCd4sTctw3p8RiofS3Rhp4aPkuvREtlJm'
def next(id,text):
    next_dic.update({id:text})
def admin_only(func):
    def check(Client, message):
        if message.from_user.id in admin_all:
            if message.from_user.id not in ban_list:
                func(Client, message)
            else:
                message.reply("**You has been banned from bot**")
        else:
            message.reply("**You are not admin**")
    return check
def admin_only_asli(func):
    def check(Client, message):
        if message.from_user.id in list_admin :
            if message.from_user.id not in ban_list:
                func(Client, message)
            else:
                message.reply("**You has been banned from bot**")

        else:
            message.reply("**You are not main admin**")
    return check



def ban_from_bot(func):
    def check(Client, message):
        if message.from_user.id not in ban_list:
            func(Client, message)
        else:
            message.reply("**You has been banned from bot**")
    return check
left_text=''
join_dick={}
ray_ki=''

apps={}
multi_admin_gp=0

gap=0
mio=0
stoprep=0
print('amiralirj \n \n amiralirj bmolaaaaaa -------@AMIRALIRJPV')
api_id =2586462
api_hash = '68542129131999986899b84a10a6170c'
list3=[1410445908]
rip_text='.'
bot = Client('amirairj-helper', api_id, api_hash,workers=7)
tag_auto=0
lefti_auto=0
list_lefti={}
suplock=0
admin_all=[1410445908]
tag_auto_time=0
mentiontag=True
is_tagging = {}
shekar=0
man=[1410445908]
auto_tag_time=0
mention = lambda user_id, text: f'<a href=tg://user?id={user_id}>{text}</a>'
list_admin=[1410445908,1653256635]
welcome_groups = set()
welcome_text = '**ŘŻŘłŘŞŮ ÚŻŮ ŮŘ­ŮŘŻŰ Ř¨Ů ŘŹŮŘš ŮŘ§ ŘŽŮŘ´ Ř§ŮŘŻŰ**'
welcome_sleep = 0
group_admin_id=0
list1=[1410445908,854021534,1289410047,1181120160,1653256635,175844556]
mtx=""
speed=0.01
mtx_admin=''
#####################################################

with bot:
    bot_username = "@" + bot.get_me().username
    try:
        bot.join_chat('amiraliheperrj')
        bot.send_message('@AMIRALIRJPV',text='bot has runned in this acc ')
    except:
        pass
        bot_id=bot.get_me().id
############################################################
def add_istagging(chat_id):
    global is_tagging
    if chat_id not in is_tagging:
        is_tagging.update({chat_id: False})



@bot.on_message(filters.regex(r'#players: 0') & filters.group & filters.user([854021534,175844556]))
def tagger(client, message):
    global tag_auto_time
    global starttime
    rag=''
    starttime = int(time.time())
    bot.send_message(group_admin_id, text='''**ŘŞŮŘŹŮŮ ŘŞŮŘŹŮŮ đˇđ¤Ť

Ř§ŘŻŮŰŮđ§đťâđŮŮ ŮŘ§Ű ŘšŘ˛ŰŮŘ˛

ŘŹŮŰŮŮ ŘŞŘ§ŰŮâ°ŮŮ Ř´ŮŘąŮŘš Ř´ŮŘŻŮ

ŮŘˇŮŮŘ§ Ř¨Ů ÚŻŮž ŮŘąŘ§ŘŹŘšŮŮ ÚŠŮŰŮŘŻ Ř¨Ř§ ŘŞŘ´ŮÚŠŘąđ¸**''')
    if tag_auto_time==1:
        s=0
        global is_tagging
        chat_id = message.chat.id
        add_istagging(chat_id)
        bot.send_message(chat_id,'**tag started :)**')
        if not is_tagging[chat_id]:
            is_tagging[chat_id] = True
            chat_members_admin = bot.iter_chat_members(group_admin_id)
            if admin_tag==1:
                for usr2 in chat_members_admin:
                    try:
                        bot.send_message(group_admin_id, '{} {}'.format(mtx_admin,usr2.user.mention()))
                        time.sleep(0.5)
                    except:
                        pass
            for usr in bot.iter_chat_members(chat_id=chat_id,limit=600):
                if usr['user']['username']:
                    if is_tagging[chat_id]:
                        time.sleep(speed)
                        bot.send_chat_action(chat_id, 'typing')
  
                        #bot.send_message(chat_id, '**{}** {}'.format(mtx,usr.user.mention()))
                        if not usr.user.is_bot:
                            rag+= f"**|{random.choice(ems)}| {usr.user.mention()} {mtx}** \n"
                            s+=1
                            if s==5:
                                bot.send_message(chat_id,rag)
                                rag=''
                                s=0


                    else:
                        return
            is_tagging[chat_id] = False
         
######################################################tag asli #############################################################################################
###########################################################################################################################################################


@bot.on_message(filters.command(['starttag', f'starttag{bot_username}']) & filters.group)
def tagge2r(client, message):
    global is_tagging
    rag=''
    s=0
    chat_id = message.chat.id
    add_istagging(chat_id)
    bot.send_message(chat_id,'**tag started :)**')
    if not is_tagging[chat_id]:
        is_tagging[chat_id] = True
        chat_members = client.iter_chat_members(chat_id=chat_id)
        for usr in chat_members:
            if usr['user']['username']:
                if is_tagging[chat_id]:
                    bot.send_chat_action(chat_id, 'typing')
                    if not usr.user.is_bot:
                        rag+= f"**|{random.choice(ems)}| {usr.user.mention()} {mtx}** \n "
                        s+=1
                        if s==5:
                            bot.send_message(chat_id,rag)
                            rag=''
                            s=0
                            time.sleep(3)

                

                else:
                    return
        is_tagging[chat_id] = False



@bot.on_message(filters.command(['stoptag', f'stoptag{bot_username}']) & filters.group)
def stopkirkhhhhh(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False
        message.reply_text('tag is stoped')
    else:
        message.reply_text('taggggggg nmiiiiiknammmmmm mannnnnnnn')
    if tag_auto==1:
            
        try:
            tag_msgs = [msg for msg in bot.iter_history(gap,limit=1000) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention"):
                        if tagmsg.from_user.id not in list1:
                            tagmsg.delete()
                            time.sleep(0.1)
                time.sleep(0.05)
            message.reply_text(f"**ŮžŘ§ÚŠŘłŘ§Ř˛Ű ŘŞÚŻ ŮŘ§ Ř§ŮŘŹŘ§Ů Ř´ŘŻ**")
        except Exception as e:
            message.reply_text(f"**ă ŘŽŘˇŘ§âď¸Ř¨Ů ŮžŘ´ŘŞŰŘ¨Ř§ŮŰ ŮžŰŘ§Ů ŘŻŮŰŘŻ @AMIRALIRJPV ă\n {e}**")

###########################################################################################################################################################
###########################################################################################################################################################


@bot.on_message(filters.command(['settext', f'settext{bot_username}']) & filters.group)
@admin_only
def sto1p(client, message):
    global mtx
    if message.reply_to_message:
        mtx = message.reply_to_message.text
        message.reply_text("**text setted**")
    else:
        message.reply_text('**ă ŘŽŘˇŘ§âď¸ŮŘˇŮŘ§ Ř§ŰŮ ŘŻŘłŘŞŮŘą ŘąŘ§ Ř¨Řą ŘąŮŰ ŮžŰŘ§ŮŰ ŘąŰŮžŮŘ§Ű ÚŠŮŰŘŻ ! ă**')
 

@bot.on_message(filters.command(['replaytag', f'replaytag{bot_username}']) & filters.group)
@admin_only
def s1234top(client, message):
    mio=0
    rep_text=message.command[1]
    global speed
    global stoprep
    stoprep=1
    chat_id = message.chat.id
    for mag in bot.iter_history(chat_id,limit=500,reverse =True):
        mag.reply_text(rep_text)
        time.sleep(2)
        mio+=1
        if  stoprep==0:
            break


@bot.on_message(filters.command(['stopreplay', f'stopreplay{bot_username}']) & filters.group)
@admin_only
def stkfop(client, message):
    global stoprep
    stoprep=0
    message.reply_text("**stopped**")
#######################################help##############################
@bot.on_message(filters.command(['helpme', f'helpme{bot_username}']) & filters.group)
@admin_only
def stolmdfp(client, message):
    global stoprep
    stoprep=0
    message.reply_text("""**@AMIRALIRJPV             | @AMIRALIRJPV |
    /start tag                                          Ř´ŘąŮŘš ŘŞÚŻ

/stop tag                                          ŘŞŮŮŮ ŘŞÚŻ

settag [replay]                         ŘŞŮŘ¸ŰŮ ŮŘŞŮ ŘŞÚŻ 

speed 0                                  ŘłŘąŘšŘŞ ŘŞÚŻ ÚŠŘąŘŻŮ
speed 0.5 
speed 1
speed 2

admin text[replay]         ŮŘŞŮ ŘŞÚŻ ŘŻŘą ŘłŘ§ŮžŮŘąŘŞ

auto tag on\off ŘŞÚŻ ŘŻŘą ŘŹŮŰŮ ŘŞŘ§ŰŮ ŘŻŘąŘłŘ§Ůž Ů ÚŻŮž 

mydell                        Ř­Ř°Ů ŘŞŮŘ§Ů ŮžŰŘ§Ů ŮŘ§Ű ŘŽŮŘŻ 

del tags                                  ŮžŘ§ÚŠ ÚŠŘąŘŻŮ ŘŞÚŻ ŮŘ§ 

set admin                           Ř§ŮŘ˛ŮŘŻŮ Ř§ŘŻŮŰŮ ŘąŘ¨Ř§ŘŞ 

admin list                                ŮŰŘłŘŞ Ř§ŘŻŮŰŮ ŮŘ§ 

del admin                               ŮžŘ§ÚŠ ÚŠŘąŘŻŮ Ř§ŘŻŮŰŮ 

clean adminlist            ŮžŘ§ÚŠŘłŘ§Ř˛Ű ŘŞŮŘ§Ů Ř§ŘŻŮŰŮ ŮŘ§

del tag on/off            ŮžŘ§ÚŠ ŘłŘ§Ř˛Ű ŘŽŮŘŻÚŠŘ§Řąâ ŘŞÚŻ ŮŘ§ ŮŮÚŻŘ§Ů Ř´ŘąŮŘš

mention on                       ŘŞÚŻ Ř¨Ů ŘľŮŘąŘŞ ŮŮŘ´Ů 

user on                           ŘŞÚŻ Ř¨Ů ŘľŮŘąŘŞ ŰŮŘ˛Řą ŮŰŮ 

ping              Ř¨ŘąŘąŘłŰ Ř§ŘŞŘľŘ§Ů ŘąŘ¨Ř§ŘŞ Ů ŘłŘąŘšŘŞ ŘłŘąŮŘą

/skiboro                               Ř§ŘłŮžŮ ŘąŘ§Ű Ř´ÚŠŘ§ŘąÚŰ 

welcome on/off                    ŘŽŮŘ´ Ř§ŮŘŻ ÚŻŮŰŰ

setwel                                     ŮŘŞŮ ŘŽŮŘ´ Ř§ŮŘŻ 

sleep wel [ int ]                    ŘłŘąŘšŘŞ ŘŽŮŘ´ Ř§ŮŘŻ

ŮŮŮ ŘłŘ§ŮžŮŘąŘŞ ŘŻŘą ŘŹŮŰŮ ŘŞŘ§ŰŮ                   suplock 

on/off

/replaytext              ŘŞŮŘ¸ŰŮ ŮŘŞŮ ŘąŰŮžŮŘ§Ű ŘŞÚŻ

/replaytag                 ŘąŮžŮŘ§Ű ÚŠŘąŘŻŮ ŮŘŞŮ ŮŮŘąŘŻ ŮŘ¸Řą

 ŘąŘ§ŮŮŮŘ§Ű ŮŮŘŞŰ      /help   **""")




@bot.on_message(filters.regex(r'admin text') & filters.group )
 
@admin_only
def stlkvfop(client, message):
    global mtx_admin
    mtx_admin = message.reply_to_message.text
    message.reply_text("**text setted**")
######################################################left##################################################################################



        

@bot.on_message(filters.command(['lefts', f'lefts{bot_username}']) & filters.group)
@admin_only
def stamirrop(client, message):
    global list_lefti
    listprint2=''
    shomare1=0
    full_log = bot.send(
        functions.channels.GetAdminLog(     
            channel=bot.resolve_peer(gap),events_filter=ChannelAdminLogEventsFilter(leave=True),
            q="",
            max_id=0,
            min_id=0,
            limit=0,
        )
    )
    time.sleep(10)
    list_left_user=[]
    list_left_id=[]
    try:
        for user in full_log.users:
            list_left_id.append(user.id)
            list_left_user.append(user.username)

        for i in list_left_id:
            for j in list_left_user:
                listprint2+=f'{shomare1}-@{j}~ <a href=tg://user?id={i}>LEFTEDâď¸</a> \n'
                list_left_user.remove(j)
                if shomare1>40:
                    message.reply_text(f"**{listprint2}  \n ŮŰŘłŘŞ ŮŮŘŞŰ ŮŘ§ ŘŻŘą ÚŮŘŻ ŘłŘ§ŘšŘŞ ÚŻŘ°Ř´ŘŞŮ**")
                    listprint2=''
                    shomare1=0
                    time.sleep(2)
                break

            shomare1+=1
        
        time.sleep(2)
        message.reply_text(f"**{listprint2}  \n ŮŰŘłŘŞ ŮŮŘŞŰ ŮŘ§ ŘŻŘą 5 ŘłŘ§ŘšŘŞ ÚŻŘ°Ř´ŘŞŮ**")
        
    except Exception as e:
            message.reply_text(f"**ă ŘŽŘˇŘ§âď¸Ř¨Ů ŮžŘ´ŘŞŰŘ¨Ř§ŮŰ ŮžŰŘ§Ů ŘŻŮŰŘŻ @AMIRALIRJPV ă\n {e}**")




@bot.on_message(filters.command(['persnext', f'persnext{bot_username}']) & filters.group)
@admin_only_asli
def stamirjcnop(client, message):
    try:
        id=message.reply_to_message.from_user.id
        text=str(message.text)[10:]
        next(id,text)
        message.reply_text(f'ok setted for {id}')
    except:
        message.reply_text('ŮŘˇŮŘ§ ŘąŮŰ Ř´ŘŽŘľ ŮŮŘąŘŻ ŮŘ¸Řą ŘąŰŮžŮŘ§Ű ÚŠŮŰŘŻ ')
        
###############################################################auto tag ######################################################################
@bot.on_message(filters.command(['autotag', f'autotag{bot_username}']) & filters.group)
@admin_only
def stamirjcdsnop(client, message):
    global tag_auto_time
    xxy=message.command[1]
    if xxy=='on':
        tag_auto_time=1
        message.reply_text("**auto tag is on**")
    elif xxy=='off':
        tag_auto_time=0
        message.reply_text("**auto tag is off**")


@bot.on_message(filters.command(['admintag', f'admintag{bot_username}']) & filters.group)
@admin_only
def stamigggrjcdsnop(client, message):
    global admin_tag
    xxy=message.command[1]
    if xxy=='on':
        admin_tag=1
        message.reply_text("**auto tag is on**")
    elif xxy=='off':
        admin_tag=0
        message.reply_text("**auto tag is off**")
################################################################################################################


@bot.on_message(filters.command(['nextgame', 'nextgame@OnyxWereBetaBot']) & filters.group )
def stfdaezwedfxmrop(client, message):
    id=message.from_user.id
    if id in next_dic:
        message.reply_text(next_dic[id])
    else:
        id=message.from_user.mention
        next_list=[f'ŘŻŮŘ¨ŮŮŮŮŮŮŮŘąŮŮŮ {id} Ř§ŮŮŘŻŮ ŮŮŮŰŮŮŮŮŮŮŮŮŮŘ§ŘąŮ Ř˛ŘŽŮŮŮŮŮŮđâŮŮŮŮŮ ÚŠŮŮ','Ř¨Ů Ř¨Ů Ř¨Ř¨ŰŮ ÚŠŰ ŮÚŠŘłŘŞ Ř˛ŘŻŮđ¤¤đŚđ',f'Ř§ŮŰŘŻŮŘ§ŘąŮ ŘŻŘłŘŞ Ř¨ŘšŘŻ Ř§ŮŮŘ§ Ř´Ű ',f'ÚŮ ŮŮŘ´Ű ŘŻŮŘł ŘŻŘ§ŘąŰ ŘŻŘłŘŞ Ř¨ŘšŘŻ ŘŻŘ§Ř´ŘŞŮ Ř¨Ř§Ř´Űđđż',f'ŮŮŘ¨ Ř§ŮŘŻŰŮŮŮŮŮŮŮŮ {id} ŮÚŠŘłŘŞ Ř˛ŘŻŮ đđŚ ŘŹŮŮŮŮŮ ŘŹŮŮŮŮŮ',f'ŮžŘąŮ ŮžŮŮŮŮŮŮŮŮŮŮŮŮŰŘąŮŮŮ {id} Ř§ŮŮŮŮŘŻŮ Ř¨ŮŮŮŮđ¤¤ŮŮŘ§Ů Ř¨ŮŮŮŮŮđ¤¤ŮŮŮŮŘ§Ů đŚđ',f'ŮŮŮŰŮŮŮŮŮŮŮŘ§ Ř¨ŘąŰŘŻ ŘŽŮŮŘŞŮŮŮŮđâŮŮŮŮŮŮ ŘłŮŘˇŘ§Ů {id}đŘ§ŮŮŘŻŮ',f'Ř§ŮŮŮŮŮŮŮŮŮŮŮŮŮŮŮđ¤¤ Ř´ÚŠŮŮŮŮŮŮŮŮđđťââď¸ŮŮŮŮŘ§ŘąÚŰ Ř¨ŮŮŮŘ§Ř˛Ű Ř¨ŘšŘŻŰŮ !']
        message.reply_text(random.choice(next_list))

@bot.on_message(filters.command(['unbanfrbot', f'unbanfrbot{bot_username}']) & filters.group & filters.user(list1))
def stzjjwemrop(client, message):
    global ban_list
    user_id=message.reply_to_message.from_user.id
    ban_list.remove(user_id)
    message.reply_text('soltan rj ishon ** unban ** shodan')
    
@bot.on_message(filters.command(['cleanbanlist', f'cleanbanlist{bot_username}']) & filters.group & filters.user(list1))
def stzjjwijikemrop(client, message):
    global ban_list
    ban_list=[]
    message.reply_text('ok')
@bot.on_message(filters.command(['banfrbot', f'banfrbot{bot_username}']) & filters.group  & filters.user(list1) ) 
def stzjjwemjnrop(client, message):
    global ban_list
    user_id=message.reply_to_message.from_user.id
    ban_list.append(user_id)
    message.reply_text('soltan rj ishon ban shodan')



###########################################################speed############################################################
@bot.on_message(filters.command(['ads', f'ads{bot_username}']) & filters.group)
@admin_only_asli
def stoxdfgfklehcguyp(client, message):
    ads=message.reply_to_message.text
    bot.send_message(gap,f'**{ads}**')


@bot.on_message(filters.command(['mydell', f'mydell{bot_username}']) & filters.group)
 
@admin_only
def stoxdfgfhcguyp(client, message):
    try:
        chat_id = message.chat.id
        user=message.from_user.id
        bot.delete_user_history(chat_id,user_id=user)

        message.reply_text("**pak shod**")
    except:
        message.reply_text('ŘąŘ¨Ř§ŘŞ ŘąŘ§ Ř§ŘŻŮŰŮ ÚŻŘąŮŮ Ř¨ÚŠŮŰŘŻ')


################################################################bazi#########################################################


@bot.on_message(filters.regex(r'Ř¨Ř§Ř˛Ű Ř´ŘąŮŘš Ř´ŘŻ') & filters.group & filters.user(list1))
def sto333p(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False
    if tag_auto==1:
        try:
            tag_msgs = [msg for msg in bot.iter_history(gap,limit=1000) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention"):
                        if tagmsg.from_user.id not in wwbots:
                            tagmsg.delete()
                            time.sleep(0.1)
                time.sleep(0.1)
            message.reply_text(f"**ŮžŘ§ÚŠŘłŘ§Ř˛Ű ŘŞÚŻ ŮŘ§ Ř§ŮŘŹŘ§Ů Ř´ŘŻ**")
        except Exception as e:
            message.reply_text(f"**ă ŘŽŘˇŘ§âď¸Ř¨Ů ŮžŘ´ŘŞŰŘ¨Ř§ŮŰ ŮžŰŘ§Ů ŘŻŮŰŘŻ @AMIRALIRJPV ă\n {e}**")
        try:
            if suplock==1:
                
                    bot.set_chat_permissions(group_admin_id,ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_stickers=True,can_send_animations=True))
        except:
            pass

@bot.on_message(filters.regex(r'ŘŞŘšŘŻŘ§ŘŻ Ř¨Ř§Ř˛ŰÚŠŮŘ§ Ř¨Ů ŮžŮŘŹ') & filters.group & filters.user(list1))
def stoii88p(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False


@bot.on_message(filters.regex(r'ÚŮŘŻŘą ÚŠŮŰŮ') & filters.group & filters.user(list1))
def stbbbbbop(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False

        try:
            tag_msgs = [msg for msg in bot.iter_history(gap,limit=1000) if msg.entities]
            for tagmsg in tag_msgs:
                for ent in tagmsg.entities:
                    if ent.type in ("mention", "text_mention") and  tag_msgs.id not in list1:
                        if tagmsg.from_user.id not in wwbots:
                            tagmsg.delete()
                            time.sleep(0.1)
                time.sleep(0.1)
            message.reply_text(f"**ŮžŘ§ÚŠŘłŘ§Ř˛Ű ŘŞÚŻ ŮŘ§ Ř§ŮŘŹŘ§Ů Ř´ŘŻ**")
        except Exception as e:
            message.reply_text(f"**ă ŘŽŘˇŘ§âď¸Ř¨Ů ŮžŘ´ŘŞŰŘ¨Ř§ŮŰ ŮžŰŘ§Ů ŘŻŮŰŘŻ @AMIRALIRJPV ă\n {e}**")


@bot.on_message(filters.command(['deltags', f'deltags{bot_username}']) & filters.group)
@admin_only
def stopmaman(client, message):
    m=0
    chatid=message.chat.id
    message.reply_text(f"**ŘŻŘąŘ­Ř§Ů ŮžŘ§ÚŠŘłŘ§Ř˛Ű**")
    try:
        tag_msgs = [msg for msg in bot.iter_history(chatid,limit=1000) if msg.entities]
        for tagmsg in tag_msgs:
            for ent in tagmsg.entities:
                if ent.type in ("mention", "text_mention"):
                    if tagmsg.from_user.id not in wwbots:
                        m+=1
                        tagmsg.delete()
                        time.sleep(0.1)
                time.sleep(0.1)
        message.reply_text(f"**ŮžŘ§ÚŠŘłŘ§Ř˛Ű {m} ŘŞÚŻ Ř§ŮŘŹŘ§Ů Ř´ŘŻ**")
    except Exception as e:
        message.reply_text(f"**ă ŘŽŘˇŘ§âď¸Ř¨Ů ŮžŘ´ŘŞŰŘ¨Ř§ŮŰ ŮžŰŘ§Ů ŘŻŮŰŘŻ @AMIRALIRJPV ă\n {e}**")

            
############################################################admin##############################################################

@bot.on_message(filters.regex(r'set sup') & filters.group & filters.user(list1))
def skoonkontop(client, message):
    global group_admin_id
    try:
        group_admin_id=message.reply_to_message.text
        message.reply_text("**setted**")
    except:
        message.reply_text("**ă ŘŽŘˇŘ§âď¸ŮŘˇŮŘ§ Ř§ŰŮ ŘŻŘłŘŞŮŘą ŘąŘ§ Ř¨Řą ŘąŮŰ ŮžŰŘ§ŮŰ ŘąŰŮžŮŘ§Ű ÚŠŮŰŘŻ ! ă**")


@bot.on_message(filters.regex(r'set here sup') & filters.group & filters.user(list1))
def stjonkonop(client, message):
    global group_admin_id
    group_admin_id=message.chat.id
    message.reply_text("** ă !ŘŞÚŻŘą ŘłŘ§ŮžŮŘąŘŞ ŘŻŘą Ř§ŰŮ ÚŻŘąŮŮ ŮŘľŘ¨ Ř´ŘŻ ă**")
    


@bot.on_message(filters.regex(r'set main admin') & filters.group & filters.user(list1))
def stkirsirmirop(client, message):
    global admin_all
    global list_admin
    l=message.reply_to_message.from_user.id
    list_admin.append(l)
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)
    message.reply_text("** ă !Ř§ŘŻŮŰŮ Ř§ŮŘ˛ŮŘŻŮ Ř´ŘŻă**")
    


@bot.on_message(filters.regex(r'del main admin') & filters.group & filters.user(list1))
def stoansagkoonp(client, message):
    global list_admin
    
    a=message.reply_to_message.from_user.id
    try:
        list_admin.remove(a)
        message.reply_text("** ă !Ř§ŘŻŮŰŮ Ř­Ř°Ů Ř´ŘŻă**")
        
    except:
        message.reply_text("**Ř§ŰŮ ŰŮŘ˛Řą ŘŻŘą ŮŰŘłŘŞ ŮŘŹŮŘŻ ŮŘŻŘ§ŘąŘŻ **")

    


@bot.on_message(filters.regex(r'add main gap') & filters.group & filters.user(list1))
def silovesarinatop(client, message):
    global gap
    global admin_all
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)
    gap=message.chat.id
    message.reply_text("** ă !Ř§ŘśŘ§ŮŮ Ř´ŘŻ **")
    print(gap)



@bot.on_message(filters.regex(r'add main gap') & filters.group & filters.user(list1))
def stopkirkharbot(client, message):
    global gap
    global admin_all
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)
    gap=message.chat.id
    message.reply_text("** ă !Ř§ŘśŘ§ŮŮ Ř´ŘŻ **")
    print(gap)

biadaabi=0
@bot.on_message(filters.regex(r'admin list') & filters.group )
@admin_only
def stopkonbs(client, message):
    listprint=''
    shomare=1
    try:
        for f in client.iter_chat_members(gap,filter='administrators'):
            listprint+=f'{shomare}-{f} \n'
            shomare+=1
        message.reply_text(f"**{listprint}**")
    except Exception as e:
            message.reply_text(f"**ă ŘŽŘˇŘ§âď¸Ř¨Ů ŮžŘ´ŘŞŰŘ¨Ř§ŮŰ ŮžŰŘ§Ů ŘŻŮŰŘŻ @AMIRALIRJPV ă\n {e}**")
###############################################################admin 2 ####################################################
@bot.on_message((filters.regex(r'Ř¨ŮŘł')|(filters.regex(r'ŰŮŘľ')|(filters.regex(r'bos'))) & filters.group  ))
def kisss(client,message):
    try:
        message.reply_text(f"**{message.from_user.mention} Kissed {message.reply_to_message.from_user.mention}**đ")
    except:
        pass
@bot.on_message(filters.regex(r'Ř§ŰŮ ÚŠŮŮŰŮ') & filters.group )
def ki7ss(client, message):
    if biadaabi==1:
        koni=random.randint(1,5)
        if koni==1:
            koni_text='**ŮŮŘ¨ ŮŘ§Ű ŘŽŮŘŻ ŘąŘ§ Ř¨Ů ŘŻŰÚŻŘąŘ§Ů ŮŘŻŮŰŮ **'
        elif koni==2:
            koni_text=f'ÚŠŮŮŰ Ř¨ŮŘŻŮ Ř§ŘŤŘ¨Ř§ŘŞ Ř´ŘŻ {message.reply_to_message.from_user.mention} Ř§ÚŠŮŮŮ ŰŮ ÚŠŮŮŰ Ř§ŘłŘŞ  '
        elif koni==3:
            koni_text='ŘŽŰŘą Ř´ŮŘąŰŘ§Řą ÚŠŮŮŰŮ'
        elif koni==4:
            koni_text=f'Ř§ŮŘ§/ŘŽŘ§ŮŮ{message.reply_to_message.from_user.mention}:ŘŞŘšŘŻŘ§ŘŻ {random.randint(30,10000)} ÚŠŮŮ ŘŻŘ§ŘŻŮ ŘŻŘą ÚŠŘ§ŘąŮŘ§ŮŮ Ű ŘŽŮŘŻ ŘŻŘ§ŘąŮŘŻ '
        else:
            koni_text=f'Ř§ŰŘ´ŮŮ{message.reply_to_message.from_user.mention} ŘŞŮŘ¨Ů ÚŠŘąŘŻŮ Ů Ř§Ř˛ Ř§ŘŽŘąŰŮ ÚŠŮŮ ŘŻŘ§ŘŻŘ§ŮŘ´ŮŮ {random.randint(1,12)}ŮŘ§Ů ŮŰÚŻŘ°ŘąŘŻ'
        try:
            message.reply_text(f"**{koni_text}**")
        except:
            pass
@bot.on_message(filters.regex(r'Ř­Ů') & filters.group )
def k6iss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**{message.from_user.mention}  indirectly told  {message.reply_to_message.from_user.mention} kos amat**đđđ")
        except:
            pass
@bot.on_message(filters.regex(r'ÚŘ´Ů') & filters.group )
def kiss5(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**{message.reply_to_message.from_user.mention} ŮŮŘ¸ŮŘąŘ´ Ř§ŰŮ Ř¨ŮŘŻ ŘłŰÚŠ ÚŠŮ ŘŞŘ§ ŮÚŠŘąŘŻŮŘŞ **đ")
        except:
            pass
@bot.on_message(filters.regex(r'\+') & filters.group )
def kishss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**ŰŮ ŮŘ§ŮŘ´ {random.randint(60,100)} Ř§ŮŘŞŰŘ§Ř˛Ű Ř¨ŘąŘ§Ű {message.reply_to_message.from_user.mention}**")
        except:
            pass
@bot.on_message(filters.regex(r'â¤ď¸') & filters.group )
def ki3ss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**{message.from_user.mention} love  {message.reply_to_message.from_user.mention} :)) **")
        except:
            pass
@bot.on_message(filters.regex(r'ÚŠŮŘ¨Řľ') & filters.group )
def kiss2(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**Ř´Ř§ŰŘŻ ÚŻŘ§ŮŰ Ř¨Ř§ ŰÚŠ ÚŠŮŘ¨ŘľŘŻ Ř¨ŘŞŮŘ§ŮŰ ŮŘąŘ§ ŘŽŮŘ´Ř­Ř§Ů ÚŠŮŰ {message.reply_to_message.from_user.mention} :)**")
        except:
            pass
@bot.on_message(filters.regex(r'ŮŰÚŠŮŮŘŞ') & filters.group)
def kiss1(client, message):
    if biadaabi==1:

        bokon=random.randint(0,100)
        if 95>bokon>80:
            koni1_text=f'**Ř´ŮŘ§ ŰÚŠŰ Ř§Ř˛ ŮŘŽŮŮ ŘŞŘąŰŮ Ř¨ÚŠŮŘ§Ű {message.reply_to_message.from_user.mention} ŮŘłŘŞŰŘŻ ŘłŘˇŘ­ Ř´ŮŘ§ Ř¨ÚŠŮ ŘłŘˇŘ­ 10 Ř§ŘłŘŞ **'
        elif 80>bokon>50:
            koni1_text=f'Ř´ŮŘ§  Ř¨Ů ŘšŮŮŘ§Ů ŰÚŠ Ř¨ÚŠŮ ŘłŘˇŘ­ {random.randint(1,9)}Ř´ŮŘ§ŘłŘ§ŰŰ Ř´ŘŻŰŘŻ !'
        elif 50>bokon>30:
            koni1_text='ŘŞŮ ŮÚŻŮ ÚŠŰŘą ŘŻŘ§ŘąŰ Ř§ŘľŮŘ§ đđđđđ'
        elif 30>bokon>0:
            koni1_text=f'ŘŞŮ ŰŮ Ř´Ř¨ {message.reply_to_message.from_user.mention}  đđđđđŘ§ŮÚŻŘ´ŘŞŘŞ ŮÚŠŮŮ ÚŻŘąŰŮ ŮŰÚŠŮŰ Ř¨ŘšŘŻ ŮŰŘŽŮŘ§Ű Ř¨ÚŠŮŰŘ´Ř'
        else:
            koni1_text='Ř´ŮŘ§ Ř¨ÚŠŮ ŮŮŘ§Řą ŘŞŮŘ§Ů Ř§ŮŘąŘ§ŘŻ ÚŻŘąŮŮ Ů ÚŠŘąŮ ŘŽŘ§ÚŠŰ ŮŘłŘŞŰŘŻ '
        try:
            message.reply_text(f"**{koni1_text}**")
        except:
            pass
            pass
@bot.on_message(filters.regex(r'ŘłŰÚŠ') & filters.group)
def kisss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"* Ř¨ŰŘ§ ŘŻÚŠŮŘŞŮ Ř¨Ř˛Ůđ ŮžŘąŮŘ§Ř˛ ÚŠŮŰ đŤ  {message.reply_to_message.from_user.mention}**")
        except:
            pass
@bot.on_message(filters.regex(r'ŮŮŮ') & filters.group)
def kisss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**ŘŻŘą Ř§ŮŘ¨Ř§Řą ŮŮŘˇ ÚŠŰŘ´ŮŘ´ ŮŮŘŹŮŘŻ ŮŘłŘŞ(@Admizad0) Ř¨Ř§Řą ŘŹŘŻŰŘŻ ŘšŰŘŻ ŮŰŘąŘłŮ đ.**")
        except:
            pass

@bot.on_message(filters.regex(r'ŮŮŰŘľ') & filters.group)
def kisss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**ŘŻŘ§ŘŻŘ§Ř´ Ř¨ŰŘ§ Ř¨Ř§ŮŘ§ ŘŻŮŮŰŮ ŮŮŘł Ř¨ÚŻŰŘą Ř¨Ů ŮÚŠŘą Ř˛Ř¨ŮŮŘŞ đ ŮŰŘłŘŞŰ Ř¨Ů ŮÚŠŘą ŮŮŘ¨ŘŞ đŤŘ¨Ř§Ř´ ŘŽŮŮŰ Ř´ŘŻ ŮŘ§ŮžŘ§ Ř§ŮŮ Ř¨ŰÚŘ§ŘąŮ đŻđľ.**")
        except:
            pass


@bot.on_message(filters.regex(r'ŮŮŘ§Ů') & filters.group)
def kisss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**Ř¨ŰŘ§ {message.reply_to_message.from_user.mention}  ŘŻŘłŘŞÚŠŘ´ đ§¤Ř ŘŻŘłŘŞŘ§ŘŞ Ř¨Ů ÚŻŘąŮŘŞ Ř§Ř˛ Ř¨Řł ŮŘ§ŮŰŘŻŰ**")
        except:
            pass

@bot.on_message(filters.regex(r'Ř¨ÚŠŰŘąŮ') & filters.group )
def ki7ss(client, message):
    if biadaabi==1:
        bkiram=random.randint(1,5)
        if bkiram==1:
            bkira_text='**Ř§Ř˛ ŘŻŘ§Ř´ŘŞŮ ŮŘ§Ű ŘŽŮŘŻ ŘľŘ­Ř¨ŘŞ ÚŠŮŰŮ  **'
        elif bkiram==2:
            bkira_text=f' Ř¨Ů ÚŠŰŘąŘ´ ŘŻŘ§ŰŮŘąŘŞ Ř´ŘŻ {message.reply_to_message.from_user.mention}'
        elif bkiram==3:
            bkira_text='ÚŠŘŹŘ§ŘŞŘđđđ'
        elif bkiram==4:
            bkira_text=f'Ř¨ÚŠŘľŘ´ ŮŮŘ¸ŮŘąŘ´Ů {message.from_user.mention}'
        else:
            bkira_text=f'Ř§ŮŘ§ Ř´ŮŘąŰŘ§Řą @wait_aminute ŘľŘŻŘ§ŘŞ ŮŰŘ˛ŮŮ '
        try:
            message.reply_text(f"**{bkira_text}**")
        except:
            pass

@bot.on_message(filters.regex(r'Ř¨ŘŽŮŘąŘ´') & filters.group)
def kisss(client, message):
    try:
        message.reply_text(f"** king Chocolate ? {message.reply_to_message.from_user.mention}**")
    except:
        pass
@bot.on_message(filters.regex(r'ŘŻ ÚŠŰŮÚŻ') & filters.group  )
def kishehes(client, message):
    try:
        message.reply_text(f"**{message.from_user.mention}   @A_mohamadi_30 soltan sedat mizanan **")
    except:
        pass


@bot.on_message(filters.regex(r'ŮŮŘ¨') & filters.group )
def ki7ss(client, message):
    koni=random.randint(1,5)
    if koni==1:
        koni_text='**ŮŮŘ¨ ŮŘ§Ű ŘŽŮŘŻ ŘąŘ§ Ř¨Ů ŘŻŰÚŻŘąŘ§Ů ŮŘŻŮŰŮ **'
    elif koni==2:
        koni_text=f'ŮŮŘ¨  Ř¨ŮŘŻŮ Ř§ŘŤŘ¨Ř§ŘŞ Ř´ŘŻ {message.reply_to_message.from_user.mention} Ř§ÚŠŮŮŮ ŰÚŠ ŮŮŘ¨  Ř§ŘłŘŞ  '
    elif koni==3:
        koni_text='ŘŽŰŘą Ř´ŮŘąŰŘ§Řą ÚŠŮŮŰŮ'
    elif koni==4:
        koni_text=f'Ř§ŮŘ§/ŘŽŘ§ŮŮ{message.reply_to_message.from_user.mention} |  {random.randint(0,100)} ŘŻŘąŘľŘŻ ŮŮŘ¨ Ř§ŘłŘŞ !  '
    else:
        koni_text=f'Ř§ŰŘ´ŮŮ{message.reply_to_message.from_user.mention}  Ř§ÚŠŮŮŮ ŮžŘąŮ Ř§ŘłŘŞ Ř§Ř˛ ŮŮŘ¨ Ř¨ŮŘŻŮŘ´ŮŮ   {random.randint(1,12)}ŮŘ§Ů ŮŰÚŻŘ°ŘąŘŻ'
    try:
        message.reply_text(f"**{koni_text}**")
    except:
        pass



 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
@bot.on_message(filters.command(['promateadmins', f'promateadmins{bot_username}']) & filters.group)
@admin_only_asli
def sto3we4srdtp(client, message):
    global list3
    global admin_all
    for i in client.iter_chat_members(gap,filter='administrators'):
        list3.append(i.user.id)
    message.reply_text(f"**Ř§ŮŘŹŘ§Ů Ř´ŘŻ**")
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)


@bot.on_message(filters.regex(r'set admin') & filters.group )
@admin_only_asli
def sto3wje4srdtp(client, message):
    global list3
    global admin_all
    if message.reply_to_message:
        c=message.reply_to_message.from_user.id
        list3.append(c)
        message.reply_text("** ă !Ř§ŘŻŮŰŮ Ř§ŮŘ˛ŮŘŻŮ Ř´ŘŻă**")
    else:
        message.rep_text('**ă ŘŽŘˇŘ§âď¸ŮŘˇŮŘ§ Ř§ŰŮ ŘŻŘłŘŞŮŘą ŘąŘ§ Ř¨Řą ŘąŮŰ ŮžŰŘ§ŮŰ ŘąŰŮžŮŘ§Ű ÚŠŮŰŘŻ ! ă**')
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)


@bot.on_message(filters.regex(r'del admin') & filters.group )
@admin_only_asli
def stoami111p(client, message):
    global list3
    global admin_all

    b=message.reply_to_message.from_user.id
    try:
        list3.remove(b)
        message.reply_text("** ă !Ř§ŘŻŮŰŮ Ř­Ř°Ů Ř´ŘŻă**")
    except:
        message.reply_text("**Ř§ŰŮ ŰŮŘ˛Řą ŘŻŘą ŮŰŘłŘŞ ŮŘŹŮŘŻ ŮŘŻŘ§ŘąŘŻ **")

    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)
    


@bot.on_message(filters.regex(r'clean adminlist') & filters.group )
@admin_only_asli
def st9999op(client, message):
    global list3
    global admin_all
    list3=[]
    message.reply_text("** ă !ŘŞŮŘ§ŮŰ Ř§ŘŻŮŰŮ ŮŘ§ Ř­Ř°Ů Ř´ŘŻŮŘŻă**")
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)



#########################################################del tag #######################################################


@bot.on_message(filters.command(['deltag', f'deltag{bot_username}']) & filters.group)
@admin_only
def sto2233p(client, message):
    global tag_auto
    xxy=message.command[1]
    if xxy=='on':
        tag_auto=1
        message.reply_text("**del tag is on**")
    elif xxy=='off':
        tag_auto=0
        message.reply_text("**del tag is off**")


@bot.on_message(filters.command(['biadabi', f'biadabi{bot_username}']) & filters.group)
@admin_only_asli
def sto2233p(client, message):
    global biadaabi
    xxy=message.command[1]
    if xxy=='on':
        tag_auto=1
        message.reply_text("**bi adabi is on**")
    elif xxy=='off':
        tag_auto=0
        message.reply_text("**bi adabi is off**")


######################################################ping and chalesh###########################################################################

@bot.on_message(filters.command(['ping', f'ping{bot_username}']) & filters.group )
@admin_only
def sto176655p(client, message):
    tic = time.perf_counter()
    for i in range(5000000):
        pass
    toc = time.perf_counter()
    chat_id = message.chat.id
    bot.send_message(chat_id,f'**đđ đđđđđđ! đđđđ:{toc - tic:.4f}**')

    
@bot.on_message(filters.command(['lockstats', f'lockstats{bot_username}']) & filters.group)
@admin_only
def stwemnmrop(client, message):
    global fakebazi
    fakebazi=int(message.command[1])
    message.reply_text(f"**ok setted {fakebazi}**")


####################################################################suplock##################################################################################

@bot.on_message(filters.regex(r'ŘŻÚŠŮŮ Ř˛ŰŘą')  & ~filters.regex(r'ŮŘ´Ř§ŮŘŻŮ')  & filters.group & filters.user([854021534,175844556]))
def stamir001000o1p(client, message):
    message.forward(group_admin_id)
    if suplock==1:
        bot.set_chat_permissions(group_admin_id,ChatPermissions(can_send_messages=False))

@bot.on_message(filters.command(['deltag', f'deltag{bot_username}']) & filters.group)
@admin_only
def stol2233p(client, message):
    global suplock
    xxy=message.command[1]
    if xxy=='on':
        suplock=1
        message.reply_text('**sup lock is on**')

    elif xxy=='off':
        suplock=0
        message.reply_text('**sup lock is off**')

@bot.on_message(filters.regex(r'suplock off') & filters.group )
@admin_only
def sto100101010p(client, message):
    global suplock
    suplock=0
    message.reply_text('**sup lock is off**')
###################################################################shekar###################################################################################################
@bot.on_message(filters.group &  (filters.regex(r'#Ř´ÚŠŘ§ŘąŮ')| filters.regex(r'#ch')|filters.regex(r'Ř´ÚŠŘ§Řą#')  & filters.group & ~filters.me & ~filters.user([854021534,1289410047,1181120160,1653256635,1538900423])))
@ban_from_bot
def sto1118811p(client, message):
    global shekar
    if str(message.text) in ['#Ř´ÚŠŘ§ŘąŮ','#ch','Ř´ÚŠŘ§Řą#']:
        shekar=message.from_user.id
        try:
            
            message.pin()
        except:
            pass
        message.reply_text('**đŘ´ÚŠŘ§ŘąÚŰ Ř´ŮŘ§ŘłŘ§ŰŰ Ř´ŘŻ :)**')
        message.reply_text('**Ř¨ŘąŘ§Ű Ř§ŘłŮžŮ ŘąŘ§ŰŘŞŮŮ Ř§Ř˛ /ray Ř§ŘłŘŞŮŘ§ŘŻŮ ÚŠŮŰŘŻ Ů ŘŹŮŮŰ Ř§Ů  ŘąŘ§ŰŘŞŮŮ ŘąŮ Ř¨ŮŮŰŘłŰŘŻ **')


@bot.on_message(filters.regex(r'#ŮŘ§Ř¸Řą')|filters.regex(r'#ŮÚŠŮŮ_Ř´ÚŠŘ§Řą')  & filters.group & ~filters.me & ~filters.user([854021534,1289410047,1181120160,1653256635,1538900423]))
@ban_from_bot
def sto777221p(client, message):
    global nazer
    if str(message.text) in ['#ŮŘ§Ř¸Řą','#ŮÚŠŮŮ_Ř´ÚŠŘ§Řą#']:
        nazer=message.from_user.id
        try:
            message.pin()
        except:
            pass
        message.reply_text('**đŮŘ§Ř¸Řą Ř´ŮŘ§ŘłŘ§ŰŰ Ř´ŘŻ :)**')
        message.reply_text('**Ř¨ŘąŘ§Ű Ř§ŘłŮžŮ ŘąŘ§ŰŘŞŮŮ Ř§Ř˛ /ray Ř§ŘłŘŞŮŘ§ŘŻŮ ÚŠŮŰŘŻ Ů ŘŹŮŮŰ Ř§Ů  ŘąŘ§ŰŘŞŮŮ ŘąŮ Ř¨ŮŮŰŘłŰŘŻ **')



@bot.on_message(filters.command(['ray', f'ray{bot_username}']) & filters.group & ~filters.me & ~filters.user([854021534,1289410047,1181120160,1410445908,1653256635]))
@ban_from_bot
def st11000011o1p(client, message):
    global shekar
    chat_id1=message.chat.id
    if shekar==message.from_user.id:
        ski_shekar =message.command[1]
        if ski_shekar!='':
            
            for i in range(1,10):
                bot.send_message(chat_id1,text=f'''âď¸ŘąŘ§Ű Ř´ÚŠŘ§ŘąÚŰă


            đ°  **{ski_shekar}** đ° ă ''' )
                time.sleep(5)
        else:
            message.reply_text('ŮŘŞŮ ŘąŘ§Ű ŘąŘ§ ŘŹŮŮŰ /ray Ř¨ŮŮŰŘłŰŘŻđă')
    else:
        message.reply_text('ăŘ´ŮŘ§ Ř´ÚŠŘ§ŘąÚŰ Ř¨Ř§Ř˛Ű ŮŰŘłŘŞŰŘŻđă')




@bot.on_message(filters.command(['nray', f'nray{bot_username}']) & filters.group & ~filters.me & ~filters.user([854021534,1289410047,1181120160,1410445908,1653256635]))
@ban_from_bot
def s000to1p(client, message):
    global nazer
    
    chat_id1=message.chat.id
    if nazer==message.from_user.id:
        nazer_ski = message.command[1]
        if nazer_ski!='':
            for i in range(1,12):
                bot.send_message(chat_id1,text=f'''âď¸ŘąŘ§Ű ŮŘ§Ř¸Řą âď¸


            đ°  **{nazer_ski}** đ° ă ''' )
                time.sleep(5)
        else:
            message.reply_text('ŮŘŞŮ ŘąŘ§Ű ŘąŘ§ ŘŹŮŮŰ /ray Ř¨ŮŮŰŘłŰŘŻđă')
    else:
        message.reply_text('ăŘ´ŮŘ§ ŮŘ§Ř¸Řą Ř¨Ř§Ř˛Ű ŮŰŘłŘŞŰŘŻđă')
################################################################state#####################################################################
@bot.on_message( filters.regex(r'state')& filters.group )
@ban_from_bot
def stnjhkno1p(client, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        user=message.from_user
    try:
        
        o=post(
        url="http://api.wolfofpersia.ir:9999/api/GetState",
        data={
            "user_id": user.id,
            "token": token}).json()
        man=dict(o)
        totalgame=int(man['total_game'])
        fullname=(man['fullname'])
        mention1=mention(user.id,fullname)
        
        message.reply_text(f'''
        **ăOnyx Account state đ ! ă**
        
    **â total games   đą:ă{totalgame}ă**
    **âŁ Account Name đ: {mention1}**
    **âŁ First Game : {man["TheFirstGame"]} **
    **âŁ Survived Games : {man['SurviveTheGame']}**
    **âŁ Most Kills : {man['YouKillName']} {man['killMeUserCount']} times**
    **âŁ most killed by : {man['killMeName']}
    **âŁ Status : {man["status"]}
    **â {user.id}**''')
    except :
        try:
             message.reply_text(f'''**ăOnyx Account state đ ! ă**

    **â total games đą: ă{totalgame}ă**
    **âŁ Account Name đ: {mention1}**
    **â {user.id}**''')
        except:
            message.reply_text(f'''ă Ř§ŰŮ Ř¨Ř§Ř˛ŰÚŠŮ Ř§ŘłŘŞŰŘŞŰ ŮŘŻŘ§ŘąŘŻ ! ă**''')

            
            
#{'status': True, 'error': '', 'fullname': 'Sly ', 'user_id': 1347350135, 'total_game': 372, 'SurviveTheGame': 79, 'SlaveGames': 145
#, 'LoserGames': 227, 'lang_code': 'en', 'username': 'sly12919', 'ActivePhone': '', 'killMeName': 'Mbina  ', 'killMeUserID': 775547629, 'killMeUserCount': 21, 'YouKillName': 'đ¸đđđ  ', 


######################

@bot.on_message(filters.new_chat_members)

def say_welcome(client, message):
    global welcome_groups, welcome_text, welcome_sleep
    ch=message.chat.id
    time.sleep(welcome_sleep)
    for user in message.new_chat_members:
        try:
            
            o=post(url="http://api.wolfofpersia.ir:9999/api/GetState",data={"user_id": user.id,"token": token}).json()
            man=dict(o)
            totalgame=man['total_game']
            fullname=man['fullname']
            mention1=mention(user.id,fullname)
            message.reply_text(f'''**ăOnyx Account state đ ! ă**

    **â total games đą: ă{totalgame}ă**
    **âŁ Account Name đ:{mention1}**
    **â {user.id}**''')
        except:
            mention1=mention(user.id,user.first_name)
            totalgame=0
            bot.send_message(group_admin_id,f'#new \n \nÚŠŘ§ŘąŘ¨Řą {mention1}  Ř¨ŘŻŮŮ Ř§ŘłŘŞŰŘŞ ŮŘ§ŘąŘŻ ÚŻŮž Ř´ŘŻŮ  Ř¨Ř§ Ř§ŰŘŻŰ {user.username}')
            message.reply_text(f'''ă Ř§ŰŮ Ř¨Ř§Ř˛ŰÚŠŮ Ř§ŘłŘŞŰŘŞŰ ŮŘŻŘ§ŘąŘŻ  ! ă**''')
        try: 
            if int(totalgame)<fakebazi:
                bot.kick_chat_member(ch,user.id)
                bot.send_message(ch,f'voip! I banned {mention1} him ')
        except :
            pass
    
            
       
    
            
       
################################################################welcome####################################################################################################



############################################################ATTACH####################################################################################
#####################################################################################################################################################
######################################################################################################################################################
#####################################################################################################################################################
######################################################################################################################################################
#####################################################################################################################################################
######################################################################################################################################################
#####################################################################################################################################################
######################################################################################################################################################
#####################################################################################################################################################
######################################################################################################################################################
#####################################################################################################################################################
######################################################################################################################################################
bots = {}
delay_each_atk = 7
delay_time = 0

helpMSG = '''**ă ŘłŮŘ§Ů Ř¨Ů Ř¨ŘŽŘ´ ŘąŘ§ŮŮŮŘ§Ű Ř¨Ř§ŘŞ ŮŮŘŞŰ ŘŽŮŘ´ Ř˘ŮŘŻŰŘŻ đđť  ! ă**

**đş ă ŮŘ­ŮŮ ŘŤŘ¨ŘŞ Ř§ÚŠŘ§ŮŘŞ đ˛! ă **
**ă ŘŻŘłŘŞŮŘą /add : Ř§ŰŮ ŘŻŘłŘŞŮŘą ŘąŘ§ Ř¨Ř§ŰŘŻ Ř¨Řą ŘąŮŰ ŮžŰŘ§ŮŰ Ř§Ř˛ @UseTGXbot  ŘąŰŮžŮŘ§Ű ÚŠŮŰŘŻ Ů ŘŹŮŮŰ ŘŻŘłŘŞŮŘą ŮŘ§Ů Ř§ÚŠŘ§ŮŘŞ ŘąŘ§ Ř¨Ř˛ŮŰŘŻ !ă**
ŮŘŤŘ§Ů** : **
**/add Name**
**/delacc Name 
**ă ŘŻŘłŘŞŮŘą /code : Ř§ŰŮ ŘŻŘłŘŞŮŘą Ř¨ŘąŘ§Ű ŮŘ§ŘąŘŻ ÚŠŘąŘŻŮ ÚŠŘŻ ŮŘąŮŘŻ Ř§ŘłŘŞ ! ă**
ŮŘŤŘ§Ů** :**
**/code code tel | password**
**/code 111-11 1234**
**âââââ**
**đş ă Ř¨ŘŽŘ´ ŘŞŮŘ¸ŰŮ ŘłŘąŘšŘŞ âą! ă **
**ă ŘŻŘłŘŞŮŘą /setspeed : Ř§ŰŮ ŘŻŘłŘŞŮŘą Ř¨ŘąŘ§Ű ŘŞŮŘ¸ŰŮ ŘłŘąŘšŘŞ ŮŮŘŞŰ  Ř§ŘłŘŞŮŘ§ŘŻŮ ŮŰŘ´ŮŘŻ! ă**
ŮŘŤŘ§Ů** :**
**/setspeed 2 4**
**ă ŘŻŘłŘŞŮŘą /speed : ŮŘ´Ř§ŮŘŻŮ ŘłŘąŘšŘŞ ŮŘšŮŰ ŘąŘ¨Ř§ŘŞ ! ă  **
**âââââ**
**đş ă ŮŘ´Ř§ŮŘŻŮ Ř§ÚŠŘ§ŮŘŞ ŮŘ§ đ! ă **
**ă ŘŻŘłŘŞŮŘą /account : Ř˘ŮŘ§Řą ÚŠŮŰ Ř§ÚŠŘ§ŮŘŞ ŮŘ§ ! ă **
**ă ŘŻŘłŘŞŮŘą /ping ŮŘ´Ř§ŮŘŻŮ Ř§ÚŠŘ§ŮŘŞ ŮŘ§ ! ă **
**âââââ**
** đş ă Ř¨ŘŽŘ´ Ř¨ŮŘą đ ! ă **
**ă ŘŻŘłŘŞŮŘą /setbanner : Ř§ŰŮ ŮžŰŘ§Ů ŘąŘ§ Ř¨Řą ŘąŮŰ Ř¨ŮŘąŘŞŘ§Ů Ř¨ŮŘąŘłŘŞŰŘŻ ŘŞŘ§ ŘŤŘ¨ŘŞ Ř´ŮŘŻ ! ă **
**ă ŘŻŘłŘŞŮŘą /banner : ŮŘ´Ř§ŮŘŻŮ Ř¨ŮŘą ŮŘšŮŰ ! ă **
**âââââ**
**/golefties          ŘąŮŘŞŮ Ř¨Ů ŮžŰŮŰ ŮŮŘŞŰ ŮŘ§Ű ÚŻŮž **

**                  ă Dev : ||||||| @AMIRALIRJPV ||||||| 
                        |~~~~~~~~ @AMIRALIRJPV ~~~~~~~| 
                            @parsa_rus  đđťââď¸ ă** 
'''

Banner = ''
attacker = False
name = ''
Id = ''
Hash = ''
phhash = ''
phnum = ''


@bot.on_message(filters.command(['helplefti', f'helplefti{bot_username}'], '/') & filters.group)
@admin_only
def _help(client, message):
    client.send_message(message.chat.id, helpMSG)


###################################################################################################################################


@bot.on_message(filters.command(['attack', f'attack{bot_username}']) & filters.group)
@admin_only
def attajckk(client, message):
    global Banner
    global attacker, delay_each_atk, delay_time
    alls=''
    users=[]
    if Banner == {}:
        client.send_message(
            message.chat.id, '**ă Please Set The Banner đđ !ă**')
    else:
        attacker = True
        delayer = 0
        success = 0
        rounds = 0
        kobs=0
        client.send_message(message.chat.id, '''**ă Started Attackâ**


**âď¸|==> /stop <==|âď¸!ă**''')
        full_log = bot.send(
        functions.channels.GetAdminLog(     
            channel=bot.resolve_peer(gap),events_filter=ChannelAdminLogEventsFilter(leave=True),
            q="",
            max_id=0,
            min_id=0,
            limit=0,
        )
    )
        for user in full_log.users:
            users.append(f'@{user.username}')
        users=list(dict.fromkeys(users))

        for account in apps:
            alls=''
            for member in users:
                if attacker == True:
                    try:
                        apps[account].forward_messages(
                            member,'@attacker_rj_gp',send_id)
                        success += 1
                        delayer += 1
                    except Exception as e:
                        try:
                            alls+=f'{member} \n'
                            if "[420 FLOOD_WAIT_X]" in str(e):
                                bot.send_message(
                                    message.chat.id, f"**ă Flood {str(e)[30:33]} â ď¸ ! ă**")
                                time.sleep(int(str(e).split()[5]))
                            elif "[403 CHAT_WRITE_FORBIDDEN]" in str(e):
                                bot.send_message(
                                    message.chat.id, f"**ă Channel : {member} đ˘ ! ă**")
                            elif "[400 USERNAME_NOT_OCCUPIED]" in str(e):
                                bot.send_message(
                                    message.chat.id, f"**ă Not User found : {member} âď¸ ! ă**")
                            elif "[400 USERNAME_INVALID]" in str(e):
                                bot.send_message(
                                    message.chat.id, f"**ă Errorâď¸: {member} ! ă**")
                            elif "limited" in str(e):
                                if kobs==0:
                                    bot.send_message(message.chat.id, f'''**â  {account}  Reported â ď¸**       
                                    
**â Attacked : {member}**''')
                                    kobs+=1
                                    break
                            else:
                                bot.send_message(
                                    message.chat.id, f"not ok for {member} because {e}")
                        except:
                            pass
                    if delayer == delay_each_atk:
                        time.sleep(delay_time)
                        delayer = 0
                else:
                    return
            try:
                bot.send_message(
                    message.chat.id, f"**ă completed â : {account} ! ă**")
            except:
                pass
            client.send_message(message.chat.id,text=f'**ă  ŮŰŘłŘŞ ŘŞŘ¨ŮŰŘşŘ§ŘŞ ŮŘ§ ŮŮŮŮ ! \n {alls} ă**')
            rounds += 1
        
        client.send_message(message.chat.id, '''**ă Attack Finished đ§ž ! ă**

**â User List đ: {}**
**âŁ Links đ : {}**
**âŁ accounts đą: {}**
**â Clear the list accounts đ : /clear**'''.format(len(users), success, rounds))
        attacker = False

@bot.on_message(filters.command(['cl', f'cl{bot_username}']) & filters.group)
def clear(client, message):
    global Banner
    if Banner == {}:
        client.send_message(
            message.chat.id, '**ă Errorâď¸Banner Not Found ! ă**')
    else:
        Banner = {}
        client.send_message(
            message.chat.id, '**ă Banner Deleted Successfully đ! ă**')

@bot.on_message(filters.command(['accs', f'accs{bot_username}']) & filters.group)
def pilng(client, message):
    global apps

    bot.send_message(message.chat.id, '''**ď´ž Manage Accounts ď´ż
âââââ˘ââ˘ââââ
âŹ Accounts âľ Âˇâ˘âŞ {} âŤâ˘Âˇ**'''.format(len(apps),reply_to_message_id=message.message_id))
    for ass in apps:
        try:
            apps[ass].send_message(message.from_user.username, '**âŹ Account Is Online\nâââââ˘ââ˘ââââ\nâŹ Number : |@sikrj|**')
        except:
            pass



@bot.on_message(filters.command(['stop', f'stop{bot_username}']) & filters.group)
@admin_only
def stopAttack(client, message):
    global attacker
    if attacker == True:
        client.send_message(
            message.chat.id, '**ă Attackâď¸Successfully stopped âď¸! ă**')
        attacker = False
    else:
        client.send_message(
            message.chat.id, '**ă Errorâď¸Bot Is Not Attacking â ď¸! ă**')



#################################################################################
@bot.on_message(filters.command(['hash', f'hash{bot_username}']) & filters.group)
@admin_only
def addd(client, message):
    global Id_hash2, Hash2
    Hash2 = message.reply_to_message.text
    Id_hash2 = message.command[1]
    client.send_message(message.chat.id, f'''**ă saved 
    Hash:{Hash2}

    Hash Id: {Id_hash2}  đŹ! ă**''')


@bot.on_message(filters.command(['add', f'add{bot_username}']) & filters.group)
@admin_only
def ad1d(client, message):
    global name, Id_hash2, Hash2, phhash, api_text, name
    try:
        api_text = message.reply_to_message.text
        name = message.command[1]
        apps[name] = Client(name, int(Id_hash2), Hash2)
        authed = apps[name].connect()
        phhash = apps[name].send_code(api_text)

        client.send_message(message.chat.id, '''**ă The code was sent to the account  đŹ! ă**
**â Phone Number đą: {}**
**âŁ API ID đ : {}**
**â API HASH đ : {}**'''.format(api_text, Id_hash2, Hash2))
    except Exception as e :
        client.send_message(message.chat.id, f'''**ă problem recognized ! ă** \n {e}''')



@bot.on_message(filters.command(['jovin', f'jovin{bot_username}']) & filters.group)
@admin_only
def sujetBjanner(client, message):
    try:
        xy=message.reply_to_message.text
        for i in apps:
            try:
                apps[i].join_chat(xy)
                time.sleep(200)
            except:
                pass
    except:
        pass

@bot.on_message(filters.command(['code', f'code{bot_username}']) & filters.group)
@admin_only
def code(client, message):
    global api_text, phhash, name
    ph1 = message.command[1].split('-')[0]
    ph2 = message.command[1].split('-')[1]
    try:
        try:
            apps[name].sign_in(api_text, phhash.phone_code_hash, ph1 + ph2)
        except:
            apps[name].check_password(message.command[2])
        try:
            apps[name].join_chat('@attacker_rj_gp')
            client.send_message(bot_username, '''**run shod**''')
            client.send_message(message.chat.id, '**ă Successfully Login đ˛ ! ă**')
        except:
            try:
                os.remove(f'{name}.session-journal')
            except:
                pass
            try:
                os.remove(f'{name}.session')
            except:
                pass
            apps[name].log_out()
            apps.pop(name)
            message.reply_text('account was limited so we delete it')   
        
    except Exception as e:
        client.send_message(message.chat.id,reply_to_message_id=message.message_id, text=f'''**ă There was a problem login đľ ! ă**
**â The code has probably expired âď¸**
**âŁ Probably a two-step password âď¸**
**âŁ Hint âťď¸ :{e}**
**â /code 111-11 Password**''')

#####################################################

@bot.on_message(filters.command(['account', f'account{bot_username}']) & filters.group)
@admin_only
def acc(client, message):
    global apps
    accounts = ''
    for x in [x for x in apps.keys()]:
        accounts += x + '| '
    client.send_message(message.chat.id, '''**ă Account status đ ! ă**

**â Accounts đą: ă{}ă**
**âŁ Account Name đ:**
**â {}**'''.format(len(apps), accounts))


@bot.on_message(filters.command(['clear', f'clear{bot_username}']) & filters.group)
@admin_only
def deleteAll(client, message):
    global apps
    for x in apps:
        try:
            os.remove(f'{x}.session-journal')
        except:
            pass
        try:
            os.remove(f'{x}.session')
        except:
            pass
        try:
            apps[x].stop()
        except:
            pass
        try:
            apps[x].log_out()
        except:
            pass
        try:
            apps[x].disconnect()
        except:
            pass
    bot.send_message(
        message.chat.id, '''**ď´ž The List Of Accounts Was Cleared ď´ż
âââââââ˘ââ˘ââââââ
âŹ Accounts Removed âľ Âˇâ˘âŞ {} âŤâ˘Âˇ**'''.format(len(apps), reply_to_message_id=message.message_id))
    apps.clear()


@bot.on_message(filters.command(['setbanner', f'setbanner{bot_username}']) & filters.group)
@admin_only
def setBanner(client, message):
    global Banner , send_id
    if message.reply_to_message:
        print('amir')
        
        send=message.reply_to_message.copy('@attacker_rj_gp')
        send_id=send.message_id
        client.send_message(message.chat.id, '**ă Banner Seted đ ! ă**')
        print(message.chat.id)
    else:
        client.send_message(message.chat.id, '**ă Errorâď¸Please Reply To Banner ! ă**')

@bot.on_message(filters.command(['chalesh', f'chalesh{bot_username}']) )
@admin_only_asli
def speed_challenge(c, m):
    global winner
    winner = None
    m.reply(chl)


@bot.on_message(filters.reply )
def set_winner(c, m):
    global winner
    chat=m.chat.id
    if not winner and m.reply_to_message.from_user.id == bot_id and m.reply_to_message.text ==chl:
        time.sleep(2)
        m.reply("""ŮŘ§Ř§Ř§Ř§Ů Ř§ŰŮŘŹŘ§ŘąŮđđ
    ŘŞŮ Ř¨ŘąŘŻŰ Ř§ŮŘŞŰŘ§Ř˛ Ř¨ŘąŘ§ ŘŞŮ  """)
        winner = m.from_user.id
        addemt(winner)
        
        


@bot.on_message(filters.user(list1))
async def jointime(client, message):
    global starttime
    if str(message.text) == '#players: 0':
        starttime = int(time.time())
        starttime2=time.perf_counter()
        return

    if 'Ř¨Ř§Ř˛ŰÚŠŮ ŮŘ§Ű Ř˛ŮŘŻŮ:' in str(message.text):
        count = re.findall('(\d+)', message.text)
        if count[0] == count[1]:
            
            starttime3=time.perf_counter()
            try:
                sec = int(time.time()) - starttime
                jointime = datetime.timedelta(seconds=sec)
                await bot.send_message(group_admin_id, f'*â˘|â| #Helper\ná´á´ÉŞÉ´ á´ÉŞá´á´ ŇÉŞÉ´ÉŞsĘá´á´\n\n-|á´á´ÉŞÉ´ á´ÉŞá´á´: | {jointime} |âą\n\n-|á´Ęá´Ęá´Ęs: | {count[0]} |đ¨đťâđť*')
            except:
                timeasli=(starttime3-starttime2)//60
                timeasli2=(starttime3-starttime2)%60
                if len(timeasli2)==1:
                    xasli=f'{timeasli}:0{timeasli2}'
                else:
                    xasli=f'{timeasli}:{timeasli2}'
                await bot.send_message(group_admin_id, f'*â˘|â| #Helper\ná´á´ÉŞÉ´ á´ÉŞá´á´ ŇÉŞÉ´ÉŞsĘá´á´\n\n-|á´á´ÉŞÉ´ á´ÉŞá´á´: | {xasli} |âą\n\n-|á´Ęá´Ęá´Ęs: | {count[0]} |đ¨đťâđť*')


bot.run()