# cargar el dataset y graficar los datos de un país

import csv
import matplotlib.pyplot as plt
import utils
import graficas
import read_csv as read



def plot_bar_countries():
    data = read.read_csv("./data/data_population.csv")
    country = input('Type country: ').title()
    print(country)
    result = utils.population_by_country(data, country)
    
    if len(result) > 0:
        country = result[0]
        print(country)
        labels , values = utils.get_population(country)
        
        graficas.bar_population(country['Country/Territory'], labels, values)

def plot_pie():
    continent = "Europe"
    data = read.read_csv("./data/data_population.csv")
    data_filtered = list(filter(lambda x : x["Continent"] == continent, data))
    labels , values = utils.get_porcentaje(data_filtered)
    
    fig, ax = plt.subplots()
    ax.pie(values , labels = labels)
    plt.savefig(f"./plot_imgs/pie-{continent}.png")
    plt.close()
    
def plot_propotion():
    df = read.read_csv('./data/data_population.csv')
    data = df.copy()
    region = "South America"
    #filtrar por región
    data = list(filter(lambda x : x['Continent'] == region, data))
    
    countries = list(map(lambda x : x['Country/Territory'], data)) #seleccionar sólo la columna "paises"
    porcentaje = list((map(lambda x : x['World Population Percentage'], data)))  # seleccionar solo la columna porcentaje
    
    graficas.pie_popuplation(region, countries , porcentaje)

if __name__ == "__main__":
    plot_bar_countries()
    plot_propotion()
    plot_pie()
    
    
    


    

    
    
    
            

