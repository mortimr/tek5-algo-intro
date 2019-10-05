#! /bin/python3

import numpy
import math
import time
import graphviz

def gen_random_graph(vertices, edges):
    ret = []
    for i in range(0, vertices):
        ret.append([])
    i = 0
    while i < edges:
        node_one = numpy.random.randint(0, vertices)
        node_two = numpy.random.randint(0, vertices)

        i += 1
        if (node_one == node_two) or (node_two in ret[node_one]) or (node_one in ret[node_two]):
            i -= 1
            continue 

        ret[node_one].append(node_two)

    return ret

def gen_line_graph(graph):
    links = []
    for vertex in range(0, len(graph)):
        for edge in graph[vertex]:
            if (vertex < edge):
                links.append((vertex, edge))
            else:
                links.append((vertex, edge))

    links = numpy.unique(links, axis=0)

    ret = {}
    for link_idx in range(0, len(links)):
        name = "{}_{}".format(links[link_idx][0], links[link_idx][1])
        ret[name] = []
        for other_link in range(link_idx + 1, len(links)):
            other_link_name = "{}_{}".format(links[other_link][0], links[other_link][1])
            if (links[link_idx][0] == links[other_link][0]) or (links[link_idx][1] == links[other_link][1]) or (links[link_idx][0] == links[other_link][1]) or (links[link_idx][1] == links[other_link][0]):
                ret[name].append(other_link_name)
    return ret


def to_graphviz(graph, file):
    dot = graphviz.Graph()
    for vertex in range(0, len(graph)):
        dot.node(str(vertex))
    for vertex in range(0, len(graph)):
        for edge in range(0, len(graph[vertex])):
            dot.edge(str(vertex), str(graph[vertex][edge]))
    dot.render(file, view=True)

def linegraph_to_graphviz(graph, file):
    dot = graphviz.Graph()
    for vertex in graph.keys():
        dot.node(vertex)
    for vertex in graph.keys():
        for edge in graph[vertex]:
            dot.edge(vertex, edge)

    dot.render(file, view=True)


# Exemple from the wikipedia line graph page (starts at 0 !)
graph = [
[1, 2, 3],
[4],
[3],
[4],
[]
]
#graph = gen_random_graph(100, 100)
to_graphviz(graph, './graph.gv')
line_graph = gen_line_graph(graph)
linegraph_to_graphviz(line_graph, './line_graph.gv')

