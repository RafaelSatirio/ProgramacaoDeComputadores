tent = 0
print("Brincadeira: descubra o número")
print("Digite um número e seu amigo devera descubrir qual número é")
num = int(input())
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
print("-------------------------------------")
while True:    #This simulates a Do Loop
    print("Tente acertar o número que seu amigo digitou")
    print("Digite um número")
    chute = int(input())
    tent = tent + 1
    if chute > num:
        print("Chutou alto!!")
    if chute < num:
        print("Chutou baixo!!")
    if num == chute: break
print("ACERTOUUUU!!")
print("Número de tentativa = " + str(tent))
