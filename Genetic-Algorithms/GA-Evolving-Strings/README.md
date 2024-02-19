# Evolving Strings with Genetic Algorithm

This project aims to implement a simple genetic algorithm (GA) to evolve a given target string: "Hi. My name is Samuel Makanjuola, and this is a simple demonstration of Genetic Algorithm. Thanks!!!!". The target string consists of 100 characters, making it a challenging search-based problem. Feel free to make appropriate changes as needed, such as modifying the target string or adjusting the GA parameters, to suit your requirements.

## Tasks

1. **GA Implementation**: The GA is designed to evolve strings iteratively, aiming to match the target string. It operates by generating an initial population of random strings and then iteratively selecting parents, performing crossover and mutation operations, and evaluating fitness until the target string is achieved.

2. **Performance Evaluation**: The GA's performance is compared against hill-climbing and random search algorithms. This comparison helps assess the GA's effectiveness in finding the target string within a reasonable time frame.

## Implementation

The GA is implemented in Python and consists of the following components:

- `ga_es.py`: Main script containing the GA implementation.
- `fitness(target, solution)`: Function to calculate the fitness score of a solution.
- `generate_solution(n)`: Function to generate a random initial solution.
- `select_parents(populations, fits, k)`: Function to select parents from the population.
- `crossover(p1, p2)`: Function to perform uniform crossover operation.
- `mutate_solution(solution, rate)`: Function to mutate a solution.
- `TARGET`: The target string to be evolved.
- `NUM_POP`: Number of individuals in the population.
- `MUTATION_RATE`: Probability rate for mutation.
- `K_SELECTION`: Number of individuals selected in tournament selection.

## Results

After 51 iterations, the GA successfully evolved the target string:

- **Solution**: "Hi. My name is Samuel Makanjuola, and this is a simple demonstration of Genetic Algorithm. Thanks!!!!"
- **Fitness Score**: 100/100
- **Time Taken**: 60.89 seconds

Performance Evaluation between the algorithms will be discussed here -> [Evolving Strings Evaluation](https://github.com/bidmak/Search-Based-Software-Engineering/blob/main/README.md#evolving-strings-performance-evaluation)

### Conclusion

The GA demonstrates its capability to efficiently evolve complex strings by leveraging genetic operators such as crossover and mutation. Its ability to explore the solution space and gradually improve fitness highlights its effectiveness in solving challenging search-based problems.

## How to Run

To run the genetic algorithm implementation:

1. Ensure you have Python installed on your system.
2. Clone the repository: git clone https://github.com/bidmak/Search-Based-Software-Engineering.git
3. Navigate to the project directory: cd Search-Based-Software-Engineering
4. Run the Python script: python genetic_algorithm.py
5. Monitor the output to observe the evolution of the target string by the GA
