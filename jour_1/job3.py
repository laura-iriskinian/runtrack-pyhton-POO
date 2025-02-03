class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        nombre1 = self.nombre1
        nombre2 = self.nombre2
        result = nombre1 + nombre2
        return result
    
operation = Operation(12, 3)
print(operation.addition())