item1 = float(input("enter 1st item's price :"))
item2 = float(input("enter 2nd item's price :"))
item3 = float(input("enter 3rd item's price :"))
total = item1 + item2 + item3
GST = total * 0.18
finalprice = total + GST
print("Amout you've to pay is :",finalprice)

