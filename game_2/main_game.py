# tijera gana a papel
# papel gana a piedra
# piedra gana a tijera

import random

saludo = """      ----Juego de piedra papel ó tijera---
 Se deberá especificar cuantas rondas serán necesarias ganar para ganar la partida
 Quien tenga la mayor cantidad de rondas será el triunfador definitivo
 
 Reglas: 
 - (1) La cantidad de rondas elegidas para jugar deberán ser entre 2 y 5 
 - (2) Para elegir la cantidad de rondas: colocar números en vez de letras:
       ejemplo: 4[bien] => cuatro[mal]
 - (3) Cuando haya un empate: nadie ganará puntos, y se deberá jugar una ronda extra"""

#arreglar input (todo minúsculas, sin espacios sin acentos y otros caracteres) 

options = ["piedra", "papel", "tijera"]
user_wins = 0
machine_wins = 0

def sin_caracteres_acentos(word):
    caracteres = [" ", ",", "-", "-" , "*", "+", "?"]

    acentos_list = { "à" : "a" , "á": "a" , "â" : "a" , "ã" : "a", "ä": "a", 
               "é" : "e", "è": "e", "ê" : "e" , "ë": "e", 
               "ì" : "i" , "í": "i", "ï" : "i", "î": "i",
               "ó": "o", "ò": "o", "ö": "o", "õ": "o", "ø": "o", "ô": "o",
               "ú": "u", "ù": "u", "ü": "u", "û": "u" }
 
    for acento in acentos_list:
        if acento in acentos_list:
            word = word.replace(acento, acentos_list[acento])
            
    for caracter in caracteres:
        if caracter in caracteres:
            word = word.replace(caracter, "")
            
    return word

def eleccion_rondas_nickname():
    user_name = input(' Escribe tu nickname: ').lower()
    user_name = sin_caracteres_acentos(user_name)
    rondas_user = input( f' Hola {user_name.upper()}. Cuantas rondas quieres jugar? =>  ')
    while True:
        if not rondas_user.isdigit():
            print(f'\n "{rondas_user}" es opción inválida: escribiste números')
            rondas_user = input(" Cuantas rondas quieres jugar? =>  ")
        elif not int(rondas_user) in range(2,6):
            print(f'\n elegiste una cantidad de rondas fuera de rango')
            rondas_user = input(" Cuantas rondas quieres jugar? =>  ")
                
        else:
            break
    return user_name, int(rondas_user)

def eleccion_jugada():
    user = input(" Elige tu jugada: [piedra][papel][tijera] => ")
    machine = random.choice(options)
    user = sin_caracteres_acentos(user).lower()
    # if not user in options: esta condicional no es necesaria
    while not user in options:
            print("\n Recuerda colocar la opción de manera correcta")
            user = input(" Elige tu jugada: [piedra][papel][tijera] => ").lower()
            user = sin_caracteres_acentos(user)
       
    return user , machine

def empate(user, machine, ronda):
        if user == machine:
            print(f' Empate! ambos eligieron: {user.upper()} ronda actual: {ronda}')


def reglas(user_name, user, machine, ronda, rondas_user):
    global user_wins
    global machine_wins
    user_up = user.upper()
    machine_up = machine.upper()
    
    if user == "piedra":
        if machine == "papel":
            machine_wins = machine_wins + 1
            return print(f' {machine_up} le gana a la {user_up}. Punto para la computadora!\n')    

        if machine == "tijera":
            user_wins += 1
            return print(f' La {user_up} le gana a la {machine_up}. Punto para {user_name}.')
            
    if user == "papel":
        if machine == "piedra":
            user_wins += 1
            return print(f' {user_up} le gana a la {machine_up}. Punto para {user_name}\n ')

        if machine == "tijera":
            machine_wins += 1
            return print(f' {machine_up} le gana a la {user_up}. Punto para la computadora \n')
            #ronda += 1
    if user == "tijera":
        if machine == "papel":
            user_wins += 1
            return print(f' La {user_up} le gana al {machine}. Punto para {user_name}\n')
        
        if machine == "piedra": 
            machine_wins += 1
            return print(f' La {machine_up} le gana a la {user_up}. Punto para la computadora\n')
                

def game():
    global user_wins
    global machine_wins
    
    ronda = 1
    print(saludo)
    user_name, rondas_user = eleccion_rondas_nickname()
    
    while True: 
        
        if user_wins >= rondas_user or machine_wins >= rondas_user:
            if user_wins > machine_wins:
                print(f'{user_name.upper()} ha ganado la partida con {user_wins} puntos\n')
                break
            
            elif machine_wins > user_wins:
                print(f' La computadora ha ganado la partida con {machine_wins} puntos\n')               
                break
        
        print(f'\n {"* -" *5} Ronda: {ronda} {"* -" *5}')
        
        if ronda > 1: # mostrar el puntaje después de la primera ronda
            print(f'Puntos: {user_name} => {user_wins} computadora => {machine_wins}\n')
            
        user, machine = eleccion_jugada()
        
        print(f'Elección de jugadas: {user_name} => {user}, COMPUTADORA => {machine}\n')
        
        if empate(user, machine, ronda) == True:
            ronda +=1
        
        else:
            reglas(user_name, user, machine, ronda, rondas_user)
            ronda += 1
        
        if machine_wins == user_wins and machine_wins !=0:
            print("Ambos jugadores tienen la misma cantida de puntos\n")
        
        if machine_wins > user_wins:
            if machine_wins == (rondas_user - 1):
                print(f' a la computadora le falta un punto para ganar!\n')
        if user_wins < machine_wins:
            if user_wins == (rondas_user -1):
                print(f' a {user_name} le falta un punto para ganar!\n')
        
        
        
        
            
            
        
        

    
    
    


    
    
if __name__ == "__main__":
    game()
    

