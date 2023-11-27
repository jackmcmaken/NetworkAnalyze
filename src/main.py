from network.packet_analyzer import PacketAnalyzer
from network.traffic_analyzer import TrafficAnalyzer
from utils.data_parser import DataParser
from utils.visualization import generate_network_graph

# Load and parse network data
data_parser = DataParser("network_capture.log")
parsed_data = data_parser.parse()

# Analyze packets
packet_analyzer = PacketAnalyzer(parsed_data["packets"])
packet_summary = packet_analyzer.analyze()

# Analyze traffic
traffic_analyzer = TrafficAnalyzer(parsed_data["traffic"])
traffic_stats = traffic_analyzer.analyze()

# Visualize results
generate_network_graph(packet_summary, traffic_stats)

# Further analysis and reporting...
