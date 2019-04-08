class node:
    def __init__(self, id, color_id):
        self.id = id
        self.color_id = color_id
        self.childs = {}


n_nodes = int(input('Indique el numero de nodos:'))
color_list = input('Indique los colores de sus nodos:').split(' ')

i = 1
nodes = {}
tree = {}

while i <= n_nodes:
    nodes[i] = node(i, color_list[i - 1])
    i = i +1

i = 1
while i <= n_nodes - 1:
    relation = input('Indique relacion:').split(' ')
    nodes[int(relation[0])].childs[int(relation[1])] = nodes[int(relation[1])]
    i = i + 1

nodes = nodes[1]
