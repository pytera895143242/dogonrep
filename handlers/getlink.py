from aiogram import types
from misc import dp,bot
from handlers.array_otvetki import array_post
import random
media_chat_id = -1001788899092

link0 = -1001167128067 #Сок
link1 = -1001653876311 #Эстетика
link2 = -1001734017178 #Твои подруги
link3 = -1001716243032 #ПОРНО 24/7
link4 = -1001701960941 #Архивы фуллов
link5 = -1001681795382 #Твои студентки
link6 = -1001518943323 #Домашка
link7 = -1001473420511 #Адская Дрочильня
chat_id = [link0,link1,link2,link3,link4,link5,link6,link7]

async def postink_post(link):
    for id in chat_id:
        text = (array_post[random.randint(0, len(array_post) - 1)]).format(link)
        post_num = random.randint(27,47)
        await bot.copy_message(chat_id= id,from_chat_id=media_chat_id,message_id=post_num,caption=text)



async def get_links():
    from pyrogram import Client
    import re
    app = Client('my_accounts')
    my_id = 1045832338
    urls = []

    @app.on_message()
    async def payments (client,message):
        if message.chat.id == -1001706149219 and message.media != None:
            """Проверяем на наличие гипер-ссылок"""
            if message.caption_entities != None:
                for link in message.caption_entities:
                    if link.url != None:
                        if link.url[0:8] == 'https://':
                            urls.append(link.url[8:])
                        elif link.url[0:7] == 'http://':
                            urls.append(link.url[7:])
                        else:
                            urls.append(link.url)


            try:
                link = (re.findall("(?P<url>https?://[^\s]+)", message.caption))
                for i in link:
                    urls.append(i[8:])

            except:
                pass


            try:
                link = (re.findall("(?P<url>t.me/[^\s]+)", message.caption))
                for i in link:
                    urls.append(i)
            except:
                pass

            if message.reply_markup != None:
                for link in message.reply_markup.inline_keyboard:
                    if link[0].url != None:
                        if link[0].url[0:8] == 'https://':
                            urls.append(link[0].url[8:])
                        elif link[0].url[0:7] == 'http://':
                            urls.append(link[0].url[7:])
                        else:
                            urls.append(link[0].url)

            print("Поиск ссылок завершен")
            ready_urls = (list(set(urls)))
            await postink_post(ready_urls[0])



    await app.start()