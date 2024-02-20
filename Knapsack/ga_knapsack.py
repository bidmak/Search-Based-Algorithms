from ypstruct import structure
from random import choices, randint, randrange, random
import numpy as np


# Problem to be solved
problemList = [
    {"item": "Pocketknife", "points": 10, "weight": 1},
    {"item": "Beans", "points": 17, "weight": 5},
    {"item": "Potatoes", "points": 15, "weight": 10},
    {"item": "Water", "points": 5, "weight": 1},
    {"item": "Sleeping Bag", "points": 30, "weight": 7},
    {"item": "Rope", "points": 10, "weight": 5},
    {"item": "Compass", "points": 30, "weight": 1},
]

# GA parameters
npop = 20
gen = 1
solution = structure()
solution.solution = [1, 1, 0, 1, 1, 1, 1]
solution.solution_points = 102


# Problem parameters
nprob = len(problemList)
maxWeight = 20


# Problem structure
problem = structure()
problem.item = None
problem.points = None
problem.weight = None

# Inserting the problems in the structure
problems = problem.repeat(nprob)
for i in range(nprob):
    problems[i].item = problemList[i]["item"]
    problems[i].points = problemList[i]["points"]
    problems[i].weight = problemList[i]["weight"]


def get_items(solution):
    s = []
    for i in range(nprob):
        if solution[i] == 1:
            s.append(problemList[i]["item"])
    return s


# Genetic representation of a solution
def genetic():
    return [np.random.choice([0, 1]) for _ in range(nprob)]


# Defining the fitness function
def fitness(x, maxWeight=maxWeight):
    points = 0
    weight = 0

    for i in range(len(x)):
        if x[i] == 1:
            points += problems[i].points
            weight += problems[i].weight
    if weight > maxWeight:
        return 0

    return points


# Selecting parent pairs
def selection(pops):
    return choices(population=pops, weights=[x.points for x in pops], k=2)


# Crossover function
def cross(p1, p2):
    child1 = p1.deepcopy()
    child2 = p2.deepcopy()
    p = randint(1, (nprob - 1))
    child1.solution = child1.solution[0:p] + child2.solution[p:]
    child2.solution = child2.solution[0:p] + child1.solution[p:]
    return child1, child2


# mutatioin
def mutation(x, rate=1, probability=0.5):
    for _ in range(rate):
        index = randrange(len(x))

        x[index] = x[index] if random() > probability else abs(x[index] - 1)
    return x


# empty templete
empty = structure()
empty.solution = None
empty.points = None


# Best solution
best_solution = empty.deepcopy()
best_solution.points = 0


# Initiallizing population
pop = empty.repeat(npop)
for i in range(npop):
    pop[i].solution = genetic()
    pop[i].points = fitness(pop[i].solution)


print(f"\n{'*' * 15} KNAPSACK {'*' * 15}")

# main loop
while best_solution.points < solution.solution_points:

    # Evaluation
    for i in range(npop):
        if pop[i].points > best_solution.points:
            best_solution = pop[i].deepcopy()
            print(f"Iterations: {gen}, best solution points: {best_solution.points}")

    if best_solution.points == solution.solution_points:
        break

    popc = []

    # select parents
    for _ in range(npop // 2):
        parent1, parent2 = selection(pop)

        # perform crossover
        child1, child2 = cross(parent1, parent2)

        # perform mutation
        child1.solution = mutation(child1.solution)
        child1.points = fitness(child1.solution)
        popc.append(child1)

        child2.solution = mutation(child2.solution)
        child2.points = fitness(child2.solution)
        popc.append(child2)

    # set pop to the populations of children
    pop = popc
    gen += 1


print("*" * 40)
print(f"Max items: {', '.join(get_items(best_solution.solution))}.\n")
