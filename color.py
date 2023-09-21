import csv
import unittest
import datetime
import random


def loadData(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = {row[0]: row[1].split(',') for row in reader if row}
    return data


data = loadData('states.txt')
print(data)


class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


def mutate(genes, geneset):
    index = random.randrange(0, len(genes))
    newGene, alternate = random.sample(geneset, 2)
    genes[index] = alternate if newGene == genes[index] else newGene


def crossover(parent1, parent2):
    if random.randint(0, 1) == 0:
        return parent1
    childGenes = parent1.Genes[:]
    start, stop = sorted(random.sample(range(len(parent1.Genes)), 2))
    childGenes[start:stop] = parent2.Genes[start:stop]
    return Chromosome(childGenes, 0)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    display(bestParent)
    if bestParent.Fitness >= optimalFitness:
        return bestParent
    while True:
        child = mutate(bestParent, geneSet, get_fitness)
        if child.Fitness > bestParent.Fitness:
            display(child)
            if child.Fitness >= optimalFitness:
                return child
            bestParent = child


def _generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def mutate(genes, geneset):
    index = random.randrange(0, len(genes))
    newGene, = random.sample(
        [gene for gene in geneset if gene != genes[index]], 1)
    genes[index] = newGene


def build_rules(items):
    rules = {}

    for state, adjacent in items.items():
        for neighbor in adjacent:
            if neighbor == '':
                continue
            rule = Rule(state, neighbor)

            if rule in rules:
                rules[rule] += 1
            else:
                rules[rule] = 1

    for k, v in rules.items():
        if v != 2:
            print("rule {} is not bidirectional".format(k))

    return rules.keys()


class Rule:

    def __init__(self, node, adjacent):
        if node < adjacent:
            node, adjacent = adjacent, node

        self.node = node
        self.adjacent = adjacent

    def __eq__(self, other):
        return self.node == other.node and self.adjacent == other.adjacent

    def __hash__(self):
        return hash(self.node) * 397 ^ hash(self.adjacent)

    def __str__(self):
        return self.node + " -> " + self.adjacent

    def isValid(self, genes, stateIndexLookUp):
        indexA = stateIndexLookUp[self.node]
        indexB = stateIndexLookUp[self.adjacent]
        return genes[indexA] != genes[indexB]


class GraphColoringTests(unittest.TestCase):
    def test(self):
        states = loadData('states.txt')
        rules = build_rules(states)
        optimalValue = len(rules)
        stateIndexLookUp = {key: index for index,
                            key in enumerate(sorted(states))}
        colors = ["Orange", "Yellow", "Green", "Blue"]
        colorLookUp = {color[0]: color for color in colors}
        geneset = list(colorLookUp.keys())
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes, rules, stateIndexLookUp)

        best = get_best(fnGetFitness, len(states),
                        optimalValue, geneset, fnDisplay)

        self.assertTrue(not optimalValue <= best.Fitness)

        keys = sorted(states.keys())
        for index in range(len(states)):
            print(keys[index] + " is " + colorLookUp[best.Genes[index]])


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(
        ''.join(map(str, candidate.Genes)),
        candidate.Fitness,
        str(timeDiff)))


def get_fitness(genes, rules, stateIndexLookUp):
    rulesThatPass = sum(
        1 for rule in rules if rule.isValid(genes, stateIndexLookUp))
    return rulesThatPass


if __name__ == '__main__':
    unittest.main()
