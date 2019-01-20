"""lista1 = list(range(0,11,1))
print(lista1)

lista2 = list(range(-10,1,1))
print(lista2)

lista3 = list(range(0,21,2))
print(lista3)

lista4 = list(range(-19,1,2))
print(lista4)

lista5 = list(range(0,51,5))
print(lista5)"""

lista_1 = ["h","o","l","a"," ","m","u","n","d","o"]
lista_2 = ["h","o","l","a"," ","l","u","n","a"]

lista_3 = []

for letra in lista_1:
    if(letra in lista_2) and (letra not in lista_3):
        lista_3.append(letra)

print(lista_3)