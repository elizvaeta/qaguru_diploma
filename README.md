# Проект по тестированию раздела "Работа в IT" Т-Банка

> <a target="_blank" href="https://www.tinkoff.ru/career/it/about/">Ссылка на раздел</a>

![Тестируемая страница](/readme/main_page.png)

## :pencil: Содержание:

- [Используемый стэк](#hammer_and_wrench-используемый-стэк)
- [Реализованные UI-проверки](#white_check_mark-реализованные-ui-проверки)
- [Реализованные API-проверки](#white_check_mark-реализованные-api-проверки)
- [Запуск тестов](#arrow_forward-запуск-тестов)
    - [Jenkins](#jenkins)
    - [Локально](#локально)
- [Отчеты о прохождении тестов](#bar_chart-отчеты-о-прохождении-тестов)
    - [Allure](#allure)
    - [Telegram](#telegram)

### :hammer_and_wrench: Используемый стэк

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Pytest](https://img.shields.io/badge/Pytest-29B6F6?style=for-the-badge&logo=pytest&logoColor=white)
![Selene](https://img.shields.io/badge/Selene-42b029?style=for-the-badge)
![Jenkins](https://img.shields.io/badge/Jenkins-000?style=for-the-badge&logo=jenkins&logoColor=white)
![Selenoid](https://img.shields.io/badge/Selenoid-0084c7?style=for-the-badge)
![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-21c55d?style=for-the-badge)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

### :white_check_mark: Реализованные UI-проверки

#### Страница "Карьера"

- [x] Наличие информационных блоков
- [x] Переход к просмотру списка вакансий
- [x] Переход к просмотру статей в блоге

#### Страница "Вакансии"

- [x] Фильтрация по специализации
- [x] Фильтрация по уровню
- [x] Фильтрация по городу

#### Страница "Быстрые офферы"

- [x] Заполнение анкеты

#### Общие компоненты

- [x] Наличие верхнего меню на всех страницах
- [x] Наличие ссылок на социальные сети в футере на всех страницах

### :white_check_mark: Реализованные API-проверки

#### Просмотр доступных тегов для фильтрации:

- [x] Успешная отправка запроса
- [x] Отправка некорректного тела ответа
- [x] Соответствие ответа json-схеме

#### Просмотр списка вакансий:

- [x] Успешная отправка запроса
- [x] Отправка некорректного тела ответа
- [x] Соответствие ответа json-схеме

#### Просмотр вакансии:

- [x] Успешный просмотр рандомной вакансии
- [x] Отправка некорректного id вакансии
- [x] Соответствие ответа json-схеме

## :arrow_forward: Запуск тестов

### Jenkins

<a target="_blank" href="https://jenkins.autotests.cloud/job/C12-ekazova-diploma">Ссылка на Jenkins</a>

1. Нажать кнопку "Build with Parameters"

![Сборка в Jenkins](/readme/jenkins_1.png)

2. Выбрать параметры

![Сборка в Jenkins](/readme/jenkins_2.png)

3. Нажать "Build"

### Локально

1. Склонировать репозиторий
2. Открыть проект и установить интерпретатор
3. Создать файл с переменными окружения `.env` по образцу в корне проекта
4. Запустить тесты

```bash
pytest
```

Можно запустить только api-тесты или только ui-тесты, используя марки:

```bash
pytest -m api_test
```

или

```bash
pytest -m ui_test
```

## :bar_chart: Отчеты о прохождении тестов

### Allure

В Jenkins можно открыть отчет после окончания сборки, выбрав сборку и перейдя по ссылке созданного артефакта:

![Отчет Allure в Jenkins](/readme/jenkins_allure.png)

Для просмотра отчета локально нужно ввести команду:

```bash
allure serve tests/allure-results
```

Примеры отображения тестов:

![Отчет в Allure](/readme/allure_1.png)
![Отчет в Allure](/readme/allure_2.png)

Видео с прохождением теста:

![Отчет в Allure](/readme/allure_3.gif)

### Telegram

Отчет о пройденных тестах приходит в Telegram:

![Отчет в Telegram](/readme/report_telegram.png)