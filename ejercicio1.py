# obtener la representacion inversa de una cadena de caracteres 

cadena = 'python'

def switch(cadena):
    for letra in range(len(cadena)-1,-1,-1):
        print(cadena[letra])

switch(cadena)