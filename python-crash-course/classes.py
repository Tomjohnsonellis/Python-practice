# Chapter 9: Classes
# This chapter covers Object-Oriented Programming
# Base Class -> Instances of that class

class Dog():
    """A Class representing the fundamentals of a Dog"""
    def __init__(self, name, age, sex="M"):
        """Initialise some attributes common to every dog"""

        self.name = name.title()
        self.age = age
        self.sex = sex.upper()

    def sit(self):
        """ Make the dog sit"""
        print("*{} sits.*".format(self.name))

    def praise(self):
        """Praise the dog"""
        if self.sex == "M":
            print("Good boy {}!".format(self.name))
        else:
            print("Good girl {}!".format(self.name))

    def age_dog(self):
        self.age += 1
        if self.age <= 10:
            print("{} is now {} years old.".format(self.name, self.age))
        else:
            print("{} has died.".format(self.name))

    def rename(self, new_name):
        print("{} has been renamed to {}.".format(self.name, new_name))
        self.name = new_name.title()
        print("Take good care of {}!".format(self.name))



class Puppy(Dog):
    """A Puppy is a young dog"""
    def __init__(self, name, age=0, sex="F"):
        super().__init__(name, age, sex)

    def sit(self):
        print("{} hasn't learnt to sit!".format(self.name))


if __name__ == "__main__":
    my_dog = Dog("bingus",5)
    my_dog.sit()
    my_dog.praise()
    new_pup = Puppy("Jingles")
    new_pup.sit()

    # my_dog.sit()
    # my_dog.praise()
    # my_dog.age_dog()
    # my_dog.age_dog()
    # my_dog.age_dog()
    # my_dog.age_dog()
    # my_dog.age_dog()
    # my_dog.age_dog()
    # my_dog.praise()
    #
    # print("-----")
    #
    # your_dog = Dog("Grunklington", 8, "F")
    # your_dog.age_dog()
    # your_dog.sit()
    # your_dog.praise()
    # your_dog.rename("Polly")



