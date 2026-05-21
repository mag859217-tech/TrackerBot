import db
import stats
import keyboards

user_data = {}


def register_handlers(bot):

    @bot.message_handler(commands=["start"])
    def start(message):

        text = (
            "Трекер настроения "
            "и продуктивности"
        )

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=keyboards.main()
        )

    @bot.message_handler(commands=["help"])
    @bot.message_handler(
        func=lambda message:
        message.text == "👩‍💻 Помощь"
    )
    def help_command(message):

        text = (
            "/start\n"
            "/add\n"
            "/stats\n"
            "/history\n"
            "/clear"
        )

        bot.send_message(
            message.chat.id,
            text
        )

    @bot.message_handler(commands=["add"])
    def add_command(message):
        add(message)

    @bot.message_handler(commands=["stats"])
    def stats_command(message):
        statistics(message)

    @bot.message_handler(commands=["history"])
    def history_command(message):
        history(message)

    @bot.message_handler(commands=["clear"])
    def clear_command(message):
        clear(message)

    @bot.message_handler(
        func=lambda message:
        message.text == "➕ Записать день"
    )
    def add(message):

        if db.has_today_record(
            message.from_user.id
        ):

            bot.send_message(
                message.chat.id,
                "Запись уже есть"
            )

            return

        user_data[message.chat.id] = {}

        msg = bot.send_message(
            message.chat.id,
            "Оцени настроение",
            reply_markup=keyboards.mood()
        )

        bot.register_next_step_handler(
            msg,
            mood
        )

    def mood(message):

        value = int(
            message.text.split()[0]
        )

        user_data[message.chat.id][
            "mood"
        ] = value

        msg = bot.send_message(
            message.chat.id,
            "Часы работы",
            reply_markup=keyboards.work()
        )

        bot.register_next_step_handler(
            msg,
            work
        )

    def work(message):

        if message.text == "Другое":

            msg = bot.send_message(
                message.chat.id,
                "Введите часы"
            )

            bot.register_next_step_handler(
                msg,
                save_work
            )

            return

        save_work(message)

    def save_work(message):

        user_data[message.chat.id][
            "work"
        ] = float(message.text)

        msg = bot.send_message(
            message.chat.id,
            "Часы сна",
            reply_markup=keyboards.sleep()
        )

        bot.register_next_step_handler(
            msg,
            sleep
        )

    def sleep(message):

        if message.text == "Другое":

            msg = bot.send_message(
                message.chat.id,
                "Введите часы"
            )

            bot.register_next_step_handler(
                msg,
                save_sleep
            )

            return

        save_sleep(message)

    def save_sleep(message):

        user_data[message.chat.id][
            "sleep"
        ] = float(message.text)

        msg = bot.send_message(
            message.chat.id,
            "Комментарий",
            reply_markup=keyboards.comment()
        )

        bot.register_next_step_handler(
            msg,
            comment
        )

    def comment(message):

        text = message.text

        if text == "Пропустить":
            text = "-"

        data = user_data[message.chat.id]

        db.add_record(
            uid=message.from_user.id,
            mood=data["mood"],
            work=data["work"],
            sleep=data["sleep"],
            comment=text
        )

        bot.send_message(
            message.chat.id,
            "Запись сохранена",
            reply_markup=keyboards.main()
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "📊 Статистика"
    )
    def statistics(message):

        bot.send_message(
            message.chat.id,
            "Выберите период",
            reply_markup=keyboards.stats()
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "За неделю"
    )
    def week(message):

        text = stats.week_stats(
            message.from_user.id
        )

        bot.send_message(
            message.chat.id,
            text
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "За месяц"
    )
    def month(message):

        text = stats.month_stats(
            message.from_user.id
        )

        bot.send_message(
            message.chat.id,
            text
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "Мои инсайты"
    )
    def insights(message):

        text = stats.insights(
            message.from_user.id
        )

        bot.send_message(
            message.chat.id,
            text
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "График"
    )
    def graph(message):

        path = stats.graph(
            message.from_user.id
        )

        if not path:

            bot.send_message(
                message.chat.id,
                "Нет данных"
            )

            return

        with open(path, "rb") as photo:

            bot.send_photo(
                message.chat.id,
                photo
            )

    @bot.message_handler(
        func=lambda message:
        message.text == "📜 История"
    )
    def history(message):

        records = db.get_records(
            message.from_user.id
        )

        if not records:

            bot.send_message(
                message.chat.id,
                "Нет данных"
            )

            return

        text = ""

        for item in records:

            text += (
                f"{item['date']}\n"
                f"Настроение: "
                f"{item['mood']}\n"
                f"Работа: "
                f"{item['work_hours']} ч\n"
                f"Сон: "
                f"{item['sleep_hours']} ч\n"
                f"Комментарий: "
                f"{item['comment']}\n\n"
            )

        bot.send_message(
            message.chat.id,
            text
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "🧹 Очистить данные"
    )
    def clear(message):

        bot.send_message(
            message.chat.id,
            "Удалить данные?",
            reply_markup=keyboards.clear()
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "Да"
    )
    def yes(message):

        db.clear_data(
            message.from_user.id
        )

        bot.send_message(
            message.chat.id,
            "Данные удалены",
            reply_markup=keyboards.main()
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "Нет"
    )
    def no(message):

        bot.send_message(
            message.chat.id,
            "Отмена",
            reply_markup=keyboards.main()
        )

    @bot.message_handler(
        func=lambda message:
        message.text == "Назад"
    )
    def back(message):

        bot.send_message(
            message.chat.id,
            "Главное меню",
            reply_markup=keyboards.main()
        )