
<template>
    <div class="registerfirst">
        <div class="container">

        <Header/>
        <div class="register__first-title">
            <h1>Вход на сайт</h1>
        </div>
        <form @submit.prevent="registerUser" class="register__first-form">
                <div class="form__inputs">
                    <div class="first__form-title">Форма регистрации</div>
                    <input v-model="responseObj.username" type="text" placeholder="Введите логин" name="login">
                    <input v-model="responseObj.email" type="email" placeholder="Введите почту" name="mail">
                    <input v-model="responseObj.password1" type="password" placeholder="Введите пароль" name="password1">
                    <input v-model="responseObj.password2" type="password" placeholder="Повторите пароль" name="password2">
                    <div class="error-message" v-if="errorMessage">{{ errorMessage }}</div>
                </div>
                <button type="submit">Зарегистрироваться</button>

                <router-link :to="'/login/'" class="login__reverse">Уже есть аккаунт</router-link>
            </form>
    </div>
    </div>

</template>

<script setup lang="js">
    import Header from '../components/Header.vue';
    import axios from 'axios';
    import { reactive, ref } from 'vue';


 const responseObj = ref({
  username: '',
  email: '',
  password1: '',
  password2: ''
});

const errorMessage = ref('');

const registerUser = async () => {
  try {
    // Проверка паролей на совпадение
    if (responseObj.value.password1 !== responseObj.value.password2) {
      errorMessage.value = 'Пароли не совпадают';
      return; // Прерываем отправку запроса
    }

    const response = await fetch('http://127.0.0.1:8000/api/v1/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(responseObj.value)
    });

    const responseData = await response.json();

    if (response.ok) {
      // Регистрация прошла успешно
      console.log('User registered successfully');
    } else {
      // Обработка ошибки регистрации
      errorMessage.value = responseData.error || 'Something went wrong.';
      console.error('Registration error:', errorMessage.value);
    }
  } catch (error) {
    // Обработка ошибки соединения или других проблем
    errorMessage.value = 'Ошибка при подключении к серверу.';
    console.error('Connection error:', error);
  }
};

</script>

<style scoped>
.login__reverse{
    display: block;
    color: #fff;
    font-size: 16px;
    margin-top: 30px;
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
    .registerfirst{
        background-image: url('/img/registration.png');
        background-size: cover;
        background-repeat: no-repeat;
        padding-bottom: 100px;
    }
    
    .register__first-title{
        color: #fff;
        padding-top: 10px;
        padding-bottom: 10px;
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 45px;
    }

    .register__first-form{
        padding: 30px 0px;
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

    .register__first-form input{

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
    .register__first-form input::placeholder{
        color: #fff;
    }


    .register__first-form button{ 
        background-color: transparent;
        border: 1px solid #E8AE33;
        border-radius: 19px;
        padding: 15px 20px;
        font-size: 16px;
        color: #fff;
        font-weight: normal;
        margin-top: 20px;
    }
    .form__inputs{
        padding-left: 68px;
        padding-right: 68px;
        padding-bottom: 20px;
        border-bottom: 1px solid #fff;
        border-radius: 19px;
    }
</style>