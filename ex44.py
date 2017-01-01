# Implicit Inheritance


class Parent(object):

    @staticmethod
    def implicit():
        print("PARENT implicit()")


class Child(Parent):
    pass
    # By inheriting the Parent class, the child class actual looks like below.  This is a way to reduce duplicate code

    # @staticmethod
    # def implicit():
    #     print("PARENT implicit()")

dad = Parent()
son = Child()
dad.implicit()
son.implicit()
print('-' * 20)
########################################################################################################################


# Override Explicitly
class Parent(object):

    @staticmethod
    def override():
        print("PARENT override()")


class Child(Parent):
    # Sometimes you want to override a method in the Parent class, essentially replacing it's functionality
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()
dad.override()
son.override()
print('-' * 20)
########################################################################################################################


# Alter Before or After
class Parent(object):

    def altered(self):
        print("PARENT altered method called")


class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE calling PARENT.altered()")
        # super() allows you to avoid calling the parent class directly, but the main advantage comes when you are
        #   using multiple inheritances
        super(Child, self).altered()
        print("CHILD, AFTER calling PARENT.altered()")


dad = Parent()
son = Child()
dad.altered()
son.altered()

