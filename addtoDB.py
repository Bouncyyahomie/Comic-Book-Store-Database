import csv
import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('DATABASE'))
db = client.store
supply = db.supply
customers = db.customer
orders = db.order

def add_supply():
    with open("./database/comic.csv") as comic:
        data = csv.reader(comic, delimiter=",")
        for row in data:
            comic = {
                "Name": row[0],
                "Stock": int(row[1]),
                "Price": int(row[2]),
            }
            supply.insert_one(comic)

add_supply()

def add_customer():
    with open("./database/customer.csv") as customer:
        data = csv.reader(customer, delimiter=",")
        for row in data:
            customer = {
                "Name": row[0],
                "Email": row[1],
                "Age": int(row[2]),
            }
            customers.insert_one(customer)

add_customer()

def add_order():
    with open("./database/order.csv") as order:
        data = csv.reader(order, delimiter=",")
        for row in data:
            order = {
                "Name": row[0],
                "Order": row[1],
                "Date": row[2],
            }
            orders.insert_one(order)

# add_order()

