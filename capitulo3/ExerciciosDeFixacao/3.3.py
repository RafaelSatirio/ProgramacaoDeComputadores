print("Digite um número para descobrir se ele é primo ou não")
num = int(input())
if num <= 1:
    print("O número que digitou não é primo!")
else:
    if num <= 3:
        print("O número que digitou é primo!")
    else:
        if num % 2 == 0 or num % 3 == 0:
            print("O número que digitou não é primo!")
        else:
            print("O número que digitou é primo!")
