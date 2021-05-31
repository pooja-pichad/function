# Question 4

# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter lega aur 0 se limit 
# tak ke beech ke sabhi even aur odd numbers ko label ke saath print karega jaisa ki niche dikhaya gaya hai.
#  For example :- Input:- Output :-

def showNumbers(limit=10):
    i=0
    while i<=limit:

        if i%2==0:
            print("even",i)
        else:
            print("odd",i)
        i=i+1
showNumbers()
