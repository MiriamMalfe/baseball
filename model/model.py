import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def getListaAnni(self):
        anni = DAO.getAnno()
        return anni

    def aggiungiNodi(self, anno):
        squadre = DAO.getSquadreAnno(anno)
        self.grafo.add_nodes_from(squadre)

    def aggiungiArchi(self, anno):
        squadre = DAO.getSquadreAnno(anno)
        for s1 in squadre:
            for s2 in squadre:
                if s1==s2:
                    pass
                else:
                    salary1 = DAO.salariSquadra(s1.teamCode, anno)
                    salary2 = DAO.salariSquadra(s2.teamCode, anno)
                    peso = salary1+salary2
                    self.grafo.add_edge(s1, s2, weight=peso)


    def creaGrafo(self, anno):
        self.aggiungiNodi(anno)
        self.aggiungiArchi(anno)

        print(f"numero di nodi: {self.grafo.number_of_nodes()}")
        print(f"numero di archi: {self.grafo.number_of_edges()}")

    def analizzaDettagli(self, squadra):
        vicini = self.grafo.neighbors(squadra)  #lista di squadre vicine al nodo che considero
        listaPesi={}   #chiave:vicino, valore:peso
        for n in vicini:
            peso = self.grafo.get_edge_data(squadra, n)["weight"]  #per vedere il peso dei vicini del nodo che considero (squadra)
            listaPesi[n]=peso
            stringa = f"lista squadre vicine: "
            for k,v in sorted(listaPesi.items(), key=lambda item: item[1], reverse=True): #ordina la lista dei pesi in base al valore relativo alla chiave
                stringa = stringa + f"\n{k.teamCode} {k.name} {v}"
        return stringa



