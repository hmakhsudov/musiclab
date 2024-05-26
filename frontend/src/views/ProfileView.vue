<template>
    <div class="profile-page-wrapper">
      <div class="container">
        <Header />
        <div class="profile-page">
          <div class="sidebar">
            <img src="/img/profile-picture.png" alt="Profile Picture" class="profile-picture">
            <nav class="sidebar-nav">
              <button
                class="nav-button"
                :class="{ active: currentComponent === 'ProfileFavorites' }"
                @click="setActiveComponent('ProfileFavorites')"
              >
                Избранное
              </button>
              <button
                class="nav-button"
                :class="{ active: currentComponent === 'ProfileTests' }"
                @click="setActiveComponent('ProfileTests')"
              >
                Тесты
              </button>
              <button
                class="nav-button"
                :class="{ active: currentComponent === 'ProfileBlogs' }"
                @click="setActiveComponent('ProfileBlogs')"
              >
                Статьи
              </button>
            </nav>
          </div>
          <div class="main-content">
            <div class="main-content-title">
              Личный кабинет
            </div>
            <div class="header">
              <div class="header__name">
                <h1 class="username">Jane Doe</h1>
                <a class="email" href="mailto:janedoe@gmail.com">janedoe@gmail.com</a>
              </div>
              <div class="rating">
                <p>Ваш общий рейтинг</p>
                <div class="rating-score">76%</div>
              </div>
            </div>
  
            <!-- Динамическое рендеринг компонентов -->
            <component :is="components[currentComponent]" />
            
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="js">
  import { ref } from 'vue'
  import Header from '@/components/Header.vue'
  import ProfileFavorites from '@/components/ProfileFavorites.vue'
  import ProfileTests from '@/components/ProfileTests.vue'
  import ProfileBlogs from '@/components/ProfileBlogs.vue'
  
  // Установите компонент по умолчанию как 'ProfileFavorites'
  const currentComponent = ref('ProfileFavorites')
  
  const components = {
    ProfileFavorites,
    ProfileTests,
    ProfileBlogs,
  }
  
  function setActiveComponent(component) {
    currentComponent.value = component;
  }
  </script>
  
<style scoped>
.profile-page-wrapper {
    background-image: url('/img/registration.png');
    background-size: cover;
    background-repeat: no-repeat;
    padding-bottom: 100px;

}

.profile-page {
    display: flex;
    justify-content: space-between;
}

.profile-picture {
    width: 300px;
    height: 300px;
    border-radius: 19px;
    margin-bottom: 80px;

}

.sidebar-nav {
    background-color: rgba(232, 174, 51, 0.68);
    border-radius: 19px;

}

.sidebar-nav button {
    display: block;
    background-color: transparent;
    border: none;
    border-bottom: 1px solid #fff;
    border-radius: 19px;
    color: #fff;
    font-size: 20px;
    font-weight: 700;
    width: 300px;
    padding-top: 20px;
    padding-bottom: 20px;
}

.sidebar-nav button:hover {
    background-color: rgba(232, 174, 51, 0.68);
}

.sidebar-nav button.active{
    background-color: rgba(232, 174, 51, 0.68);

}


.main-content {
    width: 855px;
    color: #fff;
}

.main-content-title {
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 65px;

}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 65px;
}

.header__name .username {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 20px;

}

.header__name .email {
    text-decoration: underline;
    color: #fff;
}

.rating {
    display: flex;
    align-items: center;
}

.rating p {
    color: #fff;
    width: 126px;
    padding-top: 21px;
    padding-bottom: 21px;
    padding-right: 10px;
    border-right: 1px solid #fff;
    border-radius: 19px;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    border-left: none;
    margin-right: 20px;
}

.rating-score {
    background-color: #E8AE33;
    display: flex;
    width: 126px;
    padding-top: 21px;
    padding-bottom: 21px;
    padding-right: 10px;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    font-weight: 700;
    border-radius: 19px;
}



</style>