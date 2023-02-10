#!/usr/bin/python3

import sys

def my_dictionaries():

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if verify_exists(states) == True:
        key = states[sys.argv[1]]
        print(capital_cities[key])
    else:
        print("Unknown state")

def verify_exists(states):

    valid = False

    if len(sys.argv) != 2: 
        sys.exit()
    for key, value in states.items():
        if(sys.argv[1]) == key:
            valid = True
    return(valid)

if __name__ == '__main__':
    my_dictionaries()
