cedula = input('ingrese su numero de cedula: ')

#validar que tenga 10 digitos
if (len(cedula) == 10):

    #obtener el codigo de region
    codigoregion = cedula[slice(2)]
    codigore = int(codigoregion)

    if codigore >= 1 and codigore <= 24:

        #extraer ultimo digito
        ultimodigito = cedula[slice(9, 10)]
        ultimodi = int(ultimodigito)

        #extraigo y sumo los numeros de las posiciones pares
        pares = int(cedula[slice(1, 2)]) + int(cedula[slice(3, 4)]) + int(
            cedula[slice(5, 6)]) + int(cedula[slice(7, 8)])

        #extraigo y sumo las posiciones impares
        impar1 = (int(cedula[slice(0, 1)]) * 2)
        if (impar1 > 9):
            impar1 = impar1 - 9

        impar2 = (int(cedula[slice(2, 3)]) * 2)
        if (impar2 > 9):
            impar2 = impar2 - 9

        impar3 = (int(cedula[slice(4, 5)]) * 2)
        if (impar3 > 9):
            impar3 = impar3 - 9

        impar4 = (int(cedula[slice(6, 7)]) * 2)
        if (impar4 > 9):
            impar4 = impar4 - 9

        impar5 = (int(cedula[slice(8, 9)]) * 2)
        if (impar5 > 9):
            impar5 = impar5 - 9

        sumamimpares = (impar1 + impar2 + impar3 + impar4 + impar5)

        #sumamos los pares e impares
        total = sumamimpares + pares
        print('suma total de pares e impares: ', total)

        #de entero lo convertimos a string para
        #poder extraer su primer digito
        totalstring = str(total)
        numerodecena = totalstring[slice(0, 1)]

        #convertimos el primer digito a entero
        numeroconvertido = int(numerodecena)

        #ese primer digito lo  convertimos en decena
        extraidodecena = (numeroconvertido + 1) * 10
        numeroverificador = extraidodecena - total

        if (numeroverificador == ultimodi):
            print('su cedula es correcta ', cedula)
        else:
            print('cedula incorrecta')

    else:
        print('eres extranjero')

else:
    print('el numero de cedula tiene menos de 10 digitos')
