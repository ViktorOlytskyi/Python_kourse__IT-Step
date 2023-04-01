from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
db = SQLAlchemy(app)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(20))
    notes = db.Column(db.Text)

    @classmethod
    def get_by_last_name(cls, last_name):
        return cls.query.filter_by(last_name=last_name).all()

    @classmethod
    def get_by_first_name(cls, first_name):
        return cls.query.filter_by(first_name=first_name).all()


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    with app.app_context():
        contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@app.route('/', methods=['POST'])
def index_search():
    s_item = request.form['search_field']

    with app.app_context():
        contacts_fn = Contact.get_by_first_name(s_item)
        contacts_ln = Contact.get_by_last_name(s_item)
    if len(contacts_fn) > 0:
        return render_template('index.html', contacts=contacts_fn)
    elif len(contacts_ln) > 0:
        return render_template('index.html', contacts=contacts_ln)
    else:
        return render_template('index.html', message='Не знайдено жодного контакту!')


@app.route('/add_contact')
def show_add_page():
    return render_template('add_contact.html')


@app.route('/add_contact', methods=['POST'])
def add_contact():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    notes = request.form['notes']
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,
                          notes=notes)
    try:
        with app.app_context():
            db.session.add(new_contact)
            db.session.commit()

        return redirect(url_for('index'))
    except:
        return render_template('add_contact.html', message=f"Помилка, вводу такий email вже існує")


@app.route('/del')
def del_item_page():
    return render_template('del.html')


@app.route('/del', methods=['POST'])
def del_item():
    ids = request.form['del_id']

    with app.app_context():
        try:
            contact = Contact.query.get(ids)
            db.session.delete(contact)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return render_template('del.html', message=f"Помилка, такого контакту з id {ids} не існує в списку")


@app.route('/edit_contact')
def edit_item_page():
    return render_template('edit_contact.html')


@app.route('/edit_contact', methods=['POST'])
def edit_item():
    ids = request.form['id_input']
    try:
        checkbox = request.form['checkbox_item']
    except:
        return render_template('edit_contact.html', message=f"Помилка, ви не вибрали жоден пункт меню!")
    new_data = request.form['new_val']

    with app.app_context():
        try:
            contact = Contact.query.get(ids)

            if checkbox == "first_name":
                contact.first_name = new_data
                db.session.commit()
            elif checkbox == "last_name":
                contact.last_name = new_data
                db.session.commit()
            elif checkbox == "email":
                contact.email = new_data
                db.session.commit()
            elif checkbox == "phone_number":
                contact.phone_number = new_data
                db.session.commit()
            elif checkbox == "notes":
                contact.notes = new_data
                db.session.commit()

            return redirect(url_for('index'))
        except:
            return render_template('edit_contact.html',
                                   message=f"Помилка, такого контакту з id {ids} не існує в списку")


if __name__ == '__main__':
    app.run(debug=False)
