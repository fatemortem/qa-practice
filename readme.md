# Автоматизация UI-тестов с Selenium + Pytest

Тестовый проект для практики автоматизированного тестирования веб-приложений.

## Стек:
- Python
- Pytest
- Selenium WebDriver
- Page Object Model (структура)

## Структура проекта:

test_project/ ├── pages/ # Page Object классы ├── tests/ # Позитивные и негативные тесты ├── conftest.py # Фикстуры (setup/teardown) ├── pytest.ini # Конфиг для Pytest ├── requirements.txt # Зависимости

## Запуск тестов:

1. Установить зависимости:
pip install -r requirements.txt

2. Запустить все тесты:
pytest

3. Запуск с HTML-отчётом:
pytest --html=report.html

## Покрытие:

- ✔ Успешный вход
- ✔ Неверный логин/пароль
- ✔ Пустые поля
- ✔ Отдельные позитивные/негативные тесты

---

## Автор:
[@fatemortem](https://github.com/fatemortem)
