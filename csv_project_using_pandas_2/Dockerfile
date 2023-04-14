FROM python:3.8

WORKDIR /csv_population
COPY requirements.txt /csv_project_using_pandas_2/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /csv_project_using_pandas_2/requirements.txt

COPY . /csv_population

CMD bash -c "while true; do sleep 1; done"


