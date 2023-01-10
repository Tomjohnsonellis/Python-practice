# import this

# String Manipulation
print("This is a simple message.")
text = "formatted"
print("This is a {} string.".format(text.upper()))

list_of_names = ["Adam","Ben","Christian","Douglas","Ellie","Frankie","GODZILLA"]
print("Hello! My name is {}".format(list_of_names.pop()))
import random
random_number = random.randint(0,len(list_of_names) - 1)
print("My best friend is {}".format(list_of_names.pop(random_number)))
random_number = random.randint(0,len(list_of_names) - 1)
print("My sworn enemy is {}.".format(list_of_names.pop(random_number)))

# Looping through lists
for name in list_of_names:
    print("{}, ".format(name), end="")

print("are acquaintances.")

