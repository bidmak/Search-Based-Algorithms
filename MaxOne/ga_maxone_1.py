from random import choices, randrange, randint, random
import random as rd


def value(x):
    val = "".join(map(str, x))
    return int(val, 2)


# Genetic representation of a solution
def generate(target=5):
    return [rd.choice([0, 1]) for _ in range(target)]


# Defining the fitness function
def fitness(x):
    return round((((-x) ** 2 / 10) * (3 * x)), 2)


# Selecting parent pairs
def selection(pops, weights=True):
    return choices(
        population=pops,
        weights=[fitness(value(pop)) for pop in pops] if weights == True else None,
        k=2,
    )


# Crossover function
def cross(p1, p2):
    p = randint(1, (len(p1) - 1))
    child1 = p1[0:p] + p2[p:]
    child2 = p2[0:p] + p1[p:]
    return child1, child2


# mutatioin
def mutate(x, rate=1, probability=0.01):
    for _ in range(rate):
        index = randrange(len(x))

        x[index] = x[index] if random() > probability else abs(x[index] - 1)
    return x


# GA parameters
npop = 4
generation = 1
nprob = 5

best_fitness = 0
best_solution = None
best_value = None

if __name__ == "__main__":
    target = fitness(31)

    # Initiallizing population
    pop = [generate() for _ in range(npop)]
    pop_value = [value(p) for p in pop]
    pop_fitness = [fitness(p) for p in pop_value]

    # main loop
    while best_fitness < target:

        for i in range(npop):
            if pop_fitness[i] > best_fitness:
                best_fitness = pop_fitness[i]
                best_solution = pop[i]
                best_value = pop_value[i]
                print(
                    f"generation: {generation}, solution: {best_solution}, value: {best_value}, fitness: {best_fitness}"
                )
        if best_fitness == target:
            break

        popc = []
        popc_value = []
        popc_fitness = []

        for j in range(npop // 2):
            p1, p2 = selection(pop)
            child1, child2 = cross(p1, p2)
            child1 = mutate(child1)

            popc.append(child1)
            popc_value.append(value(child1))
            popc_fitness.append(fitness(value(child1)))

            popc.append(child2)
            popc_value.append(value(child2))
            popc_fitness.append(fitness(value(child2)))

        pop = popc
        pop_value = popc_value
        pop_fitness = popc_fitness
        generation += 1
