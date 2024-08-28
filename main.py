import random
import numpy as np
import tensorflow as tf

def fitness_function(n):
  return abs(n - factorial(n))

def create_neural_network(input_shape):
  # ... (same neural network architecture as before)

def genetic_algorithm(population_size, generations, use_neural_network=False):
  population = np.random.randint(1, 100, size=population_size)

  for generation in range(generations):
    fitness_scores = [fitness_function(n) for n in population]
    parents = np.random.choice(population, size=2, replace=False, p=fitness_scores / np.sum(fitness_scores))

    # Crossover and mutation
    # ... (implement crossover and mutation)

    # Evaluate offspring
    offspring_fitness = [fitness_function(n) for n in offspring]

    # Replace low-fitness individuals
    # ... (replace individuals based on fitness)

    # Use neural network for prediction (optional)
    if use_neural_network and generation % 10 == 0:
      # ... (train and use neural network to predict fitness)

  best_n = population[np.argmin(fitness_scores)]
  return best_n

# Example usage:
population_size = 100
generations = 100
use_neural_network = True  # Experiment with this flag
best_n = genetic_algorithm(population_size, generations, use_neural_network)
print("Optimal n:", best_n)
