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

#While Loops Training
#1. Въвеждане на валидна парола
password = input("Въведете парола (мин. 8 символа): ")
while len(password) <8:
    print("🚫 Паролата трябва да съдържа поне 8 символа!")
    password = input("Въведете парола отново: ")
print("✅ Паролата е зададена успешно!")
#|||||||||||||||
# Bank 🏦
balance = 1000
while True:
    print(f"\nВашият баланс: ${balance}")
    withdral = input("Въведете сума за теглене: ")

    if withdral == "exit":
     print(f"Крайно салдо: ${balance}")
     break
    amount = int(withdral)
    if amount > balance:
        print("Недостатъчно средства!")
    else:
        balance -= amount
        print(f"Изтеглихте {amount},и оставате с {balance}.")
#||||||||||||||
while True:
    text = input('Въведи нещо: ')
    if text == 'stop':
        print("Край на програмата!")
    break

secret_number = 69
while True:
    guess = int(input('Guess the number? '))
    if guess == secret_number:
        print('You winn')
        break
    else:
        print('Try again')

#|||||||||||||
#Moving Items from One List to Another
#Start with users that need to be verified
#and an empty list to to hold confirmed users
unconfirmed_users = ['venelin','hempa','petrov','adnan']
confirmed_users = []
#Verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title}.")
    confirmed_users.append(current_user)
#Displey confirmed users
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#|||||||||||||||||
waiting_order = ['Пица','Суши','Бургер','Салата']
ready_orders = []

while waiting_order:
    current_order = waiting_order.pop()
    print(f"Приготвяне на поръчка:{current_order.title}")
    ready_orders.append(current_order)
    print("Следните поръчки са готови:")
for order in ready_orders:
    print(order)

#TRY IT YOUR SELF
#Sandwich Order Cleanup
sandwich_orders = ['Club Sandwich','Reuben Sandwich','BLT','Philly Cheesesteak','pastrami','pastrami','pastrami']
print("Sorry we run out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []
while sandwich_orders:
    orders = sandwich_orders.pop()
    print(f"I made you {orders.title()} ,sandwich")
    finished_sandwiches.append(orders)

print("\nFinished sandwiches")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)

#Dream Vacation
dream_vacation = {}
polling_active = True
while polling_active:
    name = input("Whats your name? ")
    dream_vacations = input("If you could visit one place in the world,where would you go? ")
    dream_vacation[name] = dream_vacations

    repeat = input("Would you like to let anothe person respond?  (yes/ no)")
    if repeat == 'no':
        polling_active = False
print("---Polling Results---")
for name,dream_vacations in dream_vacation.items():
    print(f"{name} would like to go to {dream_vacation}.")


