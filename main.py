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

    # Recorro el diccionario accediendo por las claves correspondientes a la población por años.
    for row in reader:
        population_data = [(row['Country'], ((2022, row['2022 Population']), (2020, row['2020 Population']), (2015, row['2015 Population']), (2010, row['2010 Population']), (2000, row['2000 Population']), (1990, row['1990 Population']), (1980, row['1980 Population']), (1970, row['1970 Population'])))]
        # print(population_data)
        dict_population = {dict(population_data)}
        print(dict_population)


# Creación de gráficos.
