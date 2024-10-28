import random

def main():
    lista = []
    lista = [random.randint(0, 10000000) for i in range(250)]
    lista.sort(reverse=True)
    print(lista)

if __name__ == "__main__":
    main()
