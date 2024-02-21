import random


SMALL_DATA = "data/newsmallfaultmatrix.txt"
BIG_DATA = "data/newbigfaultmatrix.txt"


def read_data(file_path):
    """
    Read the contents of the file and extract test case and fault information.
    """

    test_cases = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip().split(",")
            faults = [int(x) for x in "".join(line[1:])]
            test_cases.append((line[0], faults))
    return test_cases


def generate_permutations(population, num_permutations=500):
    """
    Returns a list of random permutations of a solution.
    population: solution
    num_permutations: number of random permutations of solution to be generated.
    """

    permutations = []
    for _ in range(num_permutations):
        p = population.copy()
        random.shuffle(p)
        permutations.append(p)
    return permutations


def fitness(test):
    """
    Calculates the fitness score of a test using the APFD.
    """

    num_rows = len(test)
    num_columns = len(test[0])
    total_elements = num_rows * num_columns
    first_test_pont = []

    for i in range(num_columns):
        for j in range(num_rows):
            if test[j][i] == 1:
                first_test_pont.append(j + 1)
                break

    apfd = 1 - (sum(first_test_pont) / total_elements) + (1 / (2 * num_rows))
    return apfd


def tournament_selection(populations, k=2, num_parents=2, probability=False):
    """
    Returns successful solutions from a population after a tournament selection,
    num_parents: number of parents to be selected.
    k: number of individuals to be selected for a tournament.
    probability: controls the choice of the fitter individual when set to True.
    Selection is without replacement, however, solution selection is with replacement.
    """

    if len(populations) < k:
        raise ValueError(
            "Length of k must not be greater than the length of the population."
        )

    parents = []
    for _ in range(num_parents):
        if not probability:
            selected_population = random.sample(populations, k)
            parents.append(max(selected_population, key=lambda x: x[1]))
        else:
            populations_copy = populations.copy()
            selected_population = []
            total_fitness = [fitness([p[1] for p in pop]) for pop in populations_copy]
            for _ in range(k):
                rand = random.uniform(0, sum(total_fitness))
                cumulative = 0
                for i, population in enumerate(populations_copy):
                    cumulative += total_fitness[i]
                    if cumulative >= rand:
                        selected_population.append(population)
                        populations_copy.remove(population)
                        break
            parents.append(max(selected_population, key=lambda x: x[1]))
    return parents


