"""
Some functions to raise exceptions
"""


# Making simple custom exceptions is easy thanks to OOP
# We make a new class that is an "Exception" object
# And pass our custom message to it
class BingusDetected(Exception):
    def __init__(self, message="NO BINGUS ALLOWED."):
        self.message = message
        super().__init__(self.message)


def greet_user():
    name = input("Hello, what is your name? > ")
    if name.upper() == "BINGUS":
        raise BingusDetected
    else:
        print("Hello {}!".format(name))


if __name__ == "__main__":
    greet_user()
