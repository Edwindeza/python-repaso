## impresion normal
print("hola mundo")

## comentarios
"""
Texto comentado por 
lineas
"""
# Impresion con concatenacion
nombre = 'edwin'
# print('Hola ' + 'edwin')
# print('Hola ' + nombre)
# print(f"Hola {nombre}") # A partir de python 3.6

## Variables
# python es dinámicamente tipado, una variable puede tener varios tipos de datos y mutar entre ellas 

nombre = "edwin"
edad = 18
altura = "159cm"
casado = False
casado = " no definido "
# print(f"{nombre} - {edad} - {altura} - {casado}")

jugadores = {
    10: 'Messi',
    7: 'Cristiano Ronaldo',
}
# print(jugadores[10])

#constantes
PI = 3.4

# print(PI)

##Entrada de datos

# sitio = input("Ingresa tu nick: ")
# print('Ok tu nick es:' + sitio)


## Condiciones 
# pides el dato, pero lo transformas a entero, porque todo INPUT es string
# altura = int(input("Ingresa tu altura: "))
# Comparas la altura, si cumple eres alto sino no.
# if altura >= 170:
#     print("eres alto")
# else:
#     print("no eres alto")

# color = 'amarillo'

# match color:
#     case 'verde':
#         print('Exito')
#     case 'amarillo':
#         print(' advertencia')
#     case _:
#         print('error')


#Operadores

print ( 1+1 )
print ( 1-1 )
print ( 1*1 )
print ( 1/1 )

print( 4 == 4)
print( 4 == '4')
print( 4 != 5)
print( 4 < 5)
print( 4 <= 5)



## Funciones

def mostrarAltura():
    altura = int(input("Ingresa tu altura: "))
    # Comparas la altura, si cumple eres alto sino no.
    if altura >= 170:
        print("eres alto")
    else:
        print("no eres alto")

# con parametro
def mostrarAltura2(altura):
    # Comparas la altura, si cumple eres alto sino no.
    if altura >= 170:
        print("eres alto")
    else:
        print("no eres alto")

# Con return
def mostrarAltura3(altura):
    # Comparas la altura, si cumple eres alto sino no.
    resultado = ''
    if altura >= 170:
        resultado = "eres alto"
    else:
        resultado = "no eres alto"
    return resultado

# mostrarAltura()
# mostrarAltura()
# mostrarAltura()

# altura = int(input("Ingresa tu altura: "))
# mostrarAltura2(altura)

## Listas

personas = ["Victor", "Edwin"]
print(personas[0])
print(personas[1])


#bucles
for persona in personas:
    print("- "+persona)


# objetos
javascript = {
    'nombre': 'JavaScript',
    'año': 1995
}

def description():
    print('%s fue creado en %s' % (javascript['nombre'], javascript['año']))

description()