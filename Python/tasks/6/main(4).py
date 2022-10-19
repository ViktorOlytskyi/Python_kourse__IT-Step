# Задание 1
# Есть некоторый текст. Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в
# тексте.


# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с боль

# text = "lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book! it has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
# text = text.capitalize()
# symbols = '!.?'
# for i in range(2, len(text)):
#     for s in range(len(symbols)):
#         if text[i - 2:i] == (symbols[s] + ' '):
#             text = text[:i] + text[i].upper() + text[i + 1:]
# print(text)


# # ■ Посчитайте сколько раз цифры встречаются в тексте;
# # ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# # ■ Посчитайте количество восклицательных знаков в тексте.

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book! It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."

# symb = '.,?!-'
# num = '0123456789'
# count_numb = 0
# count_symb = 0
# count = 0

# for i in range(len(text)):
#     a = text[i]
#     for l in range(len(symb)):
#         if a == symb[l]:
#             count_symb = count_symb + 1
#     for n in range(len(num)):
#         if a == num[n]:
#             count_numb = count_numb + 1
#     if text[i] == '!':
#         count = count + 1

# print(f"count of numbers in text = {count_numb}",f"\ncount of sumbols in text = {count_symb}",f"\ncount of \"!\" in text = {count}")


# Задание 2
# Пользователь с клавиатуры вводит элементы списка целых и некоторое число. Необхоимо посчитать сколько раз данное число присутствует в списке.Результат вывести на экран. 


# count = 0
# arr = []
# while count != 5:
#     arr.append(int(input("input some number please ")))
#     count = count +1
# search = int(input("input number with you want to find in array, please ")) 
# repeats = 0
# for i in range(len(arr)):
#     if arr[i] == search:
#         repeats = repeats +1
# print(f"count of repeats number {search} = {repeats}")


# Задание 3
# Пользователь с клавиатуры вводит элементы списка
# целых. Необходимо посчитать сумму всех элементов
# и их среднеарифметическое. Результаты вывести на
# экран.
count2 = 0
arr2 = []
while count2 != 5:
    arr2.append(int(input("input some number please ")))
    count2 = count2 +1

print(f"sum of all elements = {sum(arr2)}")
print(f"arithmetic mean = {sum(arr2)/count2}")