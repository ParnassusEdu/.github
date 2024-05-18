import sys

# 2-D Account Array
Account = [["James", "Plague"], ["Harry", "Koala"]]

# Balance, LOAN LIMIT, WITHDRAWAL LIMIT
AccDetails = [[250, 100, 200], [500, 1000, 400]]

accID = int(input("Account ID: "))
accName = input("Enter Name: ")
accPassword = input("Enter Password: ")

if Account[accID][0] == accName and Account[accID][1] == accPassword:
    print(f"""
Welcome Back {accName}!
Following are the options you can choose from. Enter a number from 1-4

1. Display Balance
2. Withdraw Money
3. Deposit Money
4. Exit
""")
    
    # Returns balance value, of accID (ROW), and 0th COLUMN (THE BALANCE)     
    def displayBalance(accID):
        print("Your balance is: ", AccDetails[accID][0])

    # Withdraw money
    def withdrawMoney(accID):
        amount = int(input("Amount: "))
        if amount <= AccDetails[accID][0] and amount <= AccDetails[accID][2]:
            AccDetails[accID][0] -= amount
            print(f"${amount} has been withdrawn. Your balance is ${AccDetails[accID][0]}")
        else:
            print(f"Sorry, we cannot withdraw more than the limit")
        
    # Deposit 
    def deposit(accID):
        amount = int(input("Amount: "))
        AccDetails[accID][0] += amount
        print(f"Balance: {AccDetails[accID][0]}")

    while True:
        option = int(input("Enter: "))
        
        if option == 1:
            displayBalance(accID)
        elif option == 2:
            withdrawMoney(accID)
        elif option == 3:
            deposit(accID)
        elif option == 4:
            sys.exit()
        else:
            print("Invalid option. Please enter a number from 1-4.")
else:
    print("Incorrect Account ID, Name, or Password.")
