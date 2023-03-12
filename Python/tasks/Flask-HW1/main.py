from flask import Flask, request, make_response, render_template, url_for
import datetime
import random
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/management')
def management():
    return render_template('management.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/history/people')
def people():
    return render_template('people.html')


@app.route('/history/photos')
def photos():
    return render_template('photos.html')


@app.route('/facts')
def facts():
    return render_template('facts.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.errorhandler(404)
def news_not_found(e):
    re_contacts = "^http:\/\/127\.0\.0\.1:5000\/contacts.*$"
    re_facts = "^http:\/\/127\.0\.0\.1:5000\/facts.*$"
    re_history = "^http:\/\/127\.0\.0\.1:5000\/history/.*$"
    re_management = "^http:\/\/127\.0\.0\.1:5000\/management.*$"
    re_news = "^http:\/\/127\.0\.0\.1:5000\/news.*$"
    re_people = "^http:\/\/127\.0\.0\.1:5000\/history/people.*$"
    re_photoes = "^http:\/\/127\.0\.0\.1:5000\/history/photos.*$"
    url = str(request.url)

    x1 = re.search(re_contacts, url)
    x2 = re.search(re_facts, url)
    x3 = re.search(re_history, url)
    x5 = re.search(re_management, url)
    x6 = re.search(re_news, url)
    x7 = re.search(re_people, url)
    x8 = re.search(re_photoes, url)

    if x1 != None:
        return render_template('contacts.html')
    if x2 != None:
        return render_template('facts.html')
    if x7 != None:
        return render_template('people.html')
    if x8 != None:
        return render_template('photos.html')
    if x3 != None:
        return render_template('history.html')
    if x5 != None:
        return render_template('management.html')
    if x6 != None:
        return render_template('news.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
