import sys

if len(sys.argv) > 1 :
    for str in sys.argv[1:] :
        if not str.endswith("ism") :
            print(str + "ism")
else :
    print("none")
