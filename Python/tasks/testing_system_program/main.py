# Описание режима работы для Администратора (в дальнейшем админ):
# ■ В системе может быть только один админ, логин и пароль админа задается при
# первом входе в программу.
# ■ В дальнейшем пароль и логин можно изменить (но данную возможность имеет
# только админ).
# ■ Пароль и логин необходимо хранить только в зашифрованном виде.
# ■ При работе с системой админ имеет следующие возможности:
# ▶ Управление пользователями — создание, удаление, модификация
# пользователей.
# ▶ Просмотр статистики — просмотр результатов тестирования в общем по
# категориям, по конкретным тестам, по конкретным пользователям. Результаты
# просмотра статистики можно вывести в файл.
# ▶ Управление тестированием — админ имеет возможность добавлять
# категории,тесты, вопросы к тестам, задавать правильные и неправильные
# ответы, импортировать и экспортировать категории и тесты с вопросами из
# файла (и в файл)

# ■ При регистрации нужно указывать Ф.И.О., домашний адрес, телефон.
import os
import pickle
import json

ADMIN_FILENAME = 'admin.bin'
USERS_FILENAME = 'users.bin'
CATEGORIES_FILENAME = "data.pickle"
# TESTS_FILENAME = "tests.bin"

users = []
tests = []
tests2 = []
categories = {}



class User:
    __last_score = 0
    def __init__(self):
        self.__fullname = input("Будь ласка, введіть ім'я користувача ")
        self.__address = input("Будь ласка, введіть адресу користувача ")
        self.__phone = input("Будь ласка, введіть телефон користувача ")
        self.__login = input("Будь ласка, придумайте логін користувача ")
        self.__password = input("Будь ласка, придумайте пароль користувача ")

    def __str__(self):
        return f"{self.__fullname}\n{self.__address}\n{self.__phone}\n{self.__login}\n{self.__password}\n*******************************"
    def set_fullname(self):
        self.__fullname = input("Будь ласка, введіть нове ім'я користувача ")
    def set_address(self):
        self.__address = input("Будь ласка, введіть нову адресу користувача ")
    def set_phone(self):
        self.__phone = input("Будь ласка, введіть новий телефон користувача ")
    def set_login(self):
        self.__login = input("Будь ласка, введіть новий логін користувача ")
    def set_password(self):
        self.__password = input("Будь ласка, введіть новий пароль користувача ")
    def set_last_score(self, score):
        self.__last_score = score
    def get__fullname(self):
        return self.__fullname
    def get__address(self):
        return self.__address
    def get__phone(self):
        return self.__phone
    def get__login(self):
        return self.__login
    def get__password(self):
        return self.__password
    def get_last_score(self, score):
        return self.__last_score

class Admin:

    __login = None
    __password = None


    def set_login(self, ):
        login = input("Будь ласка, введіть новий логін ")
        self.__login = login

    def set_password(self):
        password = input("Будь ласка, введіть новий пароль ")
        self.__password = password

    def get_login(self):
        return self.__login
    def get_password(self):
        return self.__password

class Ask:
    # _ask = ""
    # _answers = []
    # _write_answers = []

    def __init__(self):
        self._answers = []
        self._write_answers = []
        self._ask = ""
    # def __init__(self):
    #
    #     ask = input("Введіть запитання ")
    #     self._ask = ask
    #     while True:
    #         try:
    #             i = int(input("Скільки варіантів відповідей на запитання? "))
    #             break
    #         except:
    #             print("Помилка вводу, вводьте число!")
    #     j = 1
    #     while i!=0:
    #         answer = input(f"Введіть {j}-й варіант відповіді ")
    #         self._answers.append(answer)
    #         i-=1
    #         j+=1
    #     while True:
    #         try:
    #             i = int(input("Скільки правильних відповідей на запитання? "))
    #             break
    #         except:
    #             print("Помилка вводу, вводьте число!")
    #     while i!=0:
    #         write_answer = input("Введіть номер правильної відповіді ")
    #         self._write_answers.append(write_answer)
    #         i-=1
    def create_ask(self):
        ask = input("Введіть запитання ")
        self._ask = ask
        while True:
            try:
                i = int(input("Скільки варіантів відповідей на запитання? "))
                break
            except:
                print("Помилка вводу, вводьте число!")
        j = 1
        while i != 0:
            answer = input(f"Введіть {j}-й варіант відповіді ")
            self._answers.append(answer)
            i -= 1
            j += 1
        while True:
            try:
                i = int(input("Скільки правильних відповідей на запитання? "))
                break
            except:
                print("Помилка вводу, вводьте число!")
        while i != 0:
            write_answer = input("Введіть номер правильної відповіді ")
            self._write_answers.append(write_answer)
            i -= 1
        return self
    def get_ask(self):
        return self._ask
    def get_answers(self):
        return self._answers

