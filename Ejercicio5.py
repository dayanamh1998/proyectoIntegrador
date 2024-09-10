#Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas 
# de metro cable, registrando un puntaje que se clasifica de la siguiente
#  forma si tiene 2 puntos está con un funcionamiento defectuoso, si tiene 3 puntos 
# el funcionamiento es moderado y si tiene 4 puntos el funcionamiento es óptimo.


def clasificarCabinas(cantidadCabinas):
    clasificaciones = []
    
    for i in range(cantidadCabinas):
        puntaje = int(input("Introduce el puntaje de funcionamiento de la cabina: "))
        if puntaje == 2:
            clasificacion = "Funcionamiento defectuoso"
        elif puntaje == 3:
            clasificacion = "Funcionamiento moderado"
        elif puntaje == 4:
            clasificacion = "Funcionamiento óptimo"
        else:
            clasificacion = "Puntaje no válido"
        clasificaciones.append(clasificacion)
    
    return clasificaciones

cantidadCabinas = 407
clasificaciones = clasificarCabinas(cantidadCabinas)
print("Listado de clasificaciones de cabinas:")
for i, clasificacion in enumerate(clasificaciones):
    print(f"Cabina {i + 1}: {clasificacion}")