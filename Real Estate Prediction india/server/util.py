import json
import pickle
import numpy as np


__locations = None
__data_columns =None
__model = None

#write a function for the price depent on the x variable
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
        
    return round(__model.predict([x])[0],2)



#This function returns  the list of location names
def get_location_names():
    # util.load_saved_artifacts()
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts......hold on! Go>>>>>.....")
    global __data_columns
    global __locations
    
    with open("server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model 
    with open("server/artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)
        print("loading saved artifacts......done!")
        
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('Indira Nagar',1000, 2, 2))
    print(get_estimated_price('1st Phase JP Nagar',1000, 2, 2))
    print(get_estimated_price('banaswadi',1000, 2, 2))