# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list
#  ko arguments ki tarah le aur fir check kare ki same index waale dono integers even hain ya nahi. 
#  Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo.
#   Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur [2, 6, 18, 10, 3, 75] Toh usko yeh output deni 
#   chaiye:
# Edit on Github
# def check_numbers_list():

    
# a=[2, 6, 18, 10, 3, 75]

def check_numbers(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print(a[i],b[i],"dono even hain")
        else:
            print(a[i],b[i],"dono odd hai")
        i=i+1
check_numbers([2, 6, 18, 10, 3, 75],[7,8,4,2,90,34])
