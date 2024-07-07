import telebot
from telebot import types
points=0
objects = []
with open(r"base.txt","r") as f:
    for line in f:
        name,surname = map(str,line.split())
        objects.append(name, surname)
bot = telebot.TeleBot("")
@bot.message_handler(content_types=["text"])
def start(message):
    if message.text == "/start":
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton('Начать')
        markup.add(btn1)
        bot.send_message(message.from_user.id,'Здравствуйте, это викторина. Начать?'.format(message.from_user), reply_markup=markup)
    if message.text =='Начать':
        bot.send_message(message.from_user.id,'Как тебя зовут?')
        bot.register_next_step_handler(message, get_surname)
def get_surname(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id,'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, q1)
def q1(message):
    global surname
    surname = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) str")
    btn2 = types.KeyboardButton("(b) int")
    btn3 = types.KeyboardButton("(c) float")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Какой тип данных используется для хранения целых чисел в Python?', reply_markup=markup)

    bot.register_next_step_handler(message, q2)
def q2(message):
    if message.text =="(b) int":
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) =")
    btn2 = types.KeyboardButton("(b) ==")
    btn3 = types.KeyboardButton("(c) :")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Какой символ используется для присваивания значения переменной?', reply_markup=markup)

    bot.register_next_step_handler(message, q3)
def q3(message):
    if message.text == '(a) =':
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) Hello")
    btn2 = types.KeyboardButton("(b) World")
    btn3 = types.KeyboardButton("(c) HelloWorld")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Каков будет результат выполнения следующего кода: print("Hello" + "World")?', reply_markup=markup)

    bot.register_next_step_handler(message, q4)
def q4(message):
    if message.text == '(c) HelloWorld':
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a)  Используя фигурные скобки {}")
    btn2 = types.KeyboardButton("(b) Используя квадратные скобки []")
    btn3 = types.KeyboardButton("(c) Используя круглые скобки ()")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Как создать список в Python?', reply_markup=markup)

    bot.register_next_step_handler(message, q5)
def q5(message):
    if message.text == '(b) Используя квадратные скобки []':
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) func")
    btn2 = types.KeyboardButton("(b) def")
    btn3 = types.KeyboardButton('(c) define')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Какое ключевое слово используется для определения функции в Python?', reply_markup=markup)

    bot.register_next_step_handler(message, q6)
def q6(message):
    if message.text == '(b) def':
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) Повторить блок кода определенное количество раз")
    btn2 = types.KeyboardButton("(b) Выполнить блок кода, только если выполняется определенное условие")
    btn3 = types.KeyboardButton("(c) Вывести сообщение на консоль")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Какова цель оператора "if" в Python?', reply_markup=markup)

    bot.register_next_step_handler(message, q7)
def q7(message):
    if message.text == '(b) Выполнить блок кода, только если выполняется определенное условие':
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) 5")
    btn2 = types.KeyboardButton("(b) 6")
    btn3 = types.KeyboardButton("(c) Python")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Каков будет результат выполнения следующего кода: print(len("Python"))?', reply_markup=markup)

    bot.register_next_step_handler(message, q8)
def q8(message):
    if message.text == '(b) 6':
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) Файл, содержащий код Python, который можно импортировать и использовать в других программах")
    btn2 = types.KeyboardButton("(b) Переменная, которая хранит набор данных")
    btn3 = types.KeyboardButton("(c) Тип цикла, который перебирает последовательность значений")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Что такое модуль в Python?', reply_markup=markup)

    bot.register_next_step_handler(message, q9)
def q9(message):
    if message.text == '(a) Файл, содержащий код Python, который можно импортировать и использовать в других программах':
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) Списки упорядочены, а кортежи не упорядочены")
    btn2 = types.KeyboardButton("(b) Списки изменяемы, а кортежи неизменяемы")
    btn3 = types.KeyboardButton("(c) Списки используют квадратные скобки, а кортежи используют круглые скобки")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' В чем разница между списком и кортежем?', reply_markup=markup)

    bot.register_next_step_handler(message, q10)
def q10(message):
    if message.text == '(b) Списки изменяемы, а кортежи неизменяемы':
        global points
        points +=1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("(a) Вывести сообщение на консоль")
    btn2 = types.KeyboardButton("(b) Получить пользовательский ввод с клавиатуры")
    btn3 = types.KeyboardButton("(c) Преобразовать строку в целое число")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,' Какова цель функции input()?', reply_markup=markup)

    bot.register_next_step_handler(message, get_results)
def get_results(message):
    if message.text == '(b) Получить пользовательский ввод с клавиатуры':
        global points
        points +=1
    bot.send_message(message.from_user.id,f'Поздравляем вы прошли викторину, вы набрали {points} очка\ов') 
    with open(r"base.txt","a") as f:
        f.write(name+" "+ surname+ "\n")
        #f.write(name+" "+ surname+ " "+points + "\n")
'''    for i in range(len(object)):
        if name == object[i].name:
            if surname == object[i].surname:'''
bot.polling(none_stop=True, interval = 0)