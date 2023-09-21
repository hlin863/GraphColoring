# use dynamic programming to color each US state such that it has different colors to its neighbours.
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon


def is_valid_color(v, color, graph, colors_assigned):
    for neighbour in graph[v]:
        if colors_assigned[neighbour] == color:
            return False
    return True


def graph_coloring_util(graph, m, colors_assigned, v):
    if v == len(graph):
        return True

    for color in range(1, m + 1):
        if is_valid_color(v, color, graph, colors_assigned):
            colors_assigned[v] = color
            if graph_coloring_util(graph, m, colors_assigned, v + 1):
                return True
            colors_assigned[v] = 0

    return False


# def graph_coloring(graph, m):
#     colors_assigned = [-1] * len(graph)
#     if not graph_coloring_util(graph, m, colors_assigned, 0):
#         return False
#     return colors_assigned

def graph_coloring(graph, m):
    colors_assigned = [-1] * len(graph)
    if graph_coloring_util(graph, m, colors_assigned, 0):
        return colors_assigned
    return []


number_of_nodes = 50
probability_of_edge = 0.5


def generate_graph():

    state_data = [
        ("AK", []),
        ("AL", ["FL", "GA", "MS", "TN"]),
        ("AR", ["LA", "MS", "MO", "OK", "TN", "TX"]),
        ("AZ", ["CA", "CO", "NV", "NM", "UT"]),
        ("CA", ["AZ", "NV", "OR"]),
        ("CO", ["KS", "NE", "NM", "OK", "UT", "WY"]),
        ("CT", ["MA", "NY", "RI"]),
        ("DC", ["VA", "MD"]),
        ("DE", ["MD", "NJ", "PA"]),
        ("FL", ["AL", "GA"]),
        ("GA", ["AL", "FL", "NC", "SC", "TN"]),
        ("HI", []),
        ("IA", ["IL", "MN", "MO", "NE", "SD", "WI"]),
        ("ID", ["MT", "NV", "OR", "UT", "WA", "WY"]),
        ("IL", ["IA", "IN", "KY", "MO", "WI"]),
        ("IN", ["IL", "KY", "MI", "OH"]),
        ("KS", ["CO", "MO", "NE", "OK"]),
        ("KY", ["IL", "IN", "MO", "OH", "TN", "VA", "WV"]),
        ("LA", ["AR", "MS", "TX"]),
        ("MA", ["CT", "NH", "NY", "RI", "VT"]),
        ("MD", ["DE", "DC", "PA", "VA", "WV"]),
        ("ME", ["NH"]),
        ("MI", ["IN", "OH", "WI"]),
        ("MN", ["IA", "ND", "SD", "WI"]),
        ("MO", ["AR", "IA", "IL", "KS", "KY", "NE", "OK", "TN"]),
        ("MS", ["AL", "AR", "LA", "TN", "TX"]),
        ("MT", ["ID", "ND", "SD", "WY"]),
        ("NC", ["GA", "SC", "TN", "VA"]),
        ("ND", ["MN", "MT", "SD"]),
        ("NE", ["CO", "IA", "KS", "MO", "SD", "WY"]),
        ("NH", ["MA", "ME", "VT"]),
        ("NJ", ["CT", "NY", "PA"]),
        ("NM", ["AZ", "CO", "OK", "TX"]),
        ("NV", ["AZ", "CA", "ID", "OR", "UT"]),
        ("NY", ["CT", "MA", "NJ", "PA", "VT"]),
        ("OH", ["IN", "KY", "MI", "PA", "WV"]),
        ("OK", ["AR", "CO", "KS", "MO", "NM", "TX"]),
        ("OR", ["CA", "ID", "NV", "WA"]),
        ("PA", ["DE", "MD", "NJ", "NY", "OH", "WV"]),
        ("RI", ["CT", "MA"]),
        ("SC", ["GA", "NC"]),
        ("SD", ["IA", "MN", "MT", "ND", "NE", "WY"]),
        ("TN", ["AL", "AR", "GA", "KY", "MO", "MS", "NC", "VA"]),
        ("TX", ["AR", "LA", "NM", "OK", "WA"]),
        ("UT", ["AZ", "CO", "ID", "NV", "WY"]),
        ("VA", ["DC", "KY", "MD", "NC", "TN", "WV"]),
        ("VT", ["MA", "NH", "NY"]),
        ("WA", ["ID", "OR", "OR", "TX"]),
        ("WI", ["IA", "IL", "IN", "MI", "MN", "MO", "ND", "NE", "SD",
                "WY"]),
        ("WV", ["DC", "MD", "NC", "PA", "VA"]),
        ("WY", ["CO", "ID", "MT", "ND", "SD", "UT"])]

    states = [state[0] for state in state_data]

    adjacency_matrix = [[0 for _ in range(len(states))]
                        for _ in range(len(states))]

    for state, neighbours in state_data:
        for neighbour in neighbours:
            adjacency_matrix[states.index(state)][states.index(neighbour)] = 1
            adjacency_matrix[states.index(neighbour)][states.index(state)] = 1

    return states, adjacency_matrix


# Assuming your graph is a 2D adjacency matrix. The below line should be replaced by the actual method to get the graph.
_, adjacency_matrix = generate_graph()

# Color the graph with a maximum of m colors
m = 4
colors = graph_coloring(adjacency_matrix, m)

# colors = 'GOGOYYGOBGYOYYOOOGOBYOGOYYGOBBYOGGYYBBGOBYBYBGOOBOO'
colors = 'GOGOYYOGYBYGGYBOOGOBBBBOYYGGBBYOGGYYBBGYOYBYBYOOYOO'

# replace letter o in colors with y
# colors = colors.replace('O', 'Y')

# convert colors to lower case
colors = colors.lower()

# convert string into a list of characters
colors = list(colors)

print(colors)

# convert colors to strings: 1 -> 'r', 2 -> 'g', 3 -> 'b', 4 -> 'y'
# colors = list(map(lambda x: 'r' if x == 1 else 'g' if x ==
#               2 else 'b' if x == 3 else 'y', colors))

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
# get Texas and draw the filled polygon

STATES = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois',
          'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
          'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
          'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
          'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
          'West Virginia', 'Wisconsin', 'Wyoming']

for state in STATES:
    seg = map.states[state_names.index(state)]
    if colors[STATES.index(state)] == 'o':
        poly = Polygon(seg, facecolor='orange', edgecolor='black')
    else:
        poly = Polygon(
            seg, facecolor=colors[STATES.index(state)], edgecolor='black')
    ax.add_patch(poly)
# seg = map.states[state_names.index('Texas')]
# poly = Polygon(seg, facecolor='red', edgecolor='red')
# ax.add_patch(poly)

plt.show()
