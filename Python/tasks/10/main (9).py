# Задание 1
# Написать программу «справочник». Создать два списка
# целых. Один список хранит идентификационные коды,
# второй — телефонные номера. Реализовать меню для
# пользователя:
# ■ Отсортировать по идентификационным кодам;
# ■ Отсортировать по номерам телефона;
# ■ Вывести список пользователей с кодами и телефонами;
# ■ Выход.

ids = [2, 1, 8, 6, 5, 4, 7, 3]
phone_numbers = [685870195, 685855195, 685440195, 685330195, 682270195, 681170195, 685870199, 685875478]


def my_sort(main_list, sub_list):
    swapped = True
    ogr = len(main_list) - 1
    while swapped:
        swapped = False
        for i in range(ogr):
            if main_list[i] > main_list[i + 1]:
                swapped = True
                main_list[i], main_list[i + 1] = main_list[i + 1], main_list[i]
                sub_list[i], sub_list[i + 1] = sub_list[i + 1], sub_list[i]
        ogr -= 1
    print("sort was maded \n")


def sort_by_id(ids, phones):
    my_sort(ids, phones)


def sort_by_phone(ids, phones):
    my_sort(phones, ids)


def output_users(ids, phones):
   
    print('id - phone:')
    for id, phone in zip(ids, phones):
        print(f"{id} - {phone}")

def menu(ids, phones):
    while True:
        text = '***** Menu *****\n' \
              '1 - Sort by id codes\n' \
              '2 - Sort by phone numbers\n' \
              '3 - Output users list with phone numbers and ID\n' \
              '4 - Exit'
        print(text)
        choice = input('Plaese make choose: ')
        if choice == '1':
            sort_by_id(ids, phones)
        elif choice == '2':
            sort_by_phone(ids, phones)
        elif choice == '3':
            output_users(ids, phones)
        elif choice == '4':
            break
        else:
            pass

        print('\n\n\n')


menu(ids, phone_numbers)



# Задание 2
# Написать программу «книги». Создать два списка
# с данными. Один список хранит названия книг, второй —
# годы выпуска. Реализовать меню для пользователя:
# ■ Отсортировать по названию книг;
# ■ Отсортировать по годам выпуска;
# ■ Вывести список книг с названиями и годами выпуска;
# ■ Выход;


# years = [1997, 1980, 2001, 2002, 1960, 1861, 2020, 1751]
# book_names = ["agata kristi", "robin good", "amile poaro", "harry potter", "war and pease", "broklin", "putin huilo", "how russia lost the war"]


# def my_sort(main_list, sub_list):
#     swapped = True
#     ogr = len(main_list) - 1
#     while swapped:
#         swapped = False
#         for i in range(ogr):
#             if main_list[i] > main_list[i + 1]:
#                 swapped = True
#                 main_list[i], main_list[i + 1] = main_list[i + 1], main_list[i]
#                 sub_list[i], sub_list[i + 1] = sub_list[i + 1], sub_list[i]
#         ogr -= 1
#     print("sort was maded \n")
    
# def sort_by_id(years, book_names):
#     my_sort(years, book_names)


# def sort_by_phone(book_names, years):
#     my_sort(book_names, years)

# def output_books(years, book_names):
   
#     print('id - phone:')
#     for id, phone in zip(years, book_names):
#         print(f"{id} - {phone}")
        
# def menu(years, book_names):
#     while True:
#         text = '***** Menu *****\n' \
#               '1 - Sort by book name\n' \
#               '2 - Sort by book year\n' \
#               '3 - Output books\n' \
#               '4 - Exit'
#         print(text)
#         choice = input('Plaese make choose: ')
#         if choice == '1':
#             sort_by_id(years, book_names)
#         elif choice == '2':
#             sort_by_phone(years, book_names)
#         elif choice == '3':
#             output_books(years, book_names)
#         elif choice == '4':
#             break
#         else:
#             pass

#         print('\n\n\n')        
        
# menu(book_names,years)