import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.pesi=[]
        self.maggiori=[]


    def creaGrafo(self, ):
        self.nodi = DAO.getNodi()
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges()
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self,):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni()
        for connessione in allEdges:
            nodo1 = connessione.v1
            nodo2 = connessione.v2
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    self.grafo.add_edge(nodo1, nodo2, weight=connessione.peso)
                    self.pesi.append(connessione.peso)
    def minMax(self):
        return max(self.pesi), min(self.pesi)
    def contaArchi(self,soglia):
        contMaggiori=0
        contMinori=0
        for arco in self.grafo.edges:
            if self.grafo[arco[0]][arco[1]]["weight"]>soglia:
                contMaggiori+=1
                self.maggiori.append((arco[0],arco[1]))
            if self.grafo[arco[0]][arco[1]]["weight"] < soglia:
                contMinori += 1

        return contMaggiori, contMinori

    def getBestPath(self):
        self._soluzione = []
        self._costoMigliore = 0
        print(self.maggiori)
        for arco in self.maggiori:
            parziale = [arco]
            self._ricorsione(parziale)
            parziale.pop()
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale):
        if self.peso(parziale) > self._costoMigliore:
                    self._soluzione = copy.deepcopy(parziale)
                    self._costoMigliore = self.peso(parziale)

        for n in self.grafo.successors(parziale[-1][1]):
            if (parziale[-1][1],n) in self.maggiori:
                if (parziale[-1][1],n) not in parziale and (n,parziale[-1][1]) not in parziale:
                    parziale.append((parziale[-1][1],n))
                    self._ricorsione(parziale)
                    parziale.pop()


    def peso(self, listaArchi):
        pesoTot = 0
        for arco in listaArchi:
            pesoTot += self.grafo[arco[0]][arco[1]]["weight"]
        return pesoTot
