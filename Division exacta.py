dividiendo = int(input("Escribe un dividiendo "))
divisor = int(input("Escribe un divisor "))
resto = dividiendo % divisor 
if (dividiendo !=0) and (divisor !=0):
    print ("La division es exacta. Cociente: ", dividiendo // divisor, "Resto: ",resto)
else:
    print ("La division no es exacta. Cociente: ", dividiendo / divisor, "Resto: ", resto)
