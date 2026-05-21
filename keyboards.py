from telebot import types


def main():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "➕ Записать день",
        "📊 Статистика"
    )

    keyboard.add(
        "📜 История",
        "🧹 Очистить данные"
    )

    keyboard.add(
        "👩‍💻 Помощь"
    )

    return keyboard


def mood():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.row(
        "1 😞",
        "2 😐",
        "3 🙂",
        "4 😊",
        "5 🤩"
    )

    return keyboard


def work():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "1",
        "2",
        "4",
        "8"
    )

    keyboard.add(
        "Другое"
    )

    return keyboard


def sleep():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "6",
        "7",
        "8",
        "9"
    )

    keyboard.add(
        "Другое"
    )

    return keyboard


def comment():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "Пропустить"
    )

    return keyboard


def stats():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "За неделю",
        "За месяц"
    )

    keyboard.add(
        "Мои инсайты",
        "График"
    )

    keyboard.add(
        "Назад"
    )

    return keyboard


def clear():

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.add(
        "Да",
        "Нет"
    )

    return keyboard