print("==================================================")
input()

import json
import os
import time
from colorama import init, Fore, Style
os.system("cls")

# Initialize colorama
init(autoreset=True)

# Dictionary to store valences

def suma_diccionarios(diccionario1, diccionario2):
    for clave, valor in diccionario2.items():
        if clave in diccionario1:
            diccionario1[clave] += valor  # Sumar el valor si la clave ya existe
        else:
            diccionario1[clave] = valor  # Agregar la clave y el valor si no existe

def say(text, color):
    color = color.upper()
    colors = {
        "RESET": Style.RESET_ALL,
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    if color in colors:
        print(colors[color] + text + colors["RESET"])
    else:
        print(text)

def ask(question, color):
    color = color.upper()
    colors = {
        "RESET": Style.RESET_ALL,
        "BLACK": Fore.BLACK,
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    if color in colors:
        return input(colors[color] + question + colors["RESET"])
    else:
        return input(question)


os.chdir(f"{"J:\\VSC\\Club de Programación\\main\\elecciones"}")
option_path = "options.json"

people_path = "people.json"

say("==================================================", "CYAN")
say("  CARGANDO ELECCIONES...", "CYAN")
say("==================================================", "CYAN")
print("")


# Leer el contenido de opciones.json y cargarlo en un diccionario
with open(option_path, 'r', encoding='utf-8') as archivo:
    options = json.load(archivo)

with open(people_path, 'r', encoding='utf-8') as archivo:
    people = json.load(archivo)

# Ahora puedes usar diccionario_opciones en tu script

power = {}

for key in people:
    suma_diccionarios(power, {key: (people[key][0]-people[key][1])})

power = dict(sorted(power.items(), key=lambda item: item[1], reverse=True))

total = 0
for key in power:
    total += power[key]

time.sleep(2)
input("")
os.system("cls")

say("==================================================", "CYAN")
say("  PODER DE VOTO", "CYAN")
say("==================================================", "CYAN")
print("")

say(f"{"  TOTAL" + " "*(25-len("TOTAL")) + str(total) + " "*(10-len(str(total))) + "100%"}", "CYAN")
print("")

for key in power:
    say(f"{"  " + key + " "*(25-len(key)) + str(power[key]) + " "*(10-len(str(power[key]))) + str(round(100*power[key]/total, 1)) + "%"}", "CYAN")
    

# Esto imprime el contenido del diccionario
print("")
input()

os.system("cls")
say("==================================================", "CYAN")
say("  PROPUESTAS", "CYAN")
say("==================================================", "CYAN")
print("")

for key in options:
    say(f"{"  " + key + " "*(4-len(key)) + options[key]}", "CYAN")

input("")


# Inicializar un diccionario para almacenar los votos de cada propuesta
votes = {key: 0 for key in options.keys()}

# Preguntar a cada persona por su opción de voto
for key in power:
    # Preguntar al usuario cuál opción quiere votar
    vote = ask(f"  Voto de {key}: ", "CYAN")
    
    # Validar la entrada del usuario
    if vote in options:
        # Sumar el poder de voto a la propuesta seleccionada
        votes[vote] += power[key]  # power[key][0] es el poder de voto de la persona
        say(f"  {options[vote]}: {votes[vote]} (+{power[key]})", "GREEN")
    else:
        say("  Voto anulado", "RED")
input("")

# Imprimir el resultado de las votaciones
os.system("cls")
say("==================================================", "CYAN")
say("  RESULTADOS DE VOTACIÓN", "CYAN")
say("==================================================", "CYAN")
print("")

total_votes = sum(votes.values())

for key in votes:
    percentage = (votes[key] / total_votes * 100) if total_votes > 0 else 0
    say(f"  {options[key]}: {votes[key]} puntos de voto ({round(percentage, 1)}%)", "CYAN")

print("")
input("")