balance = 1000
while True:
    print(" 1 . check balance \n" " 2 . Deposite \n" "3 . Withdraw \n" " 4 . Exit ")

    choice = int(input("enter selected number to perform an operation "))

    match choice :
        case 1 :
            print("your current balance is :",balance)
        case 2 :
            cash = float(input("enter specific amount to deposite !"))
            balance += cash
            print("amount deposit , & your current balance is :",balance)
        case 3 :
            cash = float(input("enter specific amount to withdraw !"))
            if cash <= balance :
                balance -= cash 
                print("amount withdraw successfully , & your current balance is :",balance)
        case 4 :
            print("Exit successfully !")
            break 

