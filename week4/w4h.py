import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
# Circle, node, item, object
G.add_node('Sabina')
G.add_node('Sevinc')
G.add_node('Nigar')
G.add_node('TV')
G.add_node('Tshirt')
G.add_node('USBDisk')
G.add_node('Playstation')
G.add_node('JBL')

G.add_edge('Sabina', 'Tshirt', weight = 1, size = 'S') # * FROM --> TO 
G.add_edge('Sabina', 'TV', weight = 3, brand = 'Sony')

G.add_edge('Sevinc', 'TV', weight = 1, brand = 'Samsung')
G.add_edge('Sevinc', 'USBDisk', weight = 1, capacity = '128 GB')
G.add_edge('Sevinc', 'Playstation', weight = 2)

G.add_edge('Nigar', 'USBDisk', weight = 1, brand = 'Kingston')
G.add_edge('Nigar', 'TV', weight = 1, brand = 'LG')
G.add_edge('Nigar', 'Tshirt', weight = 5, size = 'XS', color = 'red')
G.add_edge('Nigar', 'JBL', weight = 1)
# G.add_edge( ) add_link == > FROM, TO, DATA

#G.add_edge( 'Nigar', 'Freinds', weight = 3)

G.edges[ 'Sabina', 'Tshirt' ]['color'] = 'yellow'
print("Sabina's tshirt color", G.edges['Sabina', 'Tshirt']['color'])


import pickle
pickle.dump( G, open('w4h.pickle', 'wb') )

print("DEGREE", [i for i in list(G.degree) if i[1] > 2])


manytimes = [(f, t, e) for (f, t, e) in G.edges(data=True) if e["weight"] > 1]
#* SELECT F, T, E from G.edges WHERE E['weight'] > 1

tshirts = [(f, e) for (f, t, e) in G.edges(data=True) if t == 'Tshirt']

l = [1,2,3,4,5,6,7]
l2 = [i*2 for i in l if i % 2 == 1] # odd number , tek sayilar, 1,3,5,7,
print(l2)

print("tshirts", tshirts)
print(manytimes)

plt.clf()
plt.cla()
p = nx.spring_layout(G)
nx.draw_networkx(G, with_labels=True, node_color = 'yellow', pos = p )
nx.draw_networkx_edges(G, pos=p)


#plt.show()

#! If you want to create an isolated "environment" - specific area -- [use the command below]
#! python3 -m venv myenv
#! source myenv/bin/activate
#! pip3 install ......

#! deactivate




# TRAFIK HEAVYNESS
G.add_edge('Nizami', 'Tarqovu', weight = 2.8)
G.add_edge('20 Janvar Kucesi', 'Tarqovu', weight = 1.8)
G.add_edge('20 Janvar Kucesi', 'Nizami', weight = 4.4)
G.add_edge('20 Janvar Kucesi', 'Sahil', weight = 1.7)
G.add_edge('Sumgayit', 'Sahil', weight = 1.8)




