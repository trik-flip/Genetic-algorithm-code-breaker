""""""
from Cryptic import decrypt
from Scanner import Scanner
from random import choice, random


class Worker:
    """a simple worker which will try to crack a code

    Attributes
    ----------
    fitness
    key
    scanner
    text

    Methods
    -------
    run
    """

    def __init__(self, key, encrypted_text, scanner=Scanner()) -> None:
        self.key = key
        self.scanner: Scanner = scanner
        self.run(encrypted_text, decrypt)

    def run(self, encrypted_text, decryption_function):
        """"""
        self.text = decryption_function(self.key, encrypted_text)
        self.fitness = self.scanner.check(self.text)


class Generation:
    """Creating new generations of workers made easy!

    Attributes
    ----------
    encrypted_text: str
    fitness: int
    found: bool
    generation: int
    genes: list of characters
    pop_size: int
    royals: int
    same: int
    scanner: Scanner

    Methods
    -------
    create_next_gen
    mate
    mutate
    sort
    start
    """

    def __init__(self, pop_size: int, genes: list,
                 encrypted_text: str, royals: int = 1) -> None:
        self.encrypted_text = encrypted_text
        self.genes = genes
        self.pop_size = pop_size
        self.royals = royals
        self.fitness = 0
        self.found = False
        self.generation = 1
        self.population = []
        self.same = 0
        self.scanner = Scanner()

    def create_next_gen(self) -> None:
        """"""
        next_gen = []
        self.sort()
        royals = (self.royals*self.pop_size)//100
        next_gen.extend(self.population[:royals])

        offspring = ((100-self.royals)*self.pop_size)//100
        for _ in range(offspring):
            parent1 = choice(self.population[:50])
            parent2 = choice(self.population[:50])
            child = self.mate(parent1, parent2)
            next_gen.append(child)
        self.population = next_gen

        print("Generation: {}\tKey: {}\tFitness: {}".
              format(self.generation,
                     "".join(self.population[0].key),
                     self.population[0].fitness))
        self.generation += 1
        if self.fitness == self.population[0].fitness:
            self.same += 1
        else:
            self.fitness = self.population[0].fitness
            self.key = self.population[0].key
            self.same = 0
        if self.same > 4:
            self.found = True

    def mate(self, parent1: Worker, parent2: Worker) -> Worker:
        """"""
        new_string = []
        for genes_parent1, genes_parent2 in zip(parent1.key, parent2.key):
            change = random()
            if change < .45:
                new_string.append(genes_parent1)
            elif change < .90:
                new_string.append(genes_parent2)
            else:
                new_string.append(self.mutate())
        return Worker(new_string, self.encrypted_text, self.scanner)

    def mutate(self) -> str:
        """"""
        return choice(self.genes)

    def sort(self) -> None:
        """"""
        self.population = sorted(
            self.population, key=lambda x: x.fitness, reverse=True)

    def start(self, size: int) -> str:
        """"""
        for _ in range(self.pop_size):
            self.population.append(
                Worker("".join([self.mutate() for _ in range(size)]),
                       self.encrypted_text, self.scanner))
        return self.run()

    def run(self) -> str:
        while not self.found:
            self.create_next_gen()
        return self.population[0].key
