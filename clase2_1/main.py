firstValue = input('Ingrese un valor:')
secondValue = input('Ingrese otro valor:')

if int(firstValue) == int(secondValue):
    print('Los valores son iguales.')
elif int(firstValue) > int(secondValue):
        print('El primer valor es mayor.')
else:
    print('El segundo valor es mayor.')