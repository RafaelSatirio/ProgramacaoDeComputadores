sI = 0
for v in range(1, 50 + 1, 1):
    print("Digite um número")
    num = int(input())
    if num % 2 == 1:
        if num % 3 == 0:
            sI = sI + num
        else:
            print("Não serve pra ser divisivel por 3")
    else:
        print("Não serve pra ser divisivel por 3")
print("Soma dos números impares = " + str(sI))
