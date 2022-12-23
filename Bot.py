import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import sys
import random
import Hello_ans
import Bye_ans
import Crafts
import Mobs
import requests
import Comms
import TegComms
import Help
import json

TOKEN = input()

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)
upload = vk_api.upload.VkUpload(vk)

commstate = False
needchat = True
page = 0


def send_messages(chat_id, text):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send', {'chat_id': chat_id, 'message': text, 'random_id': random_id})


def send_photos(chat_id, att):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send', {'chat_id': chat_id, 'attachment': att, 'random_id': random_id})


def send_messages_user(chat_id, text):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send', {'user_id': chat_id, 'message': text, 'random_id': random_id})


def send_photos_user(chat_id, att):
    random_id = random.randint(0, 1000000)
    vk.method('messages.send', {'user_id': chat_id, 'attachment': att, 'random_id': random_id})


for event in longpoll.listen():
    print(event.type)
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            text = 'Напиши help'
            if event.from_user:
                msg = event.text
                chat_id = event.user_id

                lmsg = msg.lower().split()

                if 'выход' in lmsg:
                    text = 'Работаю в обычном режиме!'
                    commstate = False

                elif 'крафт' == msg[:5].lower():
                    try:
                        photo = Crafts.crafts[msg[6:]][0]
                        text = Crafts.crafts[msg[6:]][1]
                        send_photos_user(chat_id, photo)
                    except KeyError:
                        text = 'Я не знаю такого крафта :('

                elif 'моб' == msg[:3].lower():
                    try:
                        photo = Mobs.mobs[msg[4:]][0]
                        text = Mobs.mobs[msg[4:]][1]
                        send_photos_user(chat_id, photo)
                    except KeyError:
                        text = 'Я не знаю такого моба :('

                elif 'игровые команды' in msg.lower():
                    text = Comms.bp(page)
                    commstate = True

                elif 'привет' in msg.lower():
                    text = random.choice(Hello_ans.hello)

                elif 'пока' in msg.lower():
                    text = random.choice(Bye_ans.bye)

                elif 'help' in lmsg:
                    text = Help.b

                # COMMSTATE TRUE

                elif commstate == True and msg.isdigit():
                    try:
                        text = TegComms.tc[int(msg) - 1][1]
                    except KeyError:
                        text = 'Выбери существующий номер! Для выхода напиши "!бот выход"'
                    except IndexError:
                        text = 'Выбери существующий номер! Для выхода напиши "!бот выход"'

                elif commstate == True and msg in ['&lt;', '&gt;']:
                    if msg == '&lt;':
                        page = (page - 1) % 3
                        text = Comms.bp(page)
                        commstate = True
                    elif msg == '&gt;':
                        page = (page + 1) % 3
                        text = Comms.bp(page)
                        commstate = True
                send_messages_user(chat_id, text)
            if event.from_chat:
                msg = event.text
                chat_id = event.chat_id

                lmsg = msg.lower().split()

                if msg == '!бот выход':
                    text = 'Работаю в обычном режиме!'
                    commstate = False

                elif '!бот крафт' == msg[:10]:
                    try:
                        photo = Crafts.crafts[msg[11:]][0]
                        text = Crafts.crafts[msg[11:]][1]
                        send_photos(chat_id, photo)
                    except KeyError:
                        text = 'Я не знаю такого крафта :('

                elif '!бот моб' == msg[:8]:
                    try:
                        photo = Mobs.mobs[msg[9:]][0]
                        text = Mobs.mobs[msg[9:]][1]
                        send_photos(chat_id, photo)
                    except KeyError:
                        text = 'Я не знаю такого моба :('

                elif '!бот игровые команды' == msg:
                    text = Comms.bp(page)
                    commstate = True

                elif '!бот привет' in msg.lower():
                    text = random.choice(Hello_ans.hello)

                elif '!бот пока' in msg.lower():
                    text = random.choice(Bye_ans.bye)

                elif msg == 'help':
                    text = Help.a

                # COMMSTATE TRUE

                elif commstate == True and msg.isdigit():
                    try:
                        text = TegComms.tc[int(msg) - 1][1]
                    except KeyError:
                        text = 'Выбери существующий номер! Для выхода напиши "!бот выход"'
                    except IndexError:
                        text = 'Выбери существующий номер! Для выхода напиши "!бот выход"'

                elif commstate == True and msg in ['&lt;', '&gt;']:
                    if msg == '&lt;':
                        page = (page - 1) % 3
                        text = Comms.bp(page)
                        commstate = True
                    elif msg == '&gt;':
                        page = (page + 1) % 3
                        text = Comms.bp(page)
                        commstate = True


                # END COMMSTATE

                else:
                    needchat = False

                if needchat:
                    send_messages(chat_id, text)
                else:
                    needchat = True
