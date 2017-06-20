# Autor: Juan Pablo Trejos Rodriguez
# Programa: ordenamiento.py
# Fecha: Sat Oct 3 07:51:18 COT 2015
# Descripcion: Este programa usa distintos metodos para ordenar una lista

import random, time

def aleatorios(n):
    """ (numero) -> (lista, lista, lista)

    retorna una lista de n numeros para cada caso: azar, ordenado, inverso

    """
    ordenado = list(range(0,n))
    azar = ordenado.copy()
    inverso = ordenado.copy()
    random.shuffle(azar)
    inverso.reverse()
    return (azar, ordenado, inverso)

def test(metodo, azar, ordenado, inverso):
    """ (funcion, lista, lista, lista) -> None
    
    Prueba el metodo de ordenamiento con una lista de tamano n
    
    """
    def prueba(metodo, lista):
        copia = lista.copy()
        ini = time.clock() # guarda la hora de inicio
        metodo(copia)
        fin = time.clock() # guarda la hora final
        return fin - ini
    t_azar = prueba(metodo, azar)
    t_ordenado = prueba(metodo, ordenado)
    t_inverso = prueba(metodo, inverso)
    print("{} ({}) : {:f}, {:f}, {:f}".format(metodo.__name__, n, t_azar, t_ordenado, t_inverso))

# Metodos de Ordenamiento

def insercion(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de insercion (Insertion)
    http://www.sorting-algorithms.com/insertion-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> insercion(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    for i in range(1, len(lista)):
        k = i
        while k > 0 and lista[k] < lista[k-1]:
            # intercambia lista[k] y lista[k-1]
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k-=1 # es igual a k=k-1

def seleccion(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de seleccion (Selection)
    http://www.sorting-algorithms.com/selection-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> seleccion(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    n = len(lista)
    for i in range(0, n):
        k = i
        for j in range(i+1, n):
            if lista[j] < lista[k]:
                k = j
        # intercambia lista[i] y lista[k]
        lista[i], lista[k] = lista[k], lista[i]    

def burbuja(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de burbuja (Bubble)
    http://www.sorting-algorithms.com/bubble-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> burbuja(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
    n = len(lista)
    for i in range(0, n):
        swapped = False
        j = n - 1
        while j > i:
            if lista[j] < lista[j-1]:
                # intercambia lista[j] y lista[j-1]
                lista[j], lista[j-1] = lista[j-1], lista[j]
                swapped = True
            j -= 1
        if not swapped: break

def shell(lista):
    """ (lista) -> None
    
    ordena la lista por el metodo de shell (Shell)
    http://www.sorting-algorithms.com/shell-sort
    
    >>> lista = [3, 6, 7, 4, 9, 2, 0, 8, 5, 1]
    >>> shell(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    """
def shell(lista):
 
 length = len(lista)
 gap = int(length/2)
 while(gap >= 1):
  i = gap
  while(i < length):
   value = lista[i]
   j = i
   while(j-gap >= 0 and value < lista[j - gap]):
    lista[j] = lista[j - gap]
    j -= gap
   lista[j] = value
   i+=1
  gap = int(gap/2)



import sys
def merge_sort(lista):
	merge_sort2(lista, 0, len(lista)-1)
	
def merge_sort2(lista, first, last):
	if first < last:
		middle = (first + last)//2
		merge_sort2(lista, first, middle)
		merge_sort2(lista, middle+1, last)
		merge(lista, first, middle, last)
		
def merge(lista, first, middle, last):
	L = lista[first:middle+1]
	R = lista[middle+1:last+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i = j = 0
	
	for k in range (first, last+1):
		if L[i] <= R[j]:
			lista[k] = L[i]
			i += 1
		else:
			lista[k] = R[j]
			j += 1



from random import randint

def quickSort(lista):
    # List of 0 or 1 items is already sorted
    if len(lista) <= 1:
        return lista
    else:
        # Pivot can be chosen randomly
        pivotIndex = randint(0, len(lista)-1)
        pivot = lista[pivotIndex]
        # Elements lower than and greater than pivot
        lesser, greater = [], []

        for index in range(len(lista)):
            # Don't do anything if you're at the pivot
            if index == pivotIndex:
                pass
            else:
                # Sort elements into < pivot and >= pivot
                el = lista[index]
                if el < pivot:
                    lesser.append(el)
                else:
                    greater.append(el)
                    
        # Sort lesser and greater, concatenate results
        return quickSort(lesser) + [pivot] + quickSort(greater)

def heapsort(lista):
    """Run heapsort on a list a
    >>> a = [32,46,77,4344564,7322,3,46,7,32457,7542,4,667,54,]
    >>> heapsort(a)
    >>> print(a)
    [3, 4, 7, 32, 46, 46, 54, 77, 667, 7322, 7542, 32457, 4344564]
    """

    heapify(lista, len(lista))
    end = len(lista)-1
    while end > 0:
        lista[end], lista[0] = lista[0], lista[end]
        end -= 1
        sift_down(lista, 0, end)

def heapify(lista, count):
    start = int((count-2)/2)
    while start >= 0:
        sift_down(lista, start, count-1)
        start -= 1

def sift_down(lista, start, end):
    root = start
    while (root*2+1) <= end:
        child = root * 2 + 1
        swap = root
        if lista[swap] < lista[child]:
            swap = child
        if (child + 1) <= end and lista[swap] < lista[child+1]:
            swap = child+1
        if swap != root:
            lista[root], lista[swap] = lista[swap], lista[root]
            root = swap
        else:
            return
# Pruebas
if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Programa Principal
for n in [100, 1000,10000]:
    azar, ordenado, inverso = aleatorios(n)
    test(insercion, azar, ordenado, inverso)
    test(seleccion, azar, ordenado, inverso)
    test(burbuja, azar, ordenado, inverso)
    test(shell, azar, ordenado, inverso)
    test(merge_sort, azar, ordenado, inverso)
    test(heapsort, azar, ordenado, inverso)
    test(quickSort, azar, ordenado, inverso)
