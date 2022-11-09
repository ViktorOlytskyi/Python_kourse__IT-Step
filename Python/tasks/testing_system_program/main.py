# Реализовать полнофункциональную систему тестирования.
# В системе должны быть 2 режима: администратор и тестируемый.
# Описание режима работа для Тестируемого (в дальнейшем гость):
# ■ Для входа в систему гость должен зарегистрироваться данная процедура
# выполняется один раз, при дальнейших входах в систему доступ идет по логину
# и паролю.
# ■ При регистрации нужно указывать Ф.И.О., домашний адрес, телефон.
# ■ Важно, чтобы логины для пользователей были уникальными.
# ■ После входа гость имеет возможность просмотреть свои предыдущие
# результаты тестирования, сдать новое тестирование. Тестирование может
# осуществляться по различным категориям знаний.
# Например:
# Математика (раздел) ->
# Дискретная математика (конкретный тест) ->
# Математический Анализ (конкретный тест)
# Физика (раздел) ->
# Квантовая физика (конкретный тест) ->
# Механика (конкретный тест)
# ■ После сдачи теста гость видит результат тестирования, количество правильно
# отвеченных вопросов, процент правильных ответов и полученную оценку.
# ■ Оценивание нужно вести на основании 12 балльной системы, привязанной к
# количеству вопросов теста.
# ■ Пароли и логины гостей хранятся в зашифрованном виде.
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
# файла (и в файл).
import os
import pickle

ADMIN_FILENAME = 'admin.bin'
USERS_FILENAME = 'users.bin'
CATEGORIES_FILENAME = "data.pickle"
STATISTICS_FILENAME = "statistics.txt"

users = []
tests = []
tests2 = []
categories = {}


class User:

    def __init__(self):
        self.__fullname = input("Будь ласка, введіть ім'я користувача ")
        self.__address = input("Будь ласка, введіть адресу користувача ")
        self.__phone = input("Будь ласка, введіть телефон користувача ")
        self.__login = input("Будь ласка, придумайте логін користувача ")
        self.__password = input("Будь ласка, придумайте пароль користувача ")
        self.__last_score = 0
        self.__last_mistakes = 0
        self.__last_test_category = ""
        self.__percent_write_ansaw_test = 0

    def __str__(self):
        return f"Ім'я - {self.__fullname}\nАдреса - {self.__address}\nТелефон - {self.__phone}\nЛогін - {self.__login}\nПароль - {self.__password}\n*******************************"

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

    def set_last_mistake(self, mistacke):
        self.__last_mistakes = mistacke

    def set_last_category(self, cat):
        self.__last_test_category = cat

    def set_percent_write_ansaw_test(self, percent):
        self.__percent_write_ansaw_test = percent

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

    def get_last_score(self):
        return self.__last_score

    def get_last_mistake(self):
        return self.__last_mistakes

    def get_last_category(self):
        return self.__last_test_category

    def get_percent_last_test(self):
        return self.__percent_write_ansaw_test



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

    def __init__(self):
        self._answers = []
        self._write_answers = []
        self._ask = ""

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

    def change_ask(self):
        ask = input("Введіть нове запитання ")
        self._ask = ask
        self._answers = []
        self._write_answers = []
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

    def get_write_answers(self):
        return self._write_answers


def tests_menu():
    while True:
        a = input("1. Створити тест\n"
                  "2. Змінити тест\n"
                  "3. Видалити тест\n"
                  "4. Експортувати в файл\n"
                  "5. Імпортувати з файлу\n"
                  "6. Вихід\n")
        if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6":
            return a
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
        if res == "1" or res == "2" or res == "3" or res == "4" or res == "5" or res == "6" or res == "7" or res == "8" or res == "9":
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
    global USERS_FILENAME
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
    print("Вітаємо в системі тестування!\nЦе перший вхід!\nПотрібно зареєструватись Адміністратору!\n\n")
    admin = Admin()
    admin.set_login()
    admin.set_password()
    try:
        with open(ADMIN_FILENAME, "wb") as file:
            pickle.dump(admin, file)
    except Exception as ex:
        print(f"\n{ex}")
        exit()

