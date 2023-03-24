# tijera gana a papel
# papel gana a piedra
# piedra gana a tijera

import random

options = ['piedra', 'papel', 'tijera']
not_names = ['hola','ola', 'olaa', 'alo', 'aloja', 'hello','',' ']

saludo = """Juguemos a piedra papel ó tijera\n
Reglas:
 - Las rondas de empate no suman puntos"
 - Si el usuario coloca mal la elección, contará como una ronda normal"""

user_wins = 0
machine_wins = 0

def quitar_guiones_acentos(word):
    acentos = {"á": "a", "à": "a", "ä" :"a", "â": "a",
               "é": "e", "è": "e", "ë" :"e", "ê": "e",
               "í": "i", "ì": "i", "ï" :"i", "î": "i",
               "ó": "o", "ò": "o", "ö" :"o", "ô": "o",
               "ù": "u", "ú": "u", "ü" :"u", "û": "u",
               "ã":"a", "õ": "o"}
    caracteres_list = [",", "_", ".", "-", "=", "+", "?", "!", "%", "/", "*" ," "]
    
    for letra in acentos:
        if letra in acentos:
            word = word.replace(letra,acentos[letra])
    
    for caracter in caracteres_list:
            if caracter in caracteres_list:
                word = word.replace( caracter , "")
    return word

def eleccion_rondas_nickname():
    #nickname
    user_name = input("\n Elige un nickname (mínimo 3 letras, máximo 10): ")
    user_name = quitar_guiones_acentos(user_name).lower()
    while True:
        if user_name in not_names or len(user_name) <3 or len(user_name) >10 :
                user_name = input("\n Favor de eligir un nombre válido (mínimo 3 letras): ").lower()
                user_name = quitar_guiones_acentos(user_name) 
        else: 
            break
    #número de rondas
    rondas_user = 0         
    while not rondas_user in range(2,6):
        print(f"\n Hola '{user_name}' Cuántas rondas se deberán ganar para ser el campeón?")
        rondas_user = int(input(" deben ser mínimo 2 máximo 5: "))
    
    return user_name , rondas_user

def eleccion_jugadas():
    # jugada         
    user = input(f"\n Ahora elige una opción: [piedra] [papel] [tijera]: ").lower()
    user = quitar_guiones_acentos(user)
    
    while not user in options:
        user = input(f"\n Ahora elige una opción: [piedra] [papel] [tijera]: ").lower()
        user = quitar_guiones_acentos(user)
    
    machine = random.choice(options)
    
    return user, machine

def empate(user, machine, user_name):
    if user == machine: 
        return print(f'Empate! {user_name} eligió: {user} y la computadora eligió: {machine}\n')
        
def reglas_func(user, machine, user_name, rondas_user):
    global user_wins
    global machine_wins
    
    if user == "piedra":
        if machine == "papel":
            machine_wins += 1
            return print(f' El {machine} le gana a la {user}. Punto para la COMPUTADORA \n')
            
        if machine == "tijera":
            user_wins += 1
            return print(f' La {user} le gana a la {machine}. Punto para {user_name.upper()} \n')
        
    if user == "papel":
        if machine == "piedra":
            user_wins += 1
            return print(f' El {user} le gana al {machine}. Punto para {user_name.upper()} ')
            
        if machine == "tijera":
            machine_wins += 1
            return print(f' La {machine} le gana al {user}. Punto para la COMPUTADORA \n')
        
    if user == "tijera":
        if machine == "papel":
            user_wins += 1
            return print(f' La {user} le gana al {machine}. Punto para {user_name.upper()}\n')
            
        if machine == "piedra":
            machine_wins += 1
            return print(f' La {machine} le gana a la {user}. Punto para la COMPUTADORA \n')
            

def juego():
    ronda_actual = 1
    print(saludo)
    user_name, rondas_user = eleccion_rondas_nickname()
    
    while True:
        print(f'\n {"- *"* 4} ronda {ronda_actual} {"- *"* 4}')
        
        user, machine = eleccion_jugadas() 
        print(f' ***** jugadas:  {user_name}: -{user.upper()}-  La computadora: -{machine.upper()}-\n')
        
        if ronda_actual >1:
            print(f"computadora :{machine_wins} - {user_name} : {user_wins}")
            if machine_wins == user_wins:
                print("Esto está muy reñido, van empatados")
    
        if empate(user, machine, user_name) == True:
            ronda_actual = ronda_actual + 1
        
        else:
            reglas_func(user, machine, user_name, rondas_user)
            ronda_actual = ronda_actual +1
        
        print("ronda:", ronda_actual, "de: ", rondas_user)
       
        
        
        if user_wins >= rondas_user or machine_wins >= rondas_user:
            if user_wins > machine_wins:
                print(f"\n {user_name.upper()} es el ganador con: {user_wins} puntos!!")
                break
        
            elif machine_wins > user_wins:
                print(f"\n La COMPUTADORA es la ganadora con {machine_wins} puntos!")
                break
            
            elif machine_wins == user_wins:
                print("\n juguemos una ronda más")
                

if __name__ == "__main__":
    juego()
    