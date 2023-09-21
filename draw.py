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

colors = results_fittest[-1].colors

# create the map
map = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
              projection='lcc', lat_1=33, lat_2=45, lon_0=-95)

# load the shapefile, use the name 'states'
map.readshapefile('st99_d00', name='states', drawbounds=True)

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca()  # get current axes instance

# define a list of 50 colors
# colors = ['r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r',
#           'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r',
#           'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b',
#           'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r',
#           'r', 'g', 'b', 'r', 'g', 'b', 'r', 'g', 'b', 'r'
#           ]

print(len(colors))
# get Texas and draw the filled polygon

STATES = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois',
          'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
          'West Virginia', 'Wisconsin', 'Wyoming']

for state in STATES:
    seg = map.states[state_names.index(state)]
    poly = Polygon(
        seg, facecolor=colors[STATES.index(state)], edgecolor='black')
    ax.add_patch(poly)
# seg = map.states[state_names.index('Texas')]
# poly = Polygon(seg, facecolor='red', edgecolor='red')
# ax.add_patch(poly)

plt.show()
