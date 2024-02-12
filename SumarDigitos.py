print("Programa que sume los dígitos de un número ingresado por el usuario")
n = int(input("Escribe el max de los números: "))
sumat = 0

while n > 0:
    num = int(input("Número: "))
    sumat = sumat + num
    n = n-1
    
print ("La suma de los números digitados es: ", sumat)
