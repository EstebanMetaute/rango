var_numeInt = int(input('ingrese la cantidad de numeros ->'))
contador = 0

for i in range(var_numeInt):
    numero = float(input('ingresa numero ->'))
    if numero >= 10 and numero <= 20:
        contador += 1

print(f'la cantidad de numeros es: {contador}')
