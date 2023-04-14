# estas son funciones para graficar
import matplotlib.pyplot as plt
import utils 


def bar_plot(file_name, labels , values):
    fig, ax = plt.subplots()
    ax.bar(labels , values)
    plt.savefig(f'./img/barplot_{file_name}.png')
    plt.close()
    
    
def pie_plot(labels, values):
    fig, ax = plt.subplots()
    plt.pie(values, labels = labels)
    plt.axis('equal')
    plt.savefig(f'./img/pie_population.png')
    plt.close()

    
if __name__ == "__main__":
    labels = ['a', 'b', 'c']
    values = [100 , 200 , 80]
    file_name = "practica"#input("Selecciona un país: ")
    bar_plot(file_name, labels ,values)
    pie_plot(labels , values)
    print(' labels: ',labels , '  values: ', values)

    