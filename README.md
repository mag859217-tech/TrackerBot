# Mood Tracker Bot

Telegram-бот для отслеживания настроения, сна и продуктивности.

# Технологии

- Python
- TeleBot
- SQLite
- Pandas
- Matplotlib

# Структура проекта

```text
├── .gitignore
├── README.md
├── bot.py
├── config.py
├── db.py
├── handlers.py
├── keyboards.py
├── requirements.txt
├── schema.sql
├── sqlschema.jpg
└── stats.py
```

# Установка

## Установка библиотек

```bash
pip install -r requirements.txt
```

# Запуск

```bash
python bot.py
```

# Команды

| Команда | Описание |
|---|---|
| /start | Запуск бота |
| /help | Помощь |
| /add | Добавление записи |
| /stats | Статистика |
| /history | История |
| /clear | Очистка данных |
