
# Завдання 1
# Реализовать программу расчета заказав кафетерии при условии, что заказ может быть на несколько человек
# и каждый клиент формирует свою часть заказа. Необходимо спросить у пользователя насколько человек заказ.
# Далее каждому человеку выводиться меню(названия напитков,кондитерских изделий и их цена) и он выбирает.
# Предусмотреть возможность выбора нескольких элементов меню для клиента, если он желает добавить еще что-то в свой заказ.
# Результат работы программы — итоговая сумма общего заказа всей компании.

try:
    num_of_orders = int(input("Hello! How many orders do you want to make? \n"))
except:
    print("Error, try again please!\n You can input only numbers\n")

americano = 20
espresso = 15
latte = 25
juice = 30
cake = 20
piece_of_cake = 25
pie = 15
roll = 10
sum = 0
ex = False

while (num_of_orders != 0 or ex == True):
    firts_level_menu = int(input("\n\nMENU:\n\n1 - drinks\n"
          "2 - confectionery products\n0 - exit"))
    if (firts_level_menu==1):
        back = 1
        while (back !=0):
            drinks_menu = int(input(f"\n\n1 - americano **** {americano} UAH\n"
                                      f"2 - espresso **** {espresso} UAH\n"
                                      f"3 - latte **** {latte} UAH\n"
                                      f"4 - fresh juice **** {cake} UAH\n"
                                      "0 - BACK\n\n"))
            if (drinks_menu == 1):
                sum = sum + americano
                print(f"You chose americano, summa = {sum}\n")
            elif (drinks_menu == 2):
                sum = sum + espresso
                print(f"You chose espresso, summa = {sum}\n")
            elif (drinks_menu == 3):
                sum = sum + latte
                print(f"You chose latte, summa = {sum}\n")
            elif (drinks_menu == 4):
                sum = sum + juice
                print(f"You chose juice, summa = {sum}\n")
            elif (drinks_menu == 0):
                back = 0
            else:
                print("Error, try again please!\n You can input only numbers\n\n")

    elif (firts_level_menu==2):
        back = 1
        while (back !=0):
            confectionery_menu = int(input(f"\n\n1 - cake **** {cake} UAH\n"
                                          f"2 - pie **** {piece_of_cake} UAH\n"
                                          f"3 - piece of cake **** {pie} UAH\n"
                                          f"4 - roll **** {roll} UAH\n"
                                          "0 - BACK\n\n"))
            if (confectionery_menu == 1):
                sum = sum + cake
                print(f"You chose cake, summa = {sum}\n")
            elif (confectionery_menu == 2):
                sum = sum + piece_of_cake
                print(f"You chose piece_of_cake, summa = {sum}\n")
            elif (confectionery_menu == 3):
                sum = sum + pie
                print(f"You chose pie, summa = {sum}\n")
            elif (confectionery_menu == 4):
                sum = sum + roll
                print(f"You chose roll, summa = {sum}\n")
            elif (confectionery_menu == 0):
                back = 0
            else:
                print("Error, try again please!\n You can input only numbers\n\n")
    elif(firts_level_menu == 0):
        ex == True
        if (num_of_orders == 0 or ex == True):
            print(f"the amount of the order is equal to {sum}\nThank you for order, good buy!\n\n")
    else:
        print("Error, try again please!\n You can input only numbers\n\n")
    num_of_orders = num_of_orders - 1
    if (num_of_orders == 0 or ex == True):
        print(f"the amount of the order is equal to {sum}\nThank you for order, good buy!\n\n")

