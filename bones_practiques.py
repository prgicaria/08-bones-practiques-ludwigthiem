#!/usr/bin/env python

'''Bones pràctiques. Executar una divisió entera

Institut Icària
Programació - 1r Batxillerat - Curs 20234-24

Demana als usuaris dos nombres enters, en fa la divisió i mostra per pantalla
la divisió, el quocient i el residu.
'''

__author__ = "Ludwig Thiem González"
__email__ = "lthiem@instituticaria.cat"
__date__ = "2024/10/23"

dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))
quocient = dividend // divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print(f"Quocient: {quocient}")
print(f"Residu: {residu}")
