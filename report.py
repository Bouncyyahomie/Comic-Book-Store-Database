import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Jakkrathorn:Bouya4710@finalproject.nt7cb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.store
supply = db.supply
customers = db.customer
orders = db.order

# 1: Find the number of orders on 12 may 2021?
def report1():
    date = orders.find({"Date":"2021-05-12"})
    print(f"On 12 may has {date.count()} orders.")

report1()

# report 2: Find how much this store gets from input comic book?
def report2():
    get = input("Enter name of comic book: ")
    order = orders.find({"Order":get})
    price = supply.find({"Name":get})
    for data in price:
        get_price = data
    order_price = get_price["Price"]
    print(f"This store get money from selling {get} is {order.count() * int(order_price)} baht.")

# report2()

#report 3: How many books in stock?
def report3():
    get_stock = []
    books = supply.find({})
    for data in books:
       get_stock.append(data["Stock"])
    
    print(f"There is {sum(get_stock)} books in stock.")

# report3()

#report 4: How much this store will get if sell every books in stock?
def report4():
    get_money = []
    books = supply.find({})
    for data in books:
       get_money.append(data["Stock"] * data["Price"])

    print(f"This store will get around {sum(get_money)} baht.")

# report4()

#report 5: How much does this store get from orders on 12 may 2021?
def report5():
    date = orders.find({"Date":"2021-05-12"})
    get_order = []
    get_price = []
    for data in date:
        get_order.append(data["Order"])

    for order in get_order:
        get_supply = supply.find({"Name": order})
        for data in get_supply:
            get_price.append(data["Price"])

    print(f"On 12 may 2021 this store get {sum(get_price)} baht.")

# report5()

#report 6: How many people that make orders on 13 may 2021?
def report6():
    date = orders.find({"Date":"2021-05-13"})
    get_name = []
    for data in date:
        get_name.append(data["Name"])

    print(f"There is {len(get_name)} people that make orders on 13 may 2021.")

# report6()

#report 7: How many customers?
def report7():
    get_customer = customers.find({})
    print(f"There is {get_customer.count()} people.")

# report7()

#report 8: How much is this book?
def report8():
    get = input("Enter name of comic book: ")
    book = supply.find({"Name":get})
    for data in book:
        price = data["Price"]
    print(f"{get} is {price} baht.")

# report8()