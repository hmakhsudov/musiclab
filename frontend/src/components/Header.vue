<template>
    <div class="container">
        <nav>
            <router-link :to="'/'">
            <div class="nav__logo">
                <img src="/img/logo.svg" alt="">
            </div>
            </router-link>
            <ul>
                <li><router-link :to="'/tests/'">Тесты</router-link></li>
                <li><router-link :to="'/'">Главная</router-link></li>
                <li><a href="#">Статьи</a></li>
              <li><router-link v-if="isAuthenticated" :to="'/'" @click="handleLogout">{{ authText }}</router-link>
      <router-link v-else :to="'/registerfirst'">{{ authText }}</router-link></li>
        </ul>
        </nav>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// Реактивная переменная для определения аутентификации
const isAuthenticated = computed(() => {
  const token = localStorage.getItem('accessToken');
  return !!token;
});

// Реактивно меняем текст ссылки в зависимости от наличия токена доступа
const authText = computed(() => isAuthenticated.value ? 'Выйти' : 'Регистрация');

// Функция для обработки нажатия на ссылку выхода
const handleLogout = () => {
  localStorage.removeItem('accessToken');
  window.location.reload(); // Обновление страницы после выхода
};
</script>
<style scoped>
    
    nav{
        padding-top: 40px;
        display: flex;
        color: #E8AE33;
        vertical-align: center;
        justify-content: space-between;
        margin-bottom: 90px;
    }

    ul{
        display: flex;
    }
    li{
        display: flex;
        align-items: center;
        margin-right: 35px;
    }
    li:last-child{
        margin-right: 0;
    }
    ul li a{
        text-decoration: none;
        color: #E8AE33;
        border: 1px solid #E8AE33;
        padding: 15px 20px;
        border-radius: 20px;
    }

</style>