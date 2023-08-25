##RANDOM MODULE
    #used to generate random numbers.
##SYNTAX:-  random.choice() ,random.randint(0,5),random.shuffle()


import random

list=[21,23,25,27,29]
print("Original list: % s"%(list))

random.shuffle(list)    #this method will create diff sequence in each iteration
print("List after applying random module: ",list)

a=random.choice(list)  #it will print any random element
print(a)

print(random.randint(1,7))  #it takes two arguments

print(random.randrange(7))   #it take only one argument

print(random.random()) #it takes no argument

print(random.sample(list, 3))

string='rashid'
# random.shuffle(string)  #error (string and tuple are immutable so can't use shuffle)
print(string)
print(random.sample(string,3)) #it will convert str to list than print


