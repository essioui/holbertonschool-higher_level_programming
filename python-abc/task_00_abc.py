#!/usr/bin/python3

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

if __name__ == "__main__":

    bobby = Dog()
    garfield = Cat()

    print(bobby.make_sound())
    print(garfield.make_sound())

# The following line will raise a TypeError because Animal is abstract
# animal = Animal()
# print(animal.make_sound())
