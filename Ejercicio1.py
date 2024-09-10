def generarSerie(limite):
    serie = [5, 8]
    while len(serie) < limite:
        siguienteValor = serie[-1] + serie[-2]
        if siguienteValor != 13:
            serie.append(siguienteValor)
    return serie

serie = generarSerie(100)  # Corregir el nombre de la función aquí
print(serie)
