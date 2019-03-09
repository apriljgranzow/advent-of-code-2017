# n = 2000
import networkx as nx
import re
from collections import defaultdict

# Process input data
def regex_input(text):
    '''Return a list of regex matches for graph nodes in the format of 
    `node <-> list of edges to other nodes` '''
    grammar = re.compile(r"(\d+) <-> (.+)")
    return grammar.findall(text)

def get_edge_tuples(matches):
    edge_tuples = set()
    for match in matches:
        node = int(match[0])
        edge_list = [int(x) for x in match[1].split(', ')]
        edge_tuples.update([(node,i) for i in edge_list])
    return edge_tuples

def create_graph(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def part_one(text):
    '''Return the number of nodes in the graph that are connected to
    node 0'''
    g = create_graph(get_edge_tuples(regex_input(text)))
    return len(list(nx.dfs_preorder_nodes(g, 0)))

def group_count(graph):
    '''Given an undirected graph, find how many distinct groups there
    are with no connection to each other'''
    visited = set()
    groups = 0
    for node in graph.nodes:
        if node not in visited:
            visited.update(list(nx.dfs_preorder_nodes(graph, node)))
            groups += 1
    return groups

def part_two(text):
    g = create_graph(get_edge_tuples(regex_input(text)))
    return group_count(g)

if __name__ == "__main__":
    with open("input.txt") as file:
        text = file.read()
    print(part_one(text))
    print(part_two(text))