### Imports
from cardHolder import cardHolder

### Menu Options
def print_menu():
    ### Print options to the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

### Deposit Function
def deposit(cardHolder):
    try:
        deposit = float(input("How much $$ would you like to deposit: "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for your deposit. Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid Input!")

### Withdraw Function
def withdraw(cardHolder):
    try:
        withdraw = float(input("How much $$ would you like to withdraw: "))
        ### Check if user has enough money
        if(cardHolder.get_balance() < withdraw):
            print("Insufficient balance!")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go! Thank you!")
    except:
        print("Invalid Input!")

### Check Balance Function
def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

### Main Function
if __name__ == "__main__":
    current_user = cardHolder("","","","","")

    ### Create a repo of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("5121468735488743", 1523, "John", "Griffith", 166.32))
    list_of_cardHolders.append(cardHolder("1654684651468472", 4367, "Ashley", "Jones", 562.40))
    list_of_cardHolders.append(cardHolder("8718978971897987", 7811, "Frida", "Dickerson", 213.93))
    list_of_cardHolders.append(cardHolder("8178797542132154", 3698, "Adam", "Smith", 753.20))
    list_of_cardHolders.append(cardHolder("1846849878578745", 9852, "James", "Ryan", 325.60))

    ### Prompt user for debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ### Check against repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")   
        except:
            print("Card number not recognized. Please try again.")
            
    ### Prompt for PIN
    while True:
        try:
            userPin = int(input("Please enter your PIN: ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid PIN. Please try again!")   
        except:
            print("Invalid PIN. Please try again!")
            
    ### Print Options
    print("Welcome ", current_user.get_firstname(), "!")
    option = 0
    while (True):
        print_menu()
        try:
            option = int(input())
        except:
            print("Invalid input. Please try again!")
        if(option == 1):
            deposit(current_user)
        elif(option == 2):
            withdraw(current_user)
        elif(option == 3):
            check_balance(current_user)
        elif(option == 4):
            break
        else:
            option = 0
            
        print("Thank you! Have a nice day!")