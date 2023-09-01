#Crear una lista y mostrar
#Ordenar la lista y mostrala
#Mostrar su longitud
#Buscar un elemento solicitado por teclado

lista1 = [9,14,5,6]
#mostrar
print(lista1)
#recorrer y mostrar
for i in lista1:
    print(i)
# ordenaa1
print(sorted(lista1))
#ordenar2
lista1.sort()
print(lista1)
#longitud
print(len(lista1))
#buscar
c=int(input("Ingrese el numero a buscar\n"))
if c in lista1:
    print("El elemto existe en la lista")
else:
    print("el elemto no está en la lista")

print(lista1.index(c))