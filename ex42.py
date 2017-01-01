"""
Use is-a when you talk about objects and classes being related to each other "by a class relationship".
Use has-a when you talk about objects and classes that are related "only because they reference each other".
"""


# Animal has-a object
class Animal(object):
    pass


# Dog has-a object
class Dog(Animal):

    def __init__(self, name):
        # Name is-a object
        self.name = name


# Cat has-a object
class Cat(Animal):

    def __init__(self, name):
        # Name is-a object
        self.name = name


# Person has-a object
class Person(object):

    def __init__(self, name):
        # name is-a person
        self.name = name

        # Person has-a pet
        self.pet = name


# Employee has-a object
class Employee(object):

    def __init__(self, name, salary):
        #
        super(Employee, self).__init__(name)
        # Salary is-a object
        self.salary = salary


# Fish has-a object
class Fish(object):
    pass


# Salmon has-a object
class Salmon(Fish):
    pass


# Halibut is-a object
class Halibut(Fish):
    pass


# rover is-a dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

# mary is-a person
mary = Person("Mary")

# pet is-a object
mary.pet = satan

# Frank is-a object
frank = Employee("Frank", 120000)

# Frank's pet is-a object
frank.pet = rover

# flipper has-a object
flipper = Fish()

# flipper has-a object
flipper = Fish()

# crouse is-a object
crouse = Salmon()

# harry is-a object
harry = Halibut()



