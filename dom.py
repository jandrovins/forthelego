#!/home/vincent/miniconda3/envs/datos/bin/python
"""
Author: Vincent A. Arcila L.
Mail: vaarcilal@eafit.edu.co
Date: March 14th 2019.
"""

import numpy as np
import cv2 as cv

def vertical(x, y):
    cv.rectangle(img, (x, y), (x+50, y+100), (0, 255, 0), 3)
    return x+50


def horizontal(x, y):
    cv.rectangle(img, (x, y), (x+100, y+50), (0, 255, 0), 3)
    return y+50


def hallarPerm(n):
    if n == 1:
        soluciones[1] = "v"
        return "v"
    if n == 2:
        s = "vv h"
        soluciones[2] = s
        return s
    if n-2 not in soluciones:
        print(n-2)
        menosDos = hallarPerm(n-2)
    else:
        menosDos = soluciones[n-2]
    if n-1 not in soluciones:
        menosUno = hallarPerm(n-1)
    else:
        menosUno = soluciones[n-1]
    solution = ""
    s = ""
    s2 = ""
    for i in menosDos:
        if i == " ":
            s = ""
            continue
        s += i
        for j in menosUno:
            if j == " ":
                s2 = ""
                continue
            s2 += j
            if not asegurarLongitud(s, s2, n):
                continue
            sol = s + s2
            if solution.find(sol) == -1:
                solution += " "
                solution += sol
            sol = s2 + s
            if solution.find(sol) == -1:
                solution += " "
                solution += sol
    solution = solution.strip(" ")
    soluciones[n] = solution
    return solution

def asegurarLongitud(s1, s2, n):
    cont = 0
    for i in s2:
        if i == "v":
            cont += 1
            continue
        elif i == "h":
            cont += 2
    for i in s1:
        if i == "v":
            cont += 1
            continue
        elif i == "h":
            cont += 2
    return n == cont

def longitudRestante(x):
    return 1300 - x



x = 0
y = 0

img = np.zeros((630, 1300, 3), np.uint8)

soluciones = {}

n = 6
images = 0
png = ".png"
name = "Sol"
s = hallarPerm(n)
x = 0
y = 0
sub = ""
longitudCadena = n * 50
for j in s.split(" "):
    if longitudRestante(x) < longitudCadena:
        y += 130
        x = 0
        if y +100 > 630:
            cv.imwrite(name+str(images)+png,img)
            images += 1
            x = 0; y = 0
            img = np.zeros((630, 1300, 3), np.uint8)
    for i in j:
        if i == "v":
            x = vertical(x,y)
        if i == "h":
            horizontal(x,y)
            horizontal(x,y+50)
            x += 100
    x += 50
cv.imwrite(name+str(images)+png,img)

cv.imshow("win1", img)
cv.moveWindow("win1", 22, 50)
cv.waitKey(0)
