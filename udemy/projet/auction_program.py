# permet de vider un ecran d une mauvaise manniere
# print("\n"*10)

# on va demander un nom puis une valuer (chiffre) qui est une offre puis demander si encore autre nom si
#  oui on redemande si non on sort le nom et la valeur la plus haute

# dic = {}
# continuer = True
# while continuer:
#     reponse = input("y a t il  une autre personne?(y/n)")
#     if reponse == "n":
#         continuer = False
#     else:
#         nom = input("quel est le nom ")
#         offre = int(input("quel est l offre "))
#         dic[f"{nom}"] = offre
# max = 0
# name_max = ""
# for key,value in dic.items():
#     print(value)
#     if value>max:
#         max = value
#         name_max = key
# print(f"la meilleur offre est {max} faite par {name_max} ")
def find_highest_bidder(bidding_dictionnary):
    winner = ""
    max_bid = 0
    for bidder in bidding_dictionnary:
        bid_amount = bidding_dictionnary[bidder]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f" the winner is {winner} with a bid of {max_bid}")

# voir avec fonction max()

dic= {}

continue_bidding = True
while continue_bidding:
    name = input("quel est votre nom ")
    price = int(input("quel est votre offre"))
    dic[name] = price
    should_continue = input("d autre participant (y/n)")
    if should_continue == "n":
        find_highest_bidder(dic)
        continue_bidding = False
    else:
        print("\n" *20)

