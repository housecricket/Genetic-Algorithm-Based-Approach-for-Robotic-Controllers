import random
class Individual:

    ''' Initializes individual with specific chromosome '''
    def __init__(self, chromosome):
        self.fitness = -1
        self.chromosome = chromosome

    ''' Initializes random individual '''
    def __init__(self, chromosomeLength):
        self.fitness = -1
        self.chromosome = [None] * chromosomeLength
        for gene in range(chromosomeLength):
            if (0.5 < random.random()):
                self.setGene(gene, 1)
            else:
                self.setGene(gene, 0)

    ''' Gets individual's chromosome '''
    def getChromosome(self):
        return self.chromosome

    ''' Gets individual's chromosome length '''
    def getChromosomeLength(self):
        return len(self.chromosome)

    ''' Set gene at offset '''
    def setGene(self, offset, gene):
        self.chromosome[offset] = gene

    ''' Get gene at offset '''
    def getGene(self, offset):
        return self.chromosome[offset]

    ''' Store individual's fitness '''
    def setFitness(self, fitness):
        self.fitness = fitness

    ''' Gets individual's fitness '''
    def getFitness(self):
        return self.fitness

    ''' Display the chromosome as a string '''
    def toString(self):
        output = ''
        for gene in range(len(self.chromosome)):
            output += str(self.chromosome[gene])
        return output