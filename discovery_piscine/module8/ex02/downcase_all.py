import sys
def downcase_it(str) :
    return(str.lower())
for str in sys.argv[1:] :
    print(downcase_it(str))