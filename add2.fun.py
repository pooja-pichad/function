# add_numbers_list naam ka function likhiye jo do integers ki 2 lists leta ho aur fir same position wale integers
#  ka sum print karta ho. Same position waale 2 integers ka sum karne ke liye Part 1 mein di gayi add_numbers 
#  waale function ka use karo. 
#  Jaise agar hum iss function
#  ko [50, 60, 10] aur [10, 20, 13] denge ko woh yeh print karega
def add_numbers():
    a=[50, 60, 10]
    b=[10, 20, 13]
    i=0
    s=0
    while i<len(a):
        s=a[i]+b[i]
        i=i+1
        print(s)
    
add_numbers()
