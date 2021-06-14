from model import Employees, Items, Orders
from sm import db

#Employees

def get_employees():
    return Employees.query.all()

def get_employee(employee_id):
    return Employees.query.filter_by(id=employee_id).first()

def create_employee(name, position, wage):
    employee = Employees(name=name, position=position, wage=wage)
    db.session.add(employee)
    db.session.commit()

def update_employee(employee_id, name, position, wage):
    employee = get_employee(employee_id)
    employee.name = name
    employee.position = position
    employee.wage = wage
    db.session.commit()

def delete_employee(employee_id):
    employee = get_employee(employee_id)
    db.session.delete(employee)
    db.session.commit()

#Items

def get_items():
    return Items.query.all()

def get_item(item_id):
    return Items.query.filter_by(id=item_id).first()

def create_item(name, description, price):
    item = Items(name=name, description=description, price=price)
    db.session.add(item)
    db.session.commit()

def update_item(item_id, name, description, price):
    item = get_item(item_id)
    item.name = name
    item.description = description
    item.price = price
    db.session.commit()

def delete_item(item_id):
    item = get_item(item_id)
    db.session.delete(item)
    db.session.commit()


#Orders

def get_orders():
    return Orders.query.all()

def get_order(order_id):
    return Orders.query.filter_by(id=order_id).first()

def create_order(itemlist, total):
    order = Orders(itemlist=itemlist, total=total)
    db.session.add(order)
    db.session.commit()

def update_order(order_id, itemlist, total):
    order = get_order(order_id)
    order.itemlist = itemlist
    order.total = total
    db.session.commit()

def delete_order(order_id):
    order = get_order(order_id)
    db.session.delete(order)
    db.session.commit()



