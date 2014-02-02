import numpy as np
from random import shuffle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
Find avarage value in array of numbers
'''
def centroid(klaster):
    centroid = []
    for x in xrange(1,len(klaster[0])):
        a = [i[x] for i in klaster]
        centroid.append(sum(a)/len(klaster))
    return centroid

'''
Euclid distanc between two points in Euclid spaces
'''
def dist(x,y):   
    return (x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2


def klasteriranje(podaci,n):
    dim = len(podaci)/6
    klasteri = []
    for i in range(5):
        klasteri.append(podaci[i*dim:(i+1)*dim])
    klasteri.append(podaci[5*dim:])
    for i in xrange(n):
        novi_klasteri = [[],[],[],[],[],[]]
        centroidi = list()
        for k in klasteri:
            centroidi.append(centroid(k))
        for p in podaci:
            pr = []
            for c in centroidi:
                pr.append(dist(c,p[1:]))
            index = pr.index(min(pr))
            novi_klasteri[index].append(p)
        klasteri = novi_klasteri
    return [klasteri,centroidi]

def ucitaj(fileName):
    file = open(fileName,'r')
    lines = file.readlines()
    podaci = []
    for line in lines[1:]:
        temp = line.strip()
        a = temp.split(',')
        podaci.append([float(b) for b in a])
    return podaci

#ucitaj('subset_1k_presents.csv')

def K_clustering():
    # lista[lista(id,dim1,dim2,dim3)]
    podaci = ucitaj('subset_1k_presents.csv')
    [klasteri,centroidi] = klasteriranje(podaci,10)
    return [klasteri,centroidi]

def main():
    [klasteri,r] = K_clustering()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    c = ['r','black','b','y','c','gray']
    g = 0;
    for klas in klasteri:
        xcoord = [i[1] for i in klas]
        ycoord = [i[2] for i in klas]
        zcoord = [i[3] for i in klas]
        ax.scatter(xcoord, ycoord, zcoord, c=c[g])
        g = g + 1
    plt.show()

if __name__ == '__main__':
    main()
