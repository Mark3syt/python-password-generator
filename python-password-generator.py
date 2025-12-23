import random
import string

def genera_password(lunghezza):
    caratteri=string.ascii_letters+string.digits+"!@#$%^&*"
    password=''
    for i in range(lunghezza):
        password+=random.choice(caratteri)
    return password

n=int(input("quante password? "))
lunghezza=int(input("lunghezza: "))

for i in range(n):

    print(genera_password(lunghezza))
    
input("\nPremi INVIO per uscire...")
