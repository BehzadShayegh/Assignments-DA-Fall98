from math import inf

class Node :
    def __init__(self) :
        self.edges = dict()
    
    def add_edge(self, m, w) :
        self.edges[m] = w

    def __str__(self) :
        string = ''
        for e,w in self.edges.items() :
            string += str(e)+'('+str(w)+')'+'  '
        return string

class Graph :
    def __init__(self) :
        self.nodes = dict()
    
    def add_node(self, n) :
        self.nodes[n] = Node()
        return self.nodes[n]

    def __str__(self) :
        string = ''
        for n,N in self.nodes.items() :
            string += str(n)+' => '+str(N)+'\n'
        return string

    def ford_fulkerson(self, source, target) :
        n = len(self.nodes)
        totalcost = 0
        while True :
            cost = 100000
            index = 0
            line = [source]
            backward = [-1]*n
            backward[source] = -2
            head = source
            while index < len(line) :
                head = line[index]
                if head == target :
                    break
                for key,val in self.nodes[head].edges.items() :
                    if val == 0 or backward[key] != -1 :
                        continue
                    backward[key] = head
                    line.append(key)
                index += 1
            if head != target : break
            while head != source :
                cost = min(cost,self.nodes[backward[head]].edges[head])
                head = backward[head]
            head = target
            while head != source :
                self.nodes[backward[head]].edges[head] -= cost
                self.nodes[head].edges[backward[head]] += cost
                head = backward[head]
            totalcost += cost
        return totalcost

n,m,c = list(map(int,input().split()))
g = Graph()
root = g.add_node(m+n)
target = g.add_node(m+n+1)
for i in range(n) :
    node = g.add_node(i)
    node.add_edge(m+n+1,c)
    target.add_edge(i,0)
for i in range(m) :
    node = g.add_node(n+i)
    root.add_edge(n+i,1)
    node.add_edge(m+n,0)
    for j in list(map(int,input().split()))[1:] :
        node.add_edge(j,1)
        g.nodes[j].add_edge(n+i,0)

# print(g)
# print()
print(g.ford_fulkerson(m+n,m+n+1))