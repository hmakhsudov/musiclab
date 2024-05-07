<script>
import Header from '../components/Header.vue'

export default {
  components: {
    Header,
  }
}
</script>
<template>
    <div>

        <div class="welcome__content">
                <div class="container">
                    <Header />

                    <div class="welcome__title">
                        <h1>Добро пожаловать в "Музыкальную лабораторную"!</h1>
                    </div>
                    <div class="welcome__text">
                        Добро пожаловать на сайт “Музыкальная Лабораторная”, где вы сможете узнать много нового о ваших любимых музыкальных группах и жанрах, пройти тесты на знание текстов песен, групп и стилей музыки. На сайте представлены статьи о музыкальных коллективах и их влиянии на мировую индустрию. Но главной особенностью являются тесты, которые помогут проверить ваши знания и посоревноваться с друзьями. Присоединяйтесь к “Музыкальной Лабораторной” и окунитесь в увлекательный мир самообразования!
                    </div>
                </div>
        </div>
            <div class="main__tests">
                <div class="container">
                    <div class="main__tests-title">
                        Тесты
                    </div>
                    <div class="main__tests-content">
                        <div class="main__tests-content-tests">
                            <div class="test__cart">
                                <div class="test__cart-title">
                                    Рок и Металл
                                </div>
                                <div class="test__cart-quantity">30 вопросов</div>
                                <div class="test__cart-genre">Жанр: рок</div>
                                <div class="test__cart-type">Тип: название песен</div>
                                <div class="test__cart-start-wrapper">
                                    <a href="#" class="test__cart-start">Начать!</a>
                                </div>
                            </div>
                            <div class="test__cart">
                                <div class="test__cart-title">
                                    Рок и Металл
                                </div>
                                <div class="test__cart-quantity">30 вопросов</div>
                                <div class="test__cart-genre">Жанр: рок</div>
                                <div class="test__cart-type">Тип: название песен</div>
                                <div class="test__cart-start-wrapper">
                                    <a href="#" class="test__cart-start">Начать!</a>
                                </div>
                            </div>
                            <div class="test__cart">
                                <div class="test__cart-title">
                                    Рок и Металл
                                </div>
                                <div class="test__cart-quantity">30 вопросов</div>
                                <div class="test__cart-genre">Жанр: рок</div>
                                <div class="test__cart-type">Тип: название песен</div>
                                <div class="test__cart-start-wrapper">
                                    <a href="#" class="test__cart-start">Начать!</a>
                                </div>
                            </div>
                        </div>
                        <div class="main__tests-content-pag">
                            <div class="pag__element">1</div>
                            <div class="pag__element">2</div>
                            <div class="pag__element">3</div>
                            <div class="pag__showmore">...</div>
                        </div>
                    </div>
                </div>
        </div>
        <div class="main__blogs">
            <div class="container">
                <div class="main__blogs-title">
                    Статьи
                </div>
                <div class="main__blogs-blogs">
                    <div class="blog">
                        <div class="blog-image"><img src="/img/groups/group1.png" alt=""></div>
                        <div class="blog-content">
                            <div class="blog-group">ABBA</div>
                            <div class="blog-type">Тип: о группе</div>
                            <div class="blog-title">
                                Драма и душевная боль, стоящая за диско-хитами ABBA
                            </div>
                        </div>
                        <a href="#" class="main__blog-read">
                            Читать!
                        </a>
                    </div>
                    <div class="blog">
                        <div class="blog-image"><img src="/img/groups/group2.png" alt=""></div>
                        <div class="blog-content">
                            <div class="blog-group">ABBA</div>
                            <div class="blog-type">Тип: о группе</div>
                            <div class="blog-title">
                                Драма и душевная боль, стоящая за диско-хитами ABBA
                            </div>
                        </div>
                        <a href="#" class="main__blog-read">
                            Читать!
                        </a>
                    </div>
                </div>
                <div class="main__blogs-content-pag">
                            <div class="pag__element">1</div>
                            <div class="pag__element">2</div>
                            <div class="pag__element">3</div>
                            <div class="pag__showmore">...</div>
                        </div>
            </div>
        </div>
        <div class="main__contacts">
            <div class="container">
                <div class="main__contacts-title" id="main__contacts">Контакты</div>
                <div class="main__contacts-content">
                    <div class="main__contacts-links">
                        <ul>
                            <li><a href="#">VK: musiclab</a></li>
                            <li><a href="#">Email: musiclab@gmail.com</a></li>
                            <li><a href="#">Telegram: @MusLab</a></li>
                        </ul>
                    </div>
                    <div class="main__contacts-form">
                        <form action="" class="feedback__form">
                            <input type="text" placeholder="Ваше имя" class="feedback__contact-input">
                            <input type="text" placeholder="Ваша почта" class="feedback__contact-input">
                            <input type="text" placeholder="Текст сообщения" class="feedback__text-input">
                            <div class="button__wrapper">
                            <button type="submit">Отправить</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>


