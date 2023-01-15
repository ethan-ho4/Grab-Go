from flask import Flask , request
from flask_cors import CORS
import FuzzySearch
import json

app = Flask(__name__)
CORS(app)

# f_loblaws = open('../loblaws.json')
# f_no_frills = open('../no-frills.json')
# f_fortinos = open('../fortinos.json')

# data_loblaws = json.load(f_loblaws)
# data_no_frills = json.load(f_no_frills)
# data_fortinos = json.load(f_fortinos)

def store_extract(user_list , store_list):
    # extract list of dictionaries for available items
    # in each store corresponding to grocery list
    available_items = []
    for items in store_list:
        for i in len(user_list):
            if (user_list[i] == items['name']):
                available_items.append(items)
    return available_items

@app.route('/breakdown' , methods=['GET'])
def store_breakdown():

    return("testing")

@app.route('/grocery-list' , methods=['POST'])
# POST --> data from frontend to backend
def grocery_list():
    # input = request.form['text']
    # print(input)
    # l_available = store_extract(input , data_loblaws)
    # n_available = store_extract(input , data_no_frills)
    # f_available = store_extract(input , data_fortinos)

    # stores_extracted = [
    #     l_available, 
    #     n_available, 
    #     f_available
    # ]

    return("testing")

if __name__ == '__main__':
    app.run(debug=True)