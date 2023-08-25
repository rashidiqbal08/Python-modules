import os
print(os.getcwd())

def newdir():
    print(os.getcwd())

#this will change the dir  os.chdir()
os.chdir('D://SAMMI')
newdir()
#os.listdir() will print all the files in that dir.
for i in os.listdir():
    print(i)
