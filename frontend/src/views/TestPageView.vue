<template>
    <div class="test__page">
        <div class="test__page-top">
            <div class="container">
                <Header/>
                <div class="test__page-top-content">
                    <div class="test__top-text">
                        <div class="test__top-title">Distrupted</div>
                        <div class="test__top-typetext">Знание текстов песен</div>
                    </div>
                    <div class="test__top-quantityblock">
                        <div class="test__top-quantity-label">
                            Кол-во вопросов 
                        </div>
                        <div class="test__top-quantity">15</div>
                    </div>
                </div>
            </div>
        </div>
            <TestQuestion/>
    </div>
</template>


<script setup>
    import Header from '../components/Header.vue'
    import TestQuestion from '../components/TestQuestion.vue'

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