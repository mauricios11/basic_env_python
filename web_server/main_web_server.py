
import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse



app = FastAPI()
@app.get('/', response_class = HTMLResponse)#En la "página principal" habrá números
def get_list():
    list_numbers = [1,2,3]
    return """
            <h1>Título</h1>
            <p> Párrafo con texto intrigante pero no muy largo</p>
            <h2> Aquí hay una lista de números</h2>
            <p> [1,2,3] lalalala no sé usar HTML auxilio</p>
"""
    
    
@app.get('/contact') #ruta de contacto    
def get_contact():
    return {'mail': 'usuario@mail.com', 'instagram' : '@usuario'}



def run():
    store.get_categories()
    

if __name__ == "__main__":
    run()
    
    
    
    
    