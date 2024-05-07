<template>
    <div class="tests">

        <div class="tests__top">
            <div class="container">
                <Header />
                <div class="tests__top-title">
                    Тесты
                </div>
                <div class="tests__top-text">Здесь вы найдете интересные тесты на знание музыкальных групп, жанров и текстов песен. Проверьте свои силы, соревнуйтесь с друзьями! Узнайте свой уровень музыкальной эрудиции, расширяйте кругозор с нашими статьями о мировых музыкальных тенденциях. Присоединитесь к нам и откройте для себя новые грани мира музыки!</div>

            </div>
        </div>
        <div class="tests__content">
            <div class="container">
                <div class="tests__content-filters">
                    <div class="tests__content-choices">
                        <div class="tests__content-choices-wrapper">
                            <button class="tests__content-choice">Тексты песен</button>
                            <button class="tests__content-choice">Факты</button>
                        </div>
                        <div class="tests__content-choices-wrapper">
                            <button class="tests__content-choice">Знание песен</button>
                            <button class="tests__content-choice">Смешанное</button>
                        </div>
                    </div>
                    <div class="tests__content-searchfield">
                        <form action="" method="get">
                            <input type="text" name="searchtest" id="searchtest">
                            <button type="submit"></button>
                        </form>
                    </div>
                </div>
                <div class="tests__content-tests">
                    <TestCart v-for="test in tests" :key="test.id" :test="test"/>
                </div>
            </div>
        </div>
            






    </div>
</template>



<script setup lang="js">
    import {onMounted, ref} from 'vue'
    import Header from '../components/Header.vue'
    import TestCart from '../components/TestCart.vue'
    import axios from 'axios';
    const tests = ref([]);

    const getTests = async () => {
        try {
            const { data } = await axios.get('http://127.0.0.1:8000/api/v1/testlist/')
            tests.value = data
        } catch (error) {
            console.log(error);
        }
    }

   /*  axios.get('http://127.0.0.1:8000/api/v1/testlist/')
    .then(response => {
        tests.push(...response.data);
    })
    .catch(error => {
        console.error('Ошибка при получении данных:', error);
    }); */

    onMounted(() => {
        getTests()
    })
</script>


<style scoped>
    .tests__top{
        background-image: url('/img/bg_tests.png');
        background-size: cover;
        background-repeat: no-repeat;
        color: #fff;
        padding-bottom: 40px;
    }

    .tests__top-title{
        font-size: 32px;
        padding-top: 10px;
        padding-bottom: 10px;
        margin-bottom: 30px;
        font-weight: 700;
    }
    .tests__top-text{
        padding-top: 30px;
        padding-bottom: 30px;
        font-size: 16px;
        line-height: 25px;
    }

    .tests__content{
        background-color: #000;
    }
    .tests__content-filters{
        padding-top: 30px;
        display: flex;
        justify-content: space-between;
        padding-bottom: 30px;

    }
    .tests__content-choice{
        background-color: #A8802D;
        border: none;
        border-bottom: 1px solid #fff;
        border-radius: 19px;
        width: 170px;
        padding-top: 15px;
        padding-bottom: 15px;
        color: #fff;
        font-weight: 700;
    }
    .tests__content-searchfield form{
        width: 220px;
        height: 48px;
        background-color: rgba(232, 174, 51, 0.68);
        border-radius: 19px;
        position: relative;
        padding: 0;
        border: none;
        box-sizing: border-box;


    }
    .tests__content-searchfield form input{
        position: absolute;
        height: 100%;
        width: 100%;
        border-radius: 19px;
        left: 0;
        top: 0;
        background-color: transparent;
        padding: 0;
        outline: none;
        padding-left: 15px;
        padding-right: 65px;
        box-sizing: border-box;
        font-size: 14px;
        color: #fff;
    }
    .tests__content-searchfield form button{
        position: absolute;
        right: 0;
        top: 0;
        height: 100%;
        width: 60px;
        border: none;
        border-radius: 19px;
        background-color: #fff;
        background-color: rgba(232, 174, 51, 0.68);
        text-align: center;
    }
    .tests__content-searchfield form button::after{
        content: "";
        background-image: url('/img/searchicon.svg');
        width: 32px;
        height: 32px;
        position: absolute;
        right: 20%;
        top: 50%;
        transform: translateX(-50%);
        transform: translateY(-50%);
        
    }
    .tests__content-tests{
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
</style>











