import matplotlib.pyplot as plt
import itertools

#Variable Globale, ensemble des points
points = []


def readfile(filename):
    """
        Fonction pour parser un fichier
    """
    file = open(filename,"r")
    
    if file.mode == "r":
        lines = file.readlines()
        
    for line in lines:
        line = line.split(' ')
        line = [i.strip() for i in line]
        p = Point(int(float(line[0])),int(float(line[1])))
        points.append(p)
    file.close()

class Point( object ):
    """
        Classe métier Point, qui permet de calculer la distance à une ligne
    """
    def __init__( self, x, y):
        self.x = x 
        self.y = y
    
    def __repr__( self ):
        return "(%r, %r)" % ( self.x, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def distanceDroite( self, ligne):
        #calcul de a et b de l'equation y = ax+b
        a = ( ligne.B.y - ligne.A.y ) / (ligne.B.x - ligne.A.x)
        b = ligne.A.y - ligne.A.x * a
        #Calcul de la distance d'un point à une droite
        dist = abs(self.y - a * self.x - b) / ((a**2 + 1)**(0.5))
        return dist

class Ligne( object ):
    """
        Classe métier Ligne
    """
    def __init__( self, A, B):
        self.A = A
        self.B = B
        
    def __repr__( self ):
        return "Ligne("+str(self.A)+", "+str(self.B)+")"
    
    def __eq__(self, other):
        return self.A == other.A and self.B == other.B


def SDBrisure(ligne):
    """
        Fonction qui calcul la distance des points à une droite(ligne)
    """
    SD = 0
    xdeb = ligne.A.x
    xfin = ligne.B.x
    if(ligne.A.x > ligne.B.x ):
        (xdeb, xfin) = (ligne.B.x, ligne.A.x)
    
    for i in range(xdeb , xfin - 1):
        SD += points[i].distanceDroite(ligne)
        
    return SD


def SDTot(listLignes):
    """
        Fonction qui calcul la somme des distances des points à une ligne brisée (liste de lignes)
    """
    SDtot = 0
    for l in listLignes : 
        SDtot += SDBrisure(l)
    return SDtot

def cout(listLignes, C):
    """
        Fonction qui calcul le cout d'une ligne brisée
        @listLignes ligne brisée
        @C coefficient
    """
    m = len(listLignes)
    return SDTot(listLignes) + m * C

def generateSolAffichage(config, pointsY):
    """
		Génère les abscisses et ordonées pour une config donnée
        pour facilité l'affichage de la solution
	"""
    X = []
    Y = []
    k = 0
    for i in config:
        k += 1
        if(i == 1):
            X.append(k)
            Y.append(pointsY[k-1])
        
    return X, Y

def generateSolLignes(config):
    """
		Génère des lignes pour une config donnée 
		(ie par quels points on passe)
	"""
    pointsY = [p.y for p in points]
    lignes = []
    tmpPoints = []
    k = 0
    for i in config:
        k += 1
        if(i == 1):
            tmpPoints.append(Point(k,pointsY[k-1]))
            
    for i in range(0,len(tmpPoints)-1):
        lignes.append(Ligne(tmpPoints[i],tmpPoints[i+1]))
        
    return lignes


def trace(config):
    """
		trace les données d'entrées et une config passant par ces points
	"""
    pointsY = [p.y for p in points]
    pointsX = [p.x for p in points]
    plt.plot(pointsX, pointsY, 'x')
    
    Xconf, Yconf = generateSolAffichage(config, pointsY)
    plt.plot(Xconf,Yconf, 'red')
    plt.show()