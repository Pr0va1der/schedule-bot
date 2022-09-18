import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests
import time

url = 'http://edu.strbsu.ru/'
bot = telebot.TeleBot("5436162375:AAFqWTmhVdbkBSh53Ju6UdjJTTY7nL_9l-o")
week = 0

print("Бот работает")


@bot.message_handler(commands=['start'])
def hello_user(message):
    text = "Привет. Чтобы выбрать факультет нажми на кнопку."
    keyboard = types.InlineKeyboardMarkup()
    facults = types.InlineKeyboardButton(text="Факультеты", callback_data="facults")
    keyboard.add(facults)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global week
    if call.data == "facult_4_prev_week":
        week -= 1
        text = parse_schedule_week(week, 191)
        keyboard = types.InlineKeyboardMarkup()
        prev_week = types.InlineKeyboardButton(text="Предыдущая", callback_data="facult_4_prev_week")
        next_week = types.InlineKeyboardButton(text="Следующая", callback_data="facult_4_next_week")
        back = types.InlineKeyboardButton(text="Назад", callback_data="facult_4")
        keyboard.add(prev_week, next_week, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
                              reply_markup=keyboard)
        bot.answer_callback_query(callback_query_id=call.id)
    elif call.data == "facult_4_next_week":
        week += 1
        text = parse_schedule_week(week, 191)
        keyboard = types.InlineKeyboardMarkup()
        prev_week = types.InlineKeyboardButton(text="Предыдущая", callback_data="facult_4_prev_week")
        next_week = types.InlineKeyboardButton(text="Следующая", callback_data="facult_4_next_week")
        back = types.InlineKeyboardButton(text="Назад", callback_data="facult_4")
        keyboard.add(prev_week, next_week, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
                              reply_markup=keyboard)
        bot.answer_callback_query(callback_query_id=call.id)
    elif call.data == "facults":
        text = "Факультеты:"
        keyboard = types.InlineKeyboardMarkup()

        facult_4 = types.InlineKeyboardButton(text="Факультет математики и информационных технологий",
                                              callback_data="facult_4")

        keyboard.add(facult_4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
                              reply_markup=keyboard)
    elif call.data == "facult_4":
        keyboard = types.InlineKeyboardMarkup()
        facult_4_group_1 = types.InlineKeyboardButton(text="АИС11", callback_data="facult_4_group_1")
        facult_4_group_2 = types.InlineKeyboardButton(text="МИ11", callback_data="facult_4_group_2")
        facult_4_group_3 = types.InlineKeyboardButton(text="МПМИ11", callback_data="facult_4_group_3")
        facult_4_group_4 = types.InlineKeyboardButton(text="МПМИ12", callback_data="facult_4_group_4")
        facult_4_group_5 = types.InlineKeyboardButton(text="ПИ11", callback_data="facult_4_group_5")
        facult_4_group_6 = types.InlineKeyboardButton(text="ПМИ11", callback_data="facult_4_group_6")
        facult_4_group_7 = types.InlineKeyboardButton(text="АИС21", callback_data="facult_4_group_7")
        facult_4_group_8 = types.InlineKeyboardButton(text="МИ21", callback_data="facult_4_group_8")
        facult_4_group_9 = types.InlineKeyboardButton(text="МПМИ21", callback_data="facult_4_group_9")
        facult_4_group_10 = types.InlineKeyboardButton(text="ПИ21", callback_data="facult_4_group_10")
        facult_4_group_11 = types.InlineKeyboardButton(text="ПМИ21", callback_data="facult_4_group_11")
        facult_4_group_12 = types.InlineKeyboardButton(text="АИС31", callback_data="facult_4_group_12")
        facult_4_group_13 = types.InlineKeyboardButton(text="ИБ31", callback_data="facult_4_group_13")
        facult_4_group_14 = types.InlineKeyboardButton(text="ПИ31", callback_data="facult_4_group_14")
        facult_4_group_15 = types.InlineKeyboardButton(text="ПМИ31", callback_data="facult_4_group_15")
        facult_4_group_16 = types.InlineKeyboardButton(text="АИС41", callback_data="facult_4_group_16")
        facult_4_group_17 = types.InlineKeyboardButton(text="АР41", callback_data="facult_4_group_17")
        facult_4_group_18 = types.InlineKeyboardButton(text="МИ41", callback_data="facult_4_group_18")
        facult_4_group_19 = types.InlineKeyboardButton(text="МФ41", callback_data="facult_4_group_19")
        facult_4_group_20 = types.InlineKeyboardButton(text="ПИ41", callback_data="facult_4_group_20")
        facult_4_group_21 = types.InlineKeyboardButton(text="ПМИ41", callback_data="facult_4_group_21")
        facult_4_group_22 = types.InlineKeyboardButton(text="ПМИ42", callback_data="facult_4_group_22")
        facult_4_group_23 = types.InlineKeyboardButton(text="МИ51", callback_data="facult_4_group_23")
        facult_4_group_24 = types.InlineKeyboardButton(text="OZSИБ11", callback_data="facult_4_group_24")
        facult_4_group_25 = types.InlineKeyboardButton(text="ZSПИ11", callback_data="facult_4_group_25")
        facult_4_group_26 = types.InlineKeyboardButton(text="ZММИ11", callback_data="facult_4_group_26")
        facult_4_group_27 = types.InlineKeyboardButton(text="OZSИБ21", callback_data="facult_4_group_27")
        facult_4_group_28 = types.InlineKeyboardButton(text="OZМПМИ21", callback_data="facult_4_group_28")
        facult_4_group_29 = types.InlineKeyboardButton(text="ZSПИ21", callback_data="facult_4_group_29")
        facult_4_group_30 = types.InlineKeyboardButton(text="ZММИ21", callback_data="facult_4_group_30")
        facult_4_group_31 = types.InlineKeyboardButton(text="ZSПИ31", callback_data="facult_4_group_31")
        facult_4_group_32 = types.InlineKeyboardButton(text="ZПИ31", callback_data="facult_4_group_32")
        facult_4_group_33 = types.InlineKeyboardButton(text="ZИНФ41", callback_data="facult_4_group_33")
        facult_4_group_34 = types.InlineKeyboardButton(text="ZSПИ51", callback_data="facult_4_group_34")
        back = types.InlineKeyboardButton(text="Назад", callback_data="facults")
        keyboard.add(facult_4_group_1, facult_4_group_2, facult_4_group_3, facult_4_group_4, facult_4_group_5,
                     facult_4_group_6, facult_4_group_7, facult_4_group_8, facult_4_group_9, facult_4_group_10,
                     facult_4_group_11, facult_4_group_12, facult_4_group_13, facult_4_group_14, facult_4_group_15,
                     facult_4_group_16, facult_4_group_17, facult_4_group_18, facult_4_group_19, facult_4_group_20,
                     facult_4_group_21, facult_4_group_22, facult_4_group_23, facult_4_group_24, facult_4_group_25,
                     facult_4_group_26, facult_4_group_27, facult_4_group_28, facult_4_group_29, facult_4_group_30,
                     facult_4_group_31, facult_4_group_32, facult_4_group_33, facult_4_group_34, back)
        text = "Группы"
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
                              reply_markup=keyboard)

    elif call.data == "facult_4_group_1":
        facult_4_create_keyboard(call, parse_schedule_week(0, 192))
    elif call.data == "facult_4_group_2":
        facult_4_create_keyboard(call, parse_schedule_week(0, 39))
    elif call.data == "facult_4_group_3":
        facult_4_create_keyboard(call, parse_schedule_week(0, 1892))
    elif call.data == "facult_4_group_4":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10397))
    elif call.data == "facult_4_group_5":
        facult_4_create_keyboard(call, parse_schedule_week(0, 2549))
    elif call.data == "facult_4_group_6":
        facult_4_create_keyboard(call, parse_schedule_week(0, 191))
    elif call.data == "facult_4_group_7":
        facult_4_create_keyboard(call, parse_schedule_week(0, 16))
    elif call.data == "facult_4_group_8":
        facult_4_create_keyboard(call, parse_schedule_week(0, 1834))
    elif call.data == "facult_4_group_9":
        facult_4_create_keyboard(call, parse_schedule_week(0, 2111))
    elif call.data == "facult_4_group_10":
        facult_4_create_keyboard(call, parse_schedule_week(0, 2714))
    elif call.data == "facult_4_group_11":
        facult_4_create_keyboard(call, parse_schedule_week(0, 13))
    elif call.data == "facult_4_group_12":
        facult_4_create_keyboard(call, parse_schedule_week(0, 270))
    elif call.data == "facult_4_group_13":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10392))
    elif call.data == "facult_4_group_14":
        facult_4_create_keyboard(call, parse_schedule_week(0, 9316))
    elif call.data == "facult_4_group_15":
        facult_4_create_keyboard(call, parse_schedule_week(0, 427))
    elif call.data == "facult_4_group_16":
        facult_4_create_keyboard(call, parse_schedule_week(0, 248))
    elif call.data == "facult_4_group_17":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10290))
    elif call.data == "facult_4_group_18":
        facult_4_create_keyboard(call, parse_schedule_week(0, 355))
    elif call.data == "facult_4_group_19":
        facult_4_create_keyboard(call, parse_schedule_week(0, 2548))
    elif call.data == "facult_4_group_20":
        facult_4_create_keyboard(call, parse_schedule_week(0, 2558))
    elif call.data == "facult_4_group_21":
        facult_4_create_keyboard(call, parse_schedule_week(0, 425))
    elif call.data == "facult_4_group_22":
        facult_4_create_keyboard(call, parse_schedule_week(0, 2098))
    elif call.data == "facult_4_group_23":
        facult_4_create_keyboard(call, parse_schedule_week(0, 255))
    elif call.data == "facult_4_group_24":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10360))
    elif call.data == "facult_4_group_25":
        facult_4_create_keyboard(call, parse_schedule_week(0, 9818))
    elif call.data == "facult_4_group_26":
        facult_4_create_keyboard(call, parse_schedule_week(0, 2726))
    elif call.data == "facult_4_group_27":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10396))
    elif call.data == "facult_4_group_28":
        facult_4_create_keyboard(call, parse_schedule_week(0, 9687))
    elif call.data == "facult_4_group_29":
        facult_4_create_keyboard(call, parse_schedule_week(0, 9982))
    elif call.data == "facult_4_group_30":
        facult_4_create_keyboard(call, parse_schedule_week(0, 9325))
    elif call.data == "facult_4_group_31":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10177))
    elif call.data == "facult_4_group_32":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10394))
    elif call.data == "facult_4_group_33":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10393))
    elif call.data == "facult_4_group_34":
        facult_4_create_keyboard(call, parse_schedule_week(0, 10293))



