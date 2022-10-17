number = input("Pick a number ")
number = int(number)
if number >= 0 and number <=100:
    print("True")
else:
    print("False")


word = input("Write a word ")
upper = 0
lower = 0

for x in word:
    if(x.isupper()):
        upper+=1
    else:
        lower+=1
print("The amount of uppercase letters is, ", upper, " and the amount of lowerrcase letters is ",  lower)



str = input("Enter a word ")
str = str[:-1]
if len(str) <= 1:
    print(input)
else:
    print((str))

