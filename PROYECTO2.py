import random

letras="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud=int(input())
clave=""
for i in range(longitud):
    temp=random.choice(letras)
    clave+=temp
print(clave)