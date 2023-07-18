
borne_inf = 1
borne_sup = 100
coups = 0

while True:
    if borne_sup < borne_inf:
        print("Vos réponses ne permettent pas de déterminer un juste prix.")
        break
        
    coups += 1
    proposition = (borne_inf + borne_sup) // 2

    print("Proposition de l'ordinateur :", proposition)
    reponse = ""
    while reponse not in ["1", "2", "3"]:
        reponse = input("1) Plus grand\n2) Plus petit\n3) Juste prix\n")

    if reponse == "1":
        borne_inf = proposition + 1
    elif reponse == "2":
        borne_sup = proposition - 1
    elif reponse == "3":
        print("Juste prix", proposition, "trouvé en", coups, "coups !")
        break
