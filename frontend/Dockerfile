# Используем базовый образ Node.js
FROM node:16

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости проекта и устанавливаем их
COPY package.json ./
RUN npm install --save-dev @rollup/rollup-linux-x64-gnu
RUN npm install --force

# Копируем все содержимое текущей директории в контейнер
COPY . .

# Открываем порт, на котором будет работать Vite сервер
EXPOSE 3000

# Команда для запуска сервера разработки Vite
CMD ["npm", "run", "dev"]
