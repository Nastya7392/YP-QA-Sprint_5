# Stellar Burgers - 5 спринт автоматизированного тестирования на Python

## Описание проекта

Проект предназначен для автоматизированного тестирования веб-сайта Stellar Burgers. В рамках проекта проводятся тесты на регистрацию пользователя, вход в систему, выход из профиля и навигацию по разделам сайта.

## Структура проекта

* **`tests/`**: Папка, содержащая все тестовые файлы и настройки.

  * `helpers.py`: Функции для генерации случайных данных, таких как имя, email и пароли.
  * `locators.py`: Локаторы для элементов на веб-странице, используемые в тестах.
  * `test\_navigation\_in\_constructor\_sections.py`: Проверяет переход по разделам "Булки", "Соусы", "Начинки" в конструкторе.
  * `test\_navigation\_to\_account.py`: Проверяет переход в личный кабинет пользователя.
  * `test\_navigation\_to\_constructor.py`: Проверяет переход в конструктор по кнопке "Конструктор" и логотипу Stellar Burgers.
  * `test\_user\_login.py`: Проверяет различные способы входа в профиль.
  * `test\_user\_logout.py`: Проверяет функциональность выхода из профиля.
  * `test\_user\_registration.py`: Проверяет регистрацию пользователя.
* **`conftest.py`**: Фикстуры и настройки для тестов, включая URL страниц и тестового пользователя.
* **`requirements.txt`**: Файл с зависимостями проекта.

## Установка

1. Клонируйте репозиторий:

&#x20;   ```bash
    git clone https://github.com/lnlydrvr/Sprint\_3.git
    ```

2. Установите зависимости:

&#x20;   ```bash
    pip install -r requirements.txt
    ```

## Запуск тестов

1. Убедитесь, что у вас установлен веб-драйвер для браузера (например, ChromeDriver для Google Chrome).
2. Запустите тесты с помощью `pytest`:

&#x20;   ```bash
    pytest
    ```

## Тесты

### `test\_user\_registration.py`

* **test\_successful\_registration**: Проверяет успешную регистрацию пользователя с корректным именем, email и паролем.
* **test\_registration\_with\_invalid\_password**: Проверяет отображение ошибки при попытке регистрации с некорректным паролем.

### `test\_user\_login.py`

* **test\_login\_via\_login\_button**: Проверяет вход по кнопке "Войти в аккаунт" на главной странице.
* **test\_login\_via\_account\_button\_in\_header**: Проверяет вход через кнопку "Личный кабинет".
* **test\_login\_via\_registration\_form**: Проверяет вход через кнопку в форме регистрации.
* **test\_login\_via\_forgot\_password\_form**: Проверяет вход через кнопку в форме восстановления пароля.

### `test\_user\_logout.py`

* **test\_logout\_from\_account**: Проверяет функциональность выхода из личного кабинета.

### `test\_navigation\_to\_account.py`

* **test\_navigate\_to\_account\_page**: Проверяет переход в личный кабинет по клику на кнопку "Личный кабинет" после входа в систему.

### `test\_navigation\_to\_constructor.py`

* **test\_navigation\_from\_account\_to\_constructor\_via\_constructor\_button**: Проверяет переход в конструктор по кнопке "Конструктор".
* **test\_navigation\_from\_account\_to\_constructor\_via\_logo**: Проверяет переход в конструктор по клику на логотип Stellar Burgers.

### `test\_navigation\_in\_constructor\_sections.py`

* **test\_navigation\_to\_sections**: Проверяет переходы между разделами "Булки", "Соусы", "Начинки" в конструкторе.