# class Test(Ask):
#     # __category = None
#     # __asks = []
#     # __score = 0
#
#     def __init__(self,category):
#         self.__category = category.lower()
#         self.__asks = []
#         self.__score = 0
#
#     def create_test(self):
#         # category = input("Будь ласка, введіть категорію ").lower()
#         #
#         # self.__category = category
#         self.__asks.append(Ask().create_ask())
#         return self
#
#     def get_category(self):
#         return self.__category
#
#     def get_asks(self):
#         return self.__asks
#     def set_score(self,score):
#         self.__score = score



# def category_reading():
#     global categories
#     if os.path.getsize(CATEGORIES_FILENAME) > 0:
#         try:
#             with open(CATEGORIES_FILENAME, "rb") as file:
#                 categories = pickle.load(file)
#                 i = 1
#                 for categorie in categories:
#                     print(f"{i}. {categorie}")
#                     i+=1
#         except Exception as ex:
#             print(f"\n{ex}")
#             exit()
#         print()
#     else:
#         print("Ще не сворена жодна з категорій тестування! Зверніться до адміністратора будь ласка!")

def tests_menu():
    while True:
        a = input("1. Створити тест\n"
              "2. Змінити тест\n"
              "3. Створити категорію\n"
              "4. Видалити тест\n"
              "5. Видалити категорію\n"
              "6. Експортувати в файл\n"
              "7. Імпортувати з файлу\n"
              "8. Вихід\n")
        if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6"or a == "7":
            return a
        elif a == "8":
            break
        else:
            print("Помилка вводу, виберіть  пункт меню!")

def admin_menu():
    ex = False
    while ex != True:
        res = input("\n1. Змінити логін\n"
              "2. Змінити пароль\n"
              "3. Створити користувача\n"
              "4. Змінити дані користувача\n"
              "5. Видалити користувача\n"
              "6. Перегляд всіх користувачів\n"
              "7. Перегляд статистики\n"
              "8. Управління тестуванням\n"
              "9. Вихід\n")
        if res == "1" or res == "2" or res == "3" or res == "4" or res == "5" or res == "6" or res == "7"or res == "8"or res == "9":
            return res
            ex = True
        else:
            print("Помилка введення! Спробуйте ще!")
def user_menu():
    ex = False
    while ex != True:
        res = input("\n1. Пройти тестування\n"
              "2. Переглянути результат попереднього тестування\n"
              "3. Вихід\n")
        if res == "1" or res == "2" or res == "3":
            return res
            ex = True
        else:
            print("Помилка введення! Спробуйте ще!")
def search_user(user_login):
    with open(USERS_FILENAME, "rb") as file:
        global users
        users = pickle.load(file)
        index = 0
        for user in users:
            if user.get__login() == user_login:
                return index
            index += 1
        return None
def write_file_users():
    global  USERS_FILENAME
    global users
    try:
        with open(USERS_FILENAME, "wb") as file:
            pickle.dump(users, file)

    except Exception as ex:
        print(f"\n{ex}")
        exit()
def write_file_tests():
    global CATEGORIES_FILENAME
    global categories
    try:
        with open(CATEGORIES_FILENAME, "wb") as file:
            # pickle.dump([foo], f, -1)
            pickle.dump(categories, file)

    except Exception as ex:
        print(f"\n{ex}")
        exit()
