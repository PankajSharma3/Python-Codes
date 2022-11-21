import random
import os
os.system('cls')

print()

s=0
while 2:
    if s>=0:
        print("Score: ",s)
    else:
        print("Score: 0")
        s=0
    print('''
                         _       _   _   ____     ___  
                        | |     | | | | |  _ \   / _ \ 
                        | |     | | | | | | | | | | | |
                        | |___  | |_| | | |_| | | |_| |
                        |_____|  \___/  |____/   \___/ 
                                                       

''')
    c=random.randrange(1,7)
    a=input("Enter your number: ")
    if a=="end":
        break
    elif a=="" or int(a)>6:
        print("Wrong Input")
    elif int(a)==c:
        print("Computer Number:",c)    
        print("You Won")
        s=s+100
    else:
        print("Computer Number:",c)    
        print("You Loose")
        print("Better Luck Next Time")
        s=s-10
    print()
    print()
    a=input("Press ENTER for Next round")
    os.system('cls')
    print()
    print()