<style scoped>
    .welcome__content{
        background-image: url("/img/welcome_bg.png");
        padding-bottom: 105px;
    }
    .welcome__title {
/*         background-image: linear-gradient(to right, #E4992A, #C09B93);
 */     margin-bottom: 50px;
        padding-top: 15px;
        padding-bottom: 15px;
        padding-left: 20px;
        background-image: url(/img/bg_gradient.png);
        background-repeat: no-repeat;
        width: 100%;


    }
    .welcome__title h1{
        font-size: 30px;
        font-weight: bold;
        color: #fff;
    }

    .welcome__text{
/*         background: linear-gradient(to right, rgba(228, 153, 42, 1) 0%, rgba(192, 155, 147, 1) 100%);
 */     border-radius: 42px;
        padding-left: 20px;
        padding-top: 50px;
        padding-bottom: 50px;
        max-width: 740px;
        font-size: 20px;
        color: #fff;
    }

    .main__tests{
        background-color: #000;
        color: #fff;
        padding-top: 50px;
    }
    .main__tests-title{
        padding-top: 18px;
        padding-bottom: 18px;
        margin-bottom: 50px;
        font-size: 30px;
        font-weight: 700;
    }
    .main__tests-content-tests{
        display: flex;
        justify-content: space-between;
        margin-bottom: 46px;
    }

    .main__tests-content-pag{
        display: flex;
        align-items: center;
        justify-content: center;
        padding-bottom: 35px;
        align-items: flex-end;

    }
    .pag__element{
        background-color: #D49F31;
        color: #000;
        border-radius: 50%;
        width: 42px;
        height: 42px;
        display: flex;
        justify-content: center;
        vertical-align: center;
        align-items: center;
        font-weight: 700;
        margin-right: 12px;
    }
    .pag__showmore{
        color: #D49F31;
        font-weight: 700;
        font-size: 25px;
    }
    .main__blogs{
        color: #Fff;
        background-image: url('/img/bg_blogs.png');
        background-repeat: no-repeat;
        background-size: cover;
        padding-top: 60px;
        font-weight: 700;
        padding-bottom: 34px;

    }

    .main__blogs-title{
        padding-top: 10px;
        padding-bottom: 10px;
        margin-bottom: 64px;
        font-size: 32px;
    }

    .blog{
        position: relative;
        background-color: #C09B93;
        width: 100%;
        display: flex;   
        border-radius: 19px;
        margin-bottom: 41px;    
        height: 263px;
    }
    .blog-image{
        margin-right: 40px;
        height: 100%;
    }
    .blog-image img{
        height: 100%;
    }
    .blog-content{
        padding-top: 40px;
    }
    .blog-group{
        font-size: 24px;
        margin-bottom: 40px;
    }
    .blog-type{
        font-size: 16px;
        border-top: 1px solid #fff;
        border-radius: 30px; 
        padding-top: 13px;
        padding-left: 35px;
        padding-bottom: 24px;
        width: 435px;
        box-sizing: border-box;

        
    }
    .blog-title{
        box-sizing: border-box;
        width: 435px;
        font-size: 16px;
        border-top: 1px solid #fff;
        border-radius: 30px; 
        padding-left: 35px;
        padding-top: 13px;
        padding-bottom: 24px;
        padding-right: 32px;
    }
    
    .main__blog-read{
        position: absolute;
        display: inline-block;
        text-decoration: none;
        color: #fff;
        background-color: #1E1E1E;
        padding: 20px 45px;
        border-radius: 19px;
        right: 34px;
        bottom: 23px;
    }
    .main__blogs-content-pag{
        display: flex;
        align-items: center;
        justify-content: center;
        padding-bottom: 35px;
        align-items: flex-end;

    }
    .main__blogs-content-pag .pag__element{
        background-color: #C09B93;
    }
    .main__blogs-content-pag .pag__showmore{
        color: #C09B93;
    }
    
    .main__contacts{
        background-color: #000;
        color: #Fff;
        padding-top: 60px;
        padding-bottom: 50px;
    }
    .main__contacts-title{
        font-size: 30px;
        font-weight: 700;
        padding-top: 10px;
        padding-bottom: 10px;
        margin-bottom: 50px;
    }
    .main__contacts-content{
        display: flex;
        justify-content: space-between;

    }

    .main__contacts-links ul li a{
        display: inline-block;
        text-decoration: none;
        width: 336px;
        padding-left: 32px;
        padding-top: 20px;
        padding-bottom: 20px;
        color: #fff;
        border: 1px solid #fff;
        border-top: 1px solid transparent;
        border-radius: 19px;
    }
    
    .feedback__form{
        width: 587px;
        max-width: 587px;
        font-weight: 700;
    }

    .feedback__form input{
        box-sizing: border-box;

        display: block;
        width: 100%;
        background-color: rgba(232, 174, 51, 0.68);
        height: 46px;
        border-radius: 19px;
        padding-left: 19px;
        border: none;
        color: #FFf;
        margin-bottom: 19px;
        position: relative;
        outline: none;
        font-weight: 700;
    }
    .feedback__form input::placeholder{
        color: #fff;
        font-weight: 700;
    }

    .button__wrapper{
        text-align: center;
    }

    .feedback__form button{
        background-color: transparent;
        color: #E8AE33;
        border: none;
        font-size: 18px;
        font-weight: 700;
    }


</style>