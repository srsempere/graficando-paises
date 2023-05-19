import csv
import matplotlib.pyplot as plt

###################
###  FUNCIONES  ###
###################

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

######################

# Leer el archivo.
with open('data.csv') as csvfile:

    # Recojo la información en forma de diccionario.
    reader = csv.DictReader(csvfile)

    dict_population = {}

    for row in reader:
        population_data = [
                            (2022, row['2022 Population']),
                            (2020, row['2020 Population']),
                            (2015, row['2015 Population']),
                            (2010, row['2010 Population']),
                            (2000, row['2000 Population']),
                            (1990, row['1990 Population']),
                            (1980, row['1980 Population']),
                            (1970, row['1970 Population'])
                            ]

        dict_population[row['Country']] = [(year, row[f'{year} Population']) for year in [2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970]]  # usar lista por descomprensión?

    # Recogida del país a buscar

    pais_busqueda = input('Introduce el nombre del país del cuál desear imprimir su gráfico => ')

    fila_encontrada = dict(dict_population[pais_busqueda])

    # Extracción de claves y valores

    key_anyo = fila_encontrada.keys()
    values_population = fila_encontrada.values()

    print(fila_encontrada)
    print(type(fila_encontrada))
    print(fila_encontrada.keys())
    print(fila_encontrada.values())

# Creación de gráficos.

    generate_bar_chart(key_anyo, values_population)
