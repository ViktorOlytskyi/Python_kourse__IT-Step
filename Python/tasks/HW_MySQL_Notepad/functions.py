from mysql.connector import connect, Error

from sql_scripts import *


def create_DB_if_not_exist():
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(CREATE_DB)

    except Error as error:
        print(error)

def create_table_user():
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(CREATE_TABLE_USER)
            coon.commit()

    except Error as error:
        print(error)

def create_table_note():
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(CREATE_TABLE_NOTE)
            coon.commit()

    except Error as error:
        print(error)

def is_login_exist(login):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(f"SELECT * FROM `user` WHERE login = '{login}';")
                if cur.fetchall():
                    return True
                else:
                    return False


    except Error as error:
        print(error)
        return False

def add_new_user_to_DB(name,surname, login, password):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(INSERT_INTO_USER.format(name,surname, login, password))
                coon.commit()


    except Error as error:
        print(error)

def is_password_coorect(login, pas):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(f"SELECT * FROM `user` WHERE login = '{login}' AND password = '{pas}';")
                if cur.fetchall():
                    return True
                else:
                    return False


    except Error as error:
        print(error)

def menu():
    print("1. Add new note\n"
          "2. Delete note\n"
          "3. Edit note\n"
          "4. View note\n"
          "5. View all notes\n"
          "6. View notes by period\n"
          "7. View notes witch incude some words\n"
          "0. Exit")

def get_user_from_DB(login,pas):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(f"SELECT * FROM `user` WHERE login = '{login}' AND password = '{pas}';")
                return cur.fetchall()


    except Error as error:
        print(error)

def add_new_note_to_DB(user_id, note):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(INSERT_INTO_NOTE.format(user_id, note))
                coon.commit()


    except Error as error:
        print(error)

def delete_note_from_DB(id, user_id):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(DELETE_NOTE.format(id, user_id))
                coon.commit()
                return True


    except Error as error:
        return False
        print(error)

def is_note_exists_in_DB(note_id):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(IS_NOTE_EXISTS.format(note_id))
                if cur.fetchall()[0][0] > 0:
                    return True
                else:
                    return False
    except Error as error:
        return False
        print(error)

def update_note_DB(new_note, note_id, user_id):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(UPDATE_NOTE.format(new_note,note_id, user_id))
                coon.commit()
                return True


    except Error as error:
        return False
        print(error)

def select_note_by_id(note_id):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(SELECT_NOTE_BY_ID.format(note_id))

                return cur.fetchall()[0]


    except Error as error:
        return False
        print(error)

def select_all_notes():
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(SELECT_ALL_NOTES)
                return cur.fetchall()

    except Error as error:
        return False
        print(error)

def select_all_notes_by_date(first_date, second_date):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(SELECT_ALL_NOTES_BY_DATE.format(first_date, second_date))
                return cur.fetchall()

    except Error as error:
        print(error)

def select_all_notes_by_word(word):
    try:
        with connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
        ) as coon:
            with coon.cursor() as cur:
                cur.execute(SELECT_ALL_BY_INCLUDE_WORD.format(word))
                return cur.fetchall()

    except Error as error:
        print(error)