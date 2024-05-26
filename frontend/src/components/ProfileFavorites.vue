<template>
    <div class="favorites">
        <div class="favorite-groups">
            <h2>Избранные группы</h2>
            <div class="groups-list">
                <div class="group">
                    <img src="/img/groups/group1.png" alt="AC/DC">
                    <p>AC/DC</p>
                </div>
                <div class="group">
                    <img src="/img/groups/group1.png" alt="ATB">
                    <p>ATB</p>
                </div>
                <div class="group">
                    <img src="/img/groups/group1.png" alt="For The Fallen Dreams">
                    <p>For The Fallen Dreams</p>
                </div>
            </div>
            <div class="groups-controls">
                <button class="control-button">Добавить группы</button>
                <button class="control-button">Посмотреть все</button>
            </div>
        </div>
        <div class="favorite-groups favorite-genres">
            <h2>Избранные жанры</h2>
            <div class="groups-list">
                <div class="group">
                    <img src="/img/groups/group1.png" alt="Транс">
                    <p>Рок</p>
                </div>
                <div class="group">
                    <img src="/img/groups/group1.png" alt="Альтернатива">
                    <p>Альтернатива</p>
                </div>
                <div class="group">
                    <img src="/img/groups/group1.png" alt="Фолк">
                    <p>Фолк</p>
                </div>
            </div>
            <div class="groups-controls">
                <button class="control-button">Добавить жанры</button>
                <button class="control-button">Посмотреть все</button>
            </div>
        </div>
    </div>
</template>


<script setup>


</script>

<style scoped>

.favorites{
    background-color: rgba(232, 174, 51, 0.68);
    border-radius: 19px;
    padding-top: 23px;
    padding-bottom: 23px;

}

.favorite-groups{
    border-bottom: 1px solid #fff;
    border-radius: 19px;
    padding-bottom: 20px;
    padding-left: 45px;
    padding-right: 45px;

}

.favorite-groups h2{
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 24px;
}

.groups-list{
    display: flex;
    justify-content: space-between;
    padding-left: 45px;
    padding-right: 45px;
    margin-bottom: 20px;
}

.group{
    position: relative;
    width: 170px;
    height: 180px;
    background-color: #000;
    border-radius: 19px;
}

.group img{
    position: absolute;
    top: 0;
    left: 0;
    border-radius: 19px;
    width: 100%;
    height: 116px;
}


.group p{
    position: absolute;
    bottom: 0;
    padding-bottom: 20px;
    padding-left: 10px;
    padding-right: 10px;
    text-align: center;
    font-size: 16px;
    font-weight: 700;
    width: 170px;
    box-sizing: border-box;
}

.groups-controls{
    text-align: center;
    width: 480px;
    display: flex;
    justify-content: space-between;
    margin: 0 auto;

}

.control-button{
    width: 207px;
    height: 48px;
    display: flex;
    justify-content: center;
    align-items: center;
    border: 1px solid rgba(232, 174, 51, 0.68);
    background-color: transparent;
    color: #fff;
    font-size: 16px;
    font-weight: 700;
    border-radius: 19px;
}

.favorite-genres{
    margin-top: 20px;
    border: none;
}

</style>