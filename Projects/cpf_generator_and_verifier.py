import random
import re
import os

def verifier():
    entry = input('Digite um CPF válido: ')
    entry = re.sub(r'[^0-9]', '', entry)
    
    
    if not entry.isdigit():
        return('CPF Inválido: O CPF deve conter apenas números.')
    
    if len(entry) != 11:
        return('CPF Inválido: O CPF digitado deve possuir exatamente 11 digitos.')
    
    if entry == entry[0] * len(entry):
        return('CPF Inválido: O CPF digitado não pode ter 11 digitos iguais.')
    
    
    nine_digits = entry[:9]
    expected_first_digit = int(entry[9])
    expected_second_digit = int(entry[10])
    
    backwards_mult_1 = 10
    result_1 = 0
    
    for digit in nine_digits:
        result_1 += int(digit) * backwards_mult_1
        backwards_mult_1 -= 1
    
    first_digit = (result_1 * 10) % 11
    first_digit = 0 if first_digit == 10 else first_digit
    ten_digits = nine_digits + str(first_digit)
    
    backwards_mult_2 = 11
    result_2 = 0
    
    for digit in ten_digits:
        result_2 += int(digit) * backwards_mult_2
        backwards_mult_2 -= 1
    
    second_digit = (result_2 * 10) % 11
    second_digit = 0 if second_digit == 10 else second_digit
    
    
    if first_digit == expected_first_digit and second_digit == expected_second_digit:
        return('O seu CPF é válido.')
    return('O seu cpf é inválido')

def generator():
    nine_digits = ''
    for i in range(9):
        nine_digits += str(random.randint(0,9))
    
    backwards_mult_1 = 10
    result_1 = 0
    
    for digit in nine_digits:
        result_1 += int(digit) * backwards_mult_1
        backwards_mult_1 -= 1
    
    first_digit = (result_1 * 10) % 11
    first_digit = 0 if first_digit == 10 else first_digit
    ten_digits = nine_digits + str(first_digit)
    
    backwards_mult_2 = 11
    result_2 = 0
    
    for digit in ten_digits:
        result_2 += int(digit) * backwards_mult_2
        backwards_mult_2 -= 1
    
    second_digit = (result_2 * 10) % 11
    second_digit = 0 if second_digit == 10 else second_digit
    eleven_digits = ten_digits + str(second_digit)
    
    formated_eleven_digits = f'{eleven_digits[:3]}.{eleven_digits[3:6]}.{eleven_digits[6:9]}-{eleven_digits[9:]}'
    
    cpf = formated_eleven_digits
    
    return (f'O CPF gerado foi: {cpf}')

print('Olá, seja bem-vindo ao verificador/gerador de CPFs.\nPor favor, escolha uma das opções a seguir:')

while True:
    entry = input('[G]erar um CPF, [V]erificar um CPF ou [S]air: ')
    generate = entry.lower().startswith('g')
    verify = entry.lower().startswith('v')
    exit = entry.lower().startswith('s')
    
    if generate:
        os.system('cls')
        print(generator())
    
    elif verify:
        os.system('cls')
        print(verifier())
    
    elif exit:
        break
    
    else:
        os.system('cls')
        print('Escolha uma das opções apresentadas.')