# graficar datos con matplotlib

import matplotlib.pyplot as plt
import utils
import graficas
import read_csv
# función para gráficos de barras 

path = './data/data_population.csv'

def run():
    data = read_csv.read_csv(path)
    #colocar un input para seleccionar continente
    data_filtered = list(filter(lambda item: item['Continent'] == 'South America', data)) # solo analizar un continente
    
    countries = list(map(lambda x: x['Country/Territory'], data_filtered)) # countries = labels
    percent = list(map(lambda x: x['World Population Percentage'], data_filtered)) # percent = values
    
    graficas.pie_plot(countries, percent)
    
    
    #input para el population_by_country de ƒ "utils"
    file_name = input('Type country: ')#file_name = country
    print(type(file_name), file_name)
    result = utils.population_by_country(data_filtered, file_name)
    
    #si hay un resultado, estamos reemplazando lo que se encontró en el csv
    #    en el csv es un diccionario, necesitamos el nombre del "country" y no el diccionario
    if len(result) > 0:
        file_name = result[0]
        print(type(file_name), file_name)
        labels, values = utils.get_population(file_name)
        graficas.bar_plot(file_name['Country/Territory'], labels, values)
    else:
        print(f'El país: "{file_name}" no se ha encontrado en la data filtrada')   
    

if __name__ == "__main__":
    run()