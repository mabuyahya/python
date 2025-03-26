import sys

if len(sys.argv) != 1 :
    str = input("what is the parameter? ")
    if str == sys.argv[1] :
        print("Good job!")
    else :
        print("Nope, sorry...")
else :
    print("none")