<template>
    <div class="test__question">
      <div class="container">
        <div class="test__question-number">
          Вопрос {{ questionIndex }}
        </div>
        <div class="test__question-fragment">
          {{ questionFragment }}
        </div>
        <div class="test__question-questiontitle">
          {{ questionTitle }}
        </div>
        <div class="test__question-questiontitle">
        это фрагмент из песни,,,,
    </div>
        <form @submit.prevent="getNextQuestion"> 
        <div class="test__question-choices">
            <label v-for="(choice, index) in choices" :key="index" class="test__question-choice">
                <input type="radio" :value="choice" v-model="selectedChoice" class="radio-button" />
                {{ choice }}
            </label>

            </div>
        <button type="submit" class="test__question-next">Следующий вопрос</button>
</form>

      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { onMounted, ref, defineProps, watch } from 'vue'

  defineProps({
    testId: String
  })


  const testId = window.location.href.match(/\/test\/(\d+)\//)[1]

  console.log(testId);

  let questionIndex = 1; // Индекс текущего вопроса
  let questionFragment = ref(''); // Фрагмент песни
  let questionTitle = ref(''); // Заголовок вопроса
  let choices = ref([]); // Варианты ответов
  const selectedChoice = ref(''); // Для хранения выбранного варианта

  watch(selectedChoice, () => {
  const labels = document.querySelectorAll('.test__question-choice');
  labels.forEach(label => {
    if (label.textContent.trim() === selectedChoice.value) {
      label.classList.add('checked');
    } else {
      label.classList.remove('checked');
    }
  });
});
  const loadQuestion = async () => {
    try {
        // Получаем данные о вопросе
        const { data: questionData } = await axios.get(`http://127.0.0.1:8000/api/v1/test/${testId}/questions/${questionIndex}/`);
        questionFragment.value = questionData.fragment;
        questionTitle.value = questionData.title;

        // Получаем данные о вариантах ответов для данного вопроса
        const { data: answersData } = await axios.get(`http://127.0.0.1:8000/api/v1/question/${questionData.id}/answers/`);
        choices.value = answersData.map(
            answer => answer.answer_text);
    } catch (error) {
        console.log(error);
    }
  };
  
  // Функция для перехода к следующему вопросу
  const getNextQuestion = () => {
    questionIndex++; // Увеличиваем индекс для запроса следующего вопроса
    loadQuestion(); // Загружаем данные о следующем вопросе
  };
  
  // Вызываем функцию загрузки данных о текущем вопросе при создании компонента
  onMounted(() => {
    loadQuestion();
  });
  </script>

<style scoped>

    .test__question{
        background-color: #000;
        padding-bottom: 60px;
    }
    .test__question-number{
        width: 320px;
        height: 82px;
        background-color: #E8AE33;
        display: flex;
        align-items: center;
        font-size: 24px;
        font-weight: 700;
        border-radius: 19px;
        justify-content: center;
        margin: 0 auto;
        margin-bottom: 45px;
    }

    .test__question-fragment{
        font-size: 20px;
        color: #fff;
        font-weight: 700;
        border: 1px solid #fff;
        border-radius: 19px;
        padding: 40px 60px;
        margin: 0 auto;
        max-width: 600px;
        margin-bottom: 72px;

    }
    .test__question-questiontitle{
        margin: 0 auto;
        margin-bottom: 23px;
        color: #fff;
        font-size: 16px;
        font-weight: 700;
        text-align: center;
    }
    .test__question-choices{
        display: flex;
        justify-content: space-between;
        margin-bottom: 55px;
    }
/* Невидимые радиокнопки */
.radio-button {
  position: absolute;
  opacity: 0;
}

/* Оформление лейблов */
.test__question-choice {
  width: 245px;
  height: 114px;
  background-color: rgba(232, 174, 51, 0.68);
  border-radius: 19px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  margin-right: 10px;
  position: relative;
}




.test__question-next{
        width: 465px;
        height: 82px;
        color: #E8AE33;
        font-weight: 700;
        font-size: 24px;
        display: flex;
        border: 1px #E8AE33 solid;
        border-radius: 19px;
        align-items: center;
        text-decoration: none;
        justify-content: center;
        margin: 0 auto;
        background-color: transparent;
        cursor: pointer;
    }

    .checked{
        border: 2px solid #fff;
        background-color: #E8AE33;
    }

</style>, watch