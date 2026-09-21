secret_num = 19
print("we've a secret number let's guess the number together ! ")
num = int(input("enter your number :"))

while True :
    if num == secret_num :
        print("you guess the right number :" , secret_num , "yeahh !")
        break
    elif num < secret_num :
        print("you're too low !")
        num = int(input("guess again :"))

    else :
        print("you're too high  ! ")
        num = int(input("guess again :"))
