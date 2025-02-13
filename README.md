📌 Project Description
This is a collection of Python exercises that I completed to practice and enhance my programming skills.

## 📝 Exercises:
- **📂 People Info:** Working with lists and dictionaries to store information about people.
- **🐾 Pets Info:** Using loops and data structures to list pet details.
- **📍 Favorite Places:** Utilizing dictionaries and lists to display favorite places.
- **🔢 Favorite Numbers:** Managing lists of favorite numbers for different people.
- **🌍 Cities Information:** Using nested dictionaries to showcase city facts.

# Try it yourself 111 - Python Practice Exercises

# People Info
person_1 = {
    'first': 'alexander',
    'last': 'petrov',
    'age': 20,
    'city':'ruse'
}
person_2 = {
    'first': 'venci',
    'last': 'genov',
    'age': 22,
    'city':'ruse'
}
person_3 = {
    'first': 'venelin',
    'last': 'venkov',
    'age': 20,
    'city':'holandiq'
}

people = [person_1,person_2,person_3]
for person in people:
    print("Person info:")
    for key,value in person.items():
        print(f"{key.title()}: {value}")

# Pets Info
pet_1 = {'animal':'dog','name':'Dayzi','owner':'Iasen'}
pet_2 = {'animal':'cat','name':'Tomi','owner':'Miro'}
pet_3 = {'animal':'hamster','name':'Hami','owner':'Sezer'}
pet_4 = {'animal':'rabit','name':'Zuek','owner':'Rumi'}

pets = [pet_1,pet_2,pet_3,pet_4]
for pet in pets:
    print("\nPets Info!")
    for key,value in pet.items():
        print(f"{key.title()}: {value.title()}")

# Favorite Places
favorite_places = {
    'Venelin': ["Paris,New York City,Sydney"],
    'Zul': ["Machu Picchu,Kyoto,Santorini"],
    'Petrov': ["Rome,Tokyo,Barcelona"]
}
for key,value in favorite_places.items():
    print(f"\n{key}'s favorite places are:")
    for values in value:
        print(f"-{value}")

# Favorite Numbers
peoples_numbers = {
    'pifo': [69,32,124,1241],
    'gafart': [1,123,4],
    'venelincho':[7,231,312],
    'koki':[5,213,412],
    'mimo':[21,352,686]
}
for name,number in peoples_numbers.items():
    print(f"\n{name} your favorite number is")
    for numb in number:
        print(f"--{numb}")

# Cities Information
cities = {
    'Berlin':{
        'Country':'Germany',
        'Population':'Around 3.7 million',
        'Fact':'Berlin is famous for the Berlin Wall, which fell in 1989.'
    },
    'London':{
        'Country':'United Kingdom',
        'Population':'Around 9 million (as of 2023)',
        'Fact':'London is home to the world\'s first underground railway.'
    },
    'Cape Town':{
        'Country':'South Africa',
        'Population':'Around 4.7 million (as of 2023)',
        'Fact':'Cape Town is home to Table Mountain.'
    }
}
for city,city_info in cities.items():
    print(f"\n{city}:")
    for key,value in city_info.items():
        print(f"{key}: {value}")

