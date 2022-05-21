
if __name__ == '__main__':
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"Name: {self.name}, Age: {self.age}"

        def __repr__(self):
            return f"<Person('{self.name}', {self.age})>"

    bob = Person("Bob", 25)
    print(bob) # <__main__.Person object at 0x000001992337CEE0> (without __str__(self))
    print(bob) # Name: Bob, Age: 25 (with __str__(self))
    print(bob.__repr__()) # <Person('Bob', 25)>
    print(repr(bob)) # <Person('Bob', 25)>

