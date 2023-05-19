import csv

# Leer el archivo.
with open('data.csv') as csvfile:

    # Recojo la información en forma de diccionario.
    reader = csv.DictReader(csvfile)

    # Recorro el diccionario accediendo por las claves correspondientes a la población por años.
    for row in reader:
        print(row['2022 Population'])
        population_data = (row['2022 Population'], row['2020 Population'], row['2015 Population'], row['2010 Population'], row['2000 Population'], row['1990 Population'], row['1980 Population'], row['1970 Population'])

    # Desempaqueto posicionalmente cada elemento de la tupla en su variable correspondiente.
    year_2022, year_2020, year_2015, year_2010, year_2000, year_1990, year_1980, year_1970 = population_data
