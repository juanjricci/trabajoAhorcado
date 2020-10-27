from partida import Partida
from repositorios import Repositorios
import random


class ServicesPartidas():

    def iniciar_partida(self, nombre, dificultad, palabra, tipo_palabra):
        intentos = dificultad*len(palabra)
        if palabra == '' and tipo_palabra == '':
            palabra = random.choice(Repositorios.palabrasList)
            pal = palabra['palabra']
            tipo = palabra['tipo_palabra']
        else:
            pal = palabra
            tipo = tipo_palabra
        partida = Partida(pal, intentos, tipo, nombre)
        if dificultad > 10 or dificultad < 1:
            raise(ValueError)
        return partida

    def get_random_palabra(self):
        palabra = random.choice(Repositorios.palabrasList)
        return palabra

    def intentar_letra(self, partida, letra):
        if letra in partida._palabra:
            for i in range(len(partida._palabra)):
                if letra == partida._palabra[i]:
                    partida._palabra_aciertos[i] = partida._palabra[i]
        partida._intentos = partida._intentos - 1
        if partida._intentos < 0:
            raise(ValueError)
        if partida._palabra_aciertos == partida._palabra:
            return 'Gano'
        elif partida._intentos == 0:
            return 'Perdio'
        else:
            return 'Continua'

    def add_partida(self, partida):
        lastKey = -1
        for key in Repositorios.partida:
            lastKey = key
        id_new = int(lastKey) + 1
        Repositorios.partida[id_new] = partida.__dict__
