import os


class Menu():

    def titulo(self):
        os.system('clear')
        print("-------------------------------")
        print("▄▀█ █ █ █▀█ █▀█ █▀▀ ▄▀█ █▀▄ █▀█")
        print("█▀█ █▀█ █▄█ █▀▄ █▄▄ █▀█ █▄▀ █▄█")
        print("-------------------------------")
        print(" ***EL JUEGO DEL AHORCADO***")
        print("-------------------------------")
        print("1. Un jugador")
        print("2. Dos jugadores")
        print("3. Salir")
        opcion = input("Elija una opcion: ")
        os.system('clear')
        if opcion == '1' or opcion == '2' or opcion == '3':
            return int(opcion)
        else:
            return input(
                "No es una de las opciones."
                " Presiona ENTER para continuar..."
                )
            os.system('clear')
