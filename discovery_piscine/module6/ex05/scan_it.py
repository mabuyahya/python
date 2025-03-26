import re
import sys

if len(sys.argv) == 3:
    len = len(re.findall(sys.argv[1], sys.argv[2]))
    if len > 0 :
        print(len)
        exit(1)
print("none")