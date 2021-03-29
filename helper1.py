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
ems = ['🦁', '🐯', '🦊', '🦄', '🐝', '🐺', '🦋', '🐞', '🐳', '🐬', '🐼', '🦚', '🎄', '🌲', '🍄', '🍁', '🌷', '🌹', '🌺', '🌸', '🌼', '🌗', '🌓', '🪐', '💫', '⭐️', '✨', '⚡️', '🔥', '🌈', '☃️', '❄️', '🍔', '🍕', '🍓', '🍉', '🍟', '🧁', '🍰', '🍭', '🍬', '🍫', '🍿', '🍩', '🍪', '🥂', '🍸', '🍹', '🧉', '🍾', '⚽️', '🏀', '🏈', '⚾️', '🥎', '🎾', '🎖', '🎗', '🥁', '🎸', '🎺', '🎷', '🏎', '🚀', '✈️', '🚁', '🛸', '🏰', '🗼', '🎡', '🛩', '📱', '💻', '🖥', '💰', '🧨', '💣', '🪓', '💎', '⚱️', '🔮', '🩸', '🦠', '🛎', '🧸', '🎉', '💌', '📯', '❤️', '🧡', '💛', '💚', '💙', '💜', '🖤', '🤍', '🤎', '❣️', '💕', '💞', '💝', '⚜️', '🔱', '📣', '♥️', '😍', '🥰', '🥳', '🤩', '🤪', '👾', '😻', '💋', '👑', '💍', '🎩']
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
chl="""وااااو اینجارو😍😍
هرکی زودتر ریپ بزنه یک امتیاز به تورنومنتش اضافه میشه ⚡️☘️



ببینیم کی برنده میشه🎁🌓"""
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
welcome_text = '**دسته گل محمدی به جمع ما خوش امدی**'
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
    bot.send_message(group_admin_id, text='''**توجـه توجـه 🚷🤫

ادمیـ🧑🏻‍🎓ـن های عزیـز

جویـن تایـ⏰ـم شـروع شـده

لطـفا به گپ مراجعـه کنیـد با تشـکر🌸**''')
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
            message.reply_text(f"**پاکسازی تگ ها انجام شد**")
        except Exception as e:
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @AMIRALIRJPV 』\n {e}**")

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
        message.reply_text('**『 خطا❗️لطفا این دستور را بر روی پیامی ریپلای کنید ! 』**')
 

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
    /start tag                                          شروع تگ

/stop tag                                          توقف تگ

settag [replay]                         تنظیم متن تگ 

speed 0                                  سرعت تگ کردن
speed 0.5 
speed 1
speed 2

admin text[replay]         متن تگ در ساپورت

auto tag on\off تگ در جوین تایم درساپ و گپ 

mydell                        حذف تمام پیام های خود 

del tags                                  پاک کردن تگ ها 

set admin                           افزودن ادمین ربات 

admin list                                لیست ادمین ها 

del admin                               پاک کردن ادمین 

clean adminlist            پاکسازی تمام ادمین ها

del tag on/off            پاک سازی خودکار‌ تگ ها هنگام شروع

mention on                       تگ به صورت منشن 

user on                           تگ به صورت یوزر نیم 

ping              بررسی اتصال ربات و سرعت سرور

/skiboro                               اسپم رای شکارچی 

welcome on/off                    خوش امد گویی

setwel                                     متن خوش امد 

sleep wel [ int ]                    سرعت خوش امد

قفل ساپورت در جوین تایم                   suplock 

on/off

/replaytext              تنظیم متن ریپلای تگ

