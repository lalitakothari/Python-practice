def grade_calculator(avg):
    if avg >= 90:
        print("You got grade A!")
    elif avg >= 80:
        print("You got grade B!")
    elif avg >= 65:
        print("You got grade C!")
    else:
        print("You're just pass!")


def get_marks():
    sub1 = float(input("Enter marks of subject 1: "))
    sub2 = float(input("Enter marks of subject 2: "))
    sub3 = float(input("Enter marks of subject 3: "))
    sub4 = float(input("Enter marks of subject 4: "))

    avg = (sub1 + sub2 + sub3 + sub4) / 4

    print("Your average is:", avg)

    grade_calculator(avg)

get_marks()