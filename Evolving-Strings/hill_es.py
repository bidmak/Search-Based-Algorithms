from ga_es import mutate_solution, generate_solution, fitness, TARGET, LEN_TAR
import time


def get_neighbours(solution, n=1000):
    neighbours = list()
    for _ in range(n):
        neighbours.append(mutate_solution(solution, rate=0.05))
    return neighbours


generation = 0
best_solution = generate_solution(LEN_TAR)
best_score = fitness(target=TARGET, solution=best_solution)

print("----- Hill Climbing Algorithm On Evolving Strings -----")
start_time = time.time()

if best_score == LEN_TAR:
    print(f"Iteration: {generation}, {best_solution}, score: {best_score}/{LEN_TAR}")

while best_score < LEN_TAR:
    generation += 1
    neighbours = get_neighbours(best_solution)
    for neighbour in neighbours:
        neighbour_score = fitness(target=TARGET, solution=neighbour)

        # First choice hill-climbing variant
        if neighbour_score > best_score:
            best_solution = neighbour
            best_score = neighbour_score
            print(f"Iteration: {generation}, Fitness score: {best_score} of {LEN_TAR}")
            break

    if best_score == LEN_TAR:
        print(f"\n-----------  Hill Climbing Solution Results -----------\n")

        print(
            f"Solution: {best_solution} \nFitness score: {best_score}/{LEN_TAR} \nIteration: {generation}"
        )
        break

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

print(f"\n------------ End of Hill Climbing Operation ------------\n")
