FROM python:3.9

WORKDIR /csv_project_using_pandas
COPY requirements.txt /csv_project_using_pandas/requirements.txt
#También es posible hacer la copia sin especificar el path: 
  #COPY requeriments.txt requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /csv_project_using_pandas/requirements.txt

COPY . /csv_project_using_pandas/

CMD bash -c "while true; do sleep 1; done"
