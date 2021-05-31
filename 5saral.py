# Question 5

# Yeh question 2 parts mein hai. Dono parts ka code same file mein likh ke submit karein.
# Question (Part 1)

# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain"
# o numbers even (2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"
# # 

def check_numbers(a,b):
    if a%2==0 and b%2==0:
        print("dono even hain")
    else:
        print("dono odd hai")
check_numbers(45,50)