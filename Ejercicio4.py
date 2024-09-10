#Elabore un programa para un Hospital que determine, y muestre el nivel de Leucemia de 803 
# pacientes clasificando su puntaje si esta inferior a 10 no tiene Leucemia; 
# si esta entre 11 y 40, nivel bajo de Leucemia; si esta entre 40 y 69, 
# nivel moderado de Leucemia, si esta entre 70 y 100, nivel grave de Leucemia.

def clasificacionLeucemia(pacientes):
    clasificaciones = []
    
    for i in range(pacientes):
        puntaje = float(input("Introduce el puntaje de leucemia del paciente: "))
        if puntaje < 10:
            clasificacion = "No tiene Leucemia"
        elif 10 <= puntaje <= 40:
            clasificacion = "Nivel bajo de Leucemia"
        elif 41 <= puntaje <= 69:
            clasificacion = "Nivel moderado de Leucemia"
        elif 70 <= puntaje <= 100:
            clasificacion = "Nivel grave de Leucemia"
        else:
            clasificacion = "Puntaje fuera del rango esperado"  # Nuevo caso para puntajes fuera del rango
        
        clasificaciones.append(clasificacion)
    
    return clasificaciones

pacientes = 803
clasificaciones = clasificacionLeucemia(pacientes)
print("Listado de clasificaciones de leucemia:")
for i, clasificacion in enumerate(clasificaciones):
    print(f"Paciente {i + 1}: {clasificacion}")

    # Esta bueno le codigo