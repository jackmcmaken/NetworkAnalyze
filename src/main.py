import src.network.traffic_analyzer as ta
import src.utils.packet_retrieve as pr
import dash_bootstrap_components as dbc
from dash import Dash, html, callback, dcc, Input, Output
import networkx as nx
from dash.dash import no_update
from networkx.readwrite import json_graph
import src.utils.visualization as vs

# setup style
external_stylesheets = [dbc.themes.DARKLY]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# get network information from modules
net = pr.PacketData()
net.capture_packets()
net_csv = pr.csv_format(net.tcp_packet_data)
# print(net_csv)
# print(ta.get_common_dst(net_csv))
net.tcp_packet_data.show()
pcapfile = net.writeFile()

# setup app layout with net info
app.layout = html.Div([
    html.Div(children=[
        html.H3('Network Analyzer'), 
        html.Hr()
    ]),
    html.Div(children=[
        html.P('Found ' + str(len(net_csv)) + ' TCP packets.'), 
        html.Br(), 
        html.P('The most common destination was ' + str(ta.get_common_dst(net_csv)))
    ]),
    html.Div(children=[
        html.H4('Network Visualization'), 
        dcc.Graph(figure=vs.graph_figure(net_csv))
    ]),
    html.Div(children=[
        html.Button('Download pcap file', id='download-button'), 
        dcc.Download(id='download', data={'filename': '_dash_no_update'})
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
    
    return dcc.send_file(pcap_content, "example")

# run app
if __name__ == '__main__':
    app.run(debug=True)
    