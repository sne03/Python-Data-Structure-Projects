#  File: Adjacency.py
#  Description: Converts an edge list into an adjacency matrix
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number:
def edge_to_adjacency(edge_list):
    # Add Your code here!
    verts = []
    for i in range(len(edge_list)):
        verts.append(edge_list[i][0])
        verts.append(edge_list[i][1])
    verts = list(set(verts))
    verts.sort()
    adj_matrix = [[0 for i in range(len(verts))] for j in range(len(verts))]
    dict_key = {}
    for i in range(len(verts)):
        dict_key[verts[i]] = i
    for i in range(len(edge_list)):
        adj_matrix[dict_key[edge_list[i][0]]][dict_key[edge_list[i][1]]] = edge_list[i][2]
    return adj_matrix
# ------ DO NOT CHANGE BELOW HERE ------ #
import ast
def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))
if __name__ == "__main__":
    main()