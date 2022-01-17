import csv
import datetime

def comics():
    books = [
        ["Robin #1", 16, 350],
        ["Robin #2", 18, 350],
        ["Night wing #3", 15, 400],
        ["Night wing #4", 39, 400],
        ["Night wing #5", 12, 400],
        ["Mister Miracle: The source of freedom #1", 13, 500],
        ["Mister Miracle: The source of freedom #2", 17, 500],
        ["Mister Miracle: The source of freedom #3", 11, 500],
        ["Mister Miracle: The source of freedom #4", 26, 500],
        ["Justice league: Last Ride #1", 23, 450],
        ["Justice league: Last Ride #2", 21, 450],
        ["Justice league: Last Ride #3", 16, 450],
        ["Justice league: Last Ride #4", 21, 450],
        ["Stargirl spring break special #1", 15, 350],
        ["Harley quinn #3", 12, 350],
        ["Teen titans academy #3", 44, 400],
        ["The Other history of the dc universe #4", 35, 500],
        ["Batman black & white #5", 52, 450],
        ["Batman black & white #6", 36, 450],
        ["Strange Adventures #10", 15, 300],
        ["Batman/superman #18", 45, 450],
        ["Batman: The dark knight detctive #3", 12, 500],
        ["Batman: The dark knight detctive #4", 28, 500],
        ["Batman: The dark knight detctive#5", 52, 500],
        ["Batman #108", 43, 450],
        ["Batman #109", 32, 450],
        ["Batman #110", 24, 500],
        ["Batman #111", 31, 500],
        ["Crime Syndicate #1", 23, 550],
        ["Crime Syndicate #2", 15, 550],
        ["Crime Syndicate #3", 22, 550],
        ["Green lantern #1", 23, 450],
        ["Green lantern #2", 16, 450],
        ["MAN-BAT #3", 25, 400],
        ["MAN-BAT #4", 22, 400],
        ["Suicide squad #1", 15, 450],
        ["Suicide squad #2", 12, 450],
        ["Suicide squad #3", 28, 450],
        ["Suicide squad #4", 14, 450],
        ["The flash #2", 16, 450],
        ["The flash #3", 23, 450],
        ["The flash #4", 15, 450],
        ["The flash #5", 15, 450]
    ]
    with open("./database/comic.csv", "w", newline="", encoding="utf-8") as c:
        fw = csv.writer(c)
        fw.writerows(books)

comics()    

def customers():
    customer = [
        ["Kaopunza", "kaopunza@gmail.com", 20],
        ["Nicenicegame", "nicenicegame@gmail.com", 19],
        ["Borrabeam", "borrabeam@gmail.com", 19],
        ["Taekung", "taekung@gmail.com", 19],
        ["Icezu", "icezu@gmail.com", 20],
        ["Kueaza", "kueaza@gmail.com", 20],
        ["Brian", "Brian@gmail.com", 65],
    ]
    with open("./database/customer.csv", "w", newline="", encoding="utf-8") as c:
        fw = csv.writer(c)
        fw.writerows(customer)

# customers()

def order():
    orders = [
        ["Kaopunza","Robin #2", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")],
        ["Nicenicegame", "Night wing #3", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")],
        ["Borrabeam", "Mister Miracle: The source of freedom #1", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")],
        ["Borrabeam", "Mister Miracle: The source of freedom #2", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")],
        ["Icezu", "Night wing #3", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")],
        ["Icezu", "Night wing #4", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")],
        ["Icezu", "Night wing #5", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")],
        ["Brian", "Night wing #3", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")],
        ["Brian", "Night wing #5", datetime.datetime(2021, 5, 12).strftime("%Y-%m-%d")], 
        ["Taekung", "Crime Syndicate #1", datetime.datetime(2021, 5, 13).strftime("%Y-%m-%d")],
        ["Kueaza", "Crime Syndicate #1", datetime.datetime(2021, 5, 13).strftime("%Y-%m-%d")]        
    ]
    with open("./database/order.csv", "w", newline="", encoding="utf-8") as o:
        fw = csv.writer(o)
        fw.writerows(orders)
# order()


