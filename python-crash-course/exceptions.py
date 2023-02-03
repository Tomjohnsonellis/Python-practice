"""
Some functions to raise exceptions
"""
# Non-Fatal issues can be reported with these modules
import warnings
import logging
def warn_user():
    warnings.warn("You are not welcome here.")
    logging.warning("Be careful!")


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

    if name.upper() == "BOB":
        warn_user()

    print("Hello {}!".format(name))


if __name__ == "__main__":
    greet_user()
    print("Have a wonderful day!")