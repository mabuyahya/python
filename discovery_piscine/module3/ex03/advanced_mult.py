i = 0
while i < 11 :
    j = 0
    print("Table of " + str(i) + ":" , end = "")
    while j < 11 :
        print("", i * j, end = "")
        j += 1
    print()
    i += 1