# читання файлу тестів:
try:
    with open('data.pickle', 'rb') as f:
        categories = pickle.load(f)
        print()
except:
    print(
        "Помилка читання файлу тестів, схоже ще не додано жодного тесту!\nЗверніться до адміністратора для створення нового тесту!")

ex = False
while ex != True:
    ans = input("Виберіть режим:\n1 - Адміністратор\n2 - Користувач\n3 - Вихід\n")
    admin_c_try = 3
    if ans == '1':

        log = input("Введіть логін ")
        if log == admin.get_login():
            while admin_c_try!=0:
                pas = input("Введіть пароль ")
                if pas != admin.get_password():
                    admin_c_try-=1
                    print(f"Невірний пароль! Кількість спроб залишилось: {admin_c_try}")
                else:
                    admin_c_try = 0
                    print("Вітаємо! Ви зайшли в режимі адміністратора!")
                    res = ""
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
                                if len(users) == 0:
                                    print("Ще не створено жодного користувача!")
                                else:
                                    for user in users:
                                        print(user)
                        elif res == "7":
                            zzz = ""
                            while True:
                                zzz = input(
                                    "1. Перегнянути статистику по всіх користувачах\n2. Експортувати статистику в файл\n")
                                if zzz == "1" or zzz == "2":
                                    break
                                else:
                                    print("Помилка вводу, виберіть пункт меню!")

                            strings = []
                            string = ""
                            with open(USERS_FILENAME, "rb") as file:
                                users = pickle.load(file)
                                if len(users) == 0:
                                    print("Ще не створено жодного користувача!")
                                else:
                                    if zzz == "1":
                                        for user in users:
                                            string = f"Користувач {user.get__fullname()}:\n" \
                                                     f"Категорія в якій пройдено тест: {user.get_last_category()}\n" \
                                                     f"Оцінка за тест: {user.get_last_score()}\n" \
                                                     f"Правильних відповідей: {user.get_last_score()}\n" \
                                                     f"Неправильних відповідей: {user.get_last_mistake()}\n" \
                                                     f"Відсоток правильних відповідей: {user.get_percent_last_test()}\n" \
                                                     f"****************************************************************"
                                            strings.append(string)
                                            print(string)
                                    elif zzz == "2":
                                        for user in users:
                                            string = f"Користувач {user.get__fullname()}:\n" \
                                                     f"Категорія в якій пройдено тест: {user.get_last_category()}\n" \
                                                     f"Оцінка за тест: {user.get_last_score()}\n" \
                                                     f"Правильних відповідей: {user.get_last_score()}\n" \
                                                     f"Неправильних відповідей: {user.get_last_mistake()}\n" \
                                                     f"Відсоток правильних відповідей: {user.get_percent_last_test()}\n" \
                                                     f"****************************************************************\n"
                                            strings.append(string)
                                        with open(STATISTICS_FILENAME, "w") as file:
                                            for strin in strings:
                                                file.write(strin)
                                        print(f"Файл статистики успішно створено, назва файлу {STATISTICS_FILENAME}")

                        elif res == "8":
                            a = ""
                            while a != "6":
                                a = tests_menu()

                                if a == "1":
                                    while True:
                                        try:
                                            cat = input("Введіть нову категорію тесту ")
                                            break
                                        except:
                                            print("Помилка вводу, введіть число!")

                                    print("Потрібно ввести 12 запитань:")
                                    for i in range(0, 12):
                                        ask = Ask()
                                        created_test = ask.create_ask()
                                        tests.append(created_test)

                                    categories[cat] = tests
                                    write_file_tests()
                                    print("Нові тести успішно створено!")

                                elif a == "2":
                                    cc = -1
                                    while True:
                                        print("виберіть тест який бажаєте змінити: ")
                                        for i, key in enumerate(categories.keys()):
                                            print(f"{i + 1}. {key}")
                                        try:
                                            cc = int(input())
                                            break
                                        except:
                                            print("Невірний ввод, виберіть пункт меню")
                                    n = int(input("Введіть номер запитання яке хочете змінити "))
                                    print("Вводьте нові дані:")
                                    m = 1
                                    for key, value in categories.items():
                                        if m == cc:
                                            t = []
                                            value[n - 1].change_ask()
                                            for test in value:
                                                t.append(test)
                                            categories[key] = t
                                            write_file_tests()
                                            print("Зміни успішно внесено!")
                                            break
                                        m += 1

                                elif a == "3":
                                    del_cat = input("Введіть назву категорії (тесту) яку бажаєте видалити ")
                                    if del_cat in categories.keys():
                                        del categories[del_cat]
                                        print(f"Тест {del_cat} успішно видалено ")
                                        write_file_tests()
                                    else:
                                        print("Такої категорії не існує, перевірте введені дані")

                                elif a == "4":
                                    print(f"Тести успішно експортовано в файл, назва файлу {CATEGORIES_FILENAME}")
                                elif a == "5":
                                    FILENAME = input(
                                        "Введіть назву файлу для імпорту тестів\nФайл має знаходитись в корінній папці програми та мати розширення \".pickle\"") + ".pickle"
                                    if os.path.getsize(FILENAME) > 0:
                                        try:
                                            with open(FILENAME, "rb") as file:
                                                categories = pickle.load(file)
                                                write_file_tests()
                                                print(f"Дані з файлу {FILENAME} успішно еспортовано!")

                                        except Exception as ex:
                                            print(
                                                f"Помилка читаня файлу!\nСхоже ви ввелели не вірну назву файлу, перевірте назву!")
                                    else:
                                        print("Ви намагаєтесь імпортувати дані з пустого файлу, імпорт не можливий!")


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
                                    print(f"{i + 1}. {key}")
                                try:
                                    c = int(input())
                                    break
                                except:
                                    print("Невірний ввод, виберіть пункт меню")
                            m = 1
                            categ = ""
                            write_answ_count = 0
                            wrong_answ_count = 0
                            for key, value in categories.items():
                                if m == c:
                                    categ = key
                                    for i in value:
                                        print(i.get_ask())
                                        for j in i.get_answers():
                                            print(j)
                                        print("*********************************************************")
                                        while True:
                                            try:
                                                a = int(input("Введіть номер правильної відповіді "))
                                                break
                                            except:
                                                print("Вводьте число!")
                                        if str(a) in i.get_write_answers():
                                            write_answ_count += 1
                                        else:
                                            wrong_answ_count += 1
                                m += 1
                            p = write_answ_count / 12 * 100
                            print(f"\nТест закінчено, ваша оцінка {write_answ_count}")
                            print(
                                f"Кількість правильних відповідей {write_answ_count}\nКількість помилок {wrong_answ_count}")
                            print(f"% правильних відповідей {p}")
                            ind = search_user(l)
                            users[ind].set_last_score(write_answ_count)
                            users[ind].set_last_mistake(wrong_answ_count)
                            users[ind].set_last_category(categ)
                            users[ind].set_percent_write_ansaw_test(p)
                            write_file_users()

                        elif r == "2":
                            ind = search_user(l)
                            try:

                                print(f"Остання категорія по якій пройдено тест: {users[ind].get_last_category()}")
                                print(f"Остання оцінка за тест: {users[ind].get_last_score()}")
                                print(f"Кількість помилок в тесті: {users[ind].get_last_mistake()}")
                            except:
                                print("Ви не пройшли ще жодного тесту, пройдіть тест для перегляду статистики!")
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
        print("Помилка вводу! Введіть 1 або 2\n")
