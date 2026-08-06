total = 0
cantidad = 0

print("Buenos dias, este programa te va a ayudar")
print("Este programa registra el promedio")
while True:
    nota = int(input("Ingrese una nota: "))

    if nota == -1:
        break

    if nota < 0 or nota > 100:
        print("Nota inválida")
    else:
        total += nota
        cantidad += 1

print("Promedio:", total / cantidad)