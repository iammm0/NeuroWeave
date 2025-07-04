from pyvis.network import Network
import networkx as nx

def visualize_graph(graph: nx.Graph, output_file: str = "graph.html"):
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    for node_id, node_data in graph.nodes(data=True):
        label = node_data.get("label", str(node_id))
        title = node_data.get("type", "")
        net.add_node(node_id, label=label, title=title)

    for source, target, edge_data in graph.edges(data=True):
        label = edge_data.get("label", "")
        net.add_edge(source, target, label=label)

    net.show_buttons(filter_=['physics'])  # 可调物理参数
    net.show(output_file)