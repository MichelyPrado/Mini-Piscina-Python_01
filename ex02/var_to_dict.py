#!/usr/bin/python3

def my_first_dictionary():

    d_list = [

        ('Hendrix' , '1942'),
        ('Allman' , '1946'),
        ('King' , '1925'),
        ('Clapton' , '1945'),
        ('Johnson' , '1911'),
        ('Berry' , '1926'),
        ('Vaughan' , '1954'),
        ('Cooder' , '1947'),
        ('Page' , '1944'),
        ('Richards' , '1943'),
        ('Hammett' , '1962'),
        ('Cobain' , '1967'),
        ('Garcia' , '1942'),
        ('Beck' , '1944'),
        ('Santana' , '1947'),
        ('Ramone' , '1948'),
        ('White' , '1975'),
        ('Frusciante', '1970'),
        ('Thompson' , '1949'),
        ('Burton' , '1939')
    ]
    new_dic = {}
    for i in d_list:
        sur_name = i[0]
        if sur_name:
            sur_name_get = new_dic.get(i[1]) #verifico se tem um ano repetido pra mais de um nome
        if sur_name_get:
            new_dic[i[1]] = sur_name_get + ' ' + sur_name #se tiver ano repetido, concatena os nomes
        else:
            new_dic[i[1]] = i[0] #se não tiver repetido, só junta  chave e valor
    for item in new_dic:
	    print(item, ":", new_dic[item])

if __name__ == '__main__':
	my_first_dictionary()
