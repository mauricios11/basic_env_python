
import requests

def get_categories():
    request = requests.get("https://api.escuelajs.co/api/v1/products")
    #el enlace lo sacamos de: https://fakeapi.platzi.com/
    print(request.status_code)#obtener el estado
    #print(request.text)
    print(type(request.text))
    
    categories = request.json()
    
    for category in categories:
        print(category['title'])#imprimir solo el título de cada categoría
    
    
    
    
    
    