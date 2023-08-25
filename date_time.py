##DATE AND TIME MODULE IN PYTHON

import time
import datetime  #we can create object with datetime by passing date
#print the current time
import calendar
print(time.localtime(time.time()))

#print the current time in formatted way
print(time.asctime(time.localtime(time.time())))


##.sleep() method to delay the time of execution
 
for i in range(0,4):
    # print("Rashid iqbal")
    print(time.asctime(time.localtime(time.time())))
    time.sleep(3)
ob=datetime.datetime(2022,10,15,17,12)
print(ob)
print(type(ob))   #type is class


##printing calender
# print(calendar.month(2022,15))

