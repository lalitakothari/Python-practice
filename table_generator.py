num = int(input("enter any number for multiplication table :"))
print("table of ", num , "is \n")

for i in range(1,11,1) :
    multi = num * i
    print( num , "*" , i , "=" , multi)