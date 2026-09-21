previous_readin = float(input("enter previouslly reading :"))
current_reading = float(input("enter currentlly reading :"))
Units_Consumed = previous_readin - current_reading 
print("units consumed =" ,Units_Consumed)

if Units_Consumed <= 100 :
    bill = Units_Consumed * 5
    print("total electricity bill is :", bill)
elif Units_Consumed <= 200 :
    bill= (100 * 5) + (Units_Consumed - 100) * 6
    print("total electricity bill is :", bill)
else : 
    print("something went wrong !")

 