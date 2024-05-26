<template>
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
</template>

<script setup>
    
</script>

<style scoped>

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

</style>