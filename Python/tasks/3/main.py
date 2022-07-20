# Пользователь вводит с клавиатуры арифметическое выражение.
# Например, 23+12. Необходимо вывести на экран результат выражения.
# В нашем примере это 35.
# Арифметическое выражение может состоять только из трёх частей:
# число, операция, число. Возможные операции: +, -,*,/


expression = str(input("Enter expression, please "))
operators = ['+', '-', '*', '/']
operator = 0
operator_index = 0

for i in expression:
    for j in operators:
        if j == i:
            operator = j
            break

operator_index = expression.index(operator)

if operator == "+":
    print(f"{expression}={int(expression[0:operator_index]) + int(expression[operator_index + 1:])}")

elif operator == "-":
    print(f"{expression}={int(expression[0:operator_index]) - int(expression[operator_index + 1:])}")
elif operator == "*":
    print(f"{expression}={int(expression[0:operator_index]) * int(expression[operator_index + 1:])}")
elif operator == "/":
    print(f"{expression}={int(expression[0:operator_index]) / int(expression[operator_index + 1:])}")
else:
    print("Error, wrong input! ")
