#! /usr/bin/python
# -*- coding: utf-8 -*-

#! /usr/bin/python
# -*- coding: utf-8 -*-

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Print inferiors a 5
for element in a:
    if element < 5:
        print element


#Crear una nova llista amb valors inferiors a 5

b = []

for element in a:
    if element <5:
        b.append(element)

print b


eleccio = int(input("Tria un numero :"))

for element in a:
    if element < eleccio:
              print element
