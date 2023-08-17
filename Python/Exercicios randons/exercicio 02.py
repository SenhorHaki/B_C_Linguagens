#Escreva um programa que escreva na tela, de I até 100, de I em I, 3 vezes. A primeira vez deve usar a estrutura de repetição for, a segunda while, e a terceira do while.
for i in range(1, 101):
    print(i)
i = 1
while i <= 100:
    print(i)
    i += 1
i = 1
while True:
    print(i)
    i += 1
    if i > 100:
        break
