// Задание 5
// Создать html-страницу со списком книг.
// При щелчке на книгу, цвет фона должен меняться на оранжевый.
// Учтите, что при повторном щелчке на другую книгу, предыдущей –
// необходимо возвращать прежний цвет.

function Orange(a){
    for(i = 1; i < 8; i++){
        document.getElementById("book"+i).style.background = "#FBF2E9";
    }

    document.getElementById("book"+a).style.background = "orange";
}