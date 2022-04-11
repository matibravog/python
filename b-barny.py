menu = """ 
1) marte
2) jupiter
"""

G_tierra = 9.8
G_marte = 3.7
G_jupiter = 22.8

U_Medida = ' [N]'

def diego():
    
    planeta = input(menu)
    
    texto = ('elegiste ' + planeta + ', ahora dime cual es tu masa ' + """
    
    """)

    texto2 = 'tu peso en ' + planeta + ' es ' 
    
    if planeta == 'marte':
        masa = int(input(texto))

        peso = str(masa * G_marte)
        print(texto2 + peso + U_Medida)

    elif planeta == 'jupiter':

        masa = int(input(texto))

        peso = str(masa * G_jupiter) 
        print(texto2 + peso + U_Medida)

diego()