import random
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# create the map
map = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
              projection='lcc', lat_1=33, lat_2=45, lon_0=-95)

# load the shapefile, use the name 'states'
map.readshapefile('st99_d00', name='states', drawbounds=True)

election_file = open('2020_election.csv', 'r')

# skip the first line of the file (the header)
election_file.readline()

# create a dictionary to store the vote percentages for each state
votes_percentage = {}

states_list = []

# read the file line by line
for line in election_file:
    line_list = line.split(',')
    state_name = line_list[0]
    percentage_string = line_list[5].strip()

    # remove the quotation marks if they exist from state name
    if state_name[0] == '"':
        state_name = state_name[1:-1]

    states_list.append(state_name)

    # remove the "%" symbol if it exists
    percentage_string = percentage_string.replace('%', '')

    vote_percentage = float(percentage_string)
    print("The vote percentage for", state_name, "is", vote_percentage, "%")
    votes_percentage[state_name] = vote_percentage

election_file.close()

state_names = [shape_dict['NAME'] for shape_dict in map.states_info]
ax = plt.gca()  # get current axes instance

print(states_list)

for state in state_names:

    if state in states_list:
        seg = map.states[state_names.index(state)]
        # Normalize the percentage
        color = cm.Reds(votes_percentage[state] / 100)
        poly = Polygon(seg, facecolor=color, edgecolor='black')
        ax.add_patch(poly)

# Create a ScalarMappable object associated with the Reds colormap and normalized to [0, 100]
sm = plt.cm.ScalarMappable(cmap=cm.Reds, norm=Normalize(vmin=0, vmax=100))
# Fake up the array of the scalar mappable.
sm._A = []
# Draw the colorbar
cbar = plt.colorbar(sm, ax=ax, orientation='vertical')
cbar.set_label('Vote Percentage (%)')

# add a title as "GOP vote percentage for each state"
plt.title('GOP vote percentage for each state in 2020 election')

plt.show()
