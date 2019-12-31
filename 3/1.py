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

    def add_node(self,i) :
        self.nodes[i] = Node(i)

    def add_edge(self,i,j,w) :
        if i == j : return
        self.nodes[i].add_edge(j,w)

    def __str__(self) :
        string = ""
        for n in self.nodes.values() :
            string += n.__str__()+'\n'
        print(string)
        return string
    
    def size(self) :
        return len(self.nodes)

    def dijkstra(self, start) :
        s = set()
        choices = dict()
        choices[start] = 0
        cost = 0
        s_no = 0
        max_s_no = self.size()
        while s_no < max_s_no :
            choice = min(choices, key=choices.get)
            cost += choices[choice]
            del choices[choice]
            s.add(choice)
            s_no += 1
            for n in self.nodes[choice].edges :
                if n.dest in s :
                    continue
                choices[n.dest] = min(n.weight,choices.get(n.dest, n.weight))
        return cost

n = int(input())
graph = Graph()
for i in range(n+1) :
    graph.add_node(i)
for i in range(n) :
    for j,w in enumerate(list(map(int, input().split()))) :
        graph.add_edge(i,j,w)
for j,w in enumerate(list(map(int, input().split()))) :
    graph.add_edge(n,j,w)
    graph.add_edge(j,n,w)
print(graph.dijkstra(n))