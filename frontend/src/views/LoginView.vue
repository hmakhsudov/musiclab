
<template>
    <div class="loginfirst">
        <div class="container">

        <Header/>
        <div class="login__first-title">
            <h1>Вход на сайт</h1>
        </div>
        <form @submit.prevent="loginUser" class="login__first-form">
                <div class="form__inputs">
                    <div class="first__form-title">Форма авторизации</div>
                    <input v-model="loginData.username" type="text" placeholder="Введите логин" name="login">
                    <input v-model="loginData.password" type="password" placeholder="Введите пароль" name="password">
                    <div class="error-message" v-if="errorMessage">{{ errorMessage }}</div>
                    <button type="submit">Войти</button>

                </div>
                <h1 class="login__reverse">Новый пользователь?</h1>
                <router-link :to="'/registerfirst/'" class="register__link">Зарегистрироваться</router-link>

        </form>
    </div>
    </div>

</template>


<script setup>
import { ref } from 'vue';
import Header from '../components/Header.vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

const loginData = ref({
  username: '',
  password: ''
});

const errorMessage = ref('');

const loginUser = async () => {
  try {
    console.log('Sending login request with data:', loginData.value); // Лог отправляемых данных
    const response = await axios.post('http://127.0.0.1:8000/api/v1/token/', {
      username: loginData.value.username,
      password: loginData.value.password
    });
    console.log('Response data:', response.data); // Лог ответа сервера
    const token = response.data.access;
    console.log('Access token:', token); // Лог токена доступа
    localStorage.setItem('accessToken', token);
    console.log('Access token saved to localStorage'); // Лог сохранения токена в localStorage
    // Перенаправление на другую страницу после успешного входа
    router.push('/profile');
  } catch (error) {
    // Обработка ошибки аутентификации
    errorMessage.value = 'Неправильные учетные данные';
    console.log('Error details:', error); // Лог деталей ошибки
    console.error('Authentication error:', errorMessage.value);
  }
};
</script>


<style scoped>
    h1{
        margin-top: 30px;
        margin-bottom: 40px;
        color: #fff;
        font-size: 30px;
        font-weight: 700;
        text-align: left;
        padding-left: 60px;

    }
    .error-message{
        text-align-last: left;
        color: #fff;
        border: 3px solid red;
        border-radius: 19px;
        padding-top: 15px;
        padding-bottom: 15px;
        padding-left: 20px;
    }
    .loginfirst{
        background-image: url('/img/registration.png');
        background-size: cover;
        background-repeat: no-repeat;
        padding-bottom: 100px;
    }
    
    .login__first-title{
        color: #fff;
        padding-top: 10px;
        padding-bottom: 10px;
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 45px;
    }

    .login__first-form{
        padding: 30px 0px;
        padding-bottom: 50px;
        text-align: center;
        background-color: rgba(232, 174, 51, 0.68);
        border-radius: 19px;
        width: 723px;
        margin: 0 auto;
    }

    .first__form-title{
        font-size: 30px;
        color: #fff;
        font-weight: 700;
        text-align-last: left;
        margin-bottom: 70px;
    }

    .login__first-form input{

        box-sizing: border-box;
        width: 100%;
        height: 45px;
        background-color: rgba(232, 174, 51, 0.68);
        border: none;
        border-radius: 19px;
        color: #fff;
        font-size: 16px;
        font-weight: 700;
        padding-left: 20px;
        padding-right: 20px;
        margin-bottom: 14px;
        outline: none;

    }
    .login__first-form input::placeholder{
        color: #fff;
    }


    .login__first-form button{ 
        background-color: transparent;
        border: 1px solid #E8AE33;
        border-radius: 19px;
        padding: 15px 80px;
        font-size: 16px;
        color: #fff;
        font-weight: normal;
        margin-top: 20px;
    }
    .register__link{
        background-color: transparent;
        border: 1px solid #E8AE33;
        border-radius: 19px;
        padding: 15px 20px;
        font-size: 16px;
        color: #fff;
        font-weight: normal;
        margin-top: 20px;
        text-decoration: none;
    }
    .form__inputs{
        padding-left: 68px;
        padding-right: 68px;
        padding-bottom: 20px;
        border-bottom: 1px solid #fff;
        border-radius: 19px;
    }
</style>