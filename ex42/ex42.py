# -*- coding: utf-8 -*-

## Animal наследует object
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ##??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

    ## Person - композиция животного некоторого вида
    self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? Хмм, что за странная магия?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover наследует Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()