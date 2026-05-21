# Mood Tracker Bot

Telegram-бот для отслеживания настроения, сна и продуктивности.

## Возможности

- Запись ежедневных данных
- Статистика за неделю
- Статистика за месяц
- График активности
- История записей
- Инсайты на основе данных
- Очистка данных

## Технологии

- Python
- TeleBot
- SQLite
- Pandas
- Matplotlib

## Структура проекта

```text
├── bot.py
├── config.py
├── db.py
├── handlers.py
├── keyboards.py
├── stats.py
├── schema.sql
├── database.db
└── README.md
```

## Установка

### 1. Клонировать проект

```bash
git clone https://github.com/your_username/project.git
```

### 2. Установить библиотеки

```bash
pip install pytelegrambotapi pandas matplotlib
```

## Настройка

Открыть файл `config.py`

```python
TOKEN = "YOUR_TOKEN"
```

Вставить токен Telegram-бота.

## Запуск

```bash
python bot.py
```

## Команды

| Команда | Описание |
|---|---|
| /start | Запуск бота |
| /help | Помощь |
| /add | Добавить запись |
| /stats | Статистика |
| /history | История |
| /clear | Очистка данных |

## База данных

Используется SQLite.

Таблица:

```sql
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    date TEXT,
    mood INTEGER,
    work_hours REAL,
    sleep_hours REAL,
    comment TEXT
);
```

## Автор

Telegram Mood Tracker Bot
