# graficar datos con matplotlib

import matplotlib.pyplot as plt
#"import utils , graficas, read_csv" ya no son necesarios al usar pandas
import pandas as pd


path = './data/data_population.csv'

def pie_p(data, continent):
    #continent = 'Europe'#input('Select continent: ')
    data_filtered = data.loc[data['Continent'] == continent]
    percent = pd.DataFrame(data_filtered['World Population Percentage']).values.flatten()
    
    countries = []
    #for country in data_filtered['Country/Territory']:
     #   countries.append(country)
     
     # same but using list comp
    [countries.append(i) for i in data_filtered['Country/Territory']]
    
    fig, ax= plt.subplots()
    ax.pie(percent, labels = countries)
    plt.savefig(f'./img/pie_plot_{continent}.png')
    plt.close()

def barplot(data, country):
    filter_country = data.loc[data['Country/Territory'] == country]
    
    column_keys = ['2022 Population','2020 Population','2015 Population',
                   '2010 Population','2000 Population','1990 Population','1980 Population']
    
    if len(filter_country) > 0:# si el país elegido está en la lista, filtrarlo
        values = pd.DataFrame(filter_country, columns = column_keys ).values.flatten()
        plt.bar(column_keys, values)
        plt.savefig(f'./img/bar_plot_{country}')
        plt.close()

    else:
        print("el país no ha sido encontrado, verificar que el nombre introducido sea el correcto")

def run(): 
    data = pd.read_csv(path) 
    continent_pie = 'Europe'#input('Select continent: ')
    country_bar = 'Mexico' #input('Select country: ')
    
    pie_p(data, continent_pie)

    barplot(data, country_bar)

    """
    Sin usar pandas
    código para pieplot & barplot de problación de países
    data = read_csv.read_csv(path)
    
    #colocar un input para seleccionar continente
    data_filtered = list(filter(lambda item: item['Continent'] == 'South America', data)) # solo analizar un continente
    
    countries = list(map(lambda x: x['Country/Territory'], data_filtered)) # countries = labels
    percent = list(map(lambda x: x['World Population Percentage'], data_filtered)) # percent = values
    
    graficas.pie_plot(countries, percent)
    
    #input para el population_by_country de ƒ "utils"
    file_name = "Chile"#input('Type country: ')#file_name = country
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
    """

if __name__ == "__main__":
    run()