


#algorithme genetique
#creation de la fonction
import numpy as np
import random
nbp=int(input("Enter the size of population:"))#Taille population(10)
tc=int(input("Enter the size of chromosome:"))#taille chromosome: nbr de cité(7)
Distance=np.array([
    [0,12,10,12,5,5,12],
    [12,0,8,12,6,8,11],
    [10,8,0,11,3,9,9],
    [12,12,11,0,11,10,5],
    [5,6,3,11,0,6,7],
    [5,8,9,10,6,0,9],
    [12,11,9,5,7,9,0]
]) #matrice contenant les distances entre les villes
print(Distance)
max_iter=int(input("Enter max number of iteration: "))#nombre max d’itérations(10)
iteration=0

def pop_initialisation(nbp,tc): 
    p=np.zeros((nbp,tc))
    pop=random.sample(range(tc),tc)
    for i in range(nbp,tc):
        p.random(sample(t),t)
        for j in range(nbp,tc): 
            pop[i],[j]=p[i]
    return pop
solution=[1,2,3,4,5,6,7]
Ft=np.zeros((nbp))

pop=pop_initialisation(nbp,tc)

def fitness(Distance,solution):   
    a=int(solution[0])
    b=int(solution[tc-1])
    a=int(solution[i])
    b=int(solution[i+1])
    d+=Distance[a][b]
    return d
    for i in solution:
        Ft=solution[i]
        for i in range(nbp-1): 
            solution=pop[i][:]
            FT[i]=fitness(Distance,solution)
    dt=Distance[a][b]
#initialiser la population 
population=pop_initialisation(nbp,tc)
#trover best
best=min(population[i])
best_fitness=get.best(population,fitness)
#4
itr=0   #iteration
#5 commencer les iterations
fit_enf=np.zero((nbp))#fitness enfant
def croisement (enf,tc,nnbp):
    while itr<=itr-max:
        #effectue un croisement
      enf=np.copy(population)
      enf=croisement(enf,tc,nbp)
      enf=enf
    #evaluer la population enfant
      for i in range(nbp-1):
        solution=enf[1][:]
        fit_enf=fitness(solution,distance)
        #remplacer les parent par leur enfant
        for i in range(Ft,fit_enf,2):
            c1=2
            c2=c1+(tc//2)
            #trouver le best
            if c2>c1:
                best=enf[i]
            else:
                best=population[i]
