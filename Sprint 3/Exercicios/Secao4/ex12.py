list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def f(x):
    return x ** 2
        
def my_map(list, f):
    return [f(x) for x in list]
    
result = my_map(list, f)

print(result)