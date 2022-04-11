turnoUno = """
HOLA 'JUGADOR 1'
Escribe un pais con la letra A:
"""
turnoDos = """
HOLA 'JUGADOR 2'
Escribe un pais con la letra B:
"""
turnoTres = """
HOLA 'JUGADOR 1'
Escribe un pais con la letra C:
"""
turnoCuatro = """
HOLA 'JUGADOR 2'
Escribe un pais con la letra D:
"""

def start():

    puntajeTotalA = 0

    def fourth():
        pais = str(input(turnoCuatro))

        if 'd' in pais[0]:
            print('correcto')

            def puntaje():
                puntaje = 1
                return puntaje

            puntajeTotal = puntaje()
            print(puntajeTotal)
            # fourth()
        
        else:
            print('incorrecto')

    def third():
        pais = str(input(turnoTres))

        if 'c' in pais[0]:
            print('correcto')

            def puntaje():
                puntaje = 1
                return puntaje

            puntajeTotal = puntaje()
            print(puntajeTotal)
            fourth()
        
        else:
            print('incorrecto')

    def second(puntajeTotal):
        pais = str(input(turnoDos))

        if 'b' in pais[0]:
            print('correcto')

            def puntaje(puntajeTotal):
                puntajeTotal = puntajeTotal + 1
                return puntajeTotal

            puntajeTotal = puntaje()
            print(puntajeTotal)
            third()
        
        else:
            print('incorrecto')

    def first():
        pais = str(input(turnoUno))

        if 'a' in pais[0]:
            print('correcto')

            def puntaje():
                puntaje = 1
                return puntaje
            puntajeTotal = puntaje()
            print(puntaje())

            second(puntajeTotal)
        
        else:
            print('incorrecto')

    first()

start()











# def validarPais(pais):
#     print(pais)
#     puntaje = 0
#     if('a' in pais):
#         puntoGanado = 1
#         puntajeTotal = puntaje + puntoGanado
#         return puntaje

#     print(puntaje)
# validarPais(pais)

