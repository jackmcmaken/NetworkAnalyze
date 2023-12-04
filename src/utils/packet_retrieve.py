from scapy.all import sniff, IP, TCP, UDP, SCTP, DNS, DNS, wrpcap
from datetime import datetime

class PacketData:
    
    def __init__(self):
        self.raw_packet_data = []
        
        # CSV formatted packet data
        self.tcp_packet_data = []
        self.udp_packet_data = []
        self.http_packet_data = []
        
        pcap = None
        
        
    def get_packet_data(self):
        return self.raw_packet_data

    # Generates csv formatted array of packets
    # def packet_callback(self, packet):
    #     # Check if the packet has IP and TCP layers
    #     if IP in packet:
    #         if TCP in packet:
    #             src_ip = packet[IP].src
    #             dst_ip = packet[IP].dst
    #             src_port = packet[TCP].sport
    #             dst_port = packet[TCP].dport
    #             self.packet_data.append([src_ip, dst_ip, src_port, dst_port])
    #         if UDP in packet:
        
                
            
    
    def capture_packets(self, time=10):
        self.tcp_packet_data = sniff(filter='tcp', timeout=time)
        #self.udp_packet_data = sniff(filter = 'udp', timeout=time)
        # self.http_packet_data = sniff(filter = 'tcp port 80', count=count)
        # self.raw_packet_data = sniff(prn=self.packet_callback, store=0, count=count)
        
    def writeFile(self):
        filename = datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".pcap"
        
        wrpcap(filename, self.tcp_packet_data)
        


def csv_format(packetArr):
    formatted = []
    for packet in packetArr:
        if IP in packet:
            if TCP in packet:
                formatted.append([packet[IP].src, packet[IP].dst, packet[TCP].sport, packet[TCP].dport])
            elif UDP in packet:
                formatted.append([packet[IP].src, packet[IP].dst, packet[UDP].sport, packet[UDP].dport])
    return formatted


