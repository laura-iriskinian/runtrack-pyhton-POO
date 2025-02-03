class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def print(self):
        nombre1 = self.nombre1
        nombre2 = self.nombre2
        return (f"Le nombre1 est {nombre1}, \nLe nombre2 est {nombre2}")
    
operation = Operation(12, 3)
print(operation.print())