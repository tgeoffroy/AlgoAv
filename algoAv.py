import matplotlib.pyplot as plt
import itertools

points = []

def readfile(filename):
    
    file = open(filename,"r")
    
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
        #calcul de a et b de l'equation y = ax+b
        a = ( ligne.B.y - ligne.A.y ) / (ligne.B.x - ligne.A.x)
        b = ligne.A.y - ligne.A.x * a
        dist = abs(self.y - a * self.x - b) / ((a**2 + 1)**(0.5))
        return dist
    
class Ligne( object ):
    def __init__( self, A, B):
        self.A = A
        self.B = B
        
    def __repr__( self ):
        return "Ligne("+str(self.A)+", "+str(self.B)+")"
    
    def __eq__(self, other):
        return self.A == other.A and self.B == other.B


def SDBrisure(ligne):
    SD = 0
    xdeb = ligne.A.x
    xfin = ligne.B.x
    if(ligne.A.x > ligne.B.x ):
        (xdeb, xfin) = (ligne.B.x, ligne.A.x)
    
    for i in range(xdeb , xfin - 1):
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

def generateSolAffichage(config, pointsY):
    """
		génère les abscisses et ordonées pour une config donnée 
		(ie par quels points on passe)
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
		génère les abscisses et ordonées pour une config donnée 
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
    print(Xconf)
    print(Yconf)
    plt.show()
    
def trace2(lignes):
    
    pointsY = [p.y for p in points]
    pointsX = [p.x for p in points]
    plt.plot(pointsX, pointsY, 'x')
    
    Xconf = []
    Yconf = []
    
    for l in lignes:
        Xconf.append(l.A.x)
        Xconf.append(l.B.x)
        Yconf.append(l.A.y)
        Yconf.append(l.B.y)
        
    plt.plot(Xconf,Yconf, 'red')
    plt.show()
    
if __name__ == "__main__"  :
    
    readfile("tst1.txt")
    
    nbPointsInter = len(points) - 2
    tousEssais = [([1]+list(i)+[1]) for i in itertools.product([0, 1], repeat= nbPointsInter)]

    pointsY = [p.y for p in points]
    print(generateSolLignes(tousEssais[3],pointsY))
    trace(tousEssais[3])
    print(tousEssais[3])
    l = Ligne(points[0],points[2])
    print(points)
    print(l)
    print(points[1].distanceDroite(l))
    print("SD")
    print(SDBrisure(l))
    

