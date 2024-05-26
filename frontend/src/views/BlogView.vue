<script>
import Header from '@/components/Header.vue'

export default {
  components: {
    Header
  }
}
</script>
<template>

  <div class="blog__header">
    <div class="container">
      <Header />
      <div class="blog__header-content">
        <div class="blog__header-image"><img src="/img/groups/group1.png" alt="group"></div>
        <div class="blog__header-text">
          <div class="blog__header-name">ABBA</div>
          <div class="blog__header-title">Драма и душевная боль, стоящая за диско-хитами ABBA</div>
        </div>
      </div>
    </div>
  </div>

  <div class="blog__content">
    <div class="container">
      <div class="blog__content-firstDescription description">
        Группа ABBA — это легенды шведской поп-сцены, одержавшие победу на «Евровидении» 1974 года и исполнившие там лучшую песню за всю историю конкурса. За короткий промежуток существования с 1973-го по 1981-й коллектив сумел выпустить столько вечных хитов, что и сегодня почитается классикой.
Все, что вам нужно знать об ABBA, заложено в названии коллектива. Его как раз собрали из первых букв имен участников: Агнета, Бьорн, Бенни и Анни-Фрид. Расскажем о каждом из них
История ABBA берет начало в 1970-м, но не в Швеции, как могло бы показаться, а на Кипре, куда обе супружеские пары отправились на отдых. Бьорн Ульвеус и Бенни Андерссон уже тогда работали над совместной пластинкой, и идея записать голоса жен для подпевок показалась им довольно интересной. Тем не менее первые песни с их участием Say It With a Song, She’s My Kind of Girl и Love Has It Ways все равно выпускались под именем мужского дуэта.
      </div>
      <div class="blog__content-image">
        <img src="/img/groups/group1.png" alt="">
      </div>
      <div class="blog__content-secondDescription description">
        Группа ABBA — это легенды шведской поп-сцены, одержавшие победу на «Евровидении» 1974 года и исполнившие там лучшую песню за всю историю конкурса. За короткий промежуток существования с 1973-го по 1981-й коллектив сумел выпустить столько вечных хитов, что и сегодня почитается классикой.
Все, что вам нужно знать об ABBA, заложено в названии коллектива. Его как раз собрали из первых букв имен участников: Агнета, Бьорн, Бенни и Анни-Фрид. Расскажем о каждом из них
История ABBA берет начало в 1970-м, но не в Швеции, как могло бы показаться, а на Кипре, куда обе супружеские пары отправились на отдых. Бьорн Ульвеус и Бенни Андерссон уже тогда работали над совместной пластинкой, и идея записать голоса жен для подпевок показалась им довольно интересной. Тем не менее первые песни с их участием Say It With a Song, She’s My Kind of Girl и Love Has It Ways все равно выпускались под именем мужского дуэта.
      </div>
    </div>
    <div class="link__wrapper">
    <router-link class="back" :to="'home'">Вернуться назад</router-link>
  </div>
  </div>

</template>
<style scoped>

.blog__header {
  background-image: url('/img/groups/group1.png');
  background-size: cover;
  background-repeat: no-repeat;
  position: relative;
  background-position: center -60px;

  /* Смещение фонового изображения вверх */
  padding-bottom: 50px;

  z-index: 1;

}

.blog__header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 1));
  pointer-events: none;
  z-index: -1;
  /* Убедитесь, что псевдоэлемент находится за остальными элементами */

}

.blog__header-content {
  display: flex;
  align-items: center;
}

.blog__header-image {
  margin-right: 60px;

}

.blog__header-text {
  color: #fff;
  font-weight: 700;
  font-size: 30px;
}

.blog__header-title {
  margin-top: 40px;
  font-size: 20px;
}


.blog__content{
  padding-top: 20px;
  padding-bottom: 20px;
  background-color: #000;
}

.description{
  background: linear-gradient(to bottom, rgba(192, 155, 147, 0.7), rgba(195, 145, 147, 0.2));
  color: #Fff;
  font-size: 16px;
  font-weight: 70;
  border-radius: 19px;
  padding: 20px 40px;
  margin-bottom: 40px;
}

.blog__content-image{
  text-align: center;
  margin-bottom: 30px;
}

.blog__content-image img{
  max-width: 800px;
}

.back{
  padding: 20px 30px;
  border-radius: 19px;
  background-color: rgba(192, 155, 147, 0.8);
  color: #fff;
  text-decoration: none;
  font-weight: 700;
}

.link__wrapper{
  text-align: center;
  margin-top: 60px;
  margin-bottom: 30px;

}
</style>