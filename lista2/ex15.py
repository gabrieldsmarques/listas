import random

number = random.randrange(1, 100)
win = False
tries = 0

while win == False:
    guess = int(input("Digite um número: "))
    if guess > number:
        print("Tente um número menor")
        tries +=1
    else:
        print("Tente um número maior")
        tries += 1
        
    if guess == number:
        print(f"Parabéns, você acertou, levou {tries} tentativas até acertar.")
        win = True
        