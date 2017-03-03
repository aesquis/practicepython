#! /usr/bin/python
# -*- coding: utf-8 -*-
import datetime
now  = datetime.datetime.today()

name = raw_input("Hey there, what's your name? ")
age = raw_input("How old are you? ")

nYears = 100 - int(age)

turn100 = now.year + nYears

print ("Hi %s, \nYou'll turn 100 in %d, Happy HB! " %(name,turn100))

def function (nYears,age):
    for i in range(nYears+1):
        nyear = now.year + i
        nage = int(age) + i
        print ("Hello, in %d, you'll turn %d" %(nyear,nage))
        i += 1

function (nYears, age)




