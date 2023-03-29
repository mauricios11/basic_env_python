 # Project 3: gráficas de países (población) | sin usar pandas

instalación del proyecto: 
    - clonar proyecto (y abrir su contenido)
    - crear y activar el ambiente
    - correr código

 
El proyecto consiste en:
    - descargar un dataset de la población de los países
    - convertirlo en una lista de diccionarios
    - filtrar por países, continentes, y regiones(partes de un continente)
      - - los elementos con gráficas tipo pie y tipo barra
    
### Installation using pip3
```zsh
git clone # clone project
python3 -m venv env # create virtual enviroment
cd csv_project
source env/bin/activate
pip3 install -r requeriments.txt

```
### run project: 
 ```zsh
 cd csv_project

 #there are 2 options: 
 python main_populatiin_pip.py # to run the program without pandas
 ```
### Organization

                ├── README.md
                ├── __pycache__
                │   ├── graficas.cpython-39.pyc
                │   ├── read_csv.cpython-39.pyc
                │   └── utils.cpython-39.pyc
                ├── data
                │   └── data_population.csv
                ├── env
                │   └── bin
                ├── graficas.py
                ├── main_population_pip.py
                ├── not_main.py
                ├── plot_imgs
                │   ├── bar_population_Austria.png
                │   ├── bar_population_Germany.png
                │   ├── bar_population_Spain.png
                │   ├── pie-Europe.png
                │   └── pie_South America.png
                ├── read_csv.py
                ├── requirements.txt
                └── utils.py



