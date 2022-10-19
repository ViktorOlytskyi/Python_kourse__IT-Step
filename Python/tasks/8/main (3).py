# Задание 1
# Напишите функцию, которая отображает на экран
# форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself.”
# Bill Gates

def bill_Gates():
    print("“Don't compare yourself with anyone in this world…",
          "if you do so, you are insulting yourself.”",
          "{:>55}".format("Bill Gates"), sep = "\n")
         
bill_Gates()

# Задание 2
# Напишите функцию, которая принимает два числа
# в качестве параметра и отображает все четные числа
# между ними.

def even_btw(a,b):
    print ("even numbers is:", end = " ")
    while a<=b:
        if a % 2 == 0:
            print(f"{a}", end = ", ")
        a+=1

even_btw(2,20)

# Задание 3
# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.
print("\n\n")
def sqare(l,sumb,isEmpty):
    if isEmpty == False:
        for i in range(l):
            print((sumb + " ") * l)
    else:
        print(sumb * l)
        for i in range(2, l):
            print(sumb, " " * (l - 2), sumb, sep = "")
        print(sumb * l)
        
sqare(10,"*",True)
sqare(10,"*",False)

# Задание 4
# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.

def min_of_five(a,b,c,d,e):
    return min(a,b,c,d,e)
   
print(min_of_five(5,10,-1,20,1))

# Задание 5
# Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
# передаются в качестве параметров. Если границы диапазона перепутаны (например, 5 — верхняя граница, 25 —
# нижняя граница), их нужно поменять местами.

def product_btw(a,b):
    c=0
    product=1
    if b < a:
        c=b
        b=a
        a=c
    while a <= b:
        product = a * product
        a+=1
    return product
print(product_btw(4,2))


# Задание 6
# Напишите функцию, которая считает количество
# цифр в числе. Число передаётся в качестве параметра. Из
# функции нужно вернуть полученное количество цифр.
# Например, если передали 3456, количество цифр будет 4.

def len_of_number(n):
    return len(str(n))

print(len_of_number(3456))

# Задание 7
# Напишите функцию, которая проверяет является ли
# число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
# true, иначе false.
# «Палиндром» — это число, у которого первая часть
# цифр равна второй перевернутой части цифр. Например,
# 123321 — палиндром (первая часть 123, вторая 321, которая
# после переворота становится 123), 546645 — палиндром,
# а 421987 — не палиндром.

def is_palindrom(n):
    temp = n
    reverse = 0
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10
    return True if n == reverse else False
    
print(is_palindrom(546645))

