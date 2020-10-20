from servicesPartidas import ServicesPartidas
from partida import Partida
from ahorcado import Ahorcado
from menu import Menu
from repositorios import Repositorios


if __name__ == '__main__':
    a = Ahorcado()
    m = Menu()

    while True:
        cantidad_jugadores = m.titulo()
        if cantidad_jugadores == 1:
            a.un_jugador()
            input('Presione cualquier tecla para continuar...')
        elif cantidad_jugadores == 2:
            a.dos_jugadores()
            print('Juego Terminado!!!')
            print('Resultados: ')
            print(Repositorios.partida)
            print('------------------------------------------')
            input('Presione cualquier tecla para continuar...')
        elif cantidad_jugadores == 3:
            break
