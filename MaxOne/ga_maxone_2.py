from random import choices, randrange, randint, random
from ga_maxone_1 import *


def binary(x):
    return [int(bit) for bit in "".join(format(byte, "08b") for byte in x.encode())]


def fitness_bin(solution):
    return sum(solution)


def pselection(pops, weights=True):
    return choices(
        population=pops,
        weights=[fitness_bin(pop) for pop in pops] if weights == True else None,
        k=2,
    )


input = "This is CS547!"
target_bytes = binary(input)
target = len(target_bytes)
npop = 1000

best_sol = None
best_fitness = fitness_bin(target_bytes)

print(f"Target fitness: {target}")
print(f"String: {input}, string_binary: {target_bytes} with fitness: {best_fitness}")
print("*" * 20, "MaxOnes", "*" * 20)

# Initiallizing population
pop = []
for i in range(npop):
    pop.append(generate(target=target))


# main loop
while best_fitness < target:

    for i in range(npop):
        fit = fitness_bin(pop[i])
        if fit > best_fitness:
            best_sol = pop[i]
            best_fitness = fit
            print(
                f"generation: {generation}, solution: {best_sol}, fitness: {best_fitness}"
            )
    if best_fitness == target:
        break

    pc = []
    for i in range(npop // 2):
        p1, p2 = pselection(pop)
        child1, child2 = cross(p1, p2)
        child1 = mutate(child1, probability=0.03)
        child2 = mutate(child2, probability=0.03)

        pc.append(child1)
        pc.append(child2)

    pop = pc
    generation += 1

print("*" * 21, "Done", "*" * 21)
