import random

prix = random.randint(1, 100)
win = False

while not win:
    reponse = input("Quelle est le juste prix?  ")

    try:
        reponse = int(reponse)
    except:
        print("Veuillez rentrer un nombre")

    if isinstance(reponse, int):
        if 1 <= reponse <= 100:
            if reponse < prix:
                print("Plus grand")
            elif reponse > prix:
                print("Plus petit")
            elif reponse == prix:
                print("Gagné!")
                win = True

        else:
            print("Veuillez rentrer un nombre entre 1 et 100")

