# нужно класс Соединение доопределить переменную ID_connection - поток данных от
# bluetooth
# функция конннетион возвращает объект соединения
# функция гет дата получает объект соединения и возвращает данные

class ConnectionSeeds :
    def __init__(self, numOfPoint: int = 0, connectionState: bool = False, data: int = 0):
        self.numOfPoint = numOfPoint
        self.connectionState = connectionState
        self.data = data

    def _repr_(self):
        return 'ConfigSeeds(%i, %s) ' % (self.numOfPoint, self.connectionState, self.data)

    def connection(self):
        pass

    def getdata(self):
        pass