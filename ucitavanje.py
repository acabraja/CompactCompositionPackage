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
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
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
    c = ['r','black','b','y','c','gray']
    g = 0;
    for klas in klasteri:
        xcoord = [i[1] for i in klas]
        ycoord = [i[2] for i in klas]
        zcoord = [i[3] for i in klas]
        ax.scatter(xcoord, ycoord, zcoord, c=c[g])
        g = g + 1
    plt.show()
    k=0
    print"--------------------------"
    s=""
    print len(klasteri[5])
    for i in klasteri:
        s=s+str(centroidi[k])
        s=s+";"
        for j in i:
            s=s+str(j[1:])+";"
    #print s

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

def main():
    # lista[lista(id,dim1,dim2,dim3)]
    podaci = ucitaj('subset_1k_presents.csv')
    klasteriranje(podaci,10)
    #matrica = np.zeros((1000,1000,), dtype=np.int)
    


    # treba minimizirati maximum
    #maximum = matrica.max()

if __name__ == '__main__':
    main()
