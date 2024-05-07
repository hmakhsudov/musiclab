<template>
    <div class="registerfirst">
        <div class="container">

        <Header/>
        <div class="register__first-title">
            <h1>Вход на сайт</h1>
        </div>
        <form action="" class="register__first-form">
            <div class="form__inputs">
                <div class="first__form-title">Форма авторизации</div>
            
            <div class="genres__top top">
                <div class="genres__top-title">Выберите любимые жанры</div>
                <form class="genres__top-searchform minisearchform">
                    <input type="text" name="searchgenre">
                    <button type="submit">Найти</button>
                </form>
            </div>
            <div class="genres__choices">
                <div class="genre">
                    <img src="/img/genres/genre1.png" alt="">
                    <div class="genre__text">Катри</div>
                </div>
            </div>


            </div>

            <button type="submit">Дальше</button>
        </form>
    </div>
    </div>

</template>

<script setup>
    import Header from '../components/Header.vue';
</script>

<style scoped>

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


    .top{
        display: flex;
        justify-content: space-between;
    }
</style>