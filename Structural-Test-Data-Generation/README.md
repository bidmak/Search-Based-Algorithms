# Structural Test Data Generation

This project is based around the problem of using Genetic Algorithm and Random Search to automatically generate test data to achieve a level of coverage of a program under test.

The program under test is an implementation of Cipolla's algorithm, adapted from [rosettacode.org](https://rosettacode.org/wiki/Cipolla's_algorithm) and modified for compatibility with Python 3. The primary goal is to explore the program's behavior and achieve comprehensive coverage, particularly focusing on statement coverage.

To effectively assess the functionality of the program under test, it is essential to insert pieces of code to gather feedback on executed portions. For this project, I've incorporated 'output', 'add_output', and 'k' into the program (program.py) to facilitate feedback collection.

## Results

**GENETIC ALGORITHM**

- Branch 1T, Test Data: [553818, 553818], Fitness: 0
- Branch 1F, Test Data: [620975, 85856], Fitness: 0
- Branch 2T, Test Data: [59036, 410420], Fitness: 0
- Branch 2F, Test Data: [982065, 501409], Fitness: 0
- Branch 3T, Test Data: [107019, 106187], Fitness: 0
- Branch 3F, Test Data: [124009, 642406], Fitness: 0
- Branch 4T, Test Data: [256292, 9], Fitness: 0.09782659673439364
- Branch 4F, Test Data: [915633, 999274], Fitness: 0

**Random Search**

- Branch 1T, Test Data: [534380, 4380], Fitness: 0.11213940829440916
- Branch 1F, Test Data: [808151, 972545], Fitness: 0
- Branch 2T, Test Data: [514266, 372175], Fitness: 0
- Branch 2F, Test Data: [951061, 331846], Fitness: 0
- Branch 3T, Test Data: [343610, 841307], Fitness: 0
- Branch 3F, Test Data: [426791, 958574], Fitness: 0
- Branch 4T, Test Data: [497265, 32441], Fitness: 0.9999999175312114
- Branch 4F, Test Data: [537897, 646766], Fitness: 0
