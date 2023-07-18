def safe_input_int(message):
    while True:
        user_input = input(message)
        
        if user_input.isdecimal():
            return int(user_input)

MIN = 1
MAX = 100

possible_numbers_min = MIN
possible_numbers_max = MAX

user_number = -1

while user_number != possible_numbers_min:
    user_number = safe_input_int(f"Veuillez entrer un nombre entre {MIN} et {MAX} : ")

    amount_of_possible_numbers_before = user_number - possible_numbers_min
    amount_of_possible_numbers_after = possible_numbers_max - user_number

    if amount_of_possible_numbers_after > amount_of_possible_numbers_before:
        if user_number >= possible_numbers_min:
            possible_numbers_min = user_number + 1
        print("C'est plus !")
    else:
        if user_number <= possible_numbers_max and possible_numbers_min != possible_numbers_max:
            possible_numbers_max = user_number - 1
        print("C'est moins !")

print(f"Félicitations, le nombre était bien {possible_numbers_min} !")