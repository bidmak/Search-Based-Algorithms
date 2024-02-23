from program.program import cipolla
from ga_stdg import (
    generate_data,
    add_output,
    is_target,
    fitness,
    TARGETS,
    POPULATION_SIZE,
    GENERATIONS,
)


# Run Random Search Algorith
def random_search(size, targets, iterations):
    random_results = []
    for target in targets:
        flag = False
        gen = 1
        best_data = None
        best_fitnes = float("inf")
        datas = [generate_data() for _ in range(size)]
        for i in range(iterations):
            for data in datas:
                output = set()
                n, p = data
                cipolla(n, p, output, add_output)
                if is_target(target, output):
                    random_results.append(
                        (
                            f"Runs: {i+1}, Target: {target}, Test Data: {data}, Fitness: {0}"
                        )
                    )
                    flag = True
                    break
                else:
                    fit = fitness(target, output)
                    if fit < best_fitnes:
                        best_fitnes = fit
                        best_data = data
                        gen += 1
            if flag:
                break
        if flag:
            continue
        random_results.append(
            (
                f"Runs: {gen}, Target: {target}, Test Data: {best_data}, Fitness: {best_fitnes}"
            )
        )
    return random_results


if __name__ == "__main__":

    print(
        "\nExecuting Random STDG program, please wait for program to complete as this may take some time\n"
    )

    print("\n", "-" * 20, " RANDOM SEARCH ALGORITHM ", "-" * 20)
    random_results = random_search(POPULATION_SIZE, TARGETS, GENERATIONS)

    for result in random_results:
        print(result)

    print(f"----------------- End of STDG Program -----------------\n")

    """
    # Results from random search algorithmt saved to a file for further analysis.
    file_path = "results/random_stdg_output.txt"
    with open(file_path, "w") as file:
        for result in random_results:
            file.write(result + "\n")
    """
