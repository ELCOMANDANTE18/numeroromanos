


def convertir_decimal_a_romano(numero_decimal):
    roman = ''
    if numero_decimal < 10:
        for digit in range(numero_decimal):
            roman += 'I'
    else:
        for digit in range (numero_decimal // 10):
            roman += 'X'
    return roman
    
                    
