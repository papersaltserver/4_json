# Описание модуля Prettify JSON

Модуль для форматированной печати json объектов из файлов на диске.

# Как использовать

Пример запуска скрипта на Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
[
    {
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18",
        "Number": 1,
        "Cells": {
            "global_id": 14371450,
            "Name": "Ароматный Мир",
            "IsNetObject": "да",
            "OperatingCompany": "Ароматный Мир",
            "TypeService": "реализация продовольственных товаров",
            "AdmArea": "Западный административный округ",
            "District": "район Кунцево",
            "Address": "улица Академика Павлова, дом 10",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ],
            "WorkingHours": [
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "понедельник"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "вторник"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "среда"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "четверг"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "пятница"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "суббота"
                },
                {
                    "Hours": "09:30-22:30",
                    "DayOfWeek": "воскресенье"
                }
            ],
            "ClarificationOfWorkingHours": null,
            "geoData": {
                "type": "Point",
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ]
            }
        }
    }
]

```
Получть данные для теста можно в любом открытом api, например https://data.mos.ru/

# Цели проекта

Этот код написан в целях обучения, в рамках курса для разработчиков - [DEVMAN.org](https://devman.org)
