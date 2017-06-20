class Nodo:
    """ Esta clase representa cada uno de los Nodos de la lista
   """
   
    # Atributos
    valor = None # el valor del nodo
    siguiente = None # apunta al siguiente nodo
    anterior = None # apunta al nodo anterior
 
    # Constructor
    def __init__(self, valor, siguiente, anterior):
        self.valor = valor
        self.siguiente = siguiente
        self.anterior = anterior
 
 
class ListaSimple:
    """ Esta clase representa una Lista Simple, donde cada Nodo
       solo conoce al Nodo siguiente
   """
   
    # Atributos
    raiz = None # es el Nodo raiz de la lista
    ultimo = None #Se hace referencia al nodo final
    anterior = None 
   
    def getVacio(self):
        if self.raiz==None:
            return True

    # Constructor
    def __init__(self, nodo):
        self.raiz = nodo
        self.ultimo = nodo
 
    # Metodos
    def insertar(self, valor):
        """ Inserta un nodo nuevo con valor en la lista
       """
        nuevo = Nodo(valor, None, None)
        # Caso 1: la lista esta vacia
        if self.raiz == None:
            self.raiz = nuevo
            self.siguiente = nuevo
            self.anterior = nuevo
        # Caso 2: el nodo nuevo va antes de la raiz
        elif nuevo.valor < self.raiz.valor:
            nuevo.siguiente = self.raiz
            nuevo.siguiente.anterior=nuevo
            self.raiz = nuevo
            self.anterior= nuevo
        else:
            insertado = False
            actual = self.raiz
            siguiente=actual.siguiente
            anterior = actual;
            # Caso 3: el nodo nuevo va entre 2 nodos ya existentes
            while actual != None:
                if nuevo.valor < actual.valor:
                    anterior.siguiente = nuevo
                    siguiente.anterior= nuevo
                    nuevo.siguiente = siguiente
                    insertado = True
                    break
                anterior = actual
                actual = actual.siguiente
            # Caso 4: el nodo nuevo va al final
            if not insertado:
                nuevo.anterior=anterior
                anterior.siguiente = nuevo;
 
    def borrarPrimero(self):
        """ Borra un nodo existente con valor de la lista
       """
        #cuando la lista esta vacia, no hay nada que eliminar
        if self.getVacio()==True:
            print ("No hay valores en la lista a eliminar")
            #Cuando solo hay un nodo creado en la lista
        elif self.raiz == self.siguiente:
            self.raiz=None
            self.siguiente=None
        else:
            temp=self.raiz
            self.raiz=self.raiz.siguiente
            temp=None
            print ("Se eliminó el primer nodo")
        pass
 
    def imprimir(self):
        """ Imprime todo los elementos de la lista
       """
        nodo = self.raiz
        while nodo != None:
            print(nodo.valor)
            nodo = nodo.siguiente
 
 
# Programa Principal
 
ls = ListaSimple(None)
ls.insertar("Juan")
ls.insertar("Marta")
ls.insertar("Maria")
ls.insertar("Lucia")
ls.insertar("Lucas")
ls.insertar("Felipe")
ls.insertar("Pedro")
ls.insertar("Diana")
ls.imprimir()
