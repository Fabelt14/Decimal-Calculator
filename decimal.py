#Decimal calculator
#HEADINGS........
print("DECIMAL CALCULATOR")
#THE PROGRAM
print("Just input any number below to round it off")
try:
    yournum = float(input("input your decimal below: \n"))
except ValueError:
    print("error")
one_decimal_place = round(yournum, 1)
two_decimal_place = round(yournum, 2)
three_decimal_place = round(yournum, 3)
four_decimal_place = round(yournum, 4)
print("Okay, we got you ?")
print("How many decimal place")
a = "a = one_decimal_place"
b = "b = two_decimal_place"
c = "c = three_decimal_place"
d = "d = four_decimal_place"
print(a)
print(b)
print(c)
print(d)
B = input("any of these options here \n")
if B == "a":
    print(one_decimal_place)
elif B == "b":
    print(two_decimal_olace)
elif B == "c":
    print(three_decimal_place)
elif B == "d":
    print(four_decimal_place)
else:
    print("Error")

#End of the program
