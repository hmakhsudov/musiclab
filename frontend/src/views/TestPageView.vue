<template>
    <div class="test__page">
        <div class="test__page-top">
            <div class="container">
                <Header/>
                <div class="test__page-top-content">
                    <div class="test__top-text">
                        <div class="test__top-title">{{ test }}</div>
                        <div class="test__top-typetext">Знание текстов песен</div>
                    </div>
                    <div class="test__top-quantityblock">
                        <div class="test__top-quantity-label">
                           Кол-во вопросов
                        </div>
                        <div class="test__top-quantity">{{ questionsCount }}</div>
                    </div>
                </div>
            </div>
        </div>
            <TestQuestion/>
    </div>
</template>


<script setup>
import Header from '../components/Header.vue';
import TestQuestion from '../components/TestQuestion.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';

// Создаем реактивные переменные для хранения данных о тесте
const test = ref(null);
const questionsCount = ref(null);

// Функция для получения ID теста из URL
const getTestIdFromUrl = () => {
  const url = window.location.href;
  const parts = url.split('/');
  const testIdIndex = parts.indexOf('test') + 1;
  return parts[testIdIndex];
};

// Функция для выполнения запроса к API и получения данных о тесте
const fetchTestData = async () => {
  try {
    const testId = getTestIdFromUrl();
    const response = await axios.get(`http://127.0.0.1:8000/api/v1/test/${testId}/`);
    console.log(response);
    const testData = response.data;
    
    // Записываем данные о тесте в соответствующие переменные
    test.value = testData.title;
    console.log(test.value);
    questionsCount.value = testData.questions_count;
  } catch (error) {
    console.error('Ошибка при получении данных о тесте:', error);
  }
};

// Вызываем функцию fetchTestData после монтирования компонента
onMounted(fetchTestData);
</script>

<style scoped>
    .test__page-top{
        background-image: url('/img/bg_tests.png');
        padding-bottom: 100px;
        
    }
    .test__page-top-content{
        display: flex;
        justify-content: space-between;
    }
    .test__top-title{
        color: #Fff;
        font-size: 32px;
        font-weight: 700;
        background-image: url('/img/textbg_darkgradient.png');
        background-size: cover;
        background-repeat: no-repeat;
        padding-bottom: 20px;
        padding-top: 20px;
        margin-bottom: 40px;
        padding-right: 60px;
        padding-left: 216px;
        border-radius: 19px;
    }
    .test__top-typetext{
        color: #Fff;
        font-size: 20px;
        font-weight: 700;
        background-image: url('/img/textbg_darkgradient.png');
        background-size: cover;
        background-repeat: no-repeat;
        padding-bottom: 20px;
        padding-top: 20px;
        margin-bottom: 40px;
        padding-right: 60px;
        padding-left: 216px;
    }

    .test__top-quantityblock{
        display: flex;
        height: 72px;
    }
    .test__top-quantity{
        font-size: 32px;
        font-weight: 700;
        color: #fff;
        background-color: #000;
        border-radius: 19px;
        padding: 27px 54px;
        box-sizing: border-box;
        display: flex;
        align-items: center;
    }
    .test__top-quantity-label{
        color: #fff;
        width: 126px;
        padding-top: 11px;
        padding-bottom: 11px;
        padding-right: 10px;
        border-right: 1px solid #fff;
        border-radius: 19px;
        box-sizing: border-box;
        display: flex;
        align-items: center;
        border-left: none;
        margin-right: 20px;
    }

</style>