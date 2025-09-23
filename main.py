# Juego de Adivinanza en Binario:
# Muestren un número en binario y desafíen al usuario a adivinar su equivalente decimal, o viceversa, reforzando la conversión entre ambos sistemas.

import random

respuestas_correctas = []
respuestas_incorrectas = []

vidas = 0
numero_inicial = 0
numero_decimal = 0

# Menú para seleccionar opción
while True:
    
    vidas = 3
    binario = ""

    print("Bienvenido al juego para adivinar un numero binario o decimal!")
    option = int(input("""
        Elija su opción:
        1. Adivinar el equivalente en decimal de un número binario
        2. Adivinar el equivalente en binario de un número decimal
        3. Ver estadísticas
        4. Salir
    """))
    
    # Opción 1 para adivinar el equivalente en decimal de un número binario
    if option == 1:

        # Lógica para generar un número binario a partir de un numero decimal aleatorio 
        numero_decimal = random.randint(0,20)
        numero_inicial = numero_decimal

        if numero_decimal == 0:
            binario = "0"
        else:
            while numero_decimal > 0:
                residuo = numero_decimal % 2
                binario = str(residuo) + binario
                numero_decimal = numero_decimal // 2

        # Bucle para repetir el juego mientras el usuario tenga vidas
        while vidas > 0:
            print(numero_inicial)
            respuesta = int(input(f"Adivina el equivalente en decimal de: {binario}\n"))
            # Condicional en caso de que el usuario adivine o no
            if respuesta == numero_inicial:
                print("Correcto! Adivinaste el número!")
                respuestas_correctas.append(respuesta)
                break
            else:
                vidas -= 1
                print(f"Incorrecto, te quedan {vidas} vidas")

            if vidas == 0: 
                print(f"Te quedaste sin vidas. La respuesta correcta era {numero_inicial}")
                respuestas_incorrectas.append(numero_inicial)
                break
    
    if option == 2:
        
        numero_decimal = random.randint(0,20)
        numero_inicial = numero_decimal

        if numero_decimal == 0:
            binario = "0"
        else:
            while numero_decimal > 0:
                residuo = numero_decimal % 2
                binario = str(residuo) + binario
                numero_decimal = numero_decimal // 2

        while vidas > 0:
            print(binario)
            respuesta = input(f"Adivina el equivalente en binario de: {numero_inicial}\n")

            if respuesta == binario:
                print("Correcto! Adivinaste el número!")
                respuestas_correctas.append(respuesta)
                break
            else:
                vidas -= 1
                print(f"Incorrecto, te quedan {vidas} vidas")

            if vidas == 0: 
                print(f"Te quedaste sin vidas. La respuesta correcta era {binario}")
                respuestas_incorrectas.append(binario)
                break

    if option == 3:

        print("Números adivinados: ")
        if len(respuestas_correctas) == 0:
            print("Sin datos")
        else:
            print(respuestas_correctas)

        print("Números sin adivinar: ")
        if len(respuestas_incorrectas) == 0:
            print("Sin datos")
        else:
            print(respuestas_incorrectas)
    
    if option == 4: 
        break

    



    

    