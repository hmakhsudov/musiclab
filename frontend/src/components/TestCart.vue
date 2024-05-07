<template>
    <div class="test__cart">
      <div class="test__cart-title">{{ test.title }}</div>
      <div class="test__cart-quantity">{{ test.questions_count }} вопросов</div>
      <div class="test__cart-genre">Жанр: {{ test.genre_name }}</div>
      <div class="test__cart-type">Тип: {{ test.testtype }}</div>
      <div class="test__cart-start-wrapper" 
      >
        <router-link :to="'/test/' + test.id + '/question/1'" class="test__cart-start">Начать!</router-link>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  import { ref } from 'vue'
  const testId = ref()
  const props = defineProps({
    test: Object,
    testId: String
  });


  </script>
  

<style>
        .test__cart{
        width: 336px;
        max-height: 336px;
        border-radius: 19px;
        background-color: rgba(232, 174, 51, 0.68);
        margin-bottom: 35px;
        color: #Fff;
    }
    .test__cart-title{
        background-color: #d19c2e;
        text-align: center;
        padding-top: 20px;
        padding-bottom: 20px;
        border-radius: 19px;
        font-size: 24px;
        font-weight: 700;
    }
    .test__cart-quantity{
        padding-left: 23px;
        padding-top: 31px;
        padding-bottom: 15px;
        border-bottom: 1px solid #fff;
        border-radius: 19px;
        font-weight: 700;
    }
    .test__cart-genre{
        padding-left: 23px;
        padding-top: 19px;
        padding-bottom: 15px;
        border-bottom: 1px solid #fff;
        border-radius: 19px;
        font-weight: 700;
    }
    .test__cart-type{
        padding-left: 23px;
        padding-top: 19px;
        padding-bottom: 15px;
        border-bottom: 1px solid #fff;
        border-radius: 19px;
        font-weight: 700;
    }
    .test__cart-start{
        display: inline-block;
        color: #fff;
        text-decoration: none;
        padding: 18px 33px;
        margin-top: 20px;
        margin-bottom: 28px;
        background-color: #1E1E1E;
        border-radius: 19px;
    }
    .test__cart-start-wrapper{
        text-align: center;
    }
</style>