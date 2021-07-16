class PresentationLayer:
    def __init__(self):
        self.name = "PresentationLayer"
    
    def setLowerLayer(self,lowerLayer):
        self.lowerLayer = lowerLayer
        
    def servicio3(self,param):
        print('entramos a : ', self.name)
        self.lowerLayer.servicio2(param)
        print("terminanos ",self.name)


class LogicLayer:
    def __init__(self):
        self.name = "LogicLayer"
    
    def setLowerLayer(self,lowerLayer):
        self.lowerLayer = lowerLayer
        
    def servicio2(self,param):
        print('entramos a : ', self.name)
        self.lowerLayer.servicio1(param)
        print("terminanos ",self.name)

class DataLayer:
    def __init__(self):
        self.name = "DataLayer"
    
    def setLowerLayer(self,lowerLayer):
        self.lowerLayer = lowerLayer
        
    def servicio1(self,param):
        print('dentro de : ',self.name)
        print('ejecutamos servicio1 con : ',param)

if __name__ == "__main__":
    ui = PresentationLayer()
    logic = LogicLayer()
    data = DataLayer()

    #conectando las capas
    ui.setLowerLayer(logic)
    logic.setLowerLayer(data)

    #utilizamos el servicio
    ui.servicio3("Giancarlo")