# print ("NavGurukul")

# def say_hello():
#     print ("Hello!")
#     print ("Aap kaise ho?")

# say_hello()
# print ("Python is awesome")
# say_hello()
# print ("Hello…")
# say_hello() 


# Q2
# names_list = ["Fiza", "Shivam", "Imtiyaz", "Deepanshu", "Rahman"]
# print (len(names_list)) 


# Q3
# def definition_say_hello():
#     print ("NavGurukul")
#     print ("NavGurukul mei humein apni learning ki responsibility leni padti hai.")

# definition_say_hello()

# print ("NavGurukul mei hum sab logo ko ek tarah se treat karte hai.")

# definition_say_hello() 

# Q4

# def function_say_bye():
#     print ("Aapko mil ke maza aaya. ")
#     print ("Bye bye")
# function_say_bye()
# function_say_bye()
# print ("Python ka istamaal bahot jagah hota hai.")
# function_say_bye()
# function_say_bye() 

# Output :-



# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list)) 

# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(str(num_x), name) 




# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev") 

# Output


# def icecream(*flavours):
#     for flavour in flavours:
#         print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry") 




# Default parameter value

# Default parameter value se yaha humara ye matlab hai ki hum function ko define karte time kisi parameter ko value assign kar dete hai taaki hum function ko bina kisi argument ke call kare to vo default value ko le le. Example :-
 
def attendance(name,status="absent"):
    print(name,"is",status," today")

attendance("kartik","present")
attendance("sonu")
attendance("vishal","present")
attendance("umesh") 