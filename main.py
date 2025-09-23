# Juego de Adivinanza en Binario:
# Muestren un número en binario y desafíen al usuario a adivinar su equivalente decimal, o viceversa, reforzando la conversión entre ambos sistemas.

# Lógica para mantener el juego mientras el usuario no presione 3,
# controlado por la variable flag.
while True:
    print("Bienvenido al juego para adivinar un numero binario o decimal!")
    option = int(input("""
        Elija su opción:
        1. Adivinar número binario
        2. Adivinar número decimal
        3. Salir
    """))

    if option == 3: 
        break

# binario = ""

# numero_decimal = int(input("Ingrese un número decimal: "))

# if numero_decimal == 0:
#     binario = "0"
# else:
#     while numero_decimal > 0:
#         residuo = numero_decimal % 2
#         binario = str(residuo) + binario
#         numero_decimal = numero_decimal // 2

# print("El número en binario es:", binario)