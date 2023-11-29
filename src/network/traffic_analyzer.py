#from scapy.all import *
from scapy.all import sniff, IP, TCP
import networkx as nx
import pandas as pd

def getPackets():
    capture = sniff(count=200)
    capture.show()
    capture.plot(lambda x:len(x))

def packet_csv():
    packet_data = []
    def packet_callback(packet):
        # Check if the packet has IP and TCP layers
        if IP in packet and TCP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            
            packet_data.append([src_ip, dst_ip, src_port, dst_port])

    sniff(filter="tcp", prn=packet_callback, store=0, count=60)

    return packet_data
    
def visualizeNet(packet_data):
    # Convert packet data to proper pandas dataframe
    csv_pandas = pd.DataFrame(packet_data, columns=["Source IP", "Destination IP", "Source Port", "Destination Port"])
    network = nx.from_pandas_edgelist(csv_pandas, source='Source IP', target='Destination IP', edge_attr=True)
    return network
