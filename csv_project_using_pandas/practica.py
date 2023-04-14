import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("./data/data_population.csv")
data = pd.DataFrame(data)
country = "Mexico" #input("Select Country: ").title()
filter_country_df = data.loc[data["Country/Territory"]== country]
years = ['2020 Population','2015 Population','2010 Population','2000 Population']
population = pd.DataFrame(filter_country_df, columns=years).values.flatten()
plt.bar(years, population)
plt.show()
print(years)
print(population)




