import random
# Liste 1 : lettres minuscules et majuscules
lettres = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z",
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

# Liste 2 : chiffres
chiffres = [
    "0","1","2","3","4","5","6","7","8","9"
]

# Liste 3 : symboles
symboles = [
    "!","@","#","$","%","^","&","*","(",")",
    "-","_","+","=","[","]","{","}",";",":",
    "'",'"',",",".","<",">","/","?","\\","|"
]

print("welcome to the pyPassword generator!")
nbr_letters = int(input("how many letters would you like in you password?  "))
nbr_symbols = int(input("how many symbols would you like in you password?  "))
nbr_numbers = int(input("how many letters would you like in you password?  "))

# password = ""
# for lettre in range(0, nbr_letters):
#     password += random.choice(lettres)
# for symbol in range(0,nbr_symbols):
#     password += random.choice(symboles)
# for chiffre in range(0, nbr_numbers):
#     password += random.choice(chiffres)

# print(password)
password = []
for lettre in range(0, nbr_letters):
    password.append(random.choice(lettres))
for symbol in range(0,nbr_symbols):
    password.append(random.choice(symboles))
for chiffre in range(0, nbr_numbers):
    password.append(random.choice(chiffres))
random.shuffle(password)
rep = ""
for lettre in password:
    rep+=lettre
print(rep)

    