import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDY(self, dd: ft.Dropdown()):
        anni = self._model.getListaAnni()
        for a in anni:
            dd.options.append(ft.dropdown.Option(text=a,
                                                 data=a,
                                                 on_click=self.readDDY))

    def readDDY(self, e):
        if e.control.data is None:
            self.anno = None
        else:
            self.anno = e.control.data   #in caso mi servisse di nuovo l'anno all'interno di qualsiasi metodo di controller
            squadre = DAO.getSquadreAnno(self.anno)
            lunghezza = len(squadre)
            stringa=f"Quantità squadre: {lunghezza}"
            for s in squadre:
                stringa = stringa + f"\n {s.teamCode} ({s.name})"
                self._view._ddSquadra.options.append(ft.dropdown.Option(text=s.teamCode,
                                                     data=s,
                                                     on_click=self.readDDS))
            self._view._txtOutSquadre.controls.clear()
            self._view._txtOutSquadre.controls.append(ft.Text(stringa))
            self._view.update_page()

    def readDDS(self, e):
        if e.control.data is None:
            self.squadra = None
        else:
            self.squadra = e.control.data


    def handleCreaGrafo(self, e):
        self._model.creaGrafo(self.anno)


    def handleDettagli(self, e):
        stringa = self._model.analizzaDettagli(self.squadra)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(stringa))
        self._view.update_page()

    def handlePercorso(self, e):
        pass