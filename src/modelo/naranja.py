from modelo.canasta import Canasta


class Naranja:

    def __init__(self):
        self.__peso = 0
        self.granja = "12-208"
        self.fecha_de_cosecha= "3 de agosto"
        self.canasta=  None

    def __init__(self, granja, peso):
        self.__peso =peso  
        self.granja = granja 
        self.fecha_de_cosecha= "3 de agosto"
        self.canasta=  None

    def recoger(self,canasta:Canasta):
        self.canasta = canasta
        canasta.naranjas.append(self)
        print("naranja agregada")

    def obtener_peso(self):
        return self.__peso