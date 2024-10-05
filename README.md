# Genetic Algorithm String Matching - COS470/570 Fall 2024

## Overview
This project is a genetic algorithm designed to match a target string. The algorithm generates an initial population of random ASCII strings and evolves it through selection, crossover, and mutation until it finds a perfect match to the target string from a text file or a default string.

## Details

### Population 
- The algorithm initializes a population of 200 random strings, each matching the length of the target string.

### Selection and Parents
- **Tournament Selection**: A tournament of 5 randomly chosen individuals is held, and the best one is selected as a parent for crossover.

### Crossover
- **Two-point crossover**: Two random indices are chosen, and the child inherits a segment of genes from each parent, (improve preserving parent traits).

### Mutation
- Mutation starts at  5% per character, gradually decreasing as generations progress, (allow more exploration initially and then refine solutions.)

### Survival Rate and Elitism
- **Survival Rate**: 20% of the population survives through selection.
- **Elitism**: The top 5 individuals of each generation move to the next.

### Stopping Criteria
- The algorithm stops when an exact match to the target is found, after 5,000 generations and patience based stopping.

## To run 

1. Run the program using:
   ```bash
   python algo.py --filename {target.txt}
   # note: This will default to use the first txt file in local directory if input is none or not found.
2. The program will start generating and evolving a population of strings until it reaches stopping conditions and the fitness score of the best individual per generation will be printed.
3. If an exact match is found, the algorithm will print the final best match and stop.

## Parameters
- **Population Size**: 200 individuals.
- **Initial Mutation Rate**: 5%, decreasing over time.
- **Elitism Count**: Top 5 individuals preserved.
- **Max Generations**: 5,000.


