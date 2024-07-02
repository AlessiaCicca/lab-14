import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        grafo = self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        massimo, minimo=self._model.minMax()
        self._view.txt_result.controls.append(ft.Text(f"Informazioni sui pesi degli archi -"
                                                      f"valore minimo: {minimo} e valore massimo: {massimo}"))
        self._view.update_page()

    def handle_countedges(self, e):
        massimo, minimo = self._model.minMax()
        soglia=self._view.txt_name.value
        if soglia=="":
            self._view.create_alert("Inserire un valore di soglia")
            pass
        if float(soglia)< minimo or float(soglia)>massimo:
            self._view.create_alert(f"Inserire un valore di soglia compreso tra {minimo} e {massimo}")
            pass
        maggiori, minori=self._model.contaArchi(float(soglia))
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {maggiori} e "
                                                      f"numero archi con peso minore della soglia: {minori}"))
        self._view.update_page()

    def handle_search(self, e):
        costo, listaNodi = self._model.getBestPath()
        self._view.txt_result3.controls.append(ft.Text(f"Peso cammino massimo: {costo}"))
        for nodo in listaNodi:
            self._view.txt_result3.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()
