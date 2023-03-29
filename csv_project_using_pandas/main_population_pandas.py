# cargar el dataset y graficar los datos de un país

import csv
import matplotlib.pyplot as plt
import utils
import graficas
import read_csv as read
import pandas as pd

country = input('Type country: ').title()

def plot_bar_countries():
    global country
    data = read.read_csv("./data/data_population.csv")

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
    df = pd.read_csv('./data/data_population.csv')
    
    #filtrar por región
    region = input("Selecciona una región: ").title()
    df_region = df[df['Continent'] == "region"]
    
    #porcentage de población en países (de la región seleccionada)
    countries_df = df_region["Country/Territory"].values #seleccionar sólo la columna "paises"
    percentage = df_region["World Population Percentage"].values  # seleccionar solo la columna porcentaje
     
    graficas.pie_popuplation(region, countries_df , percentage)


if __name__ == "__main__":
    plot_bar_countries()
    plot_propotion()
    plot_pie()
    
    
    


    

    
    
    
            

