str = input()
i = 0
while i < len(str) :
    print(str[i].capitalize(), end = "") if str[i].islower() else print(str[i].casefold(), end = "")
    i += 1
print()