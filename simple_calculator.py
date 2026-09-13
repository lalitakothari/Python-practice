num1 = float(input("enter first number :"))
num2 = float(input("enter second number :"))
operator = input("enter operator (+,-,*,/,%) to perform operation  :")

match operator:
    case '+':
     print("result :", num1 + num2)
    case '-':
      print("result :",num1 - num2)
    case '*':
      print("result :",num1 * num2)
    case '/':
      print("result :" ,num1 / num2)
    case _:
       print("invalid statement !")