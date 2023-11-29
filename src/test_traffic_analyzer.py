import src.network.traffic_analyzer
#from scapy.all import *
import networkx as nx
import matplotlib.pyplot as plt


#src.network.traffic_analyzer.getPackets()

netcsv = src.network.traffic_analyzer.packet_csv()
network = src.network.traffic_analyzer.visualizeNet(netcsv)
print("Nodes:", network.nodes())
print("Edges:", network.edges())
nx.draw_circular(network, with_labels = True)
plt.show()
