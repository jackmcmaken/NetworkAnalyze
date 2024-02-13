import networkx as nx
from networkx.readwrite import json_graph
import src.network.traffic_analyzer as ta

def graph_figure(net_csv):
    network = ta.visualizeNet(net_csv)

    # Compute the Spring layout positions for nodes
    pos = nx.spring_layout(network)

    # Create the figure for the graph
    graph = {
        "data": [
            {
                "type": "scatter",
                "x": [pos[node][0] for node in network.nodes],
                "y": [pos[node][1] for node in network.nodes],
                "mode": "markers",
                "hoverinfo": "text",
                "text": [str(node) for node in network.nodes],
            }
        ],
        "layout": {
            "title": "Network Graph",
            "showlegend": False,
            "hovermode": "closest",
            "xaxis": {"showgrid": False, "zeroline": False},
            "yaxis": {"showgrid": False, "zeroline": False},
        },
    }
    return graph

def graph2():
    G = nx.Graph()

    # example
    packets = [
        {'src': '192.168.1.1', 'dst': '192.168.1.2'},
        {'src': '192.168.1.1', 'dst': '192.168.1.3'},
        {'src': '192.168.1.2', 'dst': '192.168.1.3'},
    ]

    # Add nodes and edges
    for packet in packets:
        src = packet['src']
        dst = packet['dst']
        if not G.has_node(src):
            G.add_node(src)
        if not G.has_node(dst):
            G.add_node(dst)
        if not G.has_edge(src, dst):
            G.add_edge(src, dst, weight=0)
        G[src][dst]['weight'] += 1
        
    elements = [
        {'data': {'id': node, 'label': node}} for node in G.nodes
    ] + [
        {'data': {'source': source, 'target': target, 'weight': G[source][target]['weight']}}
        for source, target in G.edges
    ]
    return elements