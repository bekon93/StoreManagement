import app as app
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort
from flask_sqlalchemy import SQLAlchemy
from controller import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd1o2g3e4c5o6i7n'

#Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/storemanagement.db'
db = SQLAlchemy(app)



def get_db_connection():
    conn = sqlite3.connect('db/storemanagement.db')
    conn.row_factory = sqlite3.Row
    return conn

#Rederimi i faqes kryesore root
@app.route('/')
def index():
    return render_template('index.html')

#Funksionet show mundesojne shikimin e te dhenave ne databaze per 1 tabele te caktuar
@app.route('/showitems')
def showitems():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return render_template('showitems.html', items=items)

@app.route('/showorders')
def showorders():
    conn = get_db_connection()
    orders = conn.execute('SELECT * FROM orders').fetchall()
    conn.close()
    return render_template('showorders.html', orders=orders)

@app.route('/showemployees')
def showemployees():
    conn = get_db_connection()
    employees = conn.execute('SELECT * FROM employees').fetchall()
    conn.close()
    return render_template('showemployees.html', employees=employees)


#Funksionet Add mundesojne futjen e te dhenave te nje tabele te caktuar ne databaz

@app.route('/addemployees', methods=('GET', 'POST'))
def addemployees():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        wage = request.form['wage']
        if not (name and position and wage):
            flash('Fill all the boxes!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO employees (name, position, wage) VALUES (?, ?, ?)',
            (name, position, wage))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('addemployees.html')

@app.route('/additems', methods=('GET', 'POST'))
def additems():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        if not (name and description and price):
            flash('Fill all the boxes!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO items (name, description, price) VALUES (?, ?, ?)',
            (name, description, price))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('additems.html')

@app.route('/addorders', methods=('GET', 'POST'))
def addorders():
    if request.method == 'POST':
        itemlist = request.form['itemlist']
        total = request.form['total']
        if not (itemlist and total):
            flash('Fill all the boxes!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO orders (itemlist, total) VALUES (?, ?)',
            (itemlist, total))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('addorders.html')



#Funksionet Edit mundesojne Editimin e te dhenave nga nje kolone e caktuar per nje instance te caktuar,
# instanca zgjidhet me ane te id pasi qe eshte primary key

@app.route('/<int:id>/editemployees', methods=('GET', 'POST'))
def editemployees(id):
    employee = get_employee(id)
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        wage = request.form['wage']

        if not (name, position, wage):
            flash('Fill all the fields please!')
        else:
            update_employee(id,name,position,wage)
            return redirect(url_for('index'))

    return render_template('editemployees.html', employee=employee)

@app.route('/<int:id>/edititems', methods=('GET', 'POST'))
def edititems(id):
    item = get_item(id)
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        if not (name and description and price):
            flash('Fill all the fields please!')
        else:
            update_item(id,name,description,price)
            return redirect(url_for('index'))

    return render_template('edititems.html', item=item)

@app.route('/<int:id>/editorders', methods=('GET', 'POST'))
def editorders(id):
    order = get_order(id)
    if request.method == 'POST':
        itemlist = request.form['itemlist']
        total = request.form['total']

        if not (itemlist and total):
            flash('Fill all the fields please!')
        else:
            update_order(id,itemlist, total)
            return redirect(url_for('index'))

    return render_template('editorders.html', order=order)


# Funksionet Delete marrin si parameter id e nje instance te nje tabele dhe bejn fshirjen e instances

@app.route('/<int:id>/deleteemployees', methods=('GET', 'POST'))
def deleteemployees(id):
    delete_employee(id)
    flash('Employee with id "{}" was successfully deleted!'.format(id))
    return redirect(url_for('index'))

@app.route('/<int:id>/deleteitems', methods=('GET', 'POST'))
def deleteitems(id):
    delete_item(id)
    flash('Item with id "{}" was successfully deleted!'.format(id))
    return redirect(url_for('index'))

@app.route('/<int:id>/deleteorders', methods=('GET', 'POST'))
def deleteorders(id):
    delete_order(id)
    flash('Order "{}" was successfully deleted!'.format(id))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