def get_points(total_elements, num_points):
    points = []
    if total_elements % 2 == 0:
        m = 1
    else:
        m = 0

    num_segments = round((total_elements - m) // num_points)
    x = 0
    for i in range(num_points):
        a = x + 1
        b = num_segments * (i + 1) + m
        if b == total_elements:
            b -= 1
        points.append(random.randrange(a, b))
        x = b
    return points


def fill_child(total_elements, num_points, parent, points):
    child = [0] * total_elements
    x = 0
    y = 1
    if num_points % 2 == 0:
        for k in range(num_points // 2):
            for i in range(points[x], points[y] + 1):
                child[i] = parent[i]
            x += 2
            y += 2
    else:
        z = True
        while z:
            if y < num_points:
                for i in range(points[x], points[y] + 1):
                    child[i] = parent[i]
                x += 2
                y += 2
            else:
                for i in range(points[x], total_elements):
                    child[i] = parent[i]
                z = False
    return child


def crossover(parent1, parent2, num_points=2, probability=0.7):
    """
    Performs a crossover for an ordered TCP solution.
    num_points: number of crossover points,
    probability: crossover probability
    """

    if num_points > (len(parent1) - 1) // 2 or num_points < 2:
        raise ValueError(
            f"Number of points must be an integer between 2 and {(len(parent1)-1)//2}"
        )
    elif not isinstance(num_points, int):
        raise TypeError(
            f"Number of points must be an integer between 2 and {(len(parent1)-1)//2}"
        )

    if probability > random.random():
        total_elements = len(parent1)
        points = get_points(total_elements, num_points)
        child1 = fill_child(total_elements, num_points, parent1, points)
        child2 = fill_child(total_elements, num_points, parent2, points)

        # Copying the remaining elements from parents and avoiding duplicates.
        parent2_rotated = parent2[points[0] :] + parent2[: points[0]]
        x = 0
        for i in range(total_elements):
            if child1[i] == 0:
                while parent2_rotated[x] in child1:
                    x += 1
                child1[i] = parent2_rotated[x]

        parent1_rotated = parent1[points[0] :] + parent1[: points[0]]
        x = 0
        for i in range(total_elements):
            if child2[i] == 0:
                while parent1_rotated[x] in child2:
                    x += 1
                child2[i] = parent1_rotated[x]
        return child1, child2

    else:
        return parent1, parent2


def mutate(c1, c2, rate=0.01, endpoint=3, operation="swap"):
    """
    Performs mutation on two solutions.
    Provide an endpoint if using scramble or inversion operation.
    """

    if rate > random.random():
        if operation == "swap":
            index1, index2 = random.sample(range(len(c1)), 2)
            c1[index1], c1[index2] = c1[index2], c1[index1]
            c2[index1], c2[index2] = c2[index2], c2[index1]
            return c1, c2

        elif operation == "scramble" or operation == "inversion":
            if endpoint >= len(c1) - 2 or endpoint < 3:
                raise ValueError(
                    f"Length of children must be greater than 5, and value of endpoint must be an integer between 3 and {len(c1)-2 if len(c1) > 5 else 'an int greater than 5'}."
                )

            start = random.randrange(1, len(c1) - endpoint)
            end = start + endpoint
            subset = c1[start:end]
            random.shuffle(subset)
            c1[start:end] = subset

            start = random.randrange(1, len(c2) - endpoint)
            end = start + endpoint
            subset = c2[start:end]
            random.shuffle(subset)
            c2[start:end] = subset

            return c1, c2

        else:
            raise ValueError(
                "Invalid mutation operation. Choose from 'swap', 'scramble', or 'inversion'."
            )

    else:
        return c1, c2


def neighbours(solution):
    n = len(solution)
    n = n * (n - 1)
    neighbors = []
    for _ in range(n):
        sol = solution.copy()
        i1, i2 = random.sample(range(len(sol)), 2)
        sol[i1], sol[i2] = sol[i2], sol[i1]
        neighbors.append(sol)

    return neighbors


def run_ga(
    data: str,
    num_runs: int,
    population_size: int,
    num_iterations: int,
    mutation_rate: float,
    mutation_operation: str,
    crossover_points: int,
    crossover_probability: float,
    k_selection: int,
    end_point: int = 3,
    print_runtime=False,
) -> tuple[list, list, list]:
    """
    Runs the Genetic Algorithm.

    Provide an endpoint if using scramble or inversion operation for mutation.
    """

    tests = read_data(data)
    ga_iterations = []
    ga_fitness = []
    test_list = []
    for i in range(num_runs):
        npop = population_size
        it = num_iterations
        generation = 1
        best_generation = 0
        best_fitness = 0
        best_test_permutation = None

        # Initializing
        populations = generate_permutations(tests, num_permutations=npop)

        # Evaluation
        for _ in range(it):
            for pop in populations:
                test_fitness = fitness([p[1] for p in pop])
                if test_fitness > best_fitness:
                    best_fitness = test_fitness
                    best_test_permutation = [p[0] for p in pop]
                    best_generation = generation

            pc = []

            # Main loop (selection, crossover, mutation)
            for _ in range(npop // 2):
                p1, p2 = tournament_selection(populations, k=k_selection)
                c1, c2 = crossover(
                    p1,
                    p2,
                    num_points=crossover_points,
                    probability=crossover_probability,
                )
                c1, c2 = mutate(
                    c1,
                    c2,
                    rate=mutation_rate,
                    endpoint=end_point,
                    operation=mutation_operation,
                )
                pc.append(c1)
                pc.append(c2)
            populations = pc
            generation += 1

        ga_iterations.append(best_generation)
        ga_fitness.append(best_fitness)
        test_list.append(best_test_permutation)
        if print_runtime:
            print(f"run {i+1} completed with best fitness of {best_fitness} ")

    return ga_iterations, ga_fitness, test_list


def run_hill_climbing(data, num_runs, num_iterations, print_runtime=False):
    """
    Runs the Hill Climbing Algorithm.
    """

    tests = read_data(data)
    hill_iterations = []
    hill_fitness = []
    test_list = []
    for i in range(num_runs):
        generation = 1
        it = num_iterations
        best_generation = 0
        best_solution = None
        best_fitness = 0

        # Initial solution
        solutions = generate_permutations(tests, num_permutations=1)

        for _ in range(it):

            # Evaluation
            for sol in solutions:
                fit = fitness([s[1] for s in sol])
                if fit > best_fitness:
                    best_fitness = fit
                    best_solution = sol
                    best_generation = generation
                    break

            # Neighborhood Function
            solutions = neighbours(best_solution)

            generation += 1
        hill_iterations.append(best_generation)
        hill_fitness.append(best_fitness)
        test_list.append([s[0] for s in best_solution])
        if print_runtime:
            print(f"run {i+1} completed with best fitness of {best_fitness} ")

    return hill_iterations, hill_fitness, test_list


def rand_baseline(data, num_runs):
    """
    Runs the Random Baseline Search Algorithm.
    """

    tests = read_data(data)
    rand_solution = []
    rand_fitness = []
    for _ in range(num_runs):
        solution = generate_permutations(tests, num_permutations=1)
        fit = fitness([s[1] for s in solution[0]])

        rand_solution.append(solution)
        rand_fitness.append(fit)

    return rand_solution, rand_fitness
