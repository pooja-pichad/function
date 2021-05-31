def calculation(num1, num2):
    return (num1 + num2), (num1 * num2)

sum, product = calculation(10, 20)
print("Sum:", sum, "Product:", product)





def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False
def div6(y):
    if is_even(y) and y%3 == 0:
        return True
    else:
        return False
		
print(div6(12))  