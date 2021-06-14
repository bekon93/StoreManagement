from sm import db
from datetime import datetime

class Employees(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    position = db.Column(db.Text, nullable=False)
    wage = db.Column(db.Integer, nullable=False)


class Items(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)

class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.TIMESTAMP, nullable=False, default=datetime.now())
    itemlist = db.Column(db.Text, nullable=False)
    total = db.Column(db.Float, nullable=False)



