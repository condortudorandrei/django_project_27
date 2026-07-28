import random
from pprint import pprint
# picked = random.choice(numbers)

numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17]
people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]


def person_constructor_base(name, age):
    if age >=18:
        of_age = True
    else:
        of_age = False
    temp_person = {
        "name": name,
        "age": age,
        "of_age": of_age,
    }
    return temp_person

def main_constructor(people: list, numbers: list):
    persons = []
    for element in people:
        temp_age = random.choice(numbers)
        temp_person = person_constructor_base(element, temp_age)
        persons.append(temp_person)
    return persons

def show_list(persons: list):
    for element in persons:
        print(f"{element}")

def show_of_age_list(persons: list):
    for element in persons:
        if element["of_age"] == True:
            print(f"{element}")

def boomer(persons: list):
    current_age = 0
    current_person = {}
    for element in persons:
        if element["age"] > current_age:
            current_person = element
            current_age = element["age"]
    return current_person

def zoomer(persons: list):
    current_age = 999
    current_person = {}
    for element in persons:
        if element["age"] < current_age:
            current_person = element
            current_age = element["age"]
    return current_person


persons = main_constructor(people, numbers)
show_list(persons)
print("\nOf age list")
show_of_age_list(persons)
print("\nBoomer")
print(boomer(persons))
print("\nZoomer")
print(zoomer(persons))






