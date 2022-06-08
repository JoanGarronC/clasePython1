firstValue = int(input('Ingrese un valor: '))
secondValue = int(input('Ingrese otro valor: '))
multiplicationSum = 0
for index in range(firstValue):
    multiplicationSum = multiplicationSum + secondValue

print('La multiplicacion de los dos numeros es:', multiplicationSum)