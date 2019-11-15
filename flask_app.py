# export FLASK_APP=flask_app.py;flask run

from flask import Flask, render_template, request, flash, url_for, jsonify
import os
import sqlite3

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
with open(PATH + "secrets.txt") as f:
    secret = f.read()
app.secret_key = secret

PATH = os.path.dirname(os.path.realpath(__file__)) + "/"

def get_db():
    return sqlite3.connect(PATH + "chinook.db", isolation_level=None)


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("main.html")

@app.route('/customers', methods=['GET'])
def customers():
    c = get_db().cursor()
    customers = []
    for row in c.execute('select FirstName, LastName,Company,City,Country,Phone,Email from customers limit 5;'):
        d = {
            'first_name': row[0],
            'last_name': row[1],
            'company': row[2],
            'city': row[3],
            'country': row[4],
            'phone': row[5],
            'email': row[6],

        }
        customers.append(d)


    return jsonify(customers)
