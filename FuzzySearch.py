from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# input into the backend:
# list of groceries that the user wants
# location of user (address), in the backend need to find grocery stores wihtin a radius
# list of available items for each website (from scraper)

def main():

    list_of_items = ['Banana', 'Apple', 'Orange', 'Cucumber', 'Onion']


    walmart_available = [
        [{"name": "Banana", "price": 1.72, "weight": "1kg"}],
        [{"name": "Apple, Gala", "price": 4.34, "weight": "1kg"}],
        [{"name": "Pears, Bartlett", "price": 6.55, "weight": "1kg"}],
        [{"name": "Cucumber, Seedless", "price": 1.97, "weight": "single"}],
        [{"name": "Tomato, Roma", "price": 4.34, "weight": "1kg"}],
        [{"name": "Blueberries", "price": 3.97, "weight": "170g"}],
        [{"name": "Indian Okra", "price": 8.76, "weight": "1kg"}],
        [{"name": "Raspberries", "price": 3.97, "weight": "170g"}],
        [{"name": "Your Fresh Market Clementine", "price": 5.47, "weight": "2lb"}],
        [{"name": "Orange, Seedless", "price": 4.34, "weight": "1kg"}],
        [{"name": "Cantaloupe", "price": 3.97, "weight": "single"}],
        [{"name": "Fairtrade Organic Banana", "price": 2.14, "weight": "1kg"}],
        [{"name": "Mushrooms, Whole White, Your Fresh Market", "price": 2.47, "weight": "80z"}],
        [{"name": "Your Fresh Market Tomato, Grape", "price": 3.47, "weight": "10oz"}],
        [{"name": "Your Fresh Market Seedless Oranges", "price": 7.97, "weight": "4lb"}]
    ]

    loblaws_available = [
        [{"name": "English Cucumber", "price": 1.99, "weight": "single"}],
        [{"name": "Green Onion", "price": 1.99, "weight": "single"}],
        [{"name": "Celery Stalks", "price": 4.49, "weight": "single"}],
        [{"name": "Lettuce Iceberg", "price": 3.99, "weight": "single"}],
        [{"name": "Green Seedless Grapes", "price": 8.80, "weight": "1kg"}],
        [{"name": "Farmer's Market, Yellow Onions", "price": 1.99 , "weight": "3lb"}],
        [{"name": "Raspberries", "price": 4.99, "weight": "170g"}],
        [{"name": "Strawberries", "price": 3.99, "weight": "454g"}],
        [{"name": "Red Peppers", "price": 11.00, "weight": "1kg"}],
        [{"name": "Broccoli", "price": 3.99, "weight": "single"}],
        [{"name": "Zucchini", "price": 6.59, "weight": "1kg"}],
        [{"name": "Sweet Green Peppers", "price": 7.69, "weight": "1kg"}],
        [{"name": "Roma Tomatoes", "price": 7.69, "weight": "1kg"}],
        [{"name": "Red Onion", "price": 7.25, "weight": "1kg"}],
        [{"name": "PC Organics, Organic Bananas, Bunch", "price": 2.62, "weight": "1kg"}]
    ]

    # convert all units to g first
    # 1lb = 453.592g
    # 1kg = 1000g
    # 1oz = 28.3495g

    count = 0

    for items in walmart_available:
        # ex of item is {"name": "Banana", "price": 1.72, "weight": "1kg"}
        if 'kg' in items[0]["weight"]:
            number = float(items[0]["weight"].replace("kg", ""))
            walmart_available[count][0].update({"weight": str(number * 1000) + "g"})
            # temp = 
            # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")

        if 'lb' in items[0]["weight"]:
            number = float(items[0]["weight"].replace("lb", ""))
            walmart_available[count][0].update({"weight": str(number * 453.592) + "g"})
            # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")
    
        if 'oz' in items[0]["weight"]:
            number = float(items[0]["weight"].replace("oz", ""))
            walmart_available[count][0].update({"weight": str(number * 28.3495) + "g"})
            # walmart_available[count][0].update(({"weight": walmart_available[count][0]}) + "g")
        count = count + 1

    print (walmart_available)


    # print ('Enter your grocery list separated by spaces below:\n')
    # print()

    # grocery_list = input('Enter your grocery list separated by spaces below:\n')

    # found, not_found = find_available(list_of_items, grocery_list)

    # if found: # list is not empty
    #     print('Available items found:')
    #     for item in found:
    #         print (item)
    # else:
    #     print('Error: No available items found.')

    # print (found)
    # print()
    # print(not_found)

    # for item in list_of_items:
    #     if fuzz.WRatio(item, input) > 60:
    #         print ('Did you mean: ' + item)
    #         print ('Showing all results for: ' + item)

def find_available (list_of_items, input):
    found = []
    not_found = []

    list_input = input.split(" ")
    for item in list_input:
        for grocery in list_of_items:
            if fuzz.WRatio(item, grocery) > 60:
                found.append(grocery)
            else:
                not_found.append(item)
    
    return found, not_found

if __name__ == "__main__":
    main()
