from classes import Puppy

if __name__ == "__main__":
    my_pup = Puppy("Pringle", sex="M")
    print("I got a new puppy, his name is {}".format(my_pup.name))
    print("{}, sit!".format(my_pup.name))
    my_pup.sit()
    print("{} needs some training, oh well.".format(my_pup.name))
    my_pup.praise()