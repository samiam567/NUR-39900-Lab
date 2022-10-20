
def addAppendage(name, options, num):
    list = [];

    print("What " + name + "s do you want?");

    i = 0;
    while (i < num):
        choice = input("Your options are: " + str(options));
        if (choice in options):
            print('good choice!');
            list.append(choice);
        else:
            print("invalid value");
            continue;
        i+=1;

    
    return list




sauces = addAppendage("sauce", ["chocolate syrup", "strawberry syrup"],2);

print("you chose: " + str(sauces));
