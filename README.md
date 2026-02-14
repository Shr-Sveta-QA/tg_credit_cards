# tg_credit_cards
**Телеграм бот для генерации номера карты**

<h2>Телеграм бот, который генерирует номера банковских карт</h2>

> **Статус проекта:**
>
> 🟢 Поддерживается (активный) 

## Цели и Задачи
Помочь QA инженеру быстро получить нужный номер карты при тестировании в тестовой среде.

Бот геренирует номера тестовых банковских карт:
* Номера карт проходят проверку на алгоритм Луна
* Можно получить номер карты: Visa, Mastercard, Мир, Union pay

## 🖼 Скриншоты

Стартовое меню:

![image](https://github.com/Shr-Sveta-QA/tg_credit_cards/blob/main/tg_credit_cards/static/bot_menu.png)

После выбора карты Visa:

![image](https://github.com/Shr-Sveta-QA/tg_credit_cards/blob/main/tg_credit_cards/static/visa_card.png)


## 💻 Технологии

* Python
* Библиотека `telebot`
* Библиотека `faker`

## ⏬ Установка на локальном компьютере

1. Скачать проект
   
2. Создать бота через [@BotFather](https://t.me/BotFather) и вставить в проекте свой токен от бота

3. Создаём виртуальное окружение внутри папки проекта.
Далее команды для Windows (Более подробная инуструкция для Windows и для MacOS [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python -m venv venv
```

``` markdown
venv\Scripts\activate
```
4. Устанавливаем библиотеки

``` markdown
python -m pip install pyTelegramBotAPI
```

``` markdown
python -m pip install faker
```

5. Деактивация (когда закончили работу):
``` markdown
deactivate
```

## Автор

Светлана Денисова ([@vetadnsv](https://t.me/vetadnsv))
