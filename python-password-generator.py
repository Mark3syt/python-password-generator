import random
import string

def genera_password(lunghezza):
    caratteri=string.ascii_letters+string.digits+"!@#$%^&*"
    password=''
    for i in range(lunghezza):
        password+=random.choice(caratteri)
    return password

n=int(input("how many passwords? "))
lunghezza=int(input("length: "))

for i in range(n):

    print(genera_password(lunghezza))
    
input("\nPress ENTER to exit")
