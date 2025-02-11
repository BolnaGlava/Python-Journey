print ('{} {}!'.format('Pythone','rules'))

P = 'Pythone rules!'
print(f'I like the new {P}')

#Упражнения за .format():
'{} loves {}.'.format('Andro','Pythone')

'{1} is better than {0}.'.format('Beni','Mitko')

'{name} loves to smoke at least {number} joints a day!'.format(name='Andro',number=5)

'The result is {:.5f}.'.format(123.123123)

#Упражнения за f-strings:
name='Andro'
age= 21
print(f'My name is {name},and my age is {age}!')

num=5
print(f'The square of {num} is {num**3}.')

#TRAINING
d= {'simple_key':'hello'}
d ['simple_key']

d = {'k1':{'k2':'hello'}}
result = d['k1']['k2']
print(result)

d= {'k1':[{'nest_key':['this is deep',['hello']]}]}
result = d['k1']['nest_key']['this is deep']
print (result)

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
result = d ['k1']['k2']['tough']
print(result)

list5 = [1,2,2,33,4,4,11,22,3,3,2]
set(list5)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':3}]
l_one[2][0] >= l_two[2]['k1']

list = [2,1,3,5,4,7,6]
sorted(list)

hungry = True
if hungry:
    print('feed me')
else:
    print('I am not hungry') 


    
#IF,ELIF,ELSE


loc = 'mari'

if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store!') 
else:
    print('I do not know much.')

#Loops
mylist = [1,2,3,4,5]

for num in mylist:
    print('hello world')

for _ in 'Hello World':
    print('Cool!')

 #Tuple unpacking
lists = [(1,2,3),(5,6,7),(8,9,10)]
for a,b,c in lists:
    print(b)

d = {'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(key,value)


mystring = 'Sezer'

for letter in mystring:
    if letter == 'z':
        continue
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1

mylist = [1,2,3]
for num in range(0,10,2):
    print(num)


index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count +=1

#ENUMERATE
word = 'abcde'
for index,letter in enumerate (word):
    print(index)
    print(letter)
    print('\n')

#ZIP
mylist1 = [1,2,3,4,5,6]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for a,b,c in zip(mylist1,mylist2,mylist3):
    print(b)

list(zip(mylist1,mylist3))

#RANDINT - RANDOM

from random import randint
randint(0,100)
 

#програма на пайтон която върти цикъл от1 до 10 и на всеки четен индекс вкарва цифра в лист

even_index_list =[]
for i in range (1,11):
    if i % 2 == 0:
        even_index_list.append(i)
        print("Списък с четни индекси:", even_index_list)
for num in even_index_list:
    print(num)

    
mylist = []
for n in range (1,21):
    if n % 2 !=0:
        mylist.append(n)
        print('списък само нечетните числа:')


cikyl = []
for n in range(1,51):
    if n % 3==0:
        cikyl.append(n)
        print('Числата, които се делят на 3 без остатък.',cikyl)

cikyl2 = []
for n in range(1,51):
    if n % 5 == 0:
        cikyl2.append(n)
        print('Числата, които се делят на 5 без остатък.',cikyl2)

