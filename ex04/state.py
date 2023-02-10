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

    if verify_exists(capital_cities) == True: #o argumento de entrada existe 
        anacronym = get_key_capital(capital_cities, sys.argv[1]) #vou procurar ele em capital_cities e guardar na variável (valor)
        result = get_key_states(states, anacronym) #guardado o resultado em anacronym, procuro o correspondente a ele em states
        print(result)
    else:
        print("Unknown capital city")

def get_key_states(states, anacronym):
    for key, value in states.items():
        if anacronym == value:
            return(key)

def get_key_capital(capital_cities, input_user):
    for key, value in capital_cities.items():
        if input_user == value:
            return(key)

def verify_exists(capital_cities):

    valid = False

    if len(sys.argv) != 2: 
        sys.exit()
    for key, value in capital_cities.items():
        if(sys.argv[1]) == value:
            valid = True
    return(valid)

if __name__ == '__main__':
    my_dictionaries()