def conversor(tipo_pesos, valor_dolar):
    pesos = float(input('cuantos pesos '+ tipo_pesos + ' tienes?'))
    dolares = str(round((pesos / valor_dolar), 2))
    print('Tienes '+ dolares +' dolares' )

menu = """
CONVERSOR DE MONEDAS

1) USD - CLP
2) USD - ARG

"""

opcion = int(input(menu))

if opcion == 1:
    conversor('chilenos', 771)
elif opcion == 2:
    conversor('argntinos', 97)

