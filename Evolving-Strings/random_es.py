from ga_es import generate_solution, fitness, TARGET, LEN_TAR
import time


i = 1
best_score = 0

print("----- Random Search - Evolving Strings -----")
start_time = time.time()

while best_score < LEN_TAR:

    best = generate_solution(LEN_TAR)
    bestscore = fitness(target=TARGET, solution=best)
    if bestscore > best_score:
        best_score = bestscore
        print(f"Iteration: {i}, Fitness score: {best_score} of {LEN_TAR}")
    if bestscore == LEN_TAR:
        break

    # setting a 2 minutes time limit.
    if time.time() - start_time >= 120:
        print(f"\n-----------  Random Search Solution Results -----------\n")
        print(
            f" Terminated at iteration: {i}, at {(time.time() - start_time):.2f} seconds"
        )
        print(f"Best solution: {best},")
        print(f"\n------------ End of Random Search Operation ------------\n")
        break
    i += 1
