# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

points = []

def main():
    
    file = open("tst1.txt","r")
    
    if file.mode == "r":
        lines = file.readlines()
        
    for line in lines:
        line = line.split(' ')
        line = [i.strip() for i in line]
        p = Point(int(float(line[0])),int(float(line[1])))
        points.append(p)


class Point( object ):
    def __init__( self, x, y):
        self.x = x 
        self.y = y
    
    def __repr__( self ):
        return "(%r, %r)" % ( self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def distanceDroite( self, ligne):
        #calcul de a et b de l'equation ax+b
        a = ( ligne.B.y - ligne.A.y ) / (ligne.B.x - ligne.A.x)
        b = ligne.A.y - ligne.A.x * a
        dist = abs(a * self.x - self.y + b) / ((a**2 + b**2)**(1/2))
        return dist
    
class Ligne( object ):
    def __init__( self, A, B):
        self.A = A
        self.B = B
        
    def __repr__( self ):
        return "Ligne ("+str(self.A)+", "+str(self.B)+")"
    
    def __eq__(self, other):
        return self.A == other.A and self.B == other.B


def SDBrisure(ligne):
    SD = 0
    xdeb = ligne.A.x
    xfin = ligne.B.x
    if(ligne.A.x > ligne.B.x ):
        (xdeb, xfin) = (ligne.B.x, ligne.A.x)
        
    for i in range(xdeb, xfin):
        SD += points[i].distanceDroite(ligne)
        
    return SD

def SDTot(listLignes):
    SDtot = 0
    for l in listLignes : 
        SDtot += SDBrisure(l)
    return SDtot

def cout(listLignes, C):
    m = len(listLignes)
    return SDTot(listLignes) + m * C

main()

l = Ligne(points[0],points[2])
print(points)
print(l)
print(points[1].distanceDroite(l))
print("SD")
print(SDBrisure(l))
absc = [p.y for p in points]
plt.plot(absc,'x')

