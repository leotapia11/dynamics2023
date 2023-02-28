def limite(x):
    listafracc =[]
    lista_int = []
    for i in range(1,x):
        listafracc.append(("\\frac{}/{10^",i,'}'))
        lista_int.append((1/10**i))
    return listafracc,lista_int
print(limite(10))
