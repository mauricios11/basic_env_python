# estas son funciones para graficar
import matplotlib.pyplot as plt
import utils 


def bar_population(file_name, labels, values):
    fig, ax = plt.subplots()
    plt.bar(labels, values)
    plt.savefig(f"./plot_imgs/bar_population_{file_name}.png")
    plt.close()
    
    
def pie_popuplation(file_name, labels, values):
    fig, ax = plt.subplots()
    plt.pie(values, labels = labels)
    plt.axis('equal')
    plt.savefig(f"./plot_imgs/pie_{file_name}.png")
    plt.close()
    
    
    
if __name__ == "__main__":
    labels = ['a', 'b', 'c']
    values = [100 , 200 , 80]
    bar_population(labels ,values)
    pie_popuplation(labels , values)

    