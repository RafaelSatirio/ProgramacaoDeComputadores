# Módulo três
def modulo_tres():
    global b, d
    b = c * 2
    d = e + 1

# Módulo dois
def modulo_dois():
    global a, d, e
    a = c * 5
    d = a + 2
    e = b - 1
    modulo_tres()

# Módulo um
def modulo_um():
    global a, c
    a = b + 4
    c = a - 1
    modulo_dois()

# Variáveis globais
a = 5
b = a + 5
c = b - 3
modulo_um()

print("Valor de a:", a)
print("Valor de b:", b)
print("Valor de c:", c)
print("Valor de d:", d)
print("Valor de e:", e)
