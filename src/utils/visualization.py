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