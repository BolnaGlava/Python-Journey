#26.1.2025.


                        #LISTS

#[]-с това се обузначават листовете в тях можем да събираме инфо
#примерен лист 
bicycles = ['trek','annondale','redline','specialized']
print(bicycles)

#с индекси можем да си избираме какво искаме от даден лист 
print(bicycles[0])

# с командата .title() можем да направим по презентативно искането
print(bicycles[0].title())

#Създаване на изречение с ф-стринг и нещо от лист
bicycles = ['trek','annondale','redline','specialized']
message = f'My first bike was {bicycles[0].title()}'
print(message)

#Упражнения
names = 'Sezer','Mario','Andro'
print (names[1])
message = f'My names is {names[2].title()}'
print (message)

#Можем да променяме неща в напия лист
cars = ['honda','merc','bmw']
print(cars)
cars[0] = 'lada'
print (cars)

#Можем да инсъртваме елемнти в листа си insert()
cars = ['honda','merc','bmw']
cars.insert(0, 'golf')
print(cars)

#Можем да премахваме работи от нашия лист с командата del
cars = ['honda','merc','bmw']
del cars[0]
print(cars)

#Pop() Метода
cars = ['honda','merc','bmw']
poped_cars = cars.pop()
print(cars)
print(poped_cars)

#Упражнения
guest_list = ['Andro','Mario','Stoev']
message = f'I invite you to diner with me {guest_list[1].title()}'
print (message)
busy = guest_list.pop(1)
print (busy)
guest_list.insert(0,'Venelin')
guest_list.insert(3,'Mario')
guest_list.insert(4,'Denko')
guest_list.append('Goras')
print(guest_list)
print (f"This is new invitation for you guys {guest_list}")
print (f'I can invite only to people I am very sorry {guest_list}')
poped_members = guest_list.pop(0)
print (f'I am sorry i cant invite you {poped_members}')
print (f'You are still invitet do the dinner {guest_list}')
del guest_list [0]
print (guest_list)
len(guest_list)

#Sort() Метода
cars = ['honda','merc','bmw']
cars.sort()
print(cars)
cars.sort(reverse=True)

#Упражнения
destinations = ['Ruse','Burgas','Sofia','Tyrnovo','Basarbovo']
print(destinations)
destinations.sort()
print(destinations)
destinations.reverse()
print(destinations)
destinations.sort(reverse=True)
print(destinations)

#/////////////////////////////////////////  For Loop
magicians = ['andro', 'stoev','goras']
for magician in magicians:
    print(magician)

#Printing mesage with For Loop
magicians = ['andro', 'stoev','goras']
for magician in magicians:
    print(f"{magician.title()},that trick was very good.")

#Printing second mesage with For Loop
magicians = ['andro', 'stoev','goras']
for magician in magicians:
    print(f"{magician.title()},that trick was very good.")
    print(f"I can't wait to see your next trick,{magician.title()}.\n") #използвам .\n-нов ред
    #Можем да завършим loop-а с последно изречение което не се отнася към в случая магиосниците
    print('Thank you,everyone.That was a great magic show!')

#Упражнения 1
pizzas = ['caprichoza','margariata','kamen']
for pizza in pizzas:
    print(f"I really like {pizza.title()}!")
    print(f"I'am in love with {pizza.title()}!.")
    print(f"I really want to it {pizza.title()} right now!.\n")
    print('I really love pizza')

#Упражнения 2
pets = ['dog','cat','hamster']
for pet in pets:
    print(f"A {pet} would make a great pet.")
    print('Any of these animals would make a great pet!')

# range() Function
for value in range(1,10):
    print(value)

#Използване на range() за направата на лист от числа
number = list(range(1,6))
print(number)

#Упражнение
number = list(range(1,21))
for num in number:
    print(f'{num}')

number = list(range(1,1000001))
for num in number:
    print(f'{number}')

number = list(range(1,1000001))
min(number)
max(number)
sum(number)

cubes = []
for num in range(1,11):
    cubes.append(num**3)
for cube in cubes:
    print(cubes)

cubes = [num**3 for num in range(1,11)]
print(cubes)

#Looping through a slice
players = ('Andro','Simba','Denka','Goras','Stoev')
print('Here are tje first three players on my team:')
for player in players[:3]:
    print(player.title())

#Упражнение
pizzas = ['caprichoza','margariata','kamen']
friend_pizza = ['caprichoza','margariata','kamen']
friend_pizza.append('kotkata')
for piz in friend_pizza:
    print(f'My favorite pizzas are {piz.title()}')
for piz in pizzas:
    print(f'My favorite pizzas are {piz.title()}')

#TUPLES - те са обградени от () а не от []
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#For Lopp with TUPLE
dimensions = (200,50)
for dimention in dimensions:
    print(dimention)

#Упражнение
old_menu = ('salam','hlqb','sirene','domati','bira')
for menu in old_menu:
    print(menu)
new_menu = ('salam','hlqb','sirene','maslini','laina')
for menu in new_menu:
    print(menu)


#IF STATEMENTS

cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Cheking fo equality with ==

#Cheking for Inequality with !=

#Пример
requested_toppings = 'mushrooms'
if requested_toppings != 'tomato':
    print('Hold the tomato')

#Пример
answer = 12
if answer != 42:
    print('This is not the correct answer,please try again')

#Whit IN we can chek if something is in a list

toppings = ['mushrooms','qica','pile','maslini']
'maslini'in toppings
# Whit not we can chek the oposite

banned_users = ['adrei','mario','denkata']
user = 'sezer'
if user in banned_users:
    print(f'{user.title()} you can write anything you want.')


#Упражнение
#Проверка за равенство и неравенство 
x = 10
y = 20
print (x == y)
print (x !=y)

#Проверка с метода lower()
text = "Hello"
print (text.lower() == "hello")

#Проверка дали елемент е в списък 
toppings = ['mushrooms','qica','pile','maslini']
'maslini'in toppings

#IF Statmens and ELSE , ELIF
#Пример ако имаш години може да гласуваш
age = 10
if age >=18:
    print('You can vote')
    print('Have you registered to vote yet?')
else:
    print('Sorry you are not old enough to vote')
    print('Please register to vote ass soon you turn 18')

#/////////////////
