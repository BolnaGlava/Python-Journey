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

#TRY IT YOURSELF
#Pizza Toppings
while True:
    toppings = input("Enter a pizza toppings  (or type 'quit'to finish): ")
    if toppings =='quit':
        print("Your pizza is ready!")
        break
    print(f"Adding {toppings} to your pizza!")

#Movie Tickets:
while True:
    age = int(input("Whats you age? "))
    if age <3:
        price = 'Free'
    elif age >3<12:
        price = "10$"
    elif age >12:
        price = "15$"
    break
print(f"This is the cost of the ticket {price}.")
