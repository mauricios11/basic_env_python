import matplotlib.pyplot as plt

def generate_pie():
    labels = ['A','B','C']
    values = [100, 40, 300]
    
    fig, ax = plt.subplots()
    plt.pie(values, labels= labels)
    plt.savefig('img/pie.png')
    plt.close()
    
    
