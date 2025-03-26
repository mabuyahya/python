try : 
    num = int(input("Enter a number less than 25 \n"))
except ValueError : 
    print("ahmad b7kelk d5l rgm eklp")
    exit(1)
if num > 25 : print("Error")
while num <= 25 :
    print("Inside the loop, my variable is", num)
    num += 1