def create_new_user():
    out = False
    while out != True:
        user = User()
        if search_user(user.get__login()) == None:
            users.append(user)
            write_file_users()
            print(f"Користувача {user.get__login()} успішно створено")
            out = True
        else:
            print(f"Користувач з логіном {user.get__login()} існує, придумайте інший логін")
            while True:
                a = input("Спробувати знову?\n1. Так\n2. Ні-(Вихід)")
                if a == "1":
                    break
                elif a == "2":
                    out = True
                    break
                else:
                    print("Нівірне введення! Введіть 1 або 2")

if os.path.getsize(CATEGORIES_FILENAME) > 0:
    try:
        with open(CATEGORIES_FILENAME, "rb") as file:
            categories = pickle.load(file)

    except Exception as ex:
        print(f"\n{ex}")
        exit()
else:
    categories = {}

if os.path.getsize(ADMIN_FILENAME) > 0:
    try:
        with open(ADMIN_FILENAME, "rb") as file:
            admin = pickle.load(file)
    except Exception as ex:
        print(f"\n{ex}")
        exit()
    print()
else:
    print("Вітаємо в системі тестування!\nЦе перший вхід!\nПотрібно зареструватись Адміністратору!\n\n")
    admin = Admin()
    admin.set_login()
    admin.set_password()
    try:
        with open(ADMIN_FILENAME, "wb") as file:
            pickle.dump(admin, file)
    except Exception as ex:
        print(f"\n{ex}")
        exit()


# t = Test()
# # data = t.create_test()
#
# cat = {}
#
# cat[data.get_category()] = data
#
# # сохранение в файл
# with open('data.pickle', 'wb') as f:
#     pickle.dump(cat, f)
#




# чтение из файла
try:
    with open('data.pickle', 'rb') as f:
        categories = pickle.load(f)
        print()
except:
    print("Помилка читання файлу тестів")
# for key, val in data_new.items():
#     tests.append(val)

        # x = None
        # # with open("t.bin", "wb") as file:
        # #     pickle.dump(test, file)
        # # with open("t.bin", "rb") as file:
        # #     x = pickle.load(file)


        #
        # print("X:", data)

        # for key, value in categories.items():
        #     print(key, ":", value)
        #     # for i in value:
        #     #     print(i.get_asks())
        #     # for i in value:
        #     #     # print(i)
        #     #     for j in i.get_asks():
        #     #         print(j)


