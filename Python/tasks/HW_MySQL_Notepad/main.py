from mysql.connector import connect, Error
from sql_scripts import *
from functions import *
from user import *
from note import *
import re



create_DB_if_not_exist()
create_table_user()
create_table_note()


print("Hi, this is Notepad program!\n")
while True:
    ans = input("Do you have registered account in this program?\npress 'Y' to YES,'n' to NO ")
    if ans == 'y':

        while True:
            l = input("please input your login ")
            if is_login_exist(l):

                break
            else:
                print("Such login NOT exists, try again please!")
        while True:
            p = input("please input your password ")
            if is_password_coorect(l, p):
                print("Congratulations!\nWelcome to notepad system!")
                uinf = get_user_from_DB(l,p)
                user = User(uinf[0][0],uinf[0][1],uinf[0][2],uinf[0][3],uinf[0][4])
                break
            else:
                print("Wrong password please, try again!")
        c = None
        while c != '0':
            menu()
            c = input("Please make your choice, enter menu point number ")
            if c == '1':
                new_note = input("Please, input your new note ")
                add_new_note_to_DB(user.get_id(), new_note)
                print("New note was successful added!")
            elif c == '2':
                del_note = input("Please, input your note id, to delete it ")
                if delete_note_from_DB(int(del_note), user.get_id()):
                    print("Note successful deleted!")
                else:
                    print("Delete error, please check entered information, and try again!")
            elif c == '3':
                note_id = input("please, input note id to change it ")
                if is_note_exists_in_DB(note_id):
                    changed_note = input("please, input your new note ")
                    update_note_DB(changed_note,note_id, user.get_id())
                    print(f"Your note with id {note_id} was successful updated!")
                else:
                    print(f"There is no one note with id {note_id}, please try again!")
            elif c == '4':
                note_id_view = input("please, input note id to view it ")
                if is_note_exists_in_DB(note_id_view):
                    note_DB = select_note_by_id(note_id_view)
                    note = Note(note_DB[0],note_DB[1],note_DB[2], note_DB[3])
                    print(note)
                else:
                    print(f"There is no one note with id {note_id_view}, please try again!")
            elif c == '5':
                print("There is your all notes:")
                notes_DB = select_all_notes()
                for n in notes_DB:
                    note_fr_DB = Note(n[0], n[1], n[2], n[3])
                    print(note_fr_DB)
            elif c == '6':
                regex = "^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$"
                while True:
                    sdate = input("Please input start period date in format \"YYYY-MM-DD\" ")
                    print()
                    if re.search(regex, sdate) != None:
                        break
                    else:
                        print("Wrong data input, please try again!\n")

                while True:
                    fdate = input("Please input period finish date in format \"YYYY-MM-DD\" ")
                    if re.search(regex, fdate) != None:
                        break
                    else:
                        print("Wrong data input, please try again!\n")
                notes_DB_by_date = select_all_notes_by_date(sdate,fdate)
                if len(notes_DB_by_date) > 0:
                    for n in notes_DB_by_date:
                        note_fr_DB = Note(n[0], n[1], n[2], n[3])
                        print(note_fr_DB)
                else:
                    print(f"There is no one note in such ({sdate}:{fdate}) period")

            elif c == '7':
                word = input("Please input word to search ")
                notes = select_all_notes_by_word(word)
                if len(notes) > 0:
                    for n in notes:
                        note_fr_DB = Note(n[0], n[1], n[2], n[3])
                        print(note_fr_DB)
                else:
                    print(f"There is no one note with such word {word}!")

            elif c == '0':
                print("Good bye!")
            else:
                print("Input error, enter menu point number please!")
        break

    elif ans == 'n':
        print("Ok. let's start your registration\n")
        name = input("please input your name ")
        surname = input("please input your surname ")

        while True:

            lr = input("please input your new login ")

            if is_login_exist(lr):
                print("Such login exists, try again please!")

            else:
                break
        pr = input("please input your new password ")
        add_new_user_to_DB(name, surname, lr, pr)
        break
    else:
        print("input error, try again")