class Calculadora():
    def __init__(self, n1=int, n2=int) -> None:
        self.n1 = n1
        self.n2 = n2
    
    def soma(self):
        return self.n1 + self.n2
    
    def subtrai(self):
        return self.n1 - self.n2
    
    def divide(self):
        return self.n1 / self.n2
    
    def multiplica(self):
        return self.n1 * self.n2