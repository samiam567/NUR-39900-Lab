import time


# functions
def goodAns():
    print("Good choice!");

def badAns():
    print("Seriously dude?");


# list stuff
options = ["pizza", "bread", "worms and eyeballs"];


while(True):
    answer = input("What would you like to eat?\nchoices: " + str(options) + "\n");
    print("\n");

    # menu
    if (answer == options[0] or answer == options[1]):
        goodAns();
    elif (answer == options[2]):
        badAns();
    else:
        print("Invalid choice man, you're totally killing my vibe bro");

    print("\n\n\n");
    time.sleep(1);