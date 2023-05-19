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
    print(dict_population[pais_busqueda])



# Creación de gráficos.
