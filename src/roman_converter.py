def decimal_to_roman(numero):
    if not 1 <= numero <= 3999:
        raise ValueError("El número debe estar entre 1 y 3999")

    valores_romanos = [
        (1000, 'M'),
        (900,  'CM'),
        (500,  'D'),
        (400,  'CD'),
        (100,  'C'),
        (90,   'XC'),
        (50,   'L'),
        (40,   'XL'),
        (10,   'X'),
        (9,    'IX'),
        (5,    'V'),
        (4,    'IV'),
        (1,    'I')
    ]

    resultado = ""
    for valor, simbolo in valores_romanos:
        while numero >= valor:
            resultado += simbolo
            numero -= valor

    return resultado

try:
    numero = int(input("Ingresá un número decimal entre 1 y 3999: "))
    romano = decimal_to_roman(numero)
    print("En números romanos:", romano)
except ValueError as e:
    print("Error:", e)
