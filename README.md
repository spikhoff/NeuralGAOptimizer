The program aims to find the optimal value of `n` for a function `f(n) = abs(n - factorial(n))`. This can be seen as a simplified exploration of P vs. NP problems.

### Functionality

The program utilizes a genetic algorithm for the core search process. It:

1. **Generates an initial population** of `n` values.
2. **Evaluates the fitness** of each individual using the `f(n)` function.
3. **Selects parents** based on their fitness.
4. **Performs crossover and mutation** to create offspring.
5. **Evaluates the fitness of the offspring**.
6. **Replaces low-fitness individuals** with high-fitness offspring.

**Optional Neural Network Integration:**

The program allows the use of a neural network to predict the fitness of individuals after several generations. This can potentially improve the search efficiency.

### Usage

The program requires the TensorFlow library for the neural network component.

```python
import neurogeneticoptimizer

# Example usage:
population_size = 100
generations = 100
use_neural_network = True  # Experiment with this flag
best_n = neurogeneticoptimizer.genetic_algorithm(population_size, generations, use_neural_network)
print("Optimal n:", best_n)
