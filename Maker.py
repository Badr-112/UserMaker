import random
import os
from time import sleep
az = ["A" ,"B" ,"C" ,"D" ,"E", "F", "G" ,"H" ,"I" ,"J", "K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T" ,"U", "V", "W" ,"X" ,"Y" ,"Z",
    "1","2",'3','4','5','6','7','8','9','0','.','-','_']




user = ""
loop = 0
dirfile = os.getcwd() + r"\user.txt"

print("Programing By : heho.9")
def users():
    global user
    global loop
    file = open(dirfile,"w")
    numCh = int(input("Choose loop : "))
    numLen = int(input("Choose length : "))
    while True:
        randm = random.choices(az)
        user += randm[0]
        if numLen == len(user):
                
            if user[0] == '1' or user[0] == '2'or user[0] == '3'or user[0] =='4'or user[0] =='5'or user[0] =='6'or user[0] =='7'or user[0] =='8'or user[0] =='9'or user[0] =='0'or user[0] =='.'or user[0] =='-'or user[0] =='_':
                user = ""
            else:
                print(user)
                sleep(0.01)
                file.write(user + '\n')
                user = ""
                loop+=1
                if loop == numCh:
                    print("\nDone..\n")
                    agine = input("Do you want agine ? y / n :  ").lower()
                    if agine == "n":
                        print("Save in user.txt")
                        exit()
                    else:
                        loop = 0
users()

