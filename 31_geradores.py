from pympler.asizeof import asizesof

def dobro(lista):
    for i in lista:
        yield i*2


x = dobro(range(0, 100))

for i in x:
    print(i)

def mult(x, y):
    print(x * y)





