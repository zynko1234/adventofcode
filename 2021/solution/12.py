import constants
import util


def solve(input):
    ansA = None
    ansB = None

    normalized_input = normalize_input(input)

    ansA = solutionA(normalized_input)
    ansB = solutionB(normalized_input)
    return ansA, ansB


def normalize_input(input):
    output = None
    vertexes = []
    tmp_lvertex = None
    tmp_rvertex = None

    for entry in input:
        tmp_split = entry.split('-')
        lvert = tmp_split[0]
        rvert = tmp_split[1]

        lvert_exists, lvert_instance = vertex_constructed(vertexes, lvert)

        if lvert_exists == False:
            tmp_lvertex = Vertex(lvert)
            vertexes.append(tmp_lvertex)
        else:
            tmp_lvertex = lvert_instance

        rvert_exists, rvert_instance = vertex_constructed(vertexes, rvert)

        if rvert_exists == False:
            tmp_rvertex = Vertex(rvert)
            vertexes.append(tmp_rvertex)
        else:
            tmp_rvertex = rvert_instance

        # Connect these vertexes to eachother.
        tmp_lvertex.add_connection(tmp_rvertex)
        tmp_rvertex.add_connection(tmp_lvertex)

    # We just want the start vertex to operate on.
    for vertex in vertexes:
        if vertex.symbol == 'start':
            output = vertex

    return output


def vertex_constructed(vertex_list, chk_symbol):
    validity = False
    ret_vertex = None

    for entry in vertex_list:
        if entry.symbol == chk_symbol:
            validity = True
            ret_vertex = entry

    return validity, ret_vertex


def solutionA(input):
    output = 0

    return output


def solutionB(input):
    output = 0

    return output


class Vertex(object):
    def __init__(self, symbol) -> None:
        self.symbol = symbol
        self.connections = []

    def add_connection(self, in_vertex: 'Vertex'):
        exists = False

        for element in self.connections:
            if element.symbol == in_vertex.symbol:
                exists = True

        if exists is False:
            self.connections.append(in_vertex)
