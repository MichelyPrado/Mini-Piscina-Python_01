#!/usr/bin/python3

def musician():

    unsorted_list = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',
    'Beck' : '1944',
    'Santana' : '1947',
    'Ramone' : '1948',
    'White' : '1975',
    'Frusciante': '1970',
    'Thompson' : '1949',
    'Burton' : '1939',
    }

    sorted_by_name = dict(sorted(unsorted_list.items(), key=lambda k: k[0]))
    sorted_by_year = dict(sorted(sorted_by_name.items(), key=lambda k: k[1]))
    for items in sorted_by_year:
        print(items)

if __name__ == '__main__':
    musician()
