def date_detter(value) :
    return(value[1]["date_of_birth"])
def famous_births(dic) :
    for str in sorted(dic.items(), key = date_detter)  :
        print(str[1]["name"], "is a great scientist born in", str[1]["date_of_birth"])
women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
