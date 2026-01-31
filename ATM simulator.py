file_name = "atm_data.txt"
# balanace is a global variable that stores money
balance = 1000
# pin is  aglobal varaible that stores atm pin 
pin= "1234"
# defining a function (for loading the data)
def load_data():
    global balance,pin                  #global keyword allows us to modify outside variables
    try:
        file = open(file_name,"r")
        lines = file.readlines()        #readlines reads all the lines in the data and returns the lines in the form of list
        file.close()
        pin = lines[0].strip()          #first line contains pin, strip removes \n
        balance=int(lines[1].strip())   #second line contains balance
    except:
        pass                            #pass means "Do nothing"
    #program will use default balance and pin

#defining a function (for checking the balance)
def check_balance():
    print("Your balance is : ", balance)

# defining a function (for saving the data)
def save_data():
    file = open(file_name,"w")
    file.write(pin+"\n")                #write a pin into the file and go to next line
    file.write(str(balance))            #write balance as a string
    file.close()

# defining a functio (for depositing the money)
def deposit_money():
    global balance                      #global alows us to change the original balance 
    try:
        amount=int(input("Enter amount to deposit:"))
        balance = balance+amount
        save_data()                    #save updated balance to the file 
        print("Money deposited successfully")
    except:
        print("please enter numbers only")

# defining a function (to withdraw money)
def withdraw_money():
    global balance
    try:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount>balance:
            print("Insufficient balance")
        else:
            balance = balance-amount
            save_data()
            print("Please collect your cash !!!")
    except:
        print("Please enter number only")

# defining a function (to change the pin)
def change_pin():
    global pin
    old_pin = input("Enter the old pin : ")        #ask user for old pin
    if old_pin == pin :                                 #check if the old pin matches with pin
        new_pin = input("Enter your new pin: ")   #ask to enter new pin
        pin = new_pin
        save_data()
        print("Pin changed successfully")
    else:
        print("Incorrect pin")

# Main function 
def main():
    load_data()                                     #load data when the program starts 
    user_pin = input("Enter a pin: ")          #Ask user to enter the pin
    if user_pin != pin:                             #if pin is wrong stop the program
        print("Incorrect Pin !! ")
        return 
    while True:
        print("\n-------ATM Menu--------")
        print("1. Check balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change Pin")
        print("5. Exit")

        choice= input("Enter your choice : ")
        if choice == "1" :
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("Thank you for using ATM !")
            break
        else:
            print("Invalid choice")

main()