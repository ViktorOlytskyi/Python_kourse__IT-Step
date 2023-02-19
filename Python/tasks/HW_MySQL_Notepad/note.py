class Note:


    def __init__(self, id, user_id, note, date):
        self.id = id
        self.user_id = user_id
        self.note = note
        self.create_date = date

    def set_id(self,id):
        self.id = id

    def __str__(self):
        return f"******************************************\n" \
               f"id - {self.id}\nCreation date: {self.create_date}\nNote: {self.note}" \
               f"\n******************************************\n"
