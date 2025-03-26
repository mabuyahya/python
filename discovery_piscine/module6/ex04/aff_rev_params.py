import sys
if len(sys.argv) > 2 : 
    i = len(sys.argv) - 1 
    while i :
        print(sys.argv[i])
        i -= 1
else :
    print("none")

