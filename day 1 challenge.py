name=input("Enter your full name: ")
email=input("Enter your email ID: ")
mobile=input("Enter your mobile number: ")
age=int(input("Enter your age: "))
length=len(name)
if name.find(' ')!=0 and name.find(' ')!=length-1 and name.count(' ')>=1 and email.count('@')==1 and email.count('.')>=1 and email.find('@')!=0 and len(mobile)==10 and mobile>="0000000000" and mobile<="9999999999" and mobile.find('0')!=0 and age>=18 and age<=60:
    print("user profile is valid")
else:
    print("user profile is invalid")
