import random

def safe_input_int(message):
    while True:
        user_input = input(message)
        if user_input.isdecimal():
            return int(user_input)

MIN = 1
MAX = 100

secret_number = random.randint(MIN, MAX)
user_number = -1

while secret_number != user_number:
    user_number = safe_input_int(f"Veuillez entrer un nombre entre {MIN} et {MAX} : ")

    if secret_number > user_number:
        print("C'est plus !")
    elif secret_number < user_number:
        print("C'est moins !")
    else:
        print("Félicitations, vous avez gagné !")