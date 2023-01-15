from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ProcessUserinfo/<string:userinfo>', methods=['GET'])
def sendUserinfo(userinfo):
    userinfo=json.loads(userinfo)
    username = userinfo
    print()
    print (username)
    print ()

    main(username) # THIS WAS ADDDED, not sure

    return ('/')


# input into the backend:
# list of groceries that the user wants
# location of user (address), in the backend need to find grocery stores wihtin a radius
# list of available items for each website (from scraper)

def main(cart):

    walmart_available = [
        {"name": "Banana", "price": 1.72, "weight": "1kg"},
        {"name": "Apple, Gala", "price": 4.34, "weight": "1kg"},
        {"name": "Pears, Bartlett", "price": 6.55, "weight": "1kg"},
        {"name": "Cucumber, Seedless", "price": 1.97, "weight": "single"},
        {"name": "Tomato, Roma", "price": 4.34, "weight": "1kg"},
        {"name": "Blueberries", "price": 3.97, "weight": "170g"},
        {"name": "Indian Okra", "price": 8.76, "weight": "1kg"},
        {"name": "Raspberries", "price": 3.97, "weight": "170g"},
        {"name": "Your Fresh Market Clementine", "price": 5.47, "weight": "2lb"},
        {"name": "Orange, Seedless", "price": 4.34, "weight": "1kg"},
        {"name": "Cantaloupe", "price": 3.97, "weight": "single"},
        {"name": "Fairtrade Organic Banana", "price": 2.14, "weight": "1kg"},
        {"name": "Mushrooms, Whole White, Your Fresh Market", "price": 2.47, "weight": "80z"},
        {"name": "Your Fresh Market Tomato, Grape", "price": 3.47, "weight": "10oz"},
        {"name": "Your Fresh Market Seedless Oranges", "price": 7.97, "weight": "4lb"}
    ]

    loblaws_available = [
        {"name": "English Cucumber", "price": 1.99, "weight": "single"},
        {"name": "Green Onio n", "price": 1.99, "weight": "single"},
        {"name": "Celery Stalks", "price": 4.49, "weight": "single"},
        {"name": "Lettuce Iceberg", "price": 3.99, "weight": "single"},
        {"name": "Green Seedless Grapes", "price": 8.80, "weight": "1kg"},
        {"name": "Farmer's Market, Yellow Onions", "price": 1.99 , "weight": "3lb"},
        {"name": "Raspberries", "price": 4.99, "weight": "170g"},
        {"name": "Strawberries", "price": 3.99, "weight": "454g"},
        {"name": "Red Peppers", "price": 11.00, "weight": "1kg"},
        {"name": "Broccoli", "price": 3.99, "weight": "single"},
        {"name": "Zucchini", "price": 6.59, "weight": "1kg"},
        {"name": "Sweet Green Peppers", "price": 7.69, "weight": "1kg"},
        {"name": "Roma Tomatoes", "price": 7.69, "weight": "1kg"},
        {"name": "Red Onion", "price": 7.25, "weight": "1kg"},
        {"name": "PC Organics, Organic Bananas, Bunch", "price": 2.62, "weight": "1kg"}
    ]

    # For each new list, add its name to this list
    retailers_available = [walmart_available, loblaws_available]
    retailers_name = ["Walmart", "Loblaws"]

    # convert all units to g first
    # 1lb = 453.592g
    # 1kg = 1000g
    # 1oz = 28.3495g
    for retailers in retailers_available:
        # ex of retailers is (walmart_available)
        for items in retailers:
            # ex of items is {"name": "Banana", "price": 1.72, "weight": "1kg"}
            if 'kg' in items["weight"]:
                number = float(items["weight"].replace("kg", ""))
                items.update({"weight": str(number * 1000) + "g"})
                # temp = 
                # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")

            if 'lb' in items["weight"]:
                number = float(items["weight"].replace("lb", ""))
                items.update({"weight": str(number * 453.592) + "g"})
                # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")
        
            if 'oz' in items["weight"]:
                number = float(items["weight"].replace("oz", ""))
                items.update({"weight": str(number * 28.3495) + "g"})
                # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")

    # print (walmart_available)
    # print ()
    # print (loblaws_available)

    # print ('Enter your grocery list separated by spaces below:\n')
    # print()

    # cart = input('Enter your grocery list separated by commas below:\n')
    cart.replace(" ", "")
    grocery_list = cart.split(",")

    

    # walmart_available = [
    #     {"name": "Banana", "price": 1.72, "weight": "1kg"},
    #     {"name": "Apple, Gala", "price": 4.34, "weight": "1kg"},
    #     {"name": "Pears, Bartlett", "price": 6.55, "weight": "1kg"},
    #     {"name": "Cucumber, Seedless", "price": 1.97, "weight": "single"},
    #     {"name": "Tomato, Roma", "price": 4.34, "weight": "1kg"},
    #     {"name": "Blueberries", "price": 3.97, "weight": "170g"},
    #     {"name": "Indian Okra", "price": 8.76, "weight": "1kg"},
    #     {"name": "Raspberries", "price": 3.97, "weight": "170g"},
    #     {"name": "Your Fresh Market Clementine", "price": 5.47, "weight": "2lb"},
    #     {"name": "Orange, Seedless", "price": 4.34, "weight": "1kg"},
    #     {"name": "Cantaloupe", "price": 3.97, "weight": "single"},
    #     {"name": "Fairtrade Organic Banana", "price": 2.14, "weight": "1kg"},
    #     {"name": "Mushrooms, Whole White, Your Fresh Market", "price": 2.47, "weight": "80z"},
    #     {"name": "Your Fresh Market Tomato, Grape", "price": 3.47, "weight": "10oz"},
    #     {"name": "Your Fresh Market Seedless Oranges", "price": 7.97, "weight": "4lb"}
    # ]

    # grocery_list ex is ["apples", "bananas", "onions", "cucumbers"]
    count = 0

    for item in retailers_available:
        # item ex is (walmart_available)
        # print (item) # REMOVE THIS AFTER

        print ("---" + retailers_name[count] + "---")
        # print (grocery_list) # REMOVE THIS AFTER

        found = find_available(item, grocery_list)

        if found: # list is not empty
            print('Available items found:')
            for fruit in found:
                print (fruit)
            print ("......")

            cost = 0

            for fruit in found:
                for dict in item:
                    if dict["name"] == fruit:
                        cost = cost + dict["cost"]
            print ("Subtotal: " + cost)
            print ("Tax: " + (cost*0.13))
            print ("Total: " + (cost*1.13))

        else:
            print('Error: No available items found.')
        
        print ()
        
        count = count + 1

    

    # for item in list_of_items:
    #     if fuzz.WRatio(item, input) > 60:
    #         print ('Did you mean: ' + item)
    #         print ('Showing all results for: ' + item)

