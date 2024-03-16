def ordenar_bloques(myArray, n):
  i = 0
  bloqueActual = []  # Lista para almacenar números de bloque (enteros)
  bloqueVacio = True

  while i < n:
    if myArray[i] == 0:
      if not bloqueVacio:
        # Ordena e imprime el bloque
        print(" ".join(str(numero) for numero in sorted(bloqueActual)))
      else:
        print("x")  # Imprime "x" para bloque vacío
      bloqueActual = []
      bloqueVacio = True
    else:
      bloqueVacio = False
      bloqueActual.append(myArray[i])  # Agrega el número a la lista del bloque
    i += 1

  # Maneja el último bloque (si no está vacío)
  if not bloqueVacio:
    print(" ".join(str(numero) for numero in sorted(bloqueActual)))


# Ejemplo de uso
myArray = [1, 3, 2, 0, 7, 8, 1, 3, 0, 0, 6, 7, 1]
n = len(myArray)
ordenar_bloques(myArray, n)
