# Question (Part 1)

# calculator naam ka ek function banao jo teen argument leta ho - number_x, number_y, operation. number_x aur number_y mein 
# hum humesha do integers denge aur operation mein kaunsa operation karna hai woh denge. 
# Jaise: * Agar operation mein "add" diya toh number_x aur number_y ko add kar ke returna karega.

#     Agar operation mein "subtract" diya toh number_x aur number_y ko subtract kar ke return karenge.
#     Agar operation mein "multiply" diya toh number_x ko number_y se multiply kar ke returna karega.
#     Agar operation mein "divide" diya toh number_x ko number_y se divide kar ke return karega

# Neeche kuch function calls ke examples diye hue hain: * calculator(20, 25, "add") call karne pe 45 returna karega. 
# 45 hume 20+25 karne se milega.

#     calculator(40, 3, "subtract") call karne pe 37 return karega. 37 hume 40-3 karne se milega.
#     calculator(10, 4, "multiply") call karne pe 40 return karega. 40 hume 10*4 karne se milega.
#     calculator(40, 4, "divide") call karnse pe 10 return karega. 10 hume 40/3 karne se milega.

# Function likhne ke baad, yeh kaam karne ke liye function call karo aur variable mein value daalo. 
# * 24 aur 20 ko add karo aur number_1 variable mein value daalo

#     50 aur 60 ko multiply karo aur number_2 variable mein value daalo

#     80 aur 120 ko divide karo aur number_3 variable mein value daalo

#     90 aur 23 ko subtract karo aur number_4 variable mein value daalo



# def calculator(x,y,sym):
#     if sym=="+":
#         print(x+y)
#     elif sym=="-":
#         print(x-y)
#     elif sym=="*":
#         print(x*y)
#     elif sym=="/":
#         print(x/y)
# x=int(input("enter a number:"))
# y=int(input("enter a number:"))
# sym=input("enter a symbol:")
# calculator(x,y,sym)



# a="MISSISSIPPI"
# new={}
# for i in a:
#     if i not in new:
#         new[i]=1
#     else:
#         new[i]+=1
# print(new)



def even():
    i=0
    while i<10:
        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        i=i+1
even()








    



