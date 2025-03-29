# Project-AI

Проект представляет собой Telegram-бота, разработанного с использованием фреймворка aiogram 3.x. Бот имеет модульную структуру с разделением на пользовательский и административный интерфейсы.

## Технологии

- Python 3.x
- aiogram 3.17.0
- SQLAlchemy 2.0.37
- OpenAI API
- Docker

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/Project-AI.git
cd Project-AI
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
# или
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл `config.py` и добавьте в него токен вашего бота:
```python
TOKEN = "ваш_токен_бота"
```

5. Запустите бота:
```bash
python run.py
```

### Запуск через Docker

1. Соберите Docker-образ:
```bash
docker build -t project-ai .
```

2. Запустите контейнер:
```bash
docker run -d --name project-ai project-ai
```

## Структура проекта

```
Project-AI/
├── app/
│   ├── admin/         # Административные команды
│   ├── user/          # Пользовательские команды
│   └── database/      # Модели базы данных
├── dockerfile
├── requirements.txt
└── run.py
```

## Лицензия

MIT

## Автор

Ваше имя 