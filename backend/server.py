from flask import Flask , request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

f_loblaws = open('loblas.json')
f_no_frills = open('no-frills.json')
f_fortinos = open('fortinos.json')

data_loblaws = json.load(f_loblaws)
data_no_frills = json.load(f_no_frills)
data_fortinos = json.load(f_fortinos)

@app.route('/breakdown' , methods=['GET'])
def store_breakdown():
    # get price breakdown from each store to output onto
    return

@app.route('/grocery-list' , methods=['POST'])
# POST --> data from frontend to backend

def store_extract(user_list , store_list):
    # extract list of dictionaries for available items
    # in each store corresponding to grocery list
    available_items = []
    for items in store_list:
        for i in len(user_list):
            if (user_list[i] == items['name']):
                available_items.append(items)
    return available_items

def get_list(user_list):
    
    return

if __name__ == '__main__':
    app.run(debug=True)