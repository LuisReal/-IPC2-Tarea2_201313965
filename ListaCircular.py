class nodo:
  def __init__(self, valor = None, siguiente = None, anterior = None):
    self.valor = valor
    self.siguiente = siguiente
    self.anterior = anterior

class lista_circular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, valor):
        nuevo = nodo(valor = valor)
        if self.primero is None:
            self.primero =  nuevo
            
        else:      
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo

        self.ultimo = nuevo
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrer(self):
        if self.primero is None:
            return
    
        actual = self.primero
        print("valor: ", actual.valor)
    
        while actual.siguiente != self.primero and actual != None:
            actual = actual.siguiente
            print("valor: ", actual.valor)

    def buscar(self, numero):
        
        if self.primero is None:
            return

        actual = self.primero

        while actual.siguiente != self.primero and actual.valor != numero:
            actual = actual.siguiente

        if actual.valor == numero:
            print("anterior: ", actual.anterior.valor , " actual: ", actual.valor, " siguiente: ", actual.siguiente.valor)
        else:
            print("No se encontro el nodo")



lista_c = lista_circular()

lista_c.insertar(5)
lista_c.insertar(4)
lista_c.insertar(19)
lista_c.insertar(22)
lista_c.insertar(1)

numero = int(input("seleccione un numero: "))
lista_c.buscar(numero)
lista_c.recorrer()
