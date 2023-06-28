#34. Write a program to check whether the last digit of a number( entered by user ) is
#divisible by 3 or not.
num=int(input("enter number"))
if num>9:
    a=num%10
    print(a)
if a%3==0:
    print("divisible by 3")
else:
    print("not divisible by 3")
