n = 10
def pares_ate(n:int):
    for num in range(2,n + 1):
        if num % 2 == 0:
            yield num

for i in pares_ate(n):
    print(i)