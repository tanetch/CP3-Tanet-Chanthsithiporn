username = "admin"
password = "0000"
UserInputUsername = input("Username: ")
UserInputPassword = input("Password: ")
if UserInputUsername == username and UserInputPassword == password:
    print("Log in completed")
    print("Service List")
    print("1. One-side document printing 0.5 THB per page")
    print("2. Two-side document printing 1   THB per page")
    print("3. Photo printing             5   THB per page")
    UserSelect = int(input("Select the service: "))
    if UserSelect == 1:
        amount = int(input("Enter amount of page: "))
        price = 0.5*amount
        print("Total: ",price,"THB")
    elif UserSelect == 2:
        amount = int(input("Enter amount of page: "))
        price = 1*amount
        print("Total: ",price,"THB")
    elif UserSelect == 3:
        amount = int(input("Enter amount of page: "))
        price = 5*amount
        print("Total:",price,"THB")
    else:
        print("Error.")
else:
    print("Error.")
