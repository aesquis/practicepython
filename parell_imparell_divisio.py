#! /usr/bin/python
# -*- coding: utf-8 -*-

def operacio():
    num1 = float(input("Digues un nombre: "))
    num2 = float(input("Digues un segon nombre :"))

    if (num1 % 2 == 0): #Dividim per ell mateix i mirem si dona 0
        print ("El numero %s és parell" %num1)
    else: #Si no dona 0 és imparell
        print ("El numero %s és imparell" %num1)

    divisio = (num1 / num2)

    print ("%s dividit per %s dona %s \n" %(num1,num2,divisio))


while True:
    operacio()
