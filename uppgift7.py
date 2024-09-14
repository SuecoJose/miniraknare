# Uppgift 7 Minräknare : Thomas Lindholm

loop_again = True

while loop_again is True:
    valid_answer = False
    valid_operator = False

    user_input_operand1 = int(input('Ange operand:'))

    while not valid_operator:
        user_input_operator = input('Ange räknesätt:')
        if user_input_operator in ['+', '-', '*', '/', '//', '%']:
            valid_operator = True
        else:
            print("Ange en giltig operator")
            valid_operator = False

    user_input_operand2 = int(input('Ange operand:'))

    if user_input_operator == '+':
        result = user_input_operand1 + user_input_operand2
    elif user_input_operator == '-':
        result = user_input_operand1 - user_input_operand2
    elif user_input_operator == '*':
        result = user_input_operand1 * user_input_operand2
    elif user_input_operator == '/':
        if user_input_operand2 != 0:
            result = user_input_operand1 / user_input_operand2
        else:
            result = "Går ej att räkna ut division med noll"
    elif user_input_operator == '//':
        if user_input_operand2 != 0:
            result = user_input_operand1 // user_input_operand2
        else:
            result = "Går ej att räkna ut division med noll"
    elif user_input_operator == '%':
        if user_input_operand2 != 0:
            result = user_input_operand1 % user_input_operand2
        else:
            result = "Går ej att räkna ut modulus med noll"

    print(f'Svar: {user_input_operand1:2} {user_input_operator} {user_input_operand2:2} = {result:2}')

    while not valid_answer:
        user_input_again = input('Vill du avsluta (j/n)?').upper()
        valid_answer = True
        if user_input_again in ['J']:
            loop_again = False
        elif user_input_again in ['N']:
            loop_again = True
        else:
            print("felaktigt svar")
            valid_answer = False

print('Programmet avslutas!')
