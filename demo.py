from genetic import *

number_of_nodes = 50
probability_of_edge = 0.5
population_size = 100
n_generations = 50

_, adjacency_list = generate_random_graph(number_of_nodes, probability_of_edge)

initial_population = generate_random_initial_population(
    population_size, number_of_nodes, adjacency_list)

results_fitness, results_fittest = evolution(
    initial_population, n_generations, population_size)

visualize_results(results_fitness, results_fittest)

# Display the colors of the states for the fittest individual of the last generation
print("Colors of states for the fittest individual of the last generation:")
print(results_fittest[-1].colors)
