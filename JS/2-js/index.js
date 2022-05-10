//Task 1

//Написать функцию, которая принимает 2 числа и возвра-
// щает -1, если первое меньше, чем второе; 1 – если первое
// больше, чем второе; и 0 – если числа равны.

    function foo (a,b) {
        if (a<b) {
            return -1;
        }
        else if (a>b) {
            return 1;
        }
        else {
            return 0;
        }
    }
    document.write("task-1 result is: ",foo(2,2))

//Task 2

// Написать функцию, которая вычисляет факториал пере-
// данного ей числа

// function factorial(a) {
//     for(let i=1; i<=a; i++) {
//         a *= i;
//     }
//     return a;
// }

    function factorial(n) {
        result = n;
        for (let i = n - 1; i > 1; --i) {
            result *= i;
        }
        return result;
    }

    document.write("<br>task-2 result is: ",factorial(5));

//Task 3

// Написать функцию, которая принимает три отдельные
// цифры и превращает их в одно число. Например: цифры
// 1, 4, 9 превратятся в число 149.

    function onenumb (a,b,c) {
        result = String(a)+String(b)+String(c);
        return result;
    }

    document.write("<br>task-3 result is: ",onenumb(1,4,9));

//Task 4

// Написать функцию, которая принимает длину и ширину
// прямоугольника и вычисляет его площадь. Если в функцию
// передали 1 параметр, то она вычисляет площадь квадрата.


    function area(a,b = 0) {
        if(b == 0) { return a**2; }
        else {
            return a*b;}
        }
    document.write("<br>task-4 result is: ",area(10));

//Task 5

// Написать функцию, которая проверяет, является ли пере-
// данное ей число совершенным. Совершенное число – это
// число, равное сумме всех своих собственных делителей.

    function isPerfect(num) {
        sum = 1;
    
        for(divider = 2; divider <= num / 2; divider++ )
            if( num % divider == 0 )
                sum += divider;
    
        return sum == num;
    }
    document.write("<br>task-5 result is: ",isPerfect(28));

//Task 6

// Написать функцию, которая принимает минимальное и
// максимальное значения для диапазона, и выводит только
// те числа из диапазона, которые являются совершенными.
// Используйте написанную ранее функцию, чтобы узнавать,
// совершенное число или нет.

    function isPerfectDiapason(a,b) {
        document.write("<br>task-6 result is: ");
        for (;a<=b;a++) {
            if(isPerfect(a)){
                document.write(a+";");
            }
        }
    }
    isPerfectDiapason(2,18000)

//Task 7

// Написать функцию, которая принимает время (часы, мину-
// ты, секунды) и выводит его на экран в формате «чч:мм:сс».
// Если при вызове функции минуты и/или секунды не были
// переданы, то выводить их как 00.

    function time (h,m=0,s=0) {
        if(m==0) {
            m="0";
        }
        if(s==0) {
            s="0";
        }
        if(h<10) {
            h="0"+h;
        }
        if(m<10) {
            m="0"+m;
        }
        if(s<10) {
            s="0"+s;
        }
        
        document.write("<br>task-7 result is: ",String(h)+":"+m+":"+s);
    }

    time (12,30,4);

//Task 8

// Написать функцию, которая принимает часы, минуты и
// секунды и возвращает это время в секундах.

    function sec (h,m=0,s=0) {
        return (h*3600)+(m*60)+(s);
    }
    document.write("<br>task-8 result is: ",sec(22,60,15));

//Task 9

// Написать функцию, которая принимает количество секунд,
// переводит их в часы, минуты и секунды и возвращает в
// виде строки «чч:мм:сс».

    function secToTime(s) {
        let hr = Math.floor(s / 3600);
        let m = s % 3600;
        let min = Math.floor(m / 60);
        let sec = m % 60;
        return hr+":"+min+":"+sec;
    }
    document.write("<br>task-9 result is: ",secToTime(20000));

//Task 10

// Написать функцию, которая считает разницу между датами.
// Функция принимает 6 параметров, которые описывают 2
// даты, и возвращает результат в виде строки «чч:мм:сс». При
// выполнении задания используйте функции из предыду-
// щих 2-х заданий: сначала обе даты переведите в секунды,
// узнайте разницу в секундах, а потом разницу переведите
// обратно в «чч:мм:сс».

let firstDate;
let secondDate;
let dateDifference;
function dateDiff(a = 0, b = 0, c = 0, d = 0, e = 0, f = 0) {
	if (0 > a || a > 23 || b < 0 || b > 59 || c < 0 || c > 59 || 0 > d || d > 23 || e < 0 || e > 59 || f < 0 || f > 59) {
		return "Ви ввели невірні дані"
	} else {
		firstDate = a * 3600 + b * 60 + c,
		secondDate = d * 3600 + e * 60 + f;
		dateDifference = firstDate - secondDate;
		let h = Math.floor(dateDifference / 3600);
		let m = Math.floor((dateDifference % 3600) / 60);
		let s = ((dateDifference % 3600) % 60);
		return h + ':' + m + ':' + s;
	}

}
document.write("<br>task-10 result is: ",dateDiff(20,6,4,14,7,2));
