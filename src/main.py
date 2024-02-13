import src.network.traffic_analyzer as ta
import src.utils.packet_retrieve as pr
import dash_bootstrap_components as dbc
from dash import Dash, html, callback, dcc, Input, Output
import networkx as nx
from dash.dash import no_update
import dash_cytoscape as cyto
from networkx.readwrite import json_graph
import src.utils.visualization as vs

# Setup style
external_stylesheets = [dbc.themes.DARKLY]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# Get network information from modules
net = pr.PacketData()
net.capture_packets()
net_csv = pr.csv_format(net.tcp_packet_data)
net.tcp_packet_data.show()
pcapfile = net.writeFile()

# App layout
app.layout = dbc.Container(fluid=True, children=[
    dbc.Row(justify="center", align="center", className="mb-3", children=[
        dbc.Col(md=8, children=[
            html.H3('Network Analyzer', className='text-center mb-4'), 
            html.Hr()
        ])
    ]),
    dbc.Row(justify="center", align="center", className="mb-3", children=[
        dbc.Col(md=8, children=[
            dbc.Alert(f'Found {len(net_csv)} TCP packets.', color="info", className="mb-3"),
            dbc.Alert(f'The most common destination was {ta.get_common_dst(net_csv)}', color="success"),
        ])
    ]),
    dbc.Row(justify="center", align="center", className="mb-3", children=[
        dbc.Col(md=8, children=[
            html.H4('Network Visualization', className='mb-4'), 
            cyto.Cytoscape(
                id='network-graph',
                elements=vs.graph2(),
                style={'width': '100%', 'height': '400px'},
                layout={'name': 'cose'}
            )
        ])
    ]),
    dbc.Row(justify="center", align="center", className="mb-3", children=[
        dbc.Col(md=8, children=[
            dbc.Button('Download pcap file', id='download-button', color="primary", className="me-md-2"), 
            dcc.Download(id='download')
        ])
    ])
])

@app.callback(
    Output("download", "data"),
    Input("download-button", "n_clicks"),
    prevent_initial_call=True
)
def func(n_clicks):
    if n_clicks is None:
        return no_update
    
    with open(pcapfile, "rb") as file:
        pcap_content = file.read()
    
    return dcc.send_bytes(pcap_content, "network_capture.pcap")

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
