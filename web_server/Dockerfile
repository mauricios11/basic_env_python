FROM python:3.9

WORKDIR /app
#nombre del contenedor

COPY requirements.txt /web_server/requirements.txt
#pasar el archivo de instalación de librerías

RUN pip install --no-cache-dir --upgrade -r /web_server/requirements.txt
#instalar las librerías con el archivo copiado

COPY . /web_server 
#nombre de la carpeta

CMD ["uvicorn", "main_web_server:app", "--host", "0.0.0.0", "--port", "80"]
