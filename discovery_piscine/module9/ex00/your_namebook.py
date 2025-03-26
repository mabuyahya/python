def array_of_names(dir) :
    s = []
    for strr in dir :
        s.append(str(strr).capitalize() + " " + str(dir[strr]).capitalize())
    return (s)
p= {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(p))