import requests
import telebot
import markdown
import pyowm
import random
import time
# from datetime import datetime
from datetime import datetime, timedelta
# import timedelta
import mysql.connector

# для обработки xlsx
from openpyxl import load_workbook

bot = telebot.TeleBot("5125341770:AAF11nLzMCoeFV-gf96iL19hDyhOfidqo7g")

#
# from pyowm import OWM
# owm = OWM('a58cd71e6d3057b4ce76c3da27076585')
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place('Москва')
# w = observation.weather
# print(w, w.wind())



@bot.message_handler(content_types=['text'])

def send_echo(message):
    #    if message.text == "/pogoda":
    #        print('/pogoda Start')
    # owm = OWM('a58cd71e6d3057b4ce76c3da27076585')
    # mgr = owm.weather_manager()
    # делим строку для дальнейше обработки
    inCommingSTR = message.text
    if "@" in inCommingSTR:
        commandStr = inCommingSTR.split("@")
        commandStr = commandStr[0]
        chatStr = commandStr[1]
    else: commandStr = inCommingSTR

    # print(commandStr)
    dateStr = False
    if " " in commandStr:
         commandStrTemp = commandStr.split(" ")
         # print(commandStr[0] + " hui " + commandStr[1])
         if commandStrTemp[0] == "/smena":
             commandStr = commandStrTemp[0]
             dateStr = str(commandStrTemp[1])
             # print(str(commandStr) + " :: " + str(dateStr) + " hui " + str(len(dateStr)) )
         else:
             commandStr = commandStr[0]
             dateStr = False


    # print(commandStr)
    # print(len(dateStr))

    if commandStr == "/pogoda":
        owm = pyowm.OWM('a58cd71e6d3057b4ce76c3da27076585')
        ob = owm.weather_at_place('Салехард, RU')
        w = ob.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        wind = w.get_wind()["speed"]
        windGust = w.get_wind()["gust"]
        pressure = w.get_pressure()["press"] * 0.750063755419211  # / 1.333
        answerMess = "В Салехарде сейчас:\n\nтемепература: " + str(temp) + "°С\nветер: " + str(
            wind) + " м/с\nпорывы до: " + str(windGust) + " м/с\nдавление: " + str(round(pressure, 1)) + " mmHg"
        # bot.send_message(message.chat.id, answerMess)

        ###########################
        ### https://wttr.in/:help?lang=ru
        # url = 'https://wttr.in'  # не изменяйте значение URL
        #
        # weather_parameters = {
        #     '0': '',
        #     'format': 4,
        #     'T': '',
        #     'M': '',
        #     'm': '',
        #     'P': 'hPa',
        #     'lang': 'ru',
        #     # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
        # }
        #
        # response = requests.get(url + '/Салехард', params=weather_parameters)  # передайте параметры в http-запрос
        # answerMess += '\n\nИз альтернативного источника:\n'
        # answerMess += str(response.text)
        # print(response.text)
        cities = [
            'Салехард',
            'Лабытнанги',
            'Тюмень',
            'Омск',
            'Екатеринбург',
            'Рио'
        ]
        def make_url(city):
            # в URL задаём город, в котором узнаем погоду
            return f'http://wttr.in/{city}'


        def make_parameters():
            params = {
                '0': '',
                'format': 4,
                'T': '',
                'M': '',
                'm': '',
                'P': 'hPa',
                'lang': 'ru',
            }
            return params

        def what_weather(city):
            try:
                url = make_url(city)
                www = requests.get(url + '?P', params=make_parameters())
                return www.text
            except e:
                return '<сетевая ошибка>'

        def what_weather(city):
            # Напишите тело этой функции.
            # Не изменяйте остальной код!
            try:
                url = make_url(city)
                www = requests.get(url, params=make_parameters())
                return www.text
            except e:
                return '<сетевая ошибка>'

        answerMess += '\n\nИз альтернативного источника:\n'
        for city in cities:
            answerMess += what_weather(city)
        # print('Погода в городах:')


        ###########################

        bot.send_message(message.chat.id, answerMess)

    elif commandStr == "/smena":
        if dateStr == False:
            dateToday = datetime.now()
            # print(dateToday)
            dayToday = dateToday.today().strftime('%d')  # '%d/%m/%Y'
            dateToday = dateToday.today().strftime('%d.%m.%Y')
            # dayToday = int(dayToday) * 1 #убираем 0
            dateTommorow = datetime.today() + timedelta(days=1)
            dateTommorow = dateTommorow.strftime('%d.%m.%Y')

            answerLineDateToday = "Сегодня " + dateToday + " на смене:"
            answerLineDateTommorow = "\n\nЗавтра " + dateTommorow + " на смене: "
        else:
            # if re.match(r’\d{1,2}\.\d{1,2}\.\d{2,4}$’, dateStr):
            dateToday = dateStr
            dateToday = datetime.strptime(dateToday, '%d.%m.%Y')
            dateTommorow = dateToday.date() + timedelta(days=1)
            dateTommorow = dateTommorow.strftime('%d.%m.%Y')
            dateToday = dateToday.strftime('%d.%m.%Y')

            answerLineDateToday = "*" + dateToday + "* на смене:"
            answerLineDateTommorow = "\n\n*" + dateTommorow + "* на смене: "

        # answerMess = "Техники РН, РЛ и связи:\n"
        # answerMess += "Сегодня " + dateToday + " на смене:"
        # wb = load_workbook('tech.xlsx')
        # sheet = wb.get_sheet_by_name('Апрель')
        def getInfoSmena(dateInfo, dolgnost, smena):
            ddmmYYYY = dateInfo.split(".")
            dd = int(ddmmYYYY[0]) * 1
            mm = int(ddmmYYYY[1]) * 1
            massMonth = ["", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь",
                         "Октябрь", "Ноябрь", "Декабрь"]
            if dolgnost == 'tech':
                wb = load_workbook('tech.xlsx')  # подключаем файл график техников
            if dolgnost == 'ing':
                wb = load_workbook('ing.xlsx')  # подключаем файл график техников
            sheet = wb.get_sheet_by_name(massMonth[mm])
            for i in range(15, 32):
                if sheet.cell(row=i, column=dd + 1).value is not None:
                    workDay = sheet.cell(row=i, column=dd + 1).value
                    if str(smena) == str(workDay):
                        fio = sheet.cell(row = i - 1, column = 1).value
                        fio = fio.replace('.','. ')
                        return fio
                        # return sheet.cell(row=i - 1, column=1).value



        answerMess = "Техники РН, РЛ и связи:\n"
        # answerMess += "Сегодня " + dateToday + " на смене:" + dateStr
        answerMess += answerLineDateToday
        answerMess += "\nC ночи: " + getInfoSmena(dateToday, "tech", "8.5")
        answerMess += "\nВ день: " + getInfoSmena(dateToday, "tech", "12")
        answerMess += "\nВ ночь: " + getInfoSmena(dateToday, "tech", "3.5")

        # answerMess += "\n\nЗавтра " + dateTommorow + " на смене: "
        answerMess += answerLineDateTommorow
        answerMess += "\nC ночи: " + getInfoSmena(dateTommorow, "tech", "8.5")
        answerMess += "\nВ день: " + getInfoSmena(dateTommorow, "tech", "12")
        answerMess += "\nВ ночь: " + getInfoSmena(dateTommorow, "tech", "3.5")

        answerMess += "\n\nСменные:\n"
        # answerMess += "Сегодня " + dateToday + " на смене:"
        answerMess += answerLineDateToday
        answerMess += "\nC ночи: " + getInfoSmena(dateToday, "ing", "8.5")
        answerMess += "\nВ день: " + getInfoSmena(dateToday, "ing", "12")
        answerMess += "\nВ ночь: " + getInfoSmena(dateToday, "ing", "3.5")

        # answerMess += "\n\nЗавтра " + dateTommorow + " на смене: "
        answerMess += answerLineDateTommorow
        answerMess += "\nC ночи: " + getInfoSmena(dateTommorow, "ing", "8.5")
        answerMess += "\nВ день: " + getInfoSmena(dateTommorow, "ing", "12")
        answerMess += "\nВ ночь: " + getInfoSmena(dateTommorow, "ing", "3.5")

        # answerMess = markdown.markdown(answerMess)
        bot.send_message(message.chat.id, answerMess,  parse_mode="markdown")
        # bot.send_message(message.from_user.id, answerMess)
    elif commandStr == "/plan":
        dateToday = datetime.now()
        dayToday = dateToday.today().strftime('%Y-%m-%d')  # '%d/%m/%Y' 2022-04-01
        dayToday = dateToday.today().strftime('%Y-%m-%d')  # '%d/%m/%Y' 2022-04-01
        yearNow = dateToday.today().strftime('%Y')  # '%d/%m/%Y' 2022-04-01
        dayNumToday = dateToday.today().strftime('%w')
        try:
            connection = mysql.connector.connect(host='10.152.36.10',
                                                 database='arm_vdo',
                                                 user='root',
                                                 password='3333')

            answerMess = "План работ на " + dayToday + ": \n"
            ## TO2
            sql_select_Query = 'SELECT concat(ob.vidTO, " ", nameOb.name, " №", nameOb.numZav ) FROM arm_vdo.grafTO_planTO as ob Left JOIN arm_vdo.grafTO_oborudovanie as nameOb ON ob.idSred = nameOb.id where yearTO = "' + yearNow + '" and vidTO = "TO2" and dayTO = "' + dayNumToday + '" and nameOb.active = 1 '

            # sql_select_TO2 = 'SELECT concat(ob.vidTO, " ", nameOb.name) FROM arm_vdo.grafTO_planTO as ob Left JOIN arm_vdo.grafTO_oborudovanie as nameOb ON ob.idSred = nameOb.id where yearTO = "' + yearNow + '" and ob.dayTO = "' + dayNumToday + '" and vidTO = "TO2" '
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            for row in records:
                # print(row[0])
                answerMess += row[0] + '\n'
            # answerMess = answerMess.replace('&quot;','"')
            ## TO3-TO6
            sql_select_Query = 'SELECT concat(ob.vidTO, " ", nameOb.name, " №", nameOb.numZav) FROM arm_vdo.grafTO_planTO as ob Left JOIN arm_vdo.grafTO_oborudovanie as nameOb ON ob.idSred = nameOb.id where yearTO = "' + yearNow + '" and datePlanTO = "' + dayToday + '"'
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            for row in records:
                # print(row[0])
                answerMess += row[0] + '\n'
            answerMess = answerMess.replace('&quot;', '"')
        except mysql.connector.Error as e:
            print("Error reading data from MySQL table", e)
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
        # bot.send_message(message.chat.id, answerMess)
        bot.send_message(message.chat.id, answerMess)
    elif commandStr == "/zarplata":
        objects = ["Ццццц!!!", "Несссссссыыыыыы, она будет!!", "Опять ты",
                   "Может поработаем лучше, чем в телефоне залипать!", "Какая нахрен тебе зарплата! Работай давай!!!",
                   "Хули ты ноешь!! Иди трудись!!!", "Еще раз спросишь передам куда надо!!!", "Вот ты зануда",
                   "И чего с ней не так"]
        answerMess = objects[random.randint(0, len(objects)) - 1]
        bot.send_message(message.chat.id, answerMess)
    elif commandStr == "/buhat":
        objects = ["Время? Место?", 'Сегодня, '+message.from_user.first_name+', на твои', "Только по пятницам", "Отличный вариант!!", "Пиво пиво водочка",
                   "Может в другой раз", "ЗОЖ наше все"]
        answerMess = objects[random.randint(0, len(objects)) - 1]
        bot.send_message(message.chat.id, answerMess)
    elif commandStr == "/help":
        answerMess = "Информация по боту:"
        answerMess += "\n/smena - вывод информации по смене"
        answerMess += "\n/plan - план ТО на день"
        answerMess += "\n/pogoda - информация о погоде на текущее время по городу Салехард"
        bot.send_message(message.chat.id, answerMess)


# else:
#     bot.send_message(message.chat.id, message.text)
#     print(message.text)


# bot.polling( none_stop = True )
# https://ru.stackoverflow.com/questions/711998/%D0%9D%D0%B5%D0%B4%D0%BE%D1%81%D1%82%D0%B0%D1%82%D0%BE%D0%BA-bot-polling
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        # logger.error(e)  # или просто print(e) если у вас логгера нет,
        print(e)
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
