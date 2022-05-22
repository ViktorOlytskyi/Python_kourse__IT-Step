// Задание 1
// Создать html-страницу для ввода имени пользователя.
// Необходимо проверять каждый символ, который вводит поль-
// зователь. Если он ввел цифру, то не отображать ее в input.

const selectElement = document.getElementById("task1");

selectElement.addEventListener('input', function (e) {
    if (Number(e.data)) {
        e.target.value = e.target.value.substring(0, e.target.value.length - 1);;
    }
});