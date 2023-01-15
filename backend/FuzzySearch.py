from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from flask import Flask, render_template, request, redirect
import json


# input into the backend:
# list of groceries that the user wants
# location of user (address), in the backend need to find grocery stores wihtin a radius
# list of available items for each website (from scraper)

def main():

    f = open('../fortinos.json')
    fortinos = json.load(f)

    l = open('../loblaws.json')
    loblaws = json.load(l)

    n = open('../no-frills.json')
    nofrills = json.load(n)

    # For each new list, add its name to this list
    retailers_available = [fortinos, loblaws, nofrills]
    retailers_name = ["Fortinos", "Loblaws", "No Frills"]

    # convert all units to g first
    # 1lb = 453.592g
    # 1kg = 1000g
    # 1oz = 28.3495g
    for retailers in retailers_available:
        # ex of retailers is (walmart_available)
        for items in retailers:
            # ex of items is {"name": "Banana", "price": 1.72, "weight": "1kg"}
            if 'kg' in items["quantity"]:
                number = float(items["quantity"].replace("kg", ""))
                items.update({"quantity": str(number * 1000) + "g"})
                # temp = 
                # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")

            if 'lb' in items["quantity"]:
                number = float(items["quantity"].replace("lb", ""))
                items.update({"quantity": str(number * 453.592) + "g"})
                # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")
        
            if 'oz' in items["quantity"]:
                number = float(items["quantity"].replace("oz", ""))
                items.update({"quantity": str(number * 28.3495) + "g"})
                # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")

    cart = input('Enter your grocery list separated by commas below:\n')
    cart.replace(" ", "")
    grocery_list = cart.split(",")

    count = 0

    for item in retailers_available:
        print ("---" + retailers_name[count] + "---")

        found, prices = find_available(item, grocery_list)

        if found: # list is not empty
            print('Available items found:')
            count1 = 0
            for fruit in found:
                print (str(fruit) + " $" + str(prices[count1]))
                count1 = count1 + 1
            print ("......")

            cost = 0

            for fruit in found:
                for dict in item:
                    if dict["name"] == fruit:
                        cost = cost + float(dict["price"])
            print (f"Subtotal: ${cost:.2f}")
            print (f"Tax: ${cost*0.13:.2f}")
            print (f"Total: ${cost*1.13:.2f}")

        else:
            print('Error: No available items found.')
        
        print ()
        count = count + 1

def find_available (list_of_items, input):

    found = []
    prices = []

    for grocery in input:
        # print (grocery)
        for item in list_of_items: #issue: this only runs once
            # print (item[0])
            if ((fuzz.WRatio(grocery, item["name"]) > 60)):# or (grocery.lower() in item["name"].lower())):
                found.append(item["name"])
                prices.append(float(item["price"]))

    return found, prices

if __name__ == "__main__":
    main()

