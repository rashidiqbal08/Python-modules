## program to understand RegEX
from ast import pattern
import re


String='''what is your name
            i am rashid iqbal
            no.= 797938089
            i am 
            i am
            i belongs to bokaro steel cityy
            currently pursuing my b.tech degree from tit group of institute
            '''

#to check if string starts from 'wha' for this we use ^ metachar
Pattern= re.compile(r'^wha')  #will print this word if it starts with 'wha'.
match = Pattern.findall(String)
print(match)

#to check if it ends with particular word or not(for this we use $).
Pattern = re.compile(r'te$')
match= Pattern.findall(String)
print(match)
if match:
    print("Yes")

#to print the set of character for this we use [ - ]
Pattern = re.compile(r'[a-e]') #print all the char in berween a and e
match= Pattern.findall(String)
print(match)
if match:
    print("Yes")

# now we'll see some use of special sequence
# \d and \d+

s= ''' abcheetghiiikljyoooofhfvt12'''
Pattern =r'[\baeiouAEIOU]'
match2=re.findall(Pattern,s)
if match2:
    print(*match2,sep='\n')
else:
    print('-1')
start= s.start()
end= s.end()
print(start)


print(match2)
print(match)
for i in match:
    print('\n',i)

Pattern = re.compile('\d')  #will print all the digit from (0,9)
match= Pattern.findall(s) #d+ will print the group of dig.
print(match)
# and D return a string which doesnt contain anyy string.



s='rashidiqba'
match= re.search(r'^[7-9]\d{9}',s)
if match:
    print('YES')
else:
    print("NO")



import re

for _ in range(int(input())):
    if re.match(r'^[789]\d{9}$', input()):
        print('YES')
    else:
        print('NO')