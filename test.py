'''
Four different ways of doing (mostly) the same thing
There are situations to use each of these
'''

def simpleWhileLoop():
    n = 0; # start with an n of zero
    while (n < 10): # keep looping until n is greater than or equal to 4
        print("n: " + str(n)); # print out what n is
        n = n + 1; # increase n by 1
    print("final n: " + str(n));

def simpleForLoop():
    for n in range(0,10): # range(0,10) equates to [0,1,2,3,4,5,6,7,8,9], so n will first be 0, then 1, then 2, etc.
        print("n: " + str(n));
    print("final n: " + str(n));


def forLoopWithList():
    values = [0,1,2,3,4,5,6,7,8,9];

    for n in values: # for this loop n will take a different value from the list values each time the loop runs
        print("n: " + str(n));
    print("final n: " + str(n));

def simpleForLoopAccessingList():
    values = [0,1,2,3,4,5,6,7,8,9];

    for i in range(0,10): # for this loop i will take the numbers [1,10), then we will use i to access the ith value of the list and set it to n
        n = values[i]; # set n to the ith value of the list values
        print("n: " + str(n));
    print("final n: " + str(n));

