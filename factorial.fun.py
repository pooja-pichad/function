def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial(0))
print(factorial(1))
print(factorial(4))
print(factorial(5))
print(factorial(10))
