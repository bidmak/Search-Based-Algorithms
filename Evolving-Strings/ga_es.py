import random as rd
from random import randint, random
import time


def randinteger():
    return randint(32, 127)


def fitness(target: str, solution: str) -> int:
    """
    Fitness function of a simple GA to evolve strings, given a target and a solution.

    param target: The given target for the GA.
    type target: str

    param solution: The evoled string from the GA.
    type solution: str

    raise ValueError: If length of target is not equal to length of solution.
    return: A number of fitness for the given solution.
    rtype: str
    """

    n = len(target)
    if n != len(solution):
        return ValueError("length of solution must be thesame as the target")

    score = 0
    for i in range(n):
        if solution[i] == target[i]:
            score += 1
    return score


# Generation of a random initial solution
def generate_solution(n: int):
    return "".join([chr(randinteger()) for _ in range(n)])


# Tournament Fitness Selection of individuals from the population.
def select_parents(populations: list[str], fits: list[int], k: int) -> tuple:
    child_1 = max(
        rd.choices(list(zip(populations, fits)), weights=fits, k=k), key=lambda x: x[1]
    )[0]
    child_2 = max(
        rd.choices(list(zip(populations, fits)), weights=fits, k=k), key=lambda x: x[1]
    )[0]
    return child_1, child_2


# Uniform crossover operation
def crossover(p1: str, p2: str) -> str:
    child = ""
    for i in range(len(p1)):
        child += rd.choice([p1[i], p2[i]])
    return child


def mutate_solution(solution: str, rate: float = 0.01) -> str:
    """
    Mutation operation - Applying small changes to a solution.

    param solution: A set of strings or characters from the GA.
    type solution: str
    param rate: The probabily rate for a solution to undergo a mutation.
    type rate: float
    return: A new mutated solution or the original solution based on the probability.
    """

    return "".join(
        [
            chr(randinteger()) if random() < rate else solution[i]
            for i in range(len(solution))
        ]
    )


# Target parameters
TARGET = "Hi. My name is Samuel Makanjuola, and this is a simple demostration of Genetic Algorithm. Thanks!!!!"
LEN_TAR = len(TARGET)

# GA parameters
NUM_POP = 2500
MUTATION_RATE = 0.03
K_SELECTION = 3

if __name__ == "__main__":
    iteration = 1
    best_fitness = 0
    best_sol = None

    # Initial populations
    populations = [generate_solution(LEN_TAR) for _ in range(NUM_POP)]

    print("----- Simple Genetic Algorithm On Evolving Strings -----")
    start_time = time.time()

    # Main GA loop
    while best_fitness < LEN_TAR:
        fits = []
        for i in range(NUM_POP):
            fit = fitness(target=TARGET, solution=populations[i])
            fits.append(fit)

            # Evaluation
            if fit > best_fitness:
                best_fitness = fit
                best_sol = populations[i]
                print(
                    f"Iteration: {iteration}, Fitness score: {best_fitness} of {LEN_TAR}"
                )

            if best_fitness == LEN_TAR:
                print(f"\n--------------- GA Solution Results ---------------\n")

                print(
                    f"Solution: {best_sol} \nFitness score: {best_fitness}/{LEN_TAR} \nIteration: {iteration}"
                )
                break

        if best_fitness == LEN_TAR:
            break

        new_populations = []
        for _ in range(NUM_POP):

            # select parents from the tournament pool
            parent1, parent2 = select_parents(populations, fits, K_SELECTION)

            # perform crossover
            offspring = crossover(parent1, parent2)

            # perform mutation on offspring
            mutant = mutate_solution(offspring, rate=0.02)

            new_populations.append(mutant)

        populations = new_populations
        iteration += 1

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    print(f"\n--------------- End of GA Operation ---------------\n")
