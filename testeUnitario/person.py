class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def update_age(self, new_age):
        self.age = new_age

    def is_adult(self, min_age=18):
        return self.age >= min_age
