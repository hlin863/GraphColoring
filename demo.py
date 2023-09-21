from genetic import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

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

# a list of every U.S. state in alphabetical order
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois',
          'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
          'West Virginia', 'Wisconsin', 'Wyoming']


def draw_map(colors):

    fig, ax = plt.subplots(figsize=(15, 10))

    # Create the basemap with specific parameters
    m = Basemap(llcrnrlon=-125, llcrnrlat=20, urcrnrlon=-60, urcrnrlat=50,
                projection='lcc', lat_1=33, lat_2=45, lon_0=-95)

    # Draw coastlines, countries, and states for reference
    # m.drawcoastlines()
    # m.drawcountries()
    # m.drawstates()

    m.readshapefile('st99_d00', name='states', drawbounds=True)

    ax = plt.gca()  # get current axes instance

    for state, color in zip(states, colors):
        statename = state
        print(statename)
        seg = m.states[states.index(statename)]
        poly = Polygon(seg, facecolor=color, edgecolor='red')
        ax.add_patch(poly)
    # Color each state based on provided colors
    plt.title('Colored Map of US States')
    plt.show()


# draw each state on a map with the color of the state
draw_map(results_fittest[-1].colors)
