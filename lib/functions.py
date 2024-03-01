#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print(f'Hello, {name}!')
greet('laith')

def greet_with_default(name="programmer"):
    print(F'Hello, {name}!')
greet_with_default()
greet_with_default('Laith')

def add(num1, num2):
    return num1 + num2
sum = add(1,2)
print(sum)

def halve(number):
    return number / 2


def my_function(param):
    print('running my function')
    return param + 1

my_function_return_value = my_function(1)
print(my_function_return_value)

def say_hi(name):
    print(f"Hi there, {name}!")

say_hi('laith')

def say_hi(name="Engineer"):
    print(f"Hi there, {name}!")

say_hi()
say_hi('laith')

def stylish_painter():
    best_hairstyle = "Bob Ross"
    return "Jean-Michel Basquiat"
    return best_hairstyle
    print(best_hairstyle)

stylish_painter()