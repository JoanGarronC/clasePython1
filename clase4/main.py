def unitToWord(unitValue: int):
    if(unitValue == 1):
        return 'uno'
    if(unitValue == 2):
        return 'dos'
    if(unitValue == 3):
        return 'tres'
    if(unitValue == 4):
        return 'cuatro'
    if(unitValue == 5):
        return 'cinco'
    if(unitValue == 6):
        return 'seis'
    if(unitValue == 7):
        return 'siete'
    if(unitValue == 8):
        return 'ocho'
    if(unitValue == 9):
        return 'nueve'
    return ''
def tenToWord(tenValue: int, unitValue: int):
    output = ''
    if(tenValue == 1):
        if(unitValue == 0):
            return 'diez'
        if(unitValue == 1):
            return 'once'
        if(unitValue == 2):
            return 'doce'
        if(unitValue == 3):
            return 'trece'
        if(unitValue == 4):
            return 'catorce'
        if(unitValue == 5):
            return 'quince'
        if(unitValue == 6):
            return 'diez y seis'
        if(unitValue == 7):
            return 'diez y siete'
        if(unitValue == 8):
            return 'diez y ocho'
        if(unitValue == 9):
            return 'diez y nueve'
    if(tenValue == 2):
        output = 'veinte'
    if(tenValue == 3):
        output = 'treinta'
    if(tenValue == 4):
        output = 'cuarenta'
    if(tenValue == 5):
        output = 'cincuenta'
    if(tenValue == 6):
        output = 'sesenta'
    if(tenValue == 7):
        output = 'setenta'
    if(tenValue == 8):
        output = 'ochenta'
    if(tenValue == 9):
        output = 'noeventa'
    if(unitValue > 0):
        output = output + ' y'
    return output

def hundredToWord(hundredValue: int, tenValue: int, unitValue: int):
    output = ''
    if(hundredValue == 1 and tenValue == 0):
        return 'cien'
    if(hundredValue == 1 and (tenValue > 0 or unitValue > 0)):
        return 'ciento'
    if(hundredValue == 2):
        return 'doscientos'
    if(hundredValue == 3):
        return 'trecientos'
    if(hundredValue == 4):
        return 'cuatrocientos'
    if(hundredValue == 5):
        return 'quinientos'
    if(hundredValue == 6):
        return 'seiscientos'
    if(hundredValue == 7):
        return 'setecientos'
    if(hundredValue == 8):
        return 'ochocientos'
    if(hundredValue == 9):
        return 'novencientos'
    return ''

def unitThousandToWord(unitThousandValue: int):
    if(unitThousandValue == 1):
        return 'mil'
    if(unitThousandValue == 2):
        return 'dos mil'
    if(unitThousandValue == 3):
        return 'tres mil'
    if(unitThousandValue == 4):
        return 'cuatro mil'
    if(unitThousandValue == 5):
        return 'cinco mil'
    if(unitThousandValue == 6):
        return 'seis mil'
    if(unitThousandValue == 7):
        return 'siete mil'
    if(unitThousandValue == 8):
        return 'ocho mil'
    if(unitThousandValue == 9):
        return 'nueve mil'
    return ''

def convertNumberToWords(userValue: int):
    inputValue = userValue
    if inputValue == 0:
        return 'cero'

    unitThousand = int(inputValue / 1000)
    inputValue = inputValue - (unitThousand * 1000)
    hundred = int(inputValue / 100)
    inputValue = inputValue - (hundred * 100)
    ten = int(inputValue / 10)
    inputValue = inputValue - (ten * 10)
    unit = inputValue

    if userValue < 10:
        return unitToWord(unit)
    elif userValue >= 10 and userValue <= 19:
        return tenToWord(ten, unit)
    elif userValue >= 20 and userValue <= 99:
        return tenToWord(ten, unit) + ' ' + unitToWord(unit)
    elif userValue >= 100 and userValue <= 999:
        return hundredToWord(hundred, ten, unit) + ' ' + tenToWord(ten, unit) + ' ' + unitToWord(unit)
    elif userValue >= 1000 and userValue <= 9999:
        return unitThousandToWord(unitThousand) + ' ' + hundredToWord(hundred, ten, unit) + ' ' + tenToWord(ten, unit) + ' ' + unitToWord(unit)

print(convertNumberToWords(2348))


