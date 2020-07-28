from individual import Individual
import random


class Population:        

    ''' Initializes population of individuals '''

    def __init__(self, populationSize, chromosomeLength=0):
        # Initializes blank population of individuals
        if chromosomeLength == 0:
            self.population = [None] * populationSize
        else:
            # Initialize the population as an array of individuals
            self.population = [None] * populationSize
            for individualCount in range(populationSize):
                # Create an individual, initializing its chromosome to the given length
                individual = Individual(chromosomeLength)
                self.population[individualCount] = individual

    ''' Get individuals from the population '''

    def getIndividuals(self):
        return self.population

    ''' Find an individual in the population by its fitness '''

    def getFittest(self, offset):

        # Order population by fitness
        self.population.sort(key=lambda x: x.getFitness(), reverse=True)

        # Return the fittest individual
        return self.population[offset]

    ''' Set population's group fitness '''

    def setPopulationFitness(self, fitness):
        self.populationFitness = fitness

    ''' Get population's group fitness '''

    def getPopulationFitness(self):
        return self.populationFitness

    ''' Get population's size '''

    def size(self):
        return len(self.population)

    ''' Set individual at offset '''

    def setIndividual(self, offset, individual):
        self.population[offset] = individual
        return individual

    ''' Get individual at offset '''

    def getIndividual(self, offset):
        return self.population[offset]

    ''' Shuffles the population in-place '''

    def shuffle(self):
        random.shuffle(self.population)
