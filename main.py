def imc_indice(altura,peso):
    imc = peso / ((altura/100)**2)
    indice = ''
    if imc <= 18.5:
        indice = 'Magreza'
    elif imc>18.5 and imc<=24.9:
        indice = 'Normal'
    elif imc > 24.9 and imc <= 29.9:
        indice = 'Sobrepeso'
    elif imc > 29.9 and imc <= 34.9:
        indice = 'Obesidade grau I'
    elif imc >34.9 and imc <= 39.9:
        indice = 'Obesidade grau II (severa)'
    else:
        indice= 'Obesidade grau III (mórbida)'
    return imc, indice

if __name__ == '__main__':
    altura = float(input('Qual é a sua altura em cm: '))
    peso = float(input('Qual é o seu peso em kg: '))
    imc,indice = imc_indice(altura=altura,peso=peso)
    print(f'Seu IMC é de {"{:.1f}".format(imc)}, e é classificado como {indice}')
