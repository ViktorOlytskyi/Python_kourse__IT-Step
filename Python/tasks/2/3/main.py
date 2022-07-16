# Задание 3
#
# Пользователь вводит с клавиатуры строку. Проверьте является ли введенная строка палиндромом.
# Палиндром — слово или текст, которое читается одинаково слева на право и справа на лево.

text = str(input("enter some text please "))

if str(text) == "".join(reversed(text)) :
    print("Palindrome")
else:
    print("Not Palindrome")