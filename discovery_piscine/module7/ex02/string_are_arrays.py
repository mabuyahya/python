import sys
c = 0
if len(sys.argv) == 2 :
    for str in sys.argv[1] :
        if str == "z" :
            c += 1
    if c: 
        print("z" * c)
    else :
        print("none")
else :
    print("none")