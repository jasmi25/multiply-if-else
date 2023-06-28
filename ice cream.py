#4. Take a user input and check the following :-
#- if it's divisible by 3 so print ice
#- if it's divisible by 9 print cream
#- if it's divisible by both numbers so print ice
#cream?
num=int(input("enter number:-"))
if num%3==0 :
        print("ice")
if num%9==0:
    print("cream")
if num%3==0 and num%9==0:
    print("ice cream")
else:
    print("not divisible by both")
