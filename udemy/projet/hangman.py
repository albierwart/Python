import random
def ask_answer():
    
    letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
    letter = ""
    while letter not in letters:
        letter = input("tapez une lettre  ")
    return letter
vie = 2
mots = ["toti", "tita"]

num = random.randint(0,len(mots)-1)

mot = mots[num] 
# mot = random.choice(mots)
len_mot = len(mot)
aff_answer = ["_"]*len_mot

while vie > 0:
    print(f"vous avez  {vie} vies")
    print("".join(aff_answer))
    answer = ask_answer()
    if answer in mot:
        for num in range(0, len_mot):
            if answer == mot[num]:
                aff_answer[num] = answer
        print("".join(aff_answer))
        if "_" not in aff_answer:
            print("gagne")
            break
    else:
        print("rate")
        vie-=1
        if vie == 0:
            print("perdu")