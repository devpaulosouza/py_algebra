from py_algebra import matriz

# testes de aritimética
a = matriz.matriz(3,3)
a.ler_matriz()

b = matriz.matriz(3,3)
b.ler_matriz()

c = a*b

# testes Gauss-Jordan
d = matriz.matriz(2,3)
d.ler_matriz()

d.gera_pivo(0)
d.zera_coluna(0)

d.gera_pivo(1)
d.zera_coluna(1)


print(d)
