'''Programa que ejecuta el juego del ahorcado mediante list comprehension.

Condiciones:

1. Elegir aleatoriamente una palabra de una lista de palabras guardadas en un archivo aparte.
2. Mostrar el dibujo de la horca.
3. Mostrar un guión bajo por cada letra de la palabra.
4. Pedir al usuario que introduzca una letra.
5. Comprobar si esa letra está contenida en la palabra elegida.
6. Si la letra está, sustituir el guión correspondiente por dicha letra.
7. Mostrar las letras repetidas.
8. Si se falla 6 veces se completa el dibujo del ahorcado y se muestra que se ha perdido.
9. Si se aciertan todas la letras de la palabra se muestra que se ha ganado.
'''

# 1. Vamos a importar los módulos que se necesitan:

import os
import random
import time

# 2. Se eligen las palabras que usaremos para el juego. Se realiza con la ayuda de un list comprehension.
'''Para ello, definimos la ruta donde está guardado el archivo al programa, que para este caso, se va atomar de una
base de datos. La función se hace por fuera del entry point. '''
    
with open('./recursos/palabras_01.txt', 'r', encoding='utf-8') as f:
        palabra_BD = [(line.strip().upper()) for line in f]   
    
    # Métodos para cadena:
    # .strip: elimina espacios al principio y al final de un string o, en este caso, de una palabra.
    # .upper: devuelve una cadena donde todos los caracteres están en mayúsculas.

# Con ciclo for:

'''def leer_palabras01():
    palabra_BD = []
    with open('./recursos/palabras_01.txt', 'r', encoding='utf-8') as f:
        for line in f: # Con el ciclo for iteramos por cada línea del archivo.
            palabra_BD.append(line.strip().upper())
        return palabra_BD'''

# It removes the accents of a string:
def normalize(s): 
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"),)
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

# 3. Inicio del entry point:

def run():
    
    # 4. Se dfinen unas variables que vamos a necesitar.
    # 4.1. Se elige aleatoriamente una palabra de una lista de palabras.    
    
    palabra_elegida = normalize(random.choice(palabra_BD))
    escoger_palabra_lista = [letra for letra in palabra_elegida]
    escoger_palabra_lista_underscores = ['_'] * len(escoger_palabra_lista)
    letras_index_dict = {}
    for idx, letra in enumerate(palabra_elegida):
        if not letras_index_dict.get(letra):
            letras_index_dict[letra] = []
        letras_index_dict[letra].append(idx)

    # len: devuelve el número de caracteres de la cadena.
    # El método enumerate() agrega un contador a un iterable y lo devuelve (el objeto enumerate).
    # Este método devuelve el valor de la clave dada, si está presente en el diccionario.
    # idx = index

    errores = 0
    
    letras_usadas = []

    # 5.  Mostramos la cabecera e iniciamos el bucle:    

    while True:
        os.system('cls')
        print('***********************************************')
        print('************** JUEGO DEL AHORCADO *************')
        print('********* ¡Adivina la palabra oculta! *********')
        print('* Se tendrán en cuenta las vocales con acento *')
        print('**************** ¿Te arriesgas? ***************')
        print('***********************************************')
        
        if errores == 0:
            print()
            print('  +---+')
            print('  |   |')
            print('      |')
            print('      |')
            print('      |')
            print('      |')
            print('=======\n')
            print(' -> Fallo 0 de 6\n')

        elif errores == 1:    
            print()
            print('  +---+')
            print('  |   |')
            print('  O   |')
            print('      |')
            print('      |')
            print('      |')
            print('=======\n')
            print(' -> Fallo 1 de 6\n')

        elif errores == 2:    
            print()
            print('  +---+')
            print('  |   |')
            print('  O   |')
            print('  |   |')
            print('      |')
            print('      |')
            print('=======\n')
            print(' -> Fallo 2 de 6\n')

        elif errores == 3:    
            print()
            print('  +---+')
            print('  |   |')
            print('  O   |')
            print(' /|   |')
            print('      |')
            print('      |')
            print('=======\n')
            print(' -> Fallo 3 de 6\n')

        elif errores == 4:    
            print()
            print('  +---+')
            print('  |   |')
            print('  O   |')
            print(' /|\  |')
            print('      |')
            print('      |')
            print('=======\n')
            print(' -> Fallo 4 de 6\n')

        elif errores == 5:     
            print()
            print('  +---+')
            print('  |   |')
            print('  O   |')
            print(' /|\  |')
            print(' /    |')
            print('      |')
            print('=======\n')
            print(' -> Fallo 5 de 6\n')

        elif errores == 6:          
            print()
            print('  +---+')
            print('  |   |')
            print('  Q   |')
            print(' /|\  |')
            print(' / \  |')
            print('      |')
            print('=======\n')
            print(' -> Fallo 6 de 6')
            print()
            print('La palabra era: ', palabra_elegida)
            print('\n***   ¡Perdiste!   ***')
            break

        for caracter in escoger_palabra_lista_underscores:
            print(caracter + ' ', end=' ')
        print('\n')

        print('\nLetras usadas: ', letras_usadas)

        letra = input('\nEscribe una letra y adivina la palabra: ').strip() .upper()
        #assert letra.isalpha(), 'Solo se pueden ingresar letras.'

        if letra in letras_usadas:            
            print('¡Upss... Esta letra ya está usada!\n')
            time.sleep(1)            

        else:                     
            letras_usadas.append(letra)

        if letra not in escoger_palabra_lista:            
            errores += 1

        if letra in escoger_palabra_lista:
            for idx in letras_index_dict[letra]:
                escoger_palabra_lista_underscores[idx] = letra

        if '_' not in escoger_palabra_lista_underscores:
            os.system('cls')
            print('**************************')
            print('****   ¡HAS GANADO!   ****')
            print('**************************')
            print('\n')

            print('La palabra era: ', palabra_elegida)
            break

    volver = input('\n¿Quieres volver a jugar?: Sí = s, No = n: ')
    if volver == 's':
        run()

    else:
        print('\nOk. En otra acasión será.')    
   
if __name__ == '__main__':
    run()

