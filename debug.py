# Debug Code

# Ab hum function se related code ko debug karenge. Question 1
 
# def greet(names):
#     for name in names:
#         print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender") 



def greet(*names):
    for name in names:
        print("Welcome", name)

greet("Rinki", "Vishal", "Kartik", "Bijender") 