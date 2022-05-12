//Task 1
// Создать объект, описывающий автомобиль (производитель,
// модель, год выпуска, средняя скорость), и следующие функции
// для работы с этим объектом.
//1. Функция для вывода на экран информации об автомобиле.
//2. Функция для подсчета необходимого времени для пре-
//одоления переданного расстояния со средней скоростью.
//Учтите, что через каждые 4 часа дороги водителю необхо-
//димо делать перерыв на 1 час


    car = {
        producer : "Opel",
        model : "Astra",
        year : 2016,
        avarageSpeed : 60,

        show : function(){
            document.write("Producer: ",this.producer);
            document.write("<br>Model: ",this.model);
            document.write("<br>Year: ",this.year);
            document.write("<br>Avarage Speed: ",this.avarageSpeed);
        },

        time: function (distance) {
            let result = distance / this.avarageSpeed;
            let relax = 0;
            result = Math.trunc(result) + (((result - (Math.trunc(result))) * 60) / 100)
            for (let hour = 1; hour <= result; hour++) {
                if (hour % 5 == 0) {
                    relax++;
                    result++;
                }
            }
            result = result.toFixed(2).split(".");
            if (relax == 0) {
                document.write("<br>To arive this distance: ", distance, "km. You need ",result[0]," hour(s) and ", result[1], " minuts, and you dont need to relax");
            } else {
                document.write("<br>To arive this distance: ", distance, "km. You need ",result[0]," hour(s) and ", result[1], " minuts. You need for relax: ",relax," hours");
    
            }
        }
    }

    car.show();
    car.time(400);

//Task 2

// Создать объект, хранящий в себе отдельно числитель и зна-
// менатель дроби, и следующие функции для работы с этим объ-
// ектом.
// 1. Функция сложения 2-х объектов-дробей.
// 2. Функция вычитания 2-х объектов-дробей.
// 3. Функция умножения 2-х объектов-дробей.
// 4. Функция деления 2-х объектов-дробей.
// 5. Функция сокращения объекта-дроби

    const fraction1 = {
        numerator: 3,
        denominator: 5,
        show: function () {
            return this.numerator+"/"+this.denominator;
        }
    }

    const fraction2 = {
        numerator: 3,
        denominator: 9,
        show: function () {
            return this.numerator+"/"+this.denominator;
        }
    }
    // Функция сложения 2-х объектов-дробей

    function getAdd(fract1, fract2) {
        const resultFraction = {
            numerator: 0,
            denominator: 0,
        };
        resultFraction.numerator = fract1.numerator * fract2.denominator + fract1.denominator * fract2.numerator;
        resultFraction.denominator = fract2.denominator * fract1.denominator;
        return resultFraction.numerator+"/"+resultFraction.denominator;
    }
    document.write("<br><br>")
    document.write("<b>"+fraction1.show()+"+"+fraction2.show()+"=", getAdd(fraction1, fraction2)+"</b>")

    // Функция вычитания 2-х объектов-дробей;

    function getSub(fract1, fract2) {
        const resultFraction = {
            numerator: 0,
            denominator: 0,
        };
        resultFraction.numerator = fract1.numerator * fract2.denominator - fract1.denominator * fract2.numerator;
        resultFraction.denominator = fract2.denominator * fract1.denominator;
        return resultFraction.numerator+"/"+resultFraction.denominator;
    }

    document.write("<br>")
    document.write("<b>"+fraction1.show()+"-"+fraction2.show()+"=", getSub(fraction1, fraction2)+"</b>")

    // Функция умножения 2-х объектов-дробей;

    function getMult(fract1, fract2) {
        const resultFraction = {
            numerator: 0,
            denominator: 0,
        };
        resultFraction.numerator = fract1.numerator * fract2.numerator;
        resultFraction.denominator = fract2.denominator * fract1.denominator;
        return resultFraction.numerator+"/"+resultFraction.denominator;
    }

    document.write("<br>")
    document.write("<b>"+fraction1.show()+"*"+fraction2.show()+"=", getMult(fraction1, fraction2)+"</b>")

    // Функция деления 2-х объектов-дробей;

    function getDiv(fract1, fract2) {
        const resultFraction = {
            numerator: 0,
            denominator: 0,
        };
        resultFraction.numerator = fract1.numerator * fract2.denominator;
        resultFraction.denominator = fract1.denominator * fract2.numerator;
        return resultFraction.numerator+"/"+resultFraction.denominator;
    }

    document.write("<br>")
    document.write("<b>"+fraction1.show()+"/"+fraction2.show()+"=", getDiv(fraction1, fraction2)+"</b>")

    // Функция сокращения объекта-дроби.

    function getReduction(fract) {
        const resultFraction = {
            numerator: 0,
            denominator: 0,
        };
        resultFraction.numerator = fract.numerator;
        resultFraction.denominator = fract.denominator;
        const n = fract.numerator > fract.denominator ? fract.denominator : fract.numerator;
        for (let i = n; i > 1; i--) {
            if (resultFraction.numerator % n === 0 && resultFraction.denominator % n === 0) {
                resultFraction.numerator = resultFraction.numerator / n;
                resultFraction.denominator = resultFraction.denominator / n;
            }
        }
        return resultFraction.numerator+"/"+resultFraction.denominator;
    }
    document.write("<br>")
    document.write("<b>"+fraction2.show()+"=",getReduction(fraction2)+"</b>")


