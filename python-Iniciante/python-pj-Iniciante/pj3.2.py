entrada = input('Digite um numero: ')


try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_text = None

    if par_impar:
        par_impar_text = "Par"
        print(f'Seu numero {entrada_int} é {par_impar_text}')

    else:
        par_impar_text = "Impar"
        print(f'Seu numero {entrada_int} é {par_impar_text}')
except:
    print('Você não digitou um numero!!')
