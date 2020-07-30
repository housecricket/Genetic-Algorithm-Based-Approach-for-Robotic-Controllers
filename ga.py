import random
from population import Population
from robot import Robot
from individual import Individual


class GA():

    def __init__(self, populationSize, mutationRate, crossoverRate, elitismCount, tournamentSize):
        self.populationSize = populationSize
        self.mutationRate = mutationRate
        self.crossoverRate = crossoverRate
        self.elitismCount = elitismCount
        self.tournamentSize = tournamentSize

    def initPopulation(self, chromosomeLength):
        print("Initialize population")
        population = Population(self.populationSize, chromosomeLength)
        return population

    ''' Calculate fitness for an individual '''

    def calcFitness(self, individual, world):
        # Get individual's chromosome
        chromosome = individual.getChromosome()

        # Get fitness
        robot = Robot(chromosome, world, 100)
        robot.run()
        fitness = world.scoreRoute(robot.getRoute())
        # Store fitness
        individual.setFitness(fitness)
        return fitness

    ''' Evaluate the whole population '''

    def evalPopulation(self, population, world):
        populationFitness = 0
        for individual in population.getIndividuals():
            populationFitness += self.calcFitness(individual, world)
        population.setPopulationFitness(populationFitness)

    ''' Check if population has met termination condition '''

    def isTerminationConditionMet(self, generationsCount, maxGenerations):
        return (generationsCount > maxGenerations)

    ''' Selects parent for crossover using tournament selection '''
    def selectParent(self, population):
        # Create tournament
        tournament = Population(self.tournamentSize)

        # Add random individuals to the tournament
        population.shuffle()
        for i in range(self.tournamentSize):
            tournamentIndividual = population.getIndividual(i)
            tournament.setIndividual(i, tournamentIndividual)
        
        # Return the best
        return tournament.getFittest(0)

    ''' Apply mutation to population '''
    def mutatePopulation(self, population):
        # Initialize new population
        newPopulation = Population(self.populationSize)
        for populationIndex in range(population.size()):
            individual = population.getFittest(populationIndex)
            for geneIndex in range(individual.getChromosomeLength()):
                # Skip mutation if this is an elite individual
                if (populationIndex >= self.elitismCount):
                    # Does this gene need mutation?
                    if (self.mutationRate > random.random()):
                        # Get new gene
                        newGene = 1
                        if (individual.getGene(geneIndex) == 1):
                            newGene = 0
                        # Mutate gene
                        individual.setGene(geneIndex, newGene)

            # Add individual to population
            newPopulation.setIndividual(populationIndex, individual)
        
        # Return mutated population
        return newPopulation

    ''' Crossover population using single point crossover '''
    def crossoverPopulation(self, population):
        # Create new population
        newPopulation = Population(population.size())
        # Loop over current population by fitness
        for populationIndex in range(population.size()):
            parent1 = population.getFittest(populationIndex)
            # Apply crossover to this individual?
            if (self.crossoverRate > random.random()) and (populationIndex >= self.elitismCount):
                # Initialize offspring
                offspring = Individual(parent1.getChromosomeLength())

                # Find second parent
                parent2 = self.selectParent(population)

                # Get random swap point
                swapPoint = (int) (random.random() * (parent1.getChromosomeLength() + 1))

                # Loop over genome
                for geneIndex in range(parent1.getChromosomeLength()):
                    # Use half of parent1's genes and half of parent2's genes
                    if (geneIndex < swapPoint):
                        offspring.setGene(geneIndex, parent1.getGene(geneIndex))
                    else:
                        offspring.setGene(geneIndex, parent2.getGene(geneIndex))

                # Add offspring to new population
                newPopulation.setIndividual(populationIndex, offspring)
            else:
                # Add individual to new population without applying crossover
                newPopulation.setIndividual(populationIndex, parent1)
        return newPopulation


