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

    dictionary = new_dictionary(states, capital_cities)
    args = verify_exists()
    check_parameter(dictionary, args)

def check_parameter(dictionary, args): #vincula chave e valor do dicionario com os argumentos recebidos no terminal

    for elements in args:
        #se o elemento não for str vazia
        if len(elements.strip(" ")) > 0:
            #verifica se chave bate com o valor (value)
            if elements.title() in dictionary:
                print(dictionary[elements.title()], "is the capital of", elements.title())
            #verifica se o valor bate com a chave (key)   
            elif elements.title() in dictionary.values():
                print(elements.title(), "is the capital of", find_key(elements.title(), dictionary))
            else:
                print(elements, "is neither a capital city nor a state")

def new_dictionary(states, capital_cities):
    dictionary = dict()

    for key, value in states.items():
        dictionary[key] = capital_cities[value]
    return(dictionary)

def find_key(value, dictionary):
    for key, values in dictionary.items():
        if value == values:
            return(key)

def verify_exists(): 

    args_final = list()

    i = 0

    if len(sys.argv) != 2: 
        sys.exit()
    args = sys.argv[1].split(",")
    for elements in args:
        #transforma os argumentos passados como str em lista, tratando espaços e virgulas(split)
        args_final.insert(i, elements.strip(" ")) 
        i += 1
    return(args_final)#lista de arg passados no terminal pronta

if __name__ == '__main__':
    my_dictionaries()