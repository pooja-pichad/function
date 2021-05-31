# Question 3

#     Ek function banaiye jo 3 numbers ka sum aur average print kare.
#     Hum user se 3 number input karwayenge aur fir unn 3 numbers ka sum aur average print karwayenge
#      jaisa ki niche output diya hua hain.

def sum(num1,num2,num3):
    add=num1+num2+num3
    avg=add/3
    print(add)
    print("average=",avg)
num1=int(input("enter a firstnumber:"))
num2=int(input("enter a second number:"))
num3=int(input("enter a third number:"))
sum(num1,num2,num3)
    