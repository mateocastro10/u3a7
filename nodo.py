class Nodo:
    __aparato=None
    __siguiente=None
    def __init__(self, personal):
        self.__aparato=personal
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__aparato
