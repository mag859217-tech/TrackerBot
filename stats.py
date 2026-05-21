from datetime import datetime

import pandas
import matplotlib.pyplot

import db

def get_dataframe(uid):

    records = db.get_records(uid)

    if not records:
        return None

    dataframe = pandas.DataFrame(records)

    dataframe["date"] = pandas.to_datetime(
        dataframe["date"]
    )

    return dataframe


def week_stats(uid):

    dataframe = get_dataframe(uid)

    if dataframe is None:
        return "Нет данных"

    dataframe = dataframe[
        (
            datetime.now() - dataframe["date"]
        ).dt.days <= 7
    ]

    return (
        "Статистика за неделю\n\n"
        f"Настроение: "
        f"{round(dataframe['mood'].mean(), 2)}\n"
        f"Работа: "
        f"{round(dataframe['work_hours'].mean(), 2)} ч\n"
        f"Сон: "
        f"{round(dataframe['sleep_hours'].mean(), 2)} ч"
    )


def month_stats(uid):

    dataframe = get_dataframe(uid)

    if dataframe is None:
        return "Нет данных"

    dataframe = dataframe[
        (
            datetime.now() - dataframe["date"]
        ).dt.days <= 30
    ]

    return (
        "Статистика за месяц\n\n"
        f"Настроение: "
        f"{round(dataframe['mood'].mean(), 2)}\n"
        f"Работа: "
        f"{round(dataframe['work_hours'].mean(), 2)} ч\n"
        f"Сон: "
        f"{round(dataframe['sleep_hours'].mean(), 2)} ч"
    )


def insights(uid):

    dataframe = get_dataframe(uid)

    if dataframe is None:
        return "Нет данных"

    best = dataframe[
        dataframe["mood"] == dataframe["mood"].max()
    ]

    return (
        "Мои инсайты\n\n"
        f"Лучшее настроение: "
        f"{best['mood'].max()}\n"
        f"Средний сон: "
        f"{round(best['sleep_hours'].mean(), 2)} ч\n"
        f"Средняя работа: "
        f"{round(best['work_hours'].mean(), 2)} ч"
    )


def graph(uid):

    dataframe = get_dataframe(uid)

    if dataframe is None:
        return None

    matplotlib.pyplot.figure(
        figsize=(10, 5)
    )

    matplotlib.pyplot.plot(
        dataframe["date"],
        dataframe["mood"],
        marker="o",
        label="Настроение"
    )

    matplotlib.pyplot.plot(
        dataframe["date"],
        dataframe["sleep_hours"],
        marker="o",
        label="Сон"
    )

    matplotlib.pyplot.plot(
        dataframe["date"],
        dataframe["work_hours"],
        marker="o",
        label="Работа"
    )

    matplotlib.pyplot.legend()

    matplotlib.pyplot.grid()

    matplotlib.pyplot.xticks(rotation=45)

    matplotlib.pyplot.tight_layout()

    path = "graph.png"

    matplotlib.pyplot.savefig(path)

    matplotlib.pyplot.close()

    return path