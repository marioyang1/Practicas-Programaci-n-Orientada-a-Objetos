# Practicas de arreglos bidimensionales    
    
casilla = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

jugador = 1
movi = 0
movim = 0

if casilla['7'] == 'X' and casilla['8'] == 'X' and casilla['9'] == 'X':
    print('Jugador 1 \n¡GANASTE!\n¡GANASTE!\n¡GANASTE!')


def num():
    if casilla['7'] == 'O' and casilla['8'] == 'O' and casilla['9'] == 'O':
        print('Jugador 2 \n¡GANASTE!\n¡GANASTE!\n¡GANASTE!')


print(' ¡3 EN RAYA!')
print('             ')
print('    |    |  ')
print('    |  O | ')
print('----|----|----')
print('    |    | O')
print('----|----|----')
print(' X  |  X | ')
print('    |    | ')
print('             ')
print(' ¡numeros casilla por completar!')
print('             ')
print('    |    |  ')
print(' 1  |    | ')
print('----|----|----')
print(' 4  |  5 | ')
print('----|----|----')
print('    |    | 9 ')
print('    |    | ')
print('             ')

while True:
    print(casilla['1']+'   |   '+casilla['2']+'|'+casilla['3'])
    print('    |  O | ')
    print('----|----|----')
    print(casilla['4'] + '   |' + casilla['5'] + '   |   ' + casilla['6'])
    print('    |    | O')
    print('----|----|----')
    print('  X |  X | ')
    print(casilla['7'] + '   |   ' + casilla['8'] + '|   ' + casilla['9'])
    movim = num()
    if movi == 9 or movim == 1:
        break
    if True:
        if jugador == 1:
            num.insertado = input('Jugador \nElige la Casilla 9 y Gana: ')
        if num.insertado== ("9"):
                print (' \n¡GANASTE!\n¡GANASTE!\n¡GANASTE!')
                print('             ')
                print('    |    |  ')
                print('    |  O | ')
                print('----|----|----')
                print('    |    | O')
                print('----|----|----')
                print(' X  |  X | X    <------------ ¡Creaste un 3 en Raya!' ) 
                print('    |    | ')
                print('             ') 
        if num.insertado== ("9"):
            exit()
        if num.insertado== ("9"):
            exit()
    
    
    
    
    