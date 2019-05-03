#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 18:31:26 2019

@author: tibo
"""

import matplotlib.pyplot as plt

from generateData import *
from outilsLignesBrises import *
from essaisSuccessifsATrou import *

if __name__ == "__main__" :
    valeurs = [5,10,11,12,13,14,15,16,17,18,19,20]
    SansElag = []
    Elag1 = []
    Elag2 = []
    AlaFOis = []
    
    for i in valeurs:
        readfile("DataSet"+str(i))
        t0 = time.time()
        appligbri(0)
        tf = time.time()
        AlaFOis.append(tf-ti)
        
    plt.plot(valeurs,SansElag)
    plt.plot(valeurs,Elag1)
    plt.plot(valeurs,Elag2)
    plt.plot(valeurs,AlaFOis)
    plt.show()