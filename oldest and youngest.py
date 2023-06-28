#24.Take the age of 3 people by user and determine oldest and youngest among
#them
age1=int(input("enter age:-"))
age2=int(input("enter age:-"))
age3=int(input("enter age:-"))
if(age1>age2 and age1>age3):
    print("age1 is oldest=",age1)
elif(age2>age1 and age2>age3):
    print("age2 is oldest=",age2)
elif(age3>age1 and age3>age2):
    print("age3 is oldest=",age3)
else:
    print("no one is oldest")
if(age1<age2 and age1<age2):
    print("age1 is youngest=",age1)
elif(age2<age1 and age2<age3):
    print("age2 is youngest=",age2)
elif(age3<age1 and age3<age2):
    print("age3 is youngest=",age3)
else:
    print("no one is youngest")
