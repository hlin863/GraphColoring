import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def draw_colored_us_map():
    G = nx.Graph()

    # create a dictionary mapping between states and state codes
    state_dictionary = {
        "Alabama": "AL",
        "Alaska": "AK",
        "Arizona": "AZ",
        "Arkansas": "AR",
        "California": "CA",
        "Colorado": "CO",
        "Connecticut": "CT",
        "Delaware": "DE",
        "Florida": "FL",
        "Georgia": "GA",
        "Hawaii": "HI",
        "Idaho": "ID",
        "Illinois": "IL",
        "Indiana": "IN",
        "Iowa": "IA",
        "Kansas": "KS",
        "Kentucky": "KY",
        "Louisiana": "LA",
        "Maine": "ME",
        "Maryland": "MD",
        "Massachusetts": "MA",
        "Michigan": "MI",
        "Minnesota": "MN",
        "Mississippi": "MS",
        "Missouri": "MO",
        "Montana": "MT",
        "Nebraska": "NE",
        "Nevada": "NV",
        "New Hampshire": "NH",
        "New Jersey": "NJ",
        "New Mexico": "NM",
        "New York": "NY",
        "North Carolina": "NC",
        "North Dakota": "ND",
        "Ohio": "OH",
        "Oklahoma": "OK",
        "Oregon": "OR",
        "Pennsylvania": "PA",
        "Rhode Island": "RI",
        "South Carolina": "SC",
        "South Dakota": "SD",
        "Tennessee": "TN",
        "Texas": "TX",
        "Utah": "UT",
        "Vermont": "VT",
        "Virginia": "VA",
        "Washington": "WA",
        "West Virginia": "WV",
        "Wisconsin": "WI",
        "Wyoming": "WY"
    }

    # List of US states
    states = [
        "WA", "OR", "CA", "ID", "NV", "AZ", "UT", "MT", "WY", "CO", "NM", "ND", "SD", "NE", "KS",
        "OK", "TX", "MN", "IA", "MO", "AR", "LA", "WI", "IL", "MS", "IN", "KY", "TN", "AL", "FL",
        "GA", "SC", "NC", "VA", "WV", "OH", "MI", "ME", "NH", "VT", "NY", "MA", "CT", "RI", "PA",
        "DE", "MD", "NJ", "AK", "HI"
    ]

    for state in states:
        G.add_node(state)

    # Neighboring states
    borders = [
        ("WA", "OR"), ("WA", "ID"), ("OR", "CA"), ("OR",
                                                   "ID"), ("OR", "NV"), ("CA", "NV"),
        ("CA", "AZ"), ("ID", "MT"), ("ID", "WY"), ("ID",
                                                   "UT"), ("ID", "NV"), ("NV", "UT"),
        ("NV", "AZ"), ("AZ", "UT"), ("AZ", "CO"), ("AZ",
                                                   "NM"), ("UT", "WY"), ("UT", "CO"),
        ("MT", "WY"), ("MT", "ND"), ("MT", "SD"), ("WY",
                                                   "SD"), ("WY", "NE"), ("WY", "CO"),
        ("CO", "NE"), ("CO", "KS"), ("CO", "OK"), ("CO",
                                                   "NM"), ("NM", "TX"), ("NM", "OK"),
        ("ND", "SD"), ("SD", "NE"), ("SD", "IA"), ("SD",
                                                   "MN"), ("NE", "IA"), ("NE", "MO"),
        ("NE", "KS"), ("KS", "MO"), ("KS", "OK"), ("OK",
                                                   "MO"), ("OK", "AR"), ("OK", "TX"),
        ("TX", "AR"), ("TX", "LA"), ("MN", "IA"), ("MN",
                                                   "WI"), ("IA", "WI"), ("IA", "IL"),
        ("IA", "MO"), ("MO", "IL"), ("MO", "KY"), ("MO",
                                                   "TN"), ("MO", "AR"), ("AR", "LA"),
        ("AR", "MS"), ("AR", "TN"), ("LA", "MS"), ("WI",
                                                   "IL"), ("WI", "MI"), ("IL", "IN"),
        ("IL", "KY"), ("MS", "TN"), ("MS", "AL"), ("IN",
                                                   "MI"), ("IN", "OH"), ("IN", "KY"),
        ("KY", "OH"), ("KY", "WV"), ("KY", "VA"), ("KY",
                                                   "TN"), ("TN", "VA"), ("TN", "NC"),
        ("TN", "GA"), ("TN", "AL"), ("AL", "GA"), ("AL",
                                                   "FL"), ("GA", "FL"), ("GA", "SC"),
        ("GA", "NC"), ("SC", "NC"), ("NC", "VA"), ("VA",
                                                   "WV"), ("VA", "MD"), ("VA", "DE"),
        ("WV", "OH"), ("WV", "PA"), ("WV", "MD"), ("OH",
                                                   "PA"), ("MI", "OH"), ("ME", "NH"),
        ("NH", "VT"), ("NH", "MA"), ("VT", "NY"), ("VT",
                                                   "MA"), ("NY", "MA"), ("NY", "CT"),
        ("NY", "RI"), ("NY", "PA"), ("NY", "NJ"), ("MA",
                                                   "CT"), ("MA", "RI"), ("CT", "RI"),
        ("CT", "NY"), ("RI", "NY"), ("PA", "NJ"), ("DE", "NJ"), ("DE", "MD")
    ]

    for state in states:
        G.add_node(state)
    for border in borders:
        G.add_edge(*border)

    # Color the graph
    color_map = nx.coloring.greedy_color(G, strategy="largest_first")

    # Create the Basemap instance for the continental US
    m = Basemap(llcrnrlon=-119, llcrnrlat=20, urcrnrlon=-64, urcrnrlat=49,
                projection='lcc', lat_1=33, lat_2=45, lon_0=-95)

    fig, ax = plt.subplots(figsize=(12, 8))
    m.drawcoastlines()
    m.drawcountries()
    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='white', lake_color='aqua')

    m.drawparallels(range(25, 65, 20), labels=[1, 0, 0, 0])
    m.drawmeridians(range(-120, -40, 20), labels=[0, 0, 0, 1])

    # Read the US states shape files and draw them on the map
    m.readshapefile('st99_d00', name='states', drawbounds=True)

    # Iterate over the states and color them
    for info, shape in zip(m.states_info, m.states):
        # print(info)
        state_name = info['NAME']

        # check if state name is in state dictionary
        if state_name not in state_dictionary:
            continue
        # get state code from state dictionary using state name
        state_code = state_dictionary[state_name]
        print(state_code)
        print(color_map)
        if state_code in color_map:
            # Assuming maximum 4 colors, you can adjust accordingly
            color = plt.cm.rainbow(color_map[state_code] / 4.0)
            poly = plt.Polygon(shape, facecolor=color, edgecolor=color)
            ax.add_patch(poly)

    plt.show()


