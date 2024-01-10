import networkx as nx
G = nx.Graph()

G.add_node('Sahil')
G.add_node('Nizami')
G.add_node('Tarqovu')
G.add_node('20 Janvar Kucesi')
G.add_node('Sumgayit')

# BUS STOPS
G.add_edge('Nizami', 'Tarqovu')
G.add_edge('Tarqovu', '20 Janvar Kucesi')
G.add_edge('20 Janvar Kucesi', 'Sahil')
G.add_edge('Sumgayit', 'Sahil')
G.add_edge('Tarqovu', 'Sahil')

print( nx.shortest_path( G, 'Nizami', 'Sahil' ) )
                        

