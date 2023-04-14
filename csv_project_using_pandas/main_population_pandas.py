# cargar el dataset y graficar los datos de un país

import csv
import matplotlib.pyplot as plt
#dado que estamos usando pandas, ya no necesitamos: import utils y import read_csv
import graficas

import pandas as pd


country = input('Type country: ').title()
df = pd.read_csv('./data/data_population.csv')

def plot_bar_countries():
    global country
    
    df_filter_by_country = df.loc[df['Country/Territory'] == country]
    print(df_filter_by_country)
    #column_keys = values
    column_keys = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population']
    
    if len(df_filter_by_country) > 0:
        values = pd.DataFrame(df_filter_by_country, columns = column_keys).values.flatten()
        plt.bar(column_keys, values)
        plt.savefig(f'./plot_imgs/bar_plot_{country}')
        plt.close()
        
    else:
        print("There's no country with that name")
        

def plot_pie():
    continent = input('Type country: ').title()
    filter_continent_df = df.loc[df["Continent"]== continent]
    percent = filter_continent_df["World Population Percentage"]

    country_list=[]
    for country in filter_continent_df["Country/Territory"]:
        country_list.append(country)
        
    print(percent)
    
    fig, ax = plt.subplots()
    ax.pie(percent , labels = country_list)
    plt.savefig(f"./plot_imgs/pie-{continent}.png")
    plt.close()
    
def plot_propotion():
    #filtrar por región
    region = "Europe"#input("Selecciona una región: ").title()
    df_region = df[df['Continent'] == "region"]
    
    #porcentage de población en países (de la región seleccionada)
    countries_df = df_region["Country/Territory"].values #seleccionar sólo la columna "paises"
    percentage = df_region["World Population Percentage"].values  # seleccionar solo la columna porcentaje
     
    graficas.pie_popuplation(region, countries_df , percentage)


if __name__ == "__main__":
    plot_bar_countries()
    plot_propotion()
    plot_pie()
    
    
    


    

    
    
    
            

