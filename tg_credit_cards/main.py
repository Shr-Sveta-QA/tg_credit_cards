# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# В google colab добавить: !pip install Faker
# для установки необходимо в файл requirements.text добавить строки
# 'PyTelegramBotApi'
# 'faker'
from telebot import TeleBot, types
from faker import Faker
import random


TOKEN = "Тут_вставь_свой_токен"
bot = TeleBot(token=TOKEN, parse_mode='html')

faker = Faker('en_US')


# ==================================
# УНИВЕРСАЛЬНАЯ ГЕНЕРАЦИЯ LUHN
# ==================================

def generate_luhn_number(prefix: str, total_length: int) -> str:
    number = prefix

    # дополняем случайными цифрами до предпоследней
    while len(number) < total_length - 1:
        number += str(random.randint(0, 9))

    digits = [int(d) for d in number]
    digits.reverse()

    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    check_digit = (10 - (total % 10)) % 10
    return number + str(check_digit)


def format_card(number: str) -> str:
    return " ".join(number[i:i+4] for i in range(0, len(number), 4))


# ==================================
# ГЕНЕРАЦИЯ КАРТ
# ==================================

def generate_mir():
    prefix = str(random.randint(2200, 2204))
    return generate_luhn_number(prefix, 16)


def generate_mastercard():
    # Только диапазон 51–55
    prefix = str(random.randint(51, 55))
    return generate_luhn_number(prefix, 16)


def generate_unionpay():
    return generate_luhn_number("62", 16)


# ==================================
# КЛАВИАТУРА
# ==================================

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row("VISA", "Mastercard")
keyboard.row("МИР", "UnionPay")


# ==================================
# ОБРАБОТЧИКИ
# ==================================

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(
        message.chat.id,
        "💳 Привет!\nВыбери тип карты:",
        reply_markup=keyboard
    )


@bot.message_handler()
def message_handler(message):

    if message.text == "VISA":
        card_number = faker.credit_card_number('visa16')

    elif message.text == "Mastercard":
        card_number = generate_mastercard()

    elif message.text == "МИР":
        card_number = generate_mir()

    elif message.text == "UnionPay":
        card_number = generate_unionpay()

    else:
        bot.send_message(message.chat.id, "Не понимаю тебя :(")
        return

    bot.send_message(
        message.chat.id,
        f"💳 <b>{message.text}</b>\n\n<b>Номер:</b>\n<code>{format_card(card_number)}</code>"
    )


# ==================================
# ЗАПУСК
# ==================================

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
