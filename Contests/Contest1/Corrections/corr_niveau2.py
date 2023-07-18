def GetAnswer():
    valid_answers = ["plus", "moins", "ok"]
    user_answer = ""

    while not user_answer in valid_answers:
        user_answer = input("Répondez par 'plus', 'moins' ou 'ok' : ")
    
    return user_answer

print("Pensez à un nombre entre 1 et 100. \n\
Des nombres seront proposés. À vous de dire si le nombre auquel vous pensez est inférieur ou supérieur. \n\
Si votre nombre est inférieur, dites \"moins\" ; dans le cas contraire, dites \"plus\". \n\
Si le nombre est correct, dites \"ok\".")
      
input("<tapez sur entrer pour commencer>")

possible_choices_min = 1
possible_choices_max = 100

user_answer = ""
is_cheating = False

while user_answer != "ok" and is_cheating == False:
    guess = (possible_choices_max + possible_choices_min) // 2

    print(f"Est-ce {guess} ?")

    user_answer = GetAnswer()

    match(user_answer):
        case "plus":
            possible_choices_min = guess + 1
        case "moins":
            possible_choices_max = guess - 1
        case "ok":
            print("Super, le nombre a été trouvé !")

    if possible_choices_min > possible_choices_max:
        print("Vous essayez de tricher, non ?")
        is_cheating = True