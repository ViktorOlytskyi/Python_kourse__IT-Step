// Задание 4
// Создать html-страницу со светофором и кнопкой, которая
// переключает светофор на следующий цвет.

const button = document.getElementById("bt");
var lights = [];
var colors = [];

lights.push(document.getElementById("c1"));
lights.push(document.getElementById("c2"));
lights.push(document.getElementById("c3"));
colors.push("green");
colors.push("yellow");
colors.push("red");
colors.push("grey");
let i =0;

button.addEventListener('click', function (e) {
    lights[i].style.background=colors[i];
    console.log(i);
    if(i==1||i==2){
        lights[i-1].style.background=colors[3];
    }
        
    if(lights[0].style.background=="green none repeat scroll 0% 0%")
    {
        lights[2].style.background=colors[3];
    }
    i++;
    if(i==3)
    {i=0;}
    
  
});