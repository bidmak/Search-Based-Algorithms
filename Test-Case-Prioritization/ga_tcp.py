from tcp_module import run_ga, BIG_DATA, SMALL_DATA
import matplotlib.pyplot as plt
import statistics
import os


# File existence check
if not os.path.exists(BIG_DATA):
    raise FileNotFoundError(
        f"File [{BIG_DATA}] does not exist. Use the correct file path for the data in tcp_module."
    )


print("\n--------------- Test Case Prioritization ---------------\n")

# Initial fitness of the test suite in the dataset
print("Initial fitness of newsmallfaultmatrix dataset: 0.8969")
print(f"Initial fitness of newbigfaultmatrix dataset: 0.8908\n")

print(
    "Executing GA TCP program, please wait for program to complete as this may take some time\n"
)

GA_ITERATIONS = 80
NUM_POPULATIONS = 2000
NUM_RUNS = 10
MUTATION_RATE = 0.05
MUTATION_OPERATION = "swap"
CROSSOVER_POINTS = 3
CROSSOVER_PROB = 0.80
K_SELECTION = 3

iterations, fitness, test_list = run_ga(
    BIG_DATA,
    NUM_RUNS,
    NUM_POPULATIONS,
    GA_ITERATIONS,
    MUTATION_RATE,
    MUTATION_OPERATION,
    CROSSOVER_POINTS,
    CROSSOVER_PROB,
    K_SELECTION,
    print_runtime=True,
)

print(f"\n------------------- TCP Results -------------------\n")

run = 1
for it, fit in zip(iterations, fitness):
    print(f"run: {run}, max iteration: {it}, optimum fitness: {fit}")
    run += 1

print(f"\n----------------- End of TCP Operation -----------------\n")

"""
# Saving the test order for further analysis.
file_path = "ga_output.txt"
with open(file_path, "w") as file:
    for test in test_list:
        line = ",".join(test)
        file.write("[" + line + "]" + "\n")
"""

"""
# Boxplot to show the mean and standard deviation of the fitness
mean = statistics.mean(fitness)
std_dev = statistics.stdev(fitness)
maxi = max(fitness)


plt.boxplot(fitness)
text = f"Mean: {mean:.4f}\nStd:    {std_dev:.4f}"
plt.annotate(
    text,
    xy=(1, mean),
    xytext=(1.26, mean),
    fontsize=12,
    color="black",
    arrowprops=dict(arrowstyle="->", color="green"),
)

plt.xticks([1], ["Fitness"])
plt.title("Genetic Algorithm")
plt.grid(False)
plt.show()
"""