draw_colored_us_map()

###
# def draw_colored_us_map():
#     G = nx.Graph()

#     # List of US states
#     states = [
#         "WA", "OR", "CA", "ID", "NV", "AZ", "UT", "MT", "WY", "CO", "NM", "ND", "SD", "NE", "KS",
#         "OK", "TX", "MN", "IA", "MO", "AR", "LA", "WI", "IL", "MS", "IN", "KY", "TN", "AL", "FL",
#         "GA", "SC", "NC", "VA", "WV", "OH", "MI", "ME", "NH", "VT", "NY", "MA", "CT", "RI", "PA",
#         "DE", "MD", "NJ", "AK", "HI"
#     ]

#     for state in states:
#         G.add_node(state)

#     # Neighboring states
#     borders = [
#         ("WA", "OR"), ("WA", "ID"), ("OR", "CA"), ("OR",
#                                                    "ID"), ("OR", "NV"), ("CA", "NV"),
#         ("CA", "AZ"), ("ID", "MT"), ("ID", "WY"), ("ID",
#                                                    "UT"), ("ID", "NV"), ("NV", "UT"),
#         ("NV", "AZ"), ("AZ", "UT"), ("AZ", "CO"), ("AZ",
#                                                    "NM"), ("UT", "WY"), ("UT", "CO"),
#         ("MT", "WY"), ("MT", "ND"), ("MT", "SD"), ("WY",
#                                                    "SD"), ("WY", "NE"), ("WY", "CO"),
#         ("CO", "NE"), ("CO", "KS"), ("CO", "OK"), ("CO",
#                                                    "NM"), ("NM", "TX"), ("NM", "OK"),
#         ("ND", "SD"), ("SD", "NE"), ("SD", "IA"), ("SD",
#                                                    "MN"), ("NE", "IA"), ("NE", "MO"),
#         ("NE", "KS"), ("KS", "MO"), ("KS", "OK"), ("OK",
#                                                    "MO"), ("OK", "AR"), ("OK", "TX"),
#         ("TX", "AR"), ("TX", "LA"), ("MN", "IA"), ("MN",
#                                                    "WI"), ("IA", "WI"), ("IA", "IL"),
#         ("IA", "MO"), ("MO", "IL"), ("MO", "KY"), ("MO",
#                                                    "TN"), ("MO", "AR"), ("AR", "LA"),
#         ("AR", "MS"), ("AR", "TN"), ("LA", "MS"), ("WI",
#                                                    "IL"), ("WI", "MI"), ("IL", "IN"),
#         ("IL", "KY"), ("MS", "TN"), ("MS", "AL"), ("IN",
#                                                    "MI"), ("IN", "OH"), ("IN", "KY"),
#         ("KY", "OH"), ("KY", "WV"), ("KY", "VA"), ("KY",
#                                                    "TN"), ("TN", "VA"), ("TN", "NC"),
#         ("TN", "GA"), ("TN", "AL"), ("AL", "GA"), ("AL",
#                                                    "FL"), ("GA", "FL"), ("GA", "SC"),
#         ("GA", "NC"), ("SC", "NC"), ("NC", "VA"), ("VA",
#                                                    "WV"), ("VA", "MD"), ("VA", "DE"),
#         ("WV", "OH"), ("WV", "PA"), ("WV", "MD"), ("OH",
#                                                    "PA"), ("MI", "OH"), ("ME", "NH"),
#         ("NH", "VT"), ("NH", "MA"), ("VT", "NY"), ("VT",
#                                                    "MA"), ("NY", "MA"), ("NY", "CT"),
#         ("NY", "RI"), ("NY", "PA"), ("NY", "NJ"), ("MA",
#                                                    "CT"), ("MA", "RI"), ("CT", "RI"),
#         ("CT", "NY"), ("RI", "NY"), ("PA", "NJ"), ("DE", "NJ"), ("DE", "MD")
#     ]

#     for border in borders:
#         G.add_edge(*border)

#     # Color the graph
#     color_map = nx.coloring.greedy_color(G, strategy="largest_first")
#     node_colors = [color_map[node] for node in G.nodes()]

#     # Draw the graph
#     pos = nx.spring_layout(G)
#     # nx.draw(G, pos, node_color=node_colors, with_labels=True,
#     #         node_size=1000, cmap=plt.cm.rainbow)
#     # Use matplotlib to draw the nodes and edges
#     fig, ax = plt.subplots()
#     for edge in G.edges():
#         n1, n2 = edge
#         x1, y1 = pos[n1]
#         x2, y2 = pos[n2]
#         ax.plot([x1, x2], [y1, y2], color='black')  # Edges are drawn in black

#     for node, color in zip(G.nodes(), node_colors):
#         x, y = pos[node]
#         ax.scatter(x, y, color=plt.cm.rainbow(color), s=1000)
#         ax.text(x, y, node)

#     plt.show()


# draw_colored_us_map()
###
