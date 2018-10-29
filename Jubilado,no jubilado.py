edad = 0;
sexo = 1;          #0 és mujer, 1 és hombre
colorCabello = 0;
preciofinal = 0;

edad = int(input("Introduce tu edad: "))
sexo = input("Introduce tu genero (M si eres mujer, H si eres hombre): ")
colorCabello = int(input("Cual es el color de tu pelo? (1 Rubio/a, 2 Peliroja, 3 Morena, 0 otro): "))
jubilado = input("Estas jubilado? (si, no): ")

if sexo == "H":
    if jubilado == "no":
        preciofinal == 1;

if sexo == "M":
    if jubilado == "no" and colorCabello == 1: 
        preciofinal = 0;

if sexo == "H, M":
    if jubilat == "si" and edad > 65:
        precioFinal = 0;

if sexo == "M":
    if jubilado == "no" and colorCabello == 0:
        preciofinal = 0.5;

print("El precio final es:",preciofinal);
