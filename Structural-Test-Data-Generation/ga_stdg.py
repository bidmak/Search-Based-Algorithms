import random
from program.program import cipolla


# Representation of the test cases. We limit to 10**6 for domain
def generate_data():
    input_domain = [(1, 10**6) for _ in range(2)]
    return [random.randint(var[0], var[1]) for var in input_domain]


# Get and add an output of a process flow without duplicates.
def add_output(output, tuple):
    for out in output:
        if out[0] == tuple[0]:
            output.remove(out)
            break
    output.add(tuple)


def normalise(d):
    return 1 - 1.001**-d


def is_target(target, output):
    out_tars = [tar[0] for tar in output]
    return target in out_tars


# Fitness function contructed to calculate fitness by adding approach level branch distace.
def fitness(target, output_data):
    get_bd = {}
    branch_1 = ["branch 2T", "branch 2F"]
    branch_2 = ["branch 3T", "branch 3F"]
    branch_3 = ["branch 4T", "branch 4F"]
    target_names = []

    for out in output_data:
        get_bd[out[0]] = out[1]
        target_names.append(out[0])

    if target == "branch 1T":
        return 0 + normalise(get_bd["branch 1F"])
    elif target == "branch 1F":
        return 0 + normalise(get_bd["branch 1T"])
    elif target in branch_1:
        if any(b in target_names for b in branch_1):
            return (
                0 + normalise(get_bd[target[0:-1] + "F"])
                if target[-1] == "T"
                else 0 + normalise(get_bd[target[0:-1] + "T"])
            )
        else:
            return 1 + normalise(get_bd["branch 1T"])
    elif target in branch_2:
        if any(b in target_names for b in branch_2):
            return (
                0 + normalise(get_bd[target[0:-1] + "F"])
                if target[-1] == "T"
                else 0 + normalise(get_bd[target[0:-1] + "T"])
            )
        elif "branch 2T" in target_names:
            return 1 + normalise(get_bd["branch 2T"])
        else:
            return 2 + normalise(get_bd["branch 1T"])
    elif target in branch_3:
        if any(b in target_names for b in branch_3):
            return (
                0 + normalise(get_bd[target[0:-1] + "F"])
                if target[-1] == "T"
                else 0 + normalise(get_bd[target[0:-1] + "T"])
            )
        elif "branch 3T" in target_names:
            return 1 + normalise(get_bd["branch 3T"])
        elif "branch 2T" in target_names:
            return 2 + normalise(get_bd["branch 2T"])
        elif "branch 1T" in target_names:
            return 3 + normalise(get_bd["branch 1T"])


# Selection of fitter parents
def select_parents(population, weights):
    return random.choices(population, k=2, weights=weights)


# Single point crossover
def crossover(parent1, parent2):
    p1 = [str(parent1[0]), str(parent1[1])]
    p2 = [str(parent2[0]), str(parent2[1])]
    n1 = random.randint(0, min(len(p1[0]), len(p2[0])) - 1)
    n2 = random.randint(0, min(len(p1[1]), len(p2[1])) - 1)
    child1 = [p1[0][:n1] + p2[0][n1:], p1[1][:n2] + p2[1][n2:]]
    child2 = [p2[0][:n1] + p1[0][n1:], p2[1][:n2] + p1[1][n2:]]
    return [int(child1[0]), int(child1[1])], [int(child2[0]), int(child2[1])]


# Mutation: induces small random changes to chromosome.
def mutate(chromosome, rate=0.01):
    if random.random() < rate:
        mutant1 = []
        mutant2 = []
        g1, g2 = chromosome
        gene1 = str(g1)
        gene2 = str(g2)
        i1 = random.randint(0, len(gene1) - 1)
        i2 = random.randint(0, len(gene2) - 1)
        for i in range(len(gene1)):
            if i == i1:
                mutant1.append(str(random.randint(1, 9)))
            else:
                mutant1.append(gene1[i])
        for i in range(len(gene2)):
            if i == i2:
                mutant2.append(str(random.randint(1, 9)))
            else:
                mutant2.append(gene2[i])
        chromosome = [int("".join(mutant1)), int("".join(mutant2))]
    return chromosome


# Run Genetic Algorithm: Evaluation, crossover, and mutation.
def run_ga(size, mutation_rate, iterations, targets):
    results = []
    for target in targets:
        flag = False
        datas = [generate_data() for _ in range(size)]
        gen = 1
        best_data = None
        best_fitnes = float("inf")
        data_fits = []
        for i in range(iterations):

            # Evaluating the fitness of each individual in the population
            for data in datas:
                output = set()
                n, p = data
                cipolla(n, p, output, add_output)
                if is_target(target, output):
                    results.append(
                        (
                            f"Runs: {i+1}, Target: {target}, Test Data: {data}, Fitness: {0}"
                        )
                    )
                    flag = True
                    break
                else:
                    fit = fitness(target, output)
                    data_fits.append(fit)
                    if fit < best_fitnes:
                        best_fitnes = fit
                        best_data = data
                        gen += 1
            if flag:
                break

            child_datas = []
            for _ in range(size // 2):
                # Patents selection for crossover
                parents = select_parents(datas, data_fits)

                # Crossover to create new offspring
                offspring1, offspring2 = crossover(parents[0], parents[1])

                # Mutation of the offspring and adding to child population
                child_datas.append(mutate(offspring1, mutation_rate))
                child_datas.append(mutate(offspring2, mutation_rate))

            datas = child_datas
            data_fits = []

        if flag:
            continue
        results.append(
            (
                f"Runs: {gen}, Target: {target}, Test Data: {best_data}, Fitness: {best_fitnes}"
            )
        )
    return results


# Program parameters
POPULATION_SIZE = 2000
MUTATION_RATE = 0.1
GENERATIONS = 20

# Target structure.
TARGETS = [
    "branch 1T",
    "branch 1F",
    "branch 2T",
    "branch 2F",
    "branch 3T",
    "branch 3F",
    "branch 4T",
    "branch 4F",
]


if __name__ == "__main__":

    print(
        "\nExecuting GA STDG program, please wait for program to complete as this may take some time\n"
    )

    print("\n", "-" * 20, " GENETIC ALGORITHM ", "-" * 20)
    results = run_ga(POPULATION_SIZE, MUTATION_RATE, GENERATIONS, TARGETS)
    for result in results:
        print(result)

    print(f"----------------- End of STDG Program -----------------\n")

    """
    # Results from experiment saved to a file for further analysis.
    file_path = "results/ga_stdg_output.txt"
    with open(file_path, "w") as file:
        for result in results:
            file.write(result+"\n")
    """
