 # Project 3: gráficas de países (población)  
 
El proyecto consiste en:
    - descargar un dataset de la población de los países
    - convertirlo en una lista de diccionarios
    - filtrar por países, continentes, y regiones(partes de un continente)
    -  los elementos con gráficas tipo pie y tipo barra
    
 ```zsh
 cd csv_project
 python main_populatiin.py
 ```
### Organization

                ├── README.md
                ├── __pycache__
                │   ├── graficas.cpython-39.pyc
                │   ├── read_csv.cpython-39.pyc
                │   └── utils.cpython-39.pyc
                ├── data
                │   └── data_population.csv
                ├── graficas.py
                ├── main_population.py
                ├── not_main.py
                ├── plot_imgs
                │   ├── bar_population_Austria.png
                │   ├── bar_population_Germany.png
                │   ├── bar_population_Spain.png
                │   ├── pie-Europe.png
                │   └── pie_South America.png
                ├── read_csv.py
                └── utils.py

