#!/usr/bin/python3

class SwimMixin:
    """Define SwimMixin"""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Define FlyMixin"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Define Dragon class inheriting from SwimMixin and FlyMixin"""
    def roar(self):
        print("The dragon roars!")