def facult_4_create_keyboard(call, text):
    keyboard = types.InlineKeyboardMarkup()
    prev_week = types.InlineKeyboardButton(text="Предыдущая", callback_data="facult_4_prev_week")
    next_week = types.InlineKeyboardButton(text="Следующая", callback_data="facult_4_next_week")
    back = types.InlineKeyboardButton(text="Назад", callback_data="facult_4")
    keyboard.add(prev_week, next_week, back)
    markdown = """
        *bold text*
        _italic text_
        [text](URL)
        """
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text,
                          reply_markup=keyboard, parse_mode="markdown")


def parse_schedule_week(week, group):
    page = requests.post("http://edu.strbsu.ru/php/getShedule.php", data={'type': '2', 'id': f'{group}', 'week': f'{week}'})
    soup = BeautifulSoup(page.text, "html.parser")
    parse_content = soup.findAll("div", class_="day")
    text = ""
    for element in parse_content:
        day_of_week = element.find("h2", class_="date").text
        html_lessons = element.findAll("li", class_="lesson add_background")
        text += f"{day_of_week}\n"
        for lesson_element in html_lessons:
            number = lesson_element.find("div", class_="number").text
            type = ""
            if str(lesson_element.find("div", class_="type")).count("Пр"):
                type = "Пр"
            elif str(lesson_element.find("div", class_="type")).count("Лек"):
                type = "Лек"
            cab = lesson_element.find("div", class_="cab").text
            time = lesson_element.find("div", class_="time").text
            name = lesson_element.find("div", class_="name").text
            prep = lesson_element.find("div", class_="prep").text
            text += f"*{number} {name} {type} {cab}*\n{prep} {time}\n"
        text += "\n"
    return text


def parse_facults():
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    parse_content = soup.find("ul", class_="menu")
    facults = ""
    content_list = list(parse_content)
    for element in content_list[2:-1]:
        facults += f"{element.text}\n"
    return facults


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        time.sleep(5)
        bot.polling()
    # parse_facults()


