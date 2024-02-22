from tcp_module import rand_baseline, BIG_DATA, SMALL_DATA

NUM_RUNS = 10

solution, fitness = rand_baseline(BIG_DATA, NUM_RUNS)

run = 1
for fit in fitness:
    print(f"run: {run}, fitness: {fit}")
    run += 1
