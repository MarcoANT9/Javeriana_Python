#!/usr/bin/python3

# Solicitar número invitados
nGuests = int(input("Indique número invitados: "))

#Verificar capacidad del salón
if (nGuests <= 50):

    # Solicitar número de sillas
    nChairs = int(input("Ingrese número de sillas: "))

    #Verificar que las sillas alcancen
    if (nGuests <= nChairs):
        print("Rentar Salón - No Alquilar Sillas")

    else:
        nChairsRent = nGuests - nChairs
        print("Rentar Salón - Alquilar Sillas:", nChairsRent)

else:
    print("No Rentar Salón")


