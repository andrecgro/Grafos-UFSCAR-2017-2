def prim(g):
	tmp = g.copy()
	push = heappush
	pop = heappop
	nodes = tmp.nodes()
	
	for n in nodes:
		tmp.node[n]['lambda'] = 999999999
		tmp.node[n]['predecessor'] = None
	
	tmp.node[0]['lambda'] = 0
	q = []
	visitados = []
	
	for n in nodes:
		push(q, (tmp.node[n]['lambda'], n))
		
	while q:
		u = pop(q)
		u = u[1]
		visitados.append(u)
		for v in tmp.neighbors(u):
			if tmp.node[v]['lambda'] > tmp[u][v]['peso'] and not v in visitados:
				q.remove((tmp.node[v]['lambda'], v))
				tmp.node[v]['lambda'] = tmp[u][v]['peso']
				push(q, (tmp.node[v]['lambda'], v))
				tmp.node[v]['predecessor'] = u
	
	P = nx.Graph()
	for u in tmp.nodes():
		P.add_node(u)
		if tmp.node[u]['predecessor'] is not None:
			P.add_edge(u, tmp.node[u]['predecessor'])
			P[u][tmp.node[u]['predecessor']]['peso'] = tmp[u][tmp.node[u]['predecessor']]['peso']
	return P


def twiceAround(self, source):
    T = prim(self)
    T = nx.MultiGraph(T)
    T.add_edges_from(T.edges(data=True))
	
    eulerian_circuit = nx.eulerian_circuit(T, source)

    visitados = []
    ciclohamiltoniano = []

    for u,v in eulerian_circuit:
        if u not in visitados:
            visitados.append(u)
            ciclohamiltoniano.append(u)

    ciclohamiltoniano.append(ciclohamiltoniano[0])
    grafohamiltoniano = nx.create_empty_copy(self.graph)

    for i in range(len(ciclohamiltoniano)-1):
        edge = (ciclohamiltoniano[i], ciclohamiltoniano[i+1])
        grafohamiltoniano.add_edge(*edge, self.graph.get_edge_data(*edge))
        
    return (grafohamiltoniano, ciclohamiltoniano)