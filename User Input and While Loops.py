📌 About the Project
This repository contains Python exercises focused on **user input**, **while loops**, and **interactive programs**. The goal is to improve fundamental programming skills through practical examples.

## 📝 Exercises Overview:
- **🖋️ User Input:** Getting input from users and dynamically responding.
- **🔢 Numerical Input:** Handling and validating numerical inputs using `int()`.
- **🔄 While Loops:** Implementing `while` loops for repeated interactions.
- **🍕 Practical Scenarios:** Rental car inquiries, restaurant seating, and pizza topping selection.
- **🎮 Interactive Tasks:** Password validation, ATM withdrawal simulation, guessing game, and more!
- **🥪 Data Processing:** Managing lists, verifying users, and removing specific items.
    
#User Input and While Loops
name = input("Please write your name: ")
print(f"Hello {name}!")
#|||||||||||||||||||||||||||||
prompt = "If you share your name,we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name}!")

#Using int() to Accept Numerical Input
age = input("How old are you? ")
age = int(age)
age >=18

#How to use int() in program
height = input("How tall are you? ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#TRY IT YOURSELF
#Rental car
car = input("What kind of rental do you want? ")
print(f"Let me see if I can find you a {car}.")

#Restaurant Seating:
group = input("How many people are in your group? ")
group = int(group)

if group >=8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready!")

#Multiples of Ten
number = int(input("Enter a number: "))
if number % 10 == 0 :
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")


#               ||||||||||||||||||||||||||||||||||||||
#          |||||||||||||||||||||||||||||||||||||||||||||||||||
#               ||||||||||||||||||||||||||||||||||||||

#Introducing while Loops
name = input("Enter your name: ")

while name == "":
   print("You did not enter your name!")
   name = input("Enter your name: ")

print(f"Hello {name}")
