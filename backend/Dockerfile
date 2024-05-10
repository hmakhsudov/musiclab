# Используем базовый образ Python
FROM python:3.10

# Устанавливаем переменную среды для Python, отключая вывод буферизации
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости проекта и устанавливаем их
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Копируем все содержимое текущей директории в контейнер
COPY . /app/

# Открываем порт, на котором будет работать Django приложение
EXPOSE 8000

# Задержка перед выполнением команды миграции и запуском сервера Django
CMD ["sh", "-c", "sleep 10 && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
