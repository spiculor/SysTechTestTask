SysTechTestTask
Этот проект предоставляет REST API для обработки текстов (NLP) и поиска по тексту.

Установка и запуск
Клонирование репозитория
git clone https://github.com/spiculor/SysTechTestTask.git
cd <SysTechTestTask>

Запуск через Docker
Соберите контейнеры и запустите:
docker-compose up --build

API будет доступен по адресу: http://localhost:8000

Маршруты API
/process/ (POST)
/search/ (POST)

SysTechTestTask/
├── app/
│   ├── api/
│   │   └── endpoints.py       # Эндпоинты API
│   ├── core/
│   │   ├── text_processing.py # NLP-функции
│   │   └── search.py          # Логика поиска
│   ├── main.py                # Точка входа в приложение
│   └── __init__.py
├── tests/                     # Тесты
│   ├── test_process.py        # Тесты для /process/
│   ├── test_search.py         # Тесты для /search/
│   └── __init__.py
├── data.txt                   # Данные для поиска
├── requirements.txt           # Зависимости проекта
├── Dockerfile                 # Docker-конфигурация
├── docker-compose.yml         # Конфигурация Docker Compose
├── README.md                  # Документация проекта
└── api_client.py              # Скрипт для обращения к API