/replaytag                 رپلای کردن متن مورد نظر

 راهنمای لفتی      /help   **""")




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
                listprint2+=f'{shomare1}-@{j}~ <a href=tg://user?id={i}>LEFTED❗️</a> \n'
                list_left_user.remove(j)
                if shomare1>40:
                    message.reply_text(f"**{listprint2}  \n لیست لفتی ها در چند ساعت گذشته**")
                    listprint2=''
                    shomare1=0
                    time.sleep(2)
                break

            shomare1+=1
        
        time.sleep(2)
        message.reply_text(f"**{listprint2}  \n لیست لفتی ها در 5 ساعت گذشته**")
        
    except Exception as e:
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @AMIRALIRJPV 』\n {e}**")




@bot.on_message(filters.command(['persnext', f'persnext{bot_username}']) & filters.group)
@admin_only_asli
def stamirjcnop(client, message):
    try:
        id=message.reply_to_message.from_user.id
        text=str(message.text)[10:]
        next(id,text)
        message.reply_text(f'ok setted for {id}')
    except:
        message.reply_text('لطفا روی شخص مورد نظر ریپلای کنید ')
        
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
        next_list=[f'دلبـــــــرمون {id} اومده قفلیـــــــــارو زخــــــ😎⚔ــــم کنه','به به ببین کی نکست زده🤤💦💜',f'امیدوارم دست بعد الفا شی ',f'چه نقشی دوس داری دست بعد داشته باشی👀📿',f'نوب الدیـــــــن {id} نکست زده 😂💦 جـــون جـــون',f'پرو پلـــــــــــیرمون {id} اومــده بــــ🤤ــاه بـــــ🤤ــــاه 💦💜',f'قفلیـــــــا برید خونتــــ😎⚔ــــون سلطان {id}👑اومده',f'اوفـــــــــــــ🤤 شکــــــــ💂🏻‍♂️ــــارچی بـــازی بعدیو !']
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
        message.reply_text('ربات را ادمین گروه بکنید')


################################################################bazi#########################################################


@bot.on_message(filters.regex(r'بازی شروع شد') & filters.group & filters.user(list1))
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
            message.reply_text(f"**پاکسازی تگ ها انجام شد**")
        except Exception as e:
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @AMIRALIRJPV 』\n {e}**")
        try:
            if suplock==1:
                
                    bot.set_chat_permissions(group_admin_id,ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_stickers=True,can_send_animations=True))
        except:
            pass

@bot.on_message(filters.regex(r'تعداد بازیکنا به پنج') & filters.group & filters.user(list1))
def stoii88p(client, message):
    global is_tagging
    chat_id = message.chat.id
    if is_tagging[chat_id]:
        is_tagging[chat_id] = False


@bot.on_message(filters.regex(r'چقدر کمین') & filters.group & filters.user(list1))
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
            message.reply_text(f"**پاکسازی تگ ها انجام شد**")
        except Exception as e:
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @AMIRALIRJPV 』\n {e}**")


@bot.on_message(filters.command(['deltags', f'deltags{bot_username}']) & filters.group)
@admin_only
def stopmaman(client, message):
    m=0
    chatid=message.chat.id
    message.reply_text(f"**درحال پاکسازی**")
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
        message.reply_text(f"**پاکسازی {m} تگ انجام شد**")
    except Exception as e:
        message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @AMIRALIRJPV 』\n {e}**")

            
############################################################admin##############################################################

@bot.on_message(filters.regex(r'set sup') & filters.group & filters.user(list1))
def skoonkontop(client, message):
    global group_admin_id
    try:
        group_admin_id=message.reply_to_message.text
        message.reply_text("**setted**")
    except:
        message.reply_text("**『 خطا❗️لطفا این دستور را بر روی پیامی ریپلای کنید ! 』**")


@bot.on_message(filters.regex(r'set here sup') & filters.group & filters.user(list1))
def stjonkonop(client, message):
    global group_admin_id
    group_admin_id=message.chat.id
    message.reply_text("** 『 !تگر ساپورت در این گروه نصب شد 』**")
    


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
    message.reply_text("** 『 !ادمین افزوده شد』**")
    


@bot.on_message(filters.regex(r'del main admin') & filters.group & filters.user(list1))
def stoansagkoonp(client, message):
    global list_admin
    
    a=message.reply_to_message.from_user.id
    try:
        list_admin.remove(a)
        message.reply_text("** 『 !ادمین حذف شد』**")
        
    except:
        message.reply_text("**این یوزر در لیست وجود ندارد **")

    


@bot.on_message(filters.regex(r'add main gap') & filters.group & filters.user(list1))
def silovesarinatop(client, message):
    global gap
    global admin_all
    admin_all=[]
    admin_all.extend(list3)
    admin_all.extend(list1)
    admin_all.extend(list_admin)
    gap=message.chat.id
    message.reply_text("** 『 !اضافه شد **")
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
    message.reply_text("** 『 !اضافه شد **")
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
            message.reply_text(f"**『 خطا❗️به پشتیبانی پیام دهید @AMIRALIRJPV 』\n {e}**")
###############################################################admin 2 ####################################################
@bot.on_message((filters.regex(r'بوس')|(filters.regex(r'یوص')|(filters.regex(r'bos'))) & filters.group  ))
def kisss(client,message):
    try:
        message.reply_text(f"**{message.from_user.mention} Kissed {message.reply_to_message.from_user.mention}**💋")
    except:
        pass
@bot.on_message(filters.regex(r'این کونیه') & filters.group )
def ki7ss(client, message):
    if biadaabi==1:
        koni=random.randint(1,5)
        if koni==1:
            koni_text='**لقب های خود را به دیگران ندهیم **'
        elif koni==2:
            koni_text=f'کونی بودن اثبات شد {message.reply_to_message.from_user.mention} اکنون یه کونی است  '
        elif koni==3:
            koni_text='خیر شهریار کونیه'
        elif koni==4:
            koni_text=f'اقا/خانم{message.reply_to_message.from_user.mention}:تعداد {random.randint(30,10000)} کون دادن در کارنامه ی خود دارند '
        else:
            koni_text=f'ایشون{message.reply_to_message.from_user.mention} توبه کرده و از اخرین کون دادانشون {random.randint(1,12)}ماه میگذرد'
        try:
            message.reply_text(f"**{koni_text}**")
        except:
            pass
@bot.on_message(filters.regex(r'حل') & filters.group )
def k6iss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**{message.from_user.mention}  indirectly told  {message.reply_to_message.from_user.mention} kos amat**🍆🍆🍆")
        except:
            pass
@bot.on_message(filters.regex(r'چشم') & filters.group )
def kiss5(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**{message.reply_to_message.from_user.mention} منظورش این بود سیک کن تا نکردمت **🍆")
        except:
            pass
@bot.on_message(filters.regex(r'\+') & filters.group )
def kishss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**یه مالش {random.randint(60,100)} امتیازی برای {message.reply_to_message.from_user.mention}**")
        except:
            pass
@bot.on_message(filters.regex(r'❤️') & filters.group )
def ki3ss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**{message.from_user.mention} love  {message.reply_to_message.from_user.mention} :)) **")
        except:
            pass
@bot.on_message(filters.regex(r'کوبص') & filters.group )
def kiss2(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**شاید گاهی با یک کوبصد بتوانی مرا خوشحال کنی {message.reply_to_message.from_user.mention} :)**")
        except:
            pass
@bot.on_message(filters.regex(r'میکنمت') & filters.group)
def kiss1(client, message):
    if biadaabi==1:

        bokon=random.randint(0,100)
        if 95>bokon>80:
            koni1_text=f'**شما یکی از مخوف ترین بکنای {message.reply_to_message.from_user.mention} هستید سطح شما بکن سطح 10 است **'
        elif 80>bokon>50:
            koni1_text=f'شما  به عنوان یک بکن سطح {random.randint(1,9)}شناسایی شدید !'
        elif 50>bokon>30:
            koni1_text='تو مگه کیر داری اصلا 😂😂😂😂😂'
        elif 30>bokon>0:
            koni1_text=f'تو یه شب {message.reply_to_message.from_user.mention}  😂😂😂😂😂انگشتت نکنه گریه میکنی بعد میخوای بکنیش؟'
        else:
            koni1_text='شما بکن قهار تمام افراد گروه و کره خاکی هستید '
        try:
            message.reply_text(f"**{koni1_text}**")
        except:
            pass
            pass
@bot.on_message(filters.regex(r'سیک') & filters.group)
def kisss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"* بیا دکمتو بزن🛎 پرواز کنی 🛫  {message.reply_to_message.from_user.mention}**")
        except:
            pass
@bot.on_message(filters.regex(r'ممه') & filters.group)
def kisss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**در انبار فقط کیشمش موجود هست(@Admizad0) بار جدید عید میرسه 🍑.**")
        except:
            pass

@bot.on_message(filters.regex(r'نلیص') & filters.group)
def kisss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**داداش بیا بالا دومین نفس بگیر به فکر زبونت 👅 نیستی به فکر قلبت 🫀باش خونی شد لاپا اون بیچاره 🇯🇵.**")
        except:
            pass


@bot.on_message(filters.regex(r'نمال') & filters.group)
def kisss(client, message):
    if biadaabi==1:
        try:
            message.reply_text(f"**بیا {message.reply_to_message.from_user.mention}  دستکش 🧤، دستات بو گرفت از بس مالیدی**")
        except:
            pass

@bot.on_message(filters.regex(r'بکیرم') & filters.group )
def ki7ss(client, message):
    if biadaabi==1:
        bkiram=random.randint(1,5)
        if bkiram==1:
            bkira_text='**از داشته های خود صحبت کنیم  **'
        elif bkiram==2:
            bkira_text=f' به کیرش دایورت شد {message.reply_to_message.from_user.mention}'
        elif bkiram==3:
            bkira_text='کجات؟😂😂😂'
        elif bkiram==4:
            bkira_text=f'بکصش منظورشه {message.from_user.mention}'
        else:
            bkira_text=f'اقا شهریار @wait_aminute صدات میزنن '
        try:
            message.reply_text(f"**{bkira_text}**")
        except:
            pass

@bot.on_message(filters.regex(r'بخورش') & filters.group)
def kisss(client, message):
    try:
        message.reply_text(f"** king Chocolate ? {message.reply_to_message.from_user.mention}**")
    except:
        pass
@bot.on_message(filters.regex(r'د کینگ') & filters.group  )
def kishehes(client, message):
    try:
        message.reply_text(f"**{message.from_user.mention}   @A_mohamadi_30 soltan sedat mizanan **")
    except:
        pass


@bot.on_message(filters.regex(r'نوب') & filters.group )
def ki7ss(client, message):
    koni=random.randint(1,5)
    if koni==1:
        koni_text='**لقب های خود را به دیگران ندهیم **'
    elif koni==2:
        koni_text=f'نوب  بودن اثبات شد {message.reply_to_message.from_user.mention} اکنون یک نوب  است  '
    elif koni==3:
        koni_text='خیر شهریار کونیه'
    elif koni==4:
        koni_text=f'اقا/خانم{message.reply_to_message.from_user.mention} |  {random.randint(0,100)} درصد نوب است !  '
    else:
        koni_text=f'ایشون{message.reply_to_message.from_user.mention}  اکنون پرو است از نوب بودنشون   {random.randint(1,12)}ماه میگذرد'
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
    message.reply_text(f"**انجام شد**")
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
        message.reply_text("** 『 !ادمین افزوده شد』**")
    else:
        message.rep_text('**『 خطا❗️لطفا این دستور را بر روی پیامی ریپلای کنید ! 』**')
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
        message.reply_text("** 『 !ادمین حذف شد』**")
    except:
        message.reply_text("**این یوزر در لیست وجود ندارد **")

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
    message.reply_text("** 『 !تمامی ادمین ها حذف شدند』**")
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
    bot.send_message(chat_id,f'**𝖎𝖒 𝖔𝖓𝖑𝖎𝖓𝖊! 𝖕𝖎𝖓𝖌:{toc - tic:.4f}**')

    
@bot.on_message(filters.command(['lockstats', f'lockstats{bot_username}']) & filters.group)
@admin_only
def stwemnmrop(client, message):
    global fakebazi
    fakebazi=int(message.command[1])
    message.reply_text(f"**ok setted {fakebazi}**")


####################################################################suplock##################################################################################

@bot.on_message(filters.regex(r'دکمه زیر')  & ~filters.regex(r'مشاهده')  & filters.group & filters.user([854021534,175844556]))
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
@bot.on_message(filters.group &  (filters.regex(r'#شکارم')| filters.regex(r'#ch')|filters.regex(r'شکار#')  & filters.group & ~filters.me & ~filters.user([854021534,1289410047,1181120160,1653256635,1538900423])))
@ban_from_bot
def sto1118811p(client, message):
    global shekar
    if str(message.text) in ['#شکارم','#ch','شکار#']:
        shekar=message.from_user.id
        try:
            
            message.pin()
        except:
            pass
        message.reply_text('**📌شکارچی شناسایی شد :)**')
        message.reply_text('**برای اسپم رایتون از /ray استفاده کنید و جلوی ان  رایتون رو بنویسید **')


@bot.on_message(filters.regex(r'#ناظر')|filters.regex(r'#مکمل_شکار')  & filters.group & ~filters.me & ~filters.user([854021534,1289410047,1181120160,1653256635,1538900423]))
@ban_from_bot
def sto777221p(client, message):
    global nazer
    if str(message.text) in ['#ناظر','#مکمل_شکار#']:
        nazer=message.from_user.id
        try:
            message.pin()
        except:
            pass
        message.reply_text('**📌ناظر شناسایی شد :)**')
        message.reply_text('**برای اسپم رایتون از /ray استفاده کنید و جلوی ان  رایتون رو بنویسید **')



@bot.on_message(filters.command(['ray', f'ray{bot_username}']) & filters.group & ~filters.me & ~filters.user([854021534,1289410047,1181120160,1410445908,1653256635]))
@ban_from_bot
def st11000011o1p(client, message):
    global shekar
    chat_id1=message.chat.id
    if shekar==message.from_user.id:
        ski_shekar =message.command[1]
        if ski_shekar!='':
            
            for i in range(1,10):
                bot.send_message(chat_id1,text=f'''⚜️رای شکارچی』


            🔰  **{ski_shekar}** 🔰 『 ''' )
                time.sleep(5)
        else:
            message.reply_text('متن رای را جلوی /ray بنویسید📌』')
    else:
        message.reply_text('『شما شکارچی بازی نیستید📌』')




@bot.on_message(filters.command(['nray', f'nray{bot_username}']) & filters.group & ~filters.me & ~filters.user([854021534,1289410047,1181120160,1410445908,1653256635]))
@ban_from_bot
def s000to1p(client, message):
    global nazer
    
    chat_id1=message.chat.id
    if nazer==message.from_user.id:
        nazer_ski = message.command[1]
        if nazer_ski!='':
            for i in range(1,12):
                bot.send_message(chat_id1,text=f'''⚜️رای ناظر ⚜️


            🔰  **{nazer_ski}** 🔰 『 ''' )
                time.sleep(5)
        else:
            message.reply_text('متن رای را جلوی /ray بنویسید📌』')
    else:
        message.reply_text('『شما ناظر بازی نیستید📌』')
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
        **『Onyx Account state 📊 ! 』**
        
    **┏ total games   📱:『{totalgame}』**
    **┣ Account Name 📋: {mention1}**
    **┣ First Game : {man["TheFirstGame"]} **
    **┣ Survived Games : {man['SurviveTheGame']}**
    **┣ Most Kills : {man['YouKillName']} {man['killMeUserCount']} times**
    **┣ most killed by : {man['killMeName']}
    **┣ Status : {man["status"]}
    **┗ {user.id}**''')
    except :
        try:
             message.reply_text(f'''**『Onyx Account state 📊 ! 』**

    **┏ total games 📱: 『{totalgame}』**
    **┣ Account Name 📋: {mention1}**
    **┗ {user.id}**''')
        except:
            message.reply_text(f'''『 این بازیکن استیتی ندارد ! 』**''')

            
            
#{'status': True, 'error': '', 'fullname': 'Sly ', 'user_id': 1347350135, 'total_game': 372, 'SurviveTheGame': 79, 'SlaveGames': 145
#, 'LoserGames': 227, 'lang_code': 'en', 'username': 'sly12919', 'ActivePhone': '', 'killMeName': 'Mbina  ', 'killMeUserID': 775547629, 'killMeUserCount': 21, 'YouKillName': '𝕸𝖊𝖔𝖜  ', 


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
            message.reply_text(f'''**『Onyx Account state 📊 ! 』**

    **┏ total games 📱: 『{totalgame}』**
    **┣ Account Name 📋:{mention1}**
    **┗ {user.id}**''')
        except:
            mention1=mention(user.id,user.first_name)
            totalgame=0
            bot.send_message(group_admin_id,f'#new \n \nکاربر {mention1}  بدون استیت وارد گپ شده  با ایدی {user.username}')
            message.reply_text(f'''『 این بازیکن استیتی ندارد  ! 』**''')
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

helpMSG = '''**『 سلام به بخش راهنمای بات لفتی خوش آمدید 🖐🏻  ! 』**

**🔺 『 نحوه ثبت اکانت 📲! 』 **
**『 دستور /add : این دستور را باید بر روی پیامی از @UseTGXbot  ریپلای کنید و جلوی دستور نام اکانت را بزنید !』**
مثال** : **
**/add Name**
**/delacc Name 
**『 دستور /code : این دستور برای وارد کردن کد ورود است ! 』**
مثال** :**
**/code code tel | password**
**/code 111-11 1234**
**➖➖➖➖➖**
**🔺 『 بخش تنظیم سرعت ⏱! 』 **
**『 دستور /setspeed : این دستور برای تنظیم سرعت لفتی  استفاده میشود! 』**
مثال** :**
**/setspeed 2 4**
**『 دستور /speed : مشاهده سرعت فعلی ربات ! 』  **
**➖➖➖➖➖**
**🔺 『 مشاهده اکانت ها 📊! 』 **
**『 دستور /account : آمار کلی اکانت ها ! 』 **
**『 دستور /ping مشاهده اکانت ها ! 』 **
**➖➖➖➖➖**
** 🔺 『 بخش بنر 📄 ! 』 **
**『 دستور /setbanner : این پیام را بر روی بنرتان بفرستید تا ثبت شود ! 』 **
**『 دستور /banner : مشاهده بنر فعلی ! 』 **
**➖➖➖➖➖**
**/golefties          رفتن به پیوی لفتی های گپ **

**                  『 Dev : ||||||| @AMIRALIRJPV ||||||| 
                        |~~~~~~~~ @AMIRALIRJPV ~~~~~~~| 
                            @parsa_rus  💂🏻‍♂️ 』** 
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
            message.chat.id, '**『 Please Set The Banner 📍📄 !』**')
    else:
        attacker = True
        delayer = 0
        success = 0
        rounds = 0
        kobs=0
        client.send_message(message.chat.id, '''**『 Started Attack✅**


**⛔️|==> /stop <==|⛔️!』**''')
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
                                    message.chat.id, f"**『 Flood {str(e)[30:33]} ⚠️ ! 』**")
                                time.sleep(int(str(e).split()[5]))
                            elif "[403 CHAT_WRITE_FORBIDDEN]" in str(e):
                                bot.send_message(
                                    message.chat.id, f"**『 Channel : {member} 📢 ! 』**")
                            elif "[400 USERNAME_NOT_OCCUPIED]" in str(e):
                                bot.send_message(
                                    message.chat.id, f"**『 Not User found : {member} ⁉️ ! 』**")
                            elif "[400 USERNAME_INVALID]" in str(e):
                                bot.send_message(
                                    message.chat.id, f"**『 Error❗️: {member} ! 』**")
                            elif "limited" in str(e):
                                if kobs==0:
                                    bot.send_message(message.chat.id, f'''**┏  {account}  Reported ⚠️**       
                                    
**┗ Attacked : {member}**''')
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
                    message.chat.id, f"**『 completed ✅ : {account} ! 』**")
            except:
                pass
            client.send_message(message.chat.id,text=f'**『  لیست تبلیغات نا موفق ! \n {alls} 』**')
            rounds += 1
        
        client.send_message(message.chat.id, '''**『 Attack Finished 🧾 ! 』**

**┏ User List 📄: {}**
**┣ Links 🔗 : {}**
**┣ accounts 📱: {}**
**┗ Clear the list accounts 🗑 : /clear**'''.format(len(users), success, rounds))
        attacker = False

@bot.on_message(filters.command(['cl', f'cl{bot_username}']) & filters.group)
def clear(client, message):
    global Banner
    if Banner == {}:
        client.send_message(
            message.chat.id, '**『 Error❗️Banner Not Found ! 』**')
    else:
        Banner = {}
        client.send_message(
            message.chat.id, '**『 Banner Deleted Successfully 🗑! 』**')

@bot.on_message(filters.command(['accs', f'accs{bot_username}']) & filters.group)
def pilng(client, message):
    global apps

    bot.send_message(message.chat.id, '''**﴾ Manage Accounts ﴿
━━━━•◈•━━━━
⌬ Accounts ➵ ·•❪ {} ❫•·**'''.format(len(apps),reply_to_message_id=message.message_id))
    for ass in apps:
        try:
            apps[ass].send_message(message.from_user.username, '**⌬ Account Is Online\n━━━━•◈•━━━━\n⌬ Number : |@sikrj|**')
        except:
            pass



@bot.on_message(filters.command(['stop', f'stop{bot_username}']) & filters.group)
@admin_only
def stopAttack(client, message):
    global attacker
    if attacker == True:
        client.send_message(
            message.chat.id, '**『 Attack❗️Successfully stopped ⛔️! 』**')
        attacker = False
    else:
        client.send_message(
            message.chat.id, '**『 Error❗️Bot Is Not Attacking ⚠️! 』**')



#################################################################################
@bot.on_message(filters.command(['hash', f'hash{bot_username}']) & filters.group)
@admin_only
def addd(client, message):
    global Id_hash2, Hash2
    Hash2 = message.reply_to_message.text
    Id_hash2 = message.command[1]
    client.send_message(message.chat.id, f'''**『 saved 
    Hash:{Hash2}

    Hash Id: {Id_hash2}  📬! 』**''')


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

        client.send_message(message.chat.id, '''**『 The code was sent to the account  📬! 』**
**┏ Phone Number 📱: {}**
**┣ API ID 🔖 : {}**
**┗ API HASH 📋 : {}**'''.format(api_text, Id_hash2, Hash2))
    except Exception as e :
        client.send_message(message.chat.id, f'''**『 problem recognized ! 』** \n {e}''')



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
            client.send_message(message.chat.id, '**『 Successfully Login 📲 ! 』**')
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
        client.send_message(message.chat.id,reply_to_message_id=message.message_id, text=f'''**『 There was a problem login 📵 ! 』**
**┏ The code has probably expired ❗️**
**┣ Probably a two-step password ❗️**
**┣ Hint ♻️ :{e}**
**┗ /code 111-11 Password**''')

#####################################################

@bot.on_message(filters.command(['account', f'account{bot_username}']) & filters.group)
@admin_only
def acc(client, message):
    global apps
    accounts = ''
    for x in [x for x in apps.keys()]:
        accounts += x + '| '
    client.send_message(message.chat.id, '''**『 Account status 📊 ! 』**

**┏ Accounts 📱: 『{}』**
**┣ Account Name 📋:**
**┗ {}**'''.format(len(apps), accounts))


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
        message.chat.id, '''**﴾ The List Of Accounts Was Cleared ﴿
━━━━━━•◈•━━━━━━
⌬ Accounts Removed ➵ ·•❪ {} ❫•·**'''.format(len(apps), reply_to_message_id=message.message_id))
    apps.clear()


@bot.on_message(filters.command(['setbanner', f'setbanner{bot_username}']) & filters.group)
@admin_only
def setBanner(client, message):
    global Banner , send_id
    if message.reply_to_message:
        print('amir')
        
        send=message.reply_to_message.copy('@attacker_rj_gp')
        send_id=send.message_id
        client.send_message(message.chat.id, '**『 Banner Seted 📄 ! 』**')
        print(message.chat.id)
    else:
        client.send_message(message.chat.id, '**『 Error❗️Please Reply To Banner ! 』**')

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
        m.reply("""وااااو اینجارو😍😍
    تو بردی امتیاز برا تو  """)
        winner = m.from_user.id
        addemt(winner)
        
        


@bot.on_message(filters.user(list1))
async def jointime(client, message):
    global starttime
    if str(message.text) == '#players: 0':
        starttime = int(time.time())
        starttime2=time.perf_counter()
        return

    if 'بازیکن های زنده:' in str(message.text):
        count = re.findall('(\d+)', message.text)
        if count[0] == count[1]:
            
            starttime3=time.perf_counter()
            try:
                sec = int(time.time()) - starttime
                jointime = datetime.timedelta(seconds=sec)
                await bot.send_message(group_admin_id, f'*•|⛑| #Helper\nᴊᴏɪɴ ᴛɪᴍᴇ ғɪɴɪsʜᴇᴅ\n\n-|ᴊᴏɪɴ ᴛɪᴍᴇ: | {jointime} |⏱\n\n-|ᴘʟᴀʏᴇʀs: | {count[0]} |👨🏻‍💻*')
            except:
                timeasli=(starttime3-starttime2)//60
                timeasli2=(starttime3-starttime2)%60
                if len(timeasli2)==1:
                    xasli=f'{timeasli}:0{timeasli2}'
                else:
                    xasli=f'{timeasli}:{timeasli2}'
                await bot.send_message(group_admin_id, f'*•|⛑| #Helper\nᴊᴏɪɴ ᴛɪᴍᴇ ғɪɴɪsʜᴇᴅ\n\n-|ᴊᴏɪɴ ᴛɪᴍᴇ: | {xasli} |⏱\n\n-|ᴘʟᴀʏᴇʀs: | {count[0]} |👨🏻‍💻*')


bot.run()