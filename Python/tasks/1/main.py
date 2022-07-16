# Задание
# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.


Exit = False
while (Exit!=True):
    print("Choise the figure:\n")
    answer = input("1\tUpper right corner of square\n"
               "2\tBottom left corner of square\n"
               "3\tUpper triangle of square\n"
               "4\tBottom triangle of square\n"
               "5\tUpper and bottom triangle of square\n"
               "6\tLeft and right triangle of square\n"
               "7\tLeft triangle of square\n"
               "8\tRight triangle of square\n"
               "9\tUpper left corner of square\n"
               "10\tBottom right corner of square\n\n"
               "0\tExit\n\n")

    if (answer == "1"):
        i = 5
        while i >= 1:
            j = 5
            while j > i:
                # display space
                print(' ', end=' ')
                j -= 1
            k = 1
            while k <= i:
                print('*', end=' ')
                k += 1
            print("\r")
            i -= 1

    elif (answer == "2"):
        for i in range(0, 5):
            for j in range(0, i + 1):
                print("* ", end="")
            print("\r")

    elif (answer == "3"):
        for i in range(5, 1, -1):
            for space in range(0, 5 - i):
                print("  ", end="")
            for j in range(i, 2 * i - 1):
                print("* ", end="")
            for j in range(1, i - 1):
                print("* ", end="")
            print("\r")

    elif (answer == "4"):
        k = 4
        for i in range(0, 5):
            for j in range(0, k):
                print(end=" ")

            k = k - 1

            for j in range(0, i + 1):
                print("* ", end="")

            print("\r")

    elif (answer == "5"):

        i = 0
        while i <= 4:
            j = 0
            while j < i:
                print('', end=' ')
                j += 1
            k = i
            while k <= 5 - 1:
                print('*', end=' ')
                k += 1
            print()
            i += 1

        i = 4
        while i >= 0:
            j = 0
            while j < i:
                print('', end=' ')
                j += 1
            k = i
            while k <= 5 - 1:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1

    elif (answer == "6"):

        n = 3

        i = 1
        while (i <= n):

            j = 1
            while (j <= i):
                print("*", end="")
                j += 1

            k = 1
            while (k <= 2 * (n - i)):
                print(" ", end="")
                k += 1

            l = 1
            while (l <= i):
                print("*", end="")
                l += 1

            print()
            i += 1

        i = n - 1
        while (i >= 1):

            j = 1
            while (j <= i):
                print("*", end="")
                j += 1

            k = 1
            while (k <= 2 * (n - i)):
                print(" ", end="")
                k += 1

            l = 1
            while (l <= i):
                print("*", end="")
                l += 1

            print()
            i -= 1

    elif (answer == "7"):

        for i in range(0, 3):
            for j in range(0, i + 1):
                print("*", end=' ')
            print(" ")

        for i in range(3, 0, -1):
            for j in range(0, i - 1):
                print("*", end=' ')
            print(" ")

    elif (answer == "8"):
        rows = 3
        i = 1
        while i <= rows:
            j = i
            while j < rows:
                print(' ', end=' ')
                j += 1
            k = 1
            while k <= i:
                print('*', end=' ')
                k += 1
            print()
            i += 1

        i = rows
        while i >= 1:
            j = i
            while j <= rows:
                print(' ', end=' ')
                j += 1
            k = 1
            while k < i:
                print('*', end=' ')
                k += 1
            print('')
            i -= 1

    elif (answer == "9"):
        for i in range(5, 0, -1):
            for j in range(0, i):
                print("* ", end="")

            print("\r")

    elif (answer == "10"):
        k = 2 * 5 - 2
        for i in range(0, 5):

            for j in range(0, k):
                print(end=" ")

            k = k - 2
            for j in range(0, i + 1):
                print("* ", end="")

            print("\r")

    elif (answer == "0"):
        print("Good buy!")
        Exit = True

    else:
        print("input error, try again please!\n")
