try :
    f = int(input("Enter the first number:\n").strip())
    s = int(input("Enter the secend number:\n").strip())
except ValueError:
    print("error l3eon ahmad")
    exit(2)

num = f * s
print(str(f),"x",str(s),"=",str(num))
print("The result is positive.") if num > 0 else print("The result is negative.") if num < 0 else print("The result is positive and negative.")