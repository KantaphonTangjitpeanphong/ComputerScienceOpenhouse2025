usrn = "SPIP"
psw = "123456"
attempt = 3
while attempt >0:
    print("You have", attempt, "attempts left")
    username = input("input username: ")
    password = input("input password: ")
    if username == usrn and password == psw:
        print("Login successful!")
        break
    else:
        attempt -= 1
        print("Incorrect username or password.")

    


