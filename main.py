from world import World
from ga import GA

'''
As a reminder: 
0 = Empty 
1 = Wall 
2 = Starting position 
3 = Route 
4 = Goal position
'''

maxGenerations = 1000

def runGA():
    myWorld = World([
        [0, 0, 0, 0, 1, 0, 1, 3, 1],
        [1, 0, 1, 1, 1, 0, 2, 3, 1],
        [1, 0, 0, 1, 3, 3, 3, 3, 1],
        [3, 3, 3, 1, 3, 1, 1, 0, 1],
        [3, 1, 3, 3, 3, 1, 1, 0, 0],
        [3, 3, 1, 1, 1, 1, 0, 1, 1],
        [1, 3, 0, 1, 3, 3, 3, 3, 3],
        [0, 3, 1, 1, 3, 1, 0, 1, 3],
        [1, 3, 3, 3, 3, 1, 1, 1, 4],
    ])

    ga = GA(20, 0.05, 0.9, 2, 10)
    population = ga.initPopulation(128)
    ga.evalPopulation(population, myWorld)

    # Keep track of current generation
    generation = 1
    while ga.isTerminationConditionMet(generation, maxGenerations) == False:
        # Print fittest individual from population
        fittest = population.getFittest(0)

        print("G" + str(generation) + " Best solution (" + str(fittest.getFitness()) + "): " + fittest.toString())

        # Apply crossover
        population = ga.crossoverPopulation(population)

        # Apply mutation
        population = ga.mutatePopulation(population)

        # Evaluate population
        ga.evalPopulation(population, myWorld)

        # Increment the current generation
        generation +=1
    print("Stopped after " + str(maxGenerations) + " generations.")
    fittest = population.getFittest(0)
    print("Best solution (" + str(fittest.getFitness()) + "): " + fittest.toString())

if __name__ == '__main__':
    runGA()
