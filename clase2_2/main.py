firstValue = int(input('Ingresar primer valor:'))
secondValue = int(input('Ingresar segundo valor:'))
thirdValue = int(input('Ingresar tercer valor:'))

if firstValue > secondValue:
    aux = firstValue
    firstValue = secondValue
    secondValue = aux
if secondValue > thirdValue:
    aux = secondValue
    secondValue = thirdValue
    thirdValue = aux
if firstValue > secondValue:
    aux = firstValue
    firstValue = secondValue
    secondValue = aux

print('Los valores ordenados de menor a mayor son:')
print(firstValue, '-', secondValue, '-', thirdValue)