def find_available (list_of_items, input):
    # 1st: full list of items available from store
    # 2nd: input from user, ex ["apples", "bananas", "onions", "cucumbers"]

    # walmart_available = [
    #     {"name": "Banana", "price": 1.72, "weight": "1kg"},
    #     {"name": "Apple, Gala", "price": 4.34, "weight": "1kg"},
    #     {"name": "Pears, Bartlett", "price": 6.55, "weight": "1kg"},
    #     {"name": "Cucumber, Seedless", "price": 1.97, "weight": "single"},
    #     {"name": "Tomato, Roma", "price": 4.34, "weight": "1kg"},
    #     {"name": "Blueberries", "price": 3.97, "weight": "170g"},
    #     {"name": "Indian Okra", "price": 8.76, "weight": "1kg"},
    #     {"name": "Raspberries", "price": 3.97, "weight": "170g"},
    #     {"name": "Your Fresh Market Clementine", "price": 5.47, "weight": "2lb"},
    #     {"name": "Orange, Seedless", "price": 4.34, "weight": "1kg"},
    #     {"name": "Cantaloupe", "price": 3.97, "weight": "single"},
    #     {"name": "Fairtrade Organic Banana", "price": 2.14, "weight": "1kg"},
    #     {"name": "Mushrooms, Whole White, Your Fresh Market", "price": 2.47, "weight": "80z"},
    #     {"name": "Your Fresh Market Tomato, Grape", "price": 3.47, "weight": "10oz"},
    #     {"name": "Your Fresh Market Seedless Oranges", "price": 7.97, "weight": "4lb"}
    # ]

    found = []

    for grocery in input:
        # print (grocery)
        for item in list_of_items: #issue: this only runs once
            # print (item[0])
            if ((fuzz.WRatio(grocery, item["name"]) > 60) or (grocery.lower() in item["name"].lower())):
                found.append(item["name"])

    return found

    # for item in list_of_items[0]:
    #     print (item)
    #     # item is ex {"name": "Banana", "price": 1.72, "weight": "1kg"}
    #     for grocery in input:
    #         print (input)
    #         # grocery is ex "apple"

    #         if ((fuzz.WRatio(grocery, item["name"]) > 50) or (grocery.lower() in item["name"].lower())):
    #             found.append(item["name"])

    # return found

if __name__ == "__main__":
    app.run(debug=True)

