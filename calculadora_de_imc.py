import os
print('Olá, seja bem-vindo à calculadora de Índice de Massa Corporal (IMC)')

while True:
    altura = input('Digite sua altura em centímetros: ')
    peso = input('Digite seu peso em kilogramas: ')
    
    try:
        altura_float = float(altura)
        peso_float = float(peso)
    
        imc = peso_float / (altura_float ** 2)

        os.system('cls')
    
        print(f'O seu Índice de Massa Corporal é {imc:.2f}')

        abaixo_do_peso = imc <= 18.5
        peso_ideal = imc >= 18.6 and imc <= 24.9
        sobrepeso = imc >= 25 and imc <= 29.9
        obesidade_1 = imc >= 30 and imc <= 34.9
        obesidade_2 = imc >= 35 and imc <= 39.9
        obesidade_3 = imc >= 40


        if abaixo_do_peso:
            print('Você está abaixo do peso peso normal. Por favor, procure um médico!')

        if peso_ideal:
            print('Você está no seu peso ideal. Parabéns!')
    
        if sobrepeso:
            print('Você está com sobrepeso. Não é nada alarmante, mas tome cuidado.')
    
        if obesidade_1:
            print('Cuidado, você está no grau de obesidade 1. Hora de se preocupar com a saúde!')
    
        if obesidade_2:
            print('Atenção, você está no grau de obesidade 2. Por favor, visite um profissional da saúde.')
    
        if obesidade_3:
            print('Você está no grau de obesidade 3. Busque tratamento urgentemente!')


        sair = input('Deseja sair? Digite [s]im ou [n]ão: ')
        
        if sair.lower().startswith('s'):
            os.system('cls')
            break
        
        if sair.lower().startswith('n'):
            os.system('cls')
            continue

    except ValueError:
        print('Você não digitou um peso ou altura válidos. Por favor, digite apenas números.')