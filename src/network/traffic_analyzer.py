#from scapy.all import *
from src.utils.packet_retrieve import *
from scapy.all import sniff, IP, TCP
import networkx as nx
import pandas as pd

# basic function to get a set of packets
# def getPackets():
#     capture = sniff(count=200)
#     capture.show()
#     capture.plot(lambda x:len(x))

# generate visualization using source ips and destination ips
def visualizeNet(packet_data):
    # Convert packet data to proper pandas dataframe
    csv_pandas = pd.DataFrame(packet_data, columns=["Source IP", "Destination IP", "Source Port", "Destination Port"])
    network = nx.from_pandas_edgelist(csv_pandas, source='Source IP', target='Destination IP', edge_attr=True)
    return network

# get most common destination IP
def get_common_dst(packets):
    countDsts = {}
    for packet in packets:
        if packet[1] in countDsts:
            countDsts[packet[1]] = countDsts[packet[1]] + 1
        else:
            countDsts[packet[1]] = 1
    return max(countDsts, key=countDsts.get)