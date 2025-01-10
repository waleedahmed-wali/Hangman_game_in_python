import random
words = ["APPLE","BOOK","CHAIR","HOUSE","TIGER","PLANET","BRIDGE","CASTLE","GARDEN","WINTER","ALGORITHM","BINARY","COMPILER","DEBUGGING","ENCRYPTION","FIREWALL","HYPERTEXT","ITERATION","PIXEL","PROTOCOL","SYNTAX"]
secret_word = random.choice(words)
progress = []
progress2 = []
L = len(secret_word)
for n in range(0,L):
    progress.append("_")
    progress2.append("_")
for i in range(0,L):
    progress2[i] = secret_word[i]
print(progress)
Attempt = 6
def secert_word(n):
    if userG == secret_word[n]:
        if progress[n] != userG:
            print("nice gess")
            progress[n] = userG
            print(progress)
        else:
            print(progress)
            print("you already have guessed that Alphabet:")
while Attempt > 0:
    if progress == progress2:
        print("")
        print("you win")
        break
    userG = input("guess one letter of secret word:").upper()
    if userG in secret_word:
        for z in range(0,L):
            if progress == progress2:
                break
            secert_word(z)
    else:
        Attempt -= 1
        print(f'{userG} is not in secret world now you have {Attempt} more attempt')
        if Attempt ==0:
            print("")
            print("you lOSE.")