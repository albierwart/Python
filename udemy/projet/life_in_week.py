
# def life_in_week(age):
#     age_max = 90
#     nbr = (age_max-age)*52
#     return print("you have {nbr} weeks left")

# life_in_week(42)

# def calculate_love_score():
#     name1 = input("tapez le premier nom   ")
#     name2 = input("tapez le deuxieme prenom   ")

#     totName = name1+name2
#     # list_true = ["t", "r", "u", "e"]
#     list_true = "true"
#     list_love = ["l", "o", "v", "e"]
#     accurent_true= 0
#     accurent_love = 0
#     for letter in totName:
#         if letter in list_true:
#             accurent_true += 1
#         if letter in list_love:
#             accurent_love +=1
#     print(f"you love score is {accurent_true}{accurent_love}%")


# calculate_love_score()
letters = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"
]
# def encrypt(message, shift):
#     liste_index=[]

#     for letter in message:
#         liste_index.append(letters.index(letter))

#     for i in range(len(liste_index)):
#         liste_index[i] = liste_index[i] + shift

#     mot = ""
#     for num in liste_index:
#         mot = mot+letters[num]
#     print(f"here is the encoded result: {mot}")

def encrypt(message, shift):
    cipher_text = ""

    for letter in message:
        new_position = letters.index(letter) + shift
        if new_position > 25:
            new_position = new_position - 26
        cipher_text += letters[new_position]
    print(f"here is the encoded result: {cipher_text}")
encrypt("z",1)

def decrypt(message,shift):
    text=""
    for letter in message:
        new_possition = letters.index(letter) - shift
        if new_possition < 0:
            new_position = new_possition + 26
        text += letters[new_possition]

    print(f"here is the decoded result: {text}")

decrypt("a", 1)