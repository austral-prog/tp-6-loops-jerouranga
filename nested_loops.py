# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    result = []
    for fila in matrix:
        for elemento in fila:
            result.append(elemento)

    return result


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    lista = []

    for fila in matrix:
        contador = 0
        for elemento in fila:
            contador += elemento
        lista.append(contador)
    return lista


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """

    list = []
    num_cols = len(matrix[0])

    for col in range(num_cols):
        suma = 0
        for fila in range(len(matrix)):
            suma += matrix[fila][col]
        list.append(suma)

    return list
