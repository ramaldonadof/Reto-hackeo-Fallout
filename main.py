from palabra import Palabra
import os

"""actual_path = os.path.join(os.path.dirname(__file__),"words.txt")

with open(actual_path) as f:
    arr = f.readlines()"""


#arr = ["trip", "jobs", "wars", "swap", "real", "team", "vast", "tank", "loss", "sent", "coma", "salt", "draw", "came", "show"]

palabras = []

def insert(arr):
    palabras = []
    for i in arr:
        pal = Palabra(i, 0)
        palabras.append(pal)
    return palabras

def show(palabras: list[Palabra]):
    for i in palabras:
        print("Palabra: ", i.palabra, " Coincidencias: " , i.coincidencia)

def seleccion(word: str, coin: int, palabras: list):
    aux = []
    compare(word, palabras)
    if coin == 0:
        for i in palabras:
            if i.coincidencia == 0:
                aux.append(i)
    else:
        for i in palabras:
            if i.coincidencia >= coin and not (i.coincidencia == len(word)):
                aux.append(i)
    palabras = aux
    return palabras


def compare(word: str, palabras: list):
    for i in palabras:
        contador = 0
        contador = compararLetras(word, i.palabra)
        i.coincidencia = contador

def compararLetras(word: str, palabra: str) -> int:
    contador = 0
    for i in range( len(word) ):
            if word[i] == palabra[i]:
                contador +=1
    return contador



#insert(arr)

#ejem = seleccion("market", 2, palabras)

#ejem = seleccion("goal", 2, ejem)
#show(ejem)
