# leer el csv y convertirlo a un diccionario
import csv

def read_csv(path):
    with open(path , 'r') as df:
        reader = csv.reader(df, delimiter = ',')
        header = next(reader)
        
        data = []
        for row in reader:
            iterador = zip(header, row)
            country_dict = dict(iterador) #{header : row for header, row in iterador }
            data.append(country_dict)
            
        return data
    
    
if __name__ == "__main__":
    data = read_csv("./data/data_population.csv")
    print(data)