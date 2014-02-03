from ucitavanje import K_clustering
import random
'''
Initial population 
Each member of the population represents one level of packaging
'''
def sumInSpace(genome):
    dim = 100
    # dimZ not declared because dimZ = inf
    
    sumX = sum([i[1][0] for i in genome])
    sumY = sum([i[1][1] for i in genome])
    sumZ = sum([i[1][2] for i in genome])

    flag = False
    elem = []
    if sumX <= dim and sumY <= dim:
        flag = True
        elem = [1,2]
    if sumX <= dim and sumZ <= dim:
        flag = True
        elem = [1,3]
    if sumY <= dim and sumZ <= dim:
        flag = True
        elem = [2,3]

    if flag == True:
        genome[len(genome)-1][1] = elem
    else:
        genome[1].pop()

    return [flag,genome]


def InitPopulation(clusters, centroid):
    numberOfelements = sum([len(i) for i in clusters])
    allImOne = []
    for c in clusters:
        for e in c:
            allImOne.append(e)
    population = []
    order = [i for i in range(numberOfelements)]
    order = random.sample(order,numberOfelements)
    genomes = []
    for i in order:    
        genomes.append([[0,0],allImOne[i]])
        [flag,genomes] = sumInSpace(genomes)
        if flag == False:
            population.append(genomes)
            genomes = []
    return population

    
def GerationPopulation(round, previus, version):
    
    population = previus
    # Generation first population
    if round == 0:
        [clusters, centroid] = K_clustering()
        population = InitPopulation(clusters,centroid)
    else:
        previus = []

    print [p[0] for p in population]



GerationPopulation(0, [], 1)
#sumInSpace([[0,0],[[1,0,0],[1,1,0]]])

    