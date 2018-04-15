#coding=utf-8
def make_pizza(size,*toppings):
    print("\nmaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-"+topping)


def make_drink(number,*types):
    print("\nmaking a "+str(number)+"cup drink with the following types:")
    for type in types:
        print("-"+type)