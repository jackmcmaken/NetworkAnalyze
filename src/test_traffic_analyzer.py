import src.network.traffic_analyzer as ta
import src.utils.packet_retrieve as pr
#from scapy.all import *
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime


#src.network.traffic_analyzer.getPackets()

# net = src.utils.packetRetrieve.PacketData()
# net.capture_packets()
# netcsv = src.utils.packetRetrieve.csv_format()
# network = src.network.traffic_analyzer.visualizeNet(netcsv)
# print("Nodes:", network.nodes())
# print("Edges:", network.edges())
# nx.draw_circular(network, with_labels = True)
# plt.show()

# net = pr.PacketData()
# net.capture_packets()
# net.tcp_packet_data.show()
# netcsv = pr.csv_format(net.tcp_packet_data)
# print(ta.get_common_dst(netcsv))

print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
