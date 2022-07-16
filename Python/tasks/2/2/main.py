
# Задание 2
#
# Показать на экран все простые числа в диапазоне, указанном пользователем. Число называется простым, если оно делится
# без остатка только на себя и на единицу. Например,три — это простое число, а четыре нет.

try:
    n1 = int(input("Please enter the first number in the range "))
    n2 = int(input("Please enter the second number in the range "))
except:
    print("Error! You must enter number!!!")
    exit(0)

for num in range(n1, n2):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num, " - a simple number")
                break
    else:
        continue