// Задание 3
// Создать объект, описывающий время (часы, минуты, секунды), и следующие функции для работы с этим объектом.
// 1. Функция вывода времени на экран.
// 2. Функция изменения времени на переданное количество секунд.
// 3. Функция изменения времени на переданное количество минут.
// 4. Функция изменения времени на переданное количество часов.
// Учтите, что в последних 3-х функциях, при изменении одной
// части времени, может измениться и другая. Например: если ко
// времени «20:30:45» добавить 30 секунд, то должно получиться
// «20:31:15», а не «20:30:75».

const time = {
    hours: 9,
    minutes: 35,
    seconds: 22
}

// Функция вывода времени на экран;

function showTime(obj) {
    const hours = obj.hours > 9 ? obj.hours : '0' + obj.hours;
    const minutes = obj.minutes > 9 ? obj.minutes : '0' + obj.minutes;
    const seconds = obj.seconds > 9 ? obj.seconds : '0' + obj.seconds;
    return hours+":"+minutes+":"+seconds;
}

document.write("<br><br>")
document.write(showTime(time))

// Функция изменения времени на переданное количество секунд;

function convertTimeIntoSecond(obj) {
    return obj.hours * 3600 + obj.minutes * 60 + obj.seconds;
}

function getTimefromSeonds(seconds) {
    const time = {
        hours: 0,
        minutes: 0,
        seconds: 0,
    }
    time.hours = Math.trunc(seconds / 3600);
    time.minutes = Math.trunc((seconds - time.hours * 3600) / 60);
    time.seconds = (seconds - time.hours * 3600) % 60;
    return time;
}

function changeSeconds(obj, seconds) {
    const oldTimeInSecond = convertTimeIntoSecond(obj);
    const newTimeInSeconds = oldTimeInSecond + seconds;
    const newTime = getTimefromSeonds(newTimeInSeconds);
    return showTime(newTime);
}

document.write("<br>"+changeSeconds(time, 35));
document.write("<br>"+changeSeconds(time, -100));

// Функция изменения времени на переданное количество минут;

function changeMinutes(obj, minutes) {
    const oldTimeInSecond = convertTimeIntoSecond(obj);
    const newTimeInSeconds = oldTimeInSecond + minutes * 60;
    const newTime = getTimefromSeonds(newTimeInSeconds);
    return showTime(newTime);
}

document.write("<br>"+changeMinutes(time, 35));
document.write("<br>"+changeMinutes(time, -100));

// Функция изменения времени на переданное количество часов. 

function changeHours(obj, hours) {
    const oldTimeInSecond = convertTimeIntoSecond(obj);
    const newTimeInSeconds = oldTimeInSecond + hours * 3600;
    const newTime = getTimefromSeonds(newTimeInSeconds);
    return showTime(newTime);
}

document.write("<br>"+changeHours(time, 3));
document.write("<br>"+changeHours(time, -1));
