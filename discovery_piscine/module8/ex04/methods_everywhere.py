import sys

def shrink(s) :
    p = ""
    for str in s[:8] :
        p += str
    print(p)
def enlarge(s) :
    p = s
    for i in range(len(s), 8) :
        p += "Z"
    print(p)

if len(sys.argv) > 1 :
    for str in sys.argv[1:] :
        if len(str) > 8 :
            shrink(str)
        elif len(str) < 8 :
            enlarge(str)
        else :
            print(str)
else :
    print("none")
