import sys
if len(sys.argv) > 1 :
    print("parameters:", str(len(sys.argv) - 1))
    for str in sys.argv[1:] :
        print(str + ": ", len(str))
else :
    print("none")