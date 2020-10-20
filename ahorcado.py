from partida import Partida
from servicesPartidas import ServicesPartidas
from repositorios import Repositorios
import random
import os


class Ahorcado():

    def un_jugador(self):
        servicePartida = ServicesPartidas()
        pal = random.choice(Repositorios.palabrasList)
        nombre = input('Ingrese un nombre: ')
        dificultad = int(input("Ingrese una dificultad del 1 al 10 (1 --> dificil, 10 --> facil): "))
        partida = Partida(pal['palabra'], dificultad*len(pal['palabra']), pal['tipo_palabra'], nombre)
        while partida._intentos > 0:
            print('Palabra a adivinar: ', partida._palabra_aciertos)
            print('Pista: ', partida._tipo_palabra)
            print('Cantidad de intentos: ', partida._intentos)
            letra = input("Ingrese una letra: ").upper()
            if letra == 'SALIR':
                return True
            result = servicePartida.intentar_letra(partida, letra)
            if result == 'Gano':
                print(result, '! Felicitaciones, la palabra era: ', partida._palabra)
                partida._intentos = 0
                return True
            else:
                # os.system('clear')
                print(result)
                if result == 'Perdio':
                    print(result, '! Lo lamento, la palabra era: ', partida._palabra)
                    return True

    def dos_jugadores(self):
        servicePartida = ServicesPartidas()
        print('------------------')
        print('Juega el jugador 1')
        print('------------------')
        nombre1 = input('Jugador 1: Ingrese un nombre: ')
        dificultad1 = int(input('Jugador 1: Ingrese una dificultad del 1 al 10 (1 --> dificil, 10 --> facil): '))
        palabra_adivinar1 = input('Jugador 2: Ingrese una palabra (esta se utilizara para que juegue el jugador 1): ')
        tipo_palabra_adivinar1 = input('Jugador 2: Ingrese la pista o tipo de palabra: ')
        partida1 = Partida(
            palabra_adivinar1, dificultad1*len(palabra_adivinar1), tipo_palabra_adivinar1, nombre1)
        while partida1._intentos > 0:
            print('Palabra a adivinar: ', partida1._palabra_aciertos)
            print('Pista: ', partida1._tipo_palabra)
            print('Cantidad de intentos: ', partida1._intentos)
            print(nombre1, end=': ')
            letra = input("Ingrese una letra: ").upper()
            if letra == 'SALIR':
                return True
            result = servicePartida.intentar_letra(partida1, letra)
            if result == 'Gano':
                print(result, '! Felicitaciones, la palabra era: ', partida1._palabra)
                servicePartida.add_partida(partida1)
                partida1._intentos = 0
                break
            else:
                print(result)
                if result == 'Perdio':
                    print(result, '! Lo lamento, la palabra era: ', partida1._palabra)
                    servicePartida.add_partida(partida1)
                    break
        print('------------------')
        print('Juega el jugador 2')
        print('------------------')
        nombre2 = input('Jugador 2: Ingrese un nombre: ')
        dificultad2 = int(input('Jugador 2: Ingrese una dificultad del 1 al 10 (1 --> dificil, 10 --> facil): '))
        palabra_adivinar2 = input('Jugador 1: Ingrese una palabra (esta se utilizara para que juegue el jugador 2): ')
        tipo_palabra_adivinar2 = input('Jugador 1: Ingrese la pista o tipo de palabra: ')
        partida2 = Partida(
            palabra_adivinar2, dificultad2*len(palabra_adivinar2), tipo_palabra_adivinar2, nombre2)
        while partida2._intentos > 0:
            print('Palabra a adivinar: ', partida2._palabra_aciertos)
            print('Pista: ', partida2._tipo_palabra)
            print('Cantidad de intentos: ', partida2._intentos)
            print(nombre1, end=': ')
            letra = input("Ingrese una letra: ").upper()
            if letra == 'SALIR':
                return True
            result = servicePartida.intentar_letra(partida2, letra)
            if result == 'Gano':
                print(result, '! Felicitaciones, la palabra era: ', partida2._palabra)
                servicePartida.add_partida(partida2)
                partida2._intentos = 0
                return True
            else:
                print(result)
                if result == 'Perdio':
                    print(result, '! Lo lamento, la palabra era: ', partida2._palabra)
                    servicePartida.add_partida(partida2)
                    return True
