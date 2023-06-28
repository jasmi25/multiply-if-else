#3. Take a user input and display the last digit of the number
#and check if the last digit of the number is 3 or not?

num=int(input("enter number"))
if num>0:
    a=num%10
    print(a)
if a==3:
    print("the number is 3")
else:
    print("the number not 3")
