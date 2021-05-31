# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameter 
# ko hume check karana hai ki vo perfect number hain ya nahi.
#  Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 tak sabhi
#   perfect numbers ko print kare.[ hum ek aise integer number ko perfect number kahenge 
#   jo ki uske sabhi factors ( including 1 & excluding itself) ka sum uss number ke barabar 
#   hota hai. 
# Example:- Expected Output :- 


# num=int(input("enter a number"))
def perfect(num):
    i=1
    sum=0
    while i<=100:
        j=1
        while j<i-1:
            if j%i==0:
                sum=sum+i
            j=j+1
        i=i+1
        if sum!=num:
            print("itsnot perfect number",i) 
        else:
            print("its  perfect number",i)  
        # i=i+1
perfect(1<=100) 






# # def perfect():
# #     i=1
# #     p=1
# #     sum=0
# #     while i<=100:
# #         if i%p==0:
# #             sum=sum+p
# #             p=p+1
# #         i=i+1
# #     if sum==i:
# #         print("prefect number")
# #     else:
# #         print("not")
# # perfect(100)




# num=int(input("enter a number"))
# def perfect(num):
#     sum=0
#     i=1
#     while i<num:
#         if num%i==0:
#             sum=sum+i
#             if sum==num:
#                 print(num,"is perfect")
#             else:
#                 print("not perfect number")
#         i=i+1
# num=int(input("enter a number"))
# perfect(num)



# def perfect(n):
#     sum=0
#     i=1
#     for i in range(1,n):
#         if n%i==0:
#             sum=sum+i
#     if sum==n:
#         return True
#     else:
#         False
# for i in range(1,1001):
#     if perfect(i):
#         print( "perfect number ",i)
    
def perfect(n):
    sum=0
    i=1
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True
    else:
        False
for i in range(1,1001):
    if perfect(i):
        print( "perfect number ",i)
    

