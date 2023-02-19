class User:

    def __init__(self, id, name, surname, login, password):
        self.id = id
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password

    def get_id(self):
        return self.id
    def __str__(self):
        return f"******************************************\n" \
               f"id - {self.id}\nname - {self.name}\nsurname - {self.surname}" \
               f"******************************************\n"
