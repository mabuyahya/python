def greetings(strr = "noble stranger") :
    if isinstance(strr, str):
        print(strr)
    else :
        print("Error! It was not a name.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)  