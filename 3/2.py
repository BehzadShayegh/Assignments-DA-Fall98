class Edge:
    def __init__(self, dest, weight) :
        self.dest = dest
        self.weight = weight

    def __str__(self) :
        return str(self.dest)+' ('+str(self.weight)+')'
    
    def __repr__(self):
        return str(self)

    def __lt__(self, other) :
        return self.weight < other.weight

    def __gt__(self, other) :
        return self.weight > other.weight

    def __eq__(self, other) :
        return self.weight == other.weight

class Node:
    def __init__(self, id) :
        self.id = id
        self.edges = list()

    def add_edge(self, j, w) :
        self.edges.append(Edge(j,w))

    def __str__(self) :
        string = str(self.id)+" :\n"
        for e in self.edges :
            string += '\t'+e.__str__()+'\n'
        return string

class Graph:
    def __init__(self) :
        self.nodes = dict()
        self.set = set()

    def add_node(self,i) :
        if i in self.set :
            return
        self.nodes[i] = Node(i)
        self.set.add(i)

    def add_edge(self,i,j,w) :
        if i == j : return
        self.nodes[i].add_edge(j,w)
        self.nodes[j].add_edge(i,w)

    def __str__(self) :
        string = ""
        for n in self.nodes.values() :
            string += n.__str__()+'\n'
        return string
    
    def size(self) :
        return len(self.nodes)

    def dijkstra(self, start, target) :
        s = set()
        choices = dict()
        choices[start] = 0
        cost = 0
        s_no = 0
        max_s_no = self.size()
        while s_no < max_s_no :
            choice = min(choices, key=choices.get)
            cost = choices[choice]
            if choice == target :
                return cost
            del choices[choice]
            s.add(choice)
            s_no += 1
            for n in self.nodes[choice].edges :
                if n.dest in s :
                    continue
                choices[n.dest] = min(n.weight+cost,choices.get(n.dest, n.weight+cost))
        return -1

n,s,t = list(map(int, input().split()))
graph = Graph()
for a in range(n) :
    inp = sorted(list(map(int, input().split()))[1:])
    for i,node in enumerate(inp) :
        graph.add_node(node)
        for j in range(i) :
            graph.add_edge(node, inp[j], node-inp[j])

print(graph.dijkstra(s,t))