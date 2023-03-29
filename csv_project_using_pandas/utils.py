#funciones para iterar los paises del dataset

import read_csv as read



def get_population(country_dict):
    population_dict  = {'2022': int(country_dict['2022 Population']), '2020': int(country_dict['2020 Population']),
                        '2015': int(country_dict['2015 Population']),'2010': int(country_dict['2010 Population']),
                        '2000': int(country_dict['2000 Population']),'1990': int(country_dict['1990 Population']),
                        '1980': int(country_dict['1980 Population']),'1970': int(country_dict['1970 Population'])}

    keys = population_dict.keys()
    values = population_dict.values()
    return keys , values
    

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

def  get_porcentaje(data):
    porcentaje = {item['Country/Territory'] : item['World Population Percentage']
                  for item in data}
    
    keys_porcentaje = porcentaje.keys()
    values_porcentaje = porcentaje.values()
    
    
    return keys_porcentaje , values_porcentaje


    
if __name__ == "__main__":
    country_dict = read.read_csv("../data/data_population.csv")
    porcentaje = get_porcentaje(country_dict)
    print(f' porcentajeasdlfkj : \n {porcentaje}')
    
   