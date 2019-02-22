PRECIO_POR_KM = 10.5
KM = 0
print("El boleto cuesta 10.50 por km")

KM = int(input("ingrese el numero de kilometros:"))
if PRECIO_POR_KM == 10.5:
    PRECIO_POR_KM = (10.5 * KM)
    print ("El precio total del boleto es de:",PRECIO_POR_KM)
