import math

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for numero in range(1, 101):
    if primo(numero):
        print(numero)