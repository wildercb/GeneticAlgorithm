import random
import argparse

# Step 1: Read Target Text
def read_target_text(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"File '{filename}' not found. Using default target text.")
        return "Hello, World!"  # Default target text

# Step 2: Initialize Random Population
def generate_random_population(size, target_length):
    return [''.join(chr(random.randint(0, 255)) for _ in range(target_length)) for _ in range(size)]

# Step 3: Fitness Function
def calculate_fitness(individual, target):
    return sum(1 for a, b in zip(individual, target) if a == b)

# Step 4.1: Selection of Parents (Tournament Selection)
def select_parents(population, fitness_scores, tournament_size=5):
    tournament = random.sample(list(zip(population, fitness_scores)), tournament_size)
    return max(tournament, key=lambda x: x[1])[0]

# Step 4.2: Crossover Function (Two-point Crossover)
def crossover(parent1, parent2):
    if len(parent1) < 2:
        return parent1  # Avoids error for short strings
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))
    return parent1[:point1] + parent2[point1:point2] + parent1[point2:]

# Step 4.3: Mutation Function
def mutate(individual, mutation_rate):
    return ''.join(chr(random.randint(0, 255)) if random.random() < mutation_rate else char for char in individual)

# Step 5 & 6: Main Evolution Function
def evolve_population(target, population_size=200, initial_mutation_rate=0.05, max_generations=5000, survival_rate=0.2, elitism_count=5):
    target_length = len(target)
    population = generate_random_population(population_size, target_length)
    mutation_rate = initial_mutation_rate

    for generation in range(max_generations):
        # Calculate fitness for all individuals
        fitness_scores = [calculate_fitness(individual, target) for individual in population]
        max_fitness = max(fitness_scores)

        # Print best fitness value of the generation
        best_individual = population[fitness_scores.index(max_fitness)]
        print(f"Generation {generation}: Best Fitness = {max_fitness}")

        # If found exact match, stop
        if best_individual == target:
            print("Exact match found!")
            print(f"Best Individual: {best_individual}")
            return

        # Step 5: Select next generation parents
        next_generation = []

        # Elitism: Directly carry over top individuals to next generation
        sorted_population = sorted(zip(population, fitness_scores), key=lambda x: x[1], reverse=True)
        elites = [individual for individual, _ in sorted_population[:elitism_count]]
        next_generation.extend(elites)

        # Adjust mutation rate based on fitness improvement
        mutation_rate = max(0.01, mutation_rate * 0.99)

        # Fill remaining population with offspring using tournament selection and crossover
        while len(next_generation) < population_size:
            parent1 = select_parents(population, fitness_scores)
            parent2 = select_parents(population, fitness_scores)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            next_generation.append(child)

        population = next_generation

    print("Max generations reached without finding exact match.")
    print(f"Best Individual: {best_individual}")

if __name__ == "__main__":
    # Command line argument parsing
    parser = argparse.ArgumentParser(description="Genetic Algorithm for ASCII String Matching")
    parser.add_argument('--filename', type=str, default=None, help='Filename containing the target text')
    args = parser.parse_args()

    # Read target text from file
    target_text = read_target_text(args.filename) if args.filename else "Hello, World!"

    # Start evolving
    evolve_population(target_text)