ex = False
while ex != True:
    ans = input("Виберіть режим:\n1 - Адміністратор\n2 - Користувач\n3 - Вихід\n")
    if ans == '1':

        log = input("Введіть логін ")
        if log == admin.get_login():
            pas = input("Введіть пароль ")
            if pas != admin.get_password():
                print("Невірний пароль!")
            else:
                print("Вітаємо! Ви зайшли в режимі адміністратора!")
                res=""
                while res != "9":
                    res = admin_menu()
                    if res == "1":
                        admin.set_login()
                        try:
                            with open(ADMIN_FILENAME, "wb") as file:
                                pickle.dump(admin, file)
                                print("Логін адміністратора успішно змінено")
                        except Exception as ex:
                            print(f"\n{ex}")
                            exit()
                    elif res == "2":
                        admin.set_password()
                        try:
                            with open(ADMIN_FILENAME, "wb") as file:
                                pickle.dump(admin, file)
                                print("Пароль адміністратора успішно змінено")
                        except Exception as ex:
                            print(f"\n{ex}")
                            exit()
                    elif res == "3":
                        create_new_user()
                    elif res == "4":
                        l = input("Введіть логін користувача для пошуку в БД ")
                        i = search_user(l)

                        if i != None:
                            print(f"Користувача {l} знайдено!")
                            while True:
                                data = input("Які дані потрібно змінити?\n\n"
                                             "1. ПІБ\n"
                                             "2. Адресу\n"
                                             "3. Телефон\n"
                                             "4. Логін\n"
                                             "5. Пароль\n"
                                             "6. Вийти\n")
                                if data == "1":
                                    users[i].set_fullname()
                                    write_file_users()
                                    print(f"ПІБ {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "2":
                                    users[i].set_address()
                                    write_file_users()
                                    print(f"Адресу {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "3":
                                    users[i].set_phone()
                                    write_file_users()
                                    print(f"Телефон {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "4":
                                    users[i].set_login()
                                    write_file_users()
                                    print(f"Логін {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "5":
                                    users[i].set_password()
                                    write_file_users()
                                    print(f"Пароль {users[i].get__login()} успішно змінено")
                                    break
                                elif data == "6":
                                    break
                                else:
                                    print("Помилка вводу, введіть цифру від 1 до 6")
                        else:
                            print(f"{l} не знайдено, спробуйте ще!")
                    elif res == "5":
                        l = input("Введіть логін користувача для видалення ")
                        i = search_user(l)
                        if i != None:
                            users.pop(i)
                            write_file_users()
                            print(f"Користувача {l} знайдено та успішно видалено!")
                        else:
                            print(f"{l} не знайдено, спробуйте ще!")
                    elif res == "6":
                        with open(USERS_FILENAME, "rb") as file:
                            users = pickle.load(file)
                            for user in users:
                                print(user)
                    elif res == "7":
                        pass
                    elif res == "8":
                        a = tests_menu()
                        if a == "1":
                            while True:
                                try:
                                    cat = input("Введіть нову категорію тесту ")
                                    break
                                except:
                                    print("Помилка вводу, введіть число!")
                            # for i in range(0, q):
                            #     test = Test()
                            #     created_test = test.create_test()
                            #     # tests.update({test.__test_name(): test})
                            #     # cat =
                            #     if test.get_category() not in categories.keys():
                            #         print("Було створено нову категорію тестів")
                            #     tests.append(created_test)
                            #
                            # for test in tests:
                            #     arr = []
                            #     arr.append(test)
                            #     categories[test.get_category()] = arr

                            print("Потрібно ввести 12 запитань:")
                            for i in range(0,2):
                                ask = Ask()
                                created_test = ask.create_ask()
                                tests.append(created_test)

                            categories[cat] = tests
                            write_file_tests()
                            print("Нові тести успішно створено!")


                        elif a == "2":
                            pass
                        elif a == "3":
                            pass
                        elif a == "4":
                            pass
                        elif a == "5":
                            pass
                        elif a == "6":
                            pass
                        elif a == "7":
                            pass
                    elif res == "9":
                        print("До побачення!")


        else:
            print("Невірний логін!")
        ex = True
    elif ans == "2":
        while True:
            m = input("1. Вхід\n"
                  "2. Реєстрація\n"
                  "3. Вийти\n")
            if m == "1":
                with open(USERS_FILENAME, "rb") as file:
                    users = pickle.load(file)

                l = input("Введіть логін користувача ")
                ind = search_user(l)
                if ind == None:
                    print("Користувача з таким логіном не існує, перевірте введені дані або зареєструйтесь!")
                else:
                    p = input("Введіть пароль користувача ")
                    if users[ind].get__password() != p:
                        print("Ви ввели не вірний пароль!")
                    else:
                        print("Вітаємо в системі тестування!")
                        r = user_menu()
                        if r == "1":
                            c = -1
                            while True:
                                print("Виберіть категорію: ")
                                for i, key in enumerate(categories.keys()):
                                    print(f"{i+1}. {key}")
                                try:
                                   c = int(input())
                                   break
                                except:
                                    print("Невірний ввод, виберіть пункт меню")
                            m=1
                            for key, value in categories.items():
                                if m == c :
                                    for i in value:
                                        print(i.get_ask())
                                        for j in i.get_answers():
                                            print(j)
                                m+=1


                        elif r == "2":
                            print(f"Остання оцінка за тест: {users[ind].get_last_score()}")
                        elif r == "3":
                            break

            elif m == "2":
                create_new_user()
            elif m == "3":
                break
            else:
                print("Помилка вводу, виберіть пункт меню!")
        ex = True
    elif ans == "3":
        print("До побачення!")
        ex = True
    else:
        print("Помилка вводу! Введіть 1 або 2 \n")