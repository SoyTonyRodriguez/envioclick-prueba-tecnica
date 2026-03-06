# Ejercicio 2
# Dado un arreglo de diccionarios con diferentes atributos, se deben ordernar
# por prioridad encontrada en el atributo del diccionario con nombre:
# “priority”, adicionalmente se debe considerar que el ordenamiento puede ser
# ascendente o descendente dependiendo de la entrada al algoritmo, tambien
# dentro del listado de elementos unicamente se ordenaran aquellos elementos
# que cumplan con los criterios de un filtro de entrada, este filtro es
# dinamico y puede contener N filtros.

# Como salida se debe entregar un listado de elementos donde los primeros
# elementos son los elementos filtrados y ordenados segun los criterios y los
# siguientes elementos son los restantes que no cumplen los criterios sin
# alterar su orden original de entrada.

from python_test.input import data, input_filter, sort_type

SORT_FIELD = 'priority'
SORT_TYPE = sort_type


class Solution:
    # Class constructor.
    def __init__(self):
        pass

    # Compare two values based on a specified operator.
    # If the operator is not recognized, the function returns False.
    def evaluate_comparison(self, data_value, operator, comparison_value):
        """Compara dos valores según el operador"""
        if operator == '=':
            return data_value == comparison_value
        elif operator == '==':
            return data_value == comparison_value
        elif operator == '!=':
            return data_value != comparison_value
        elif operator == '<':
            return data_value < comparison_value
        elif operator == '>':
            return data_value > comparison_value
        elif operator == '<=':
            return data_value <= comparison_value
        elif operator == '>=':
            return data_value >= comparison_value
        return False

    # Sort a list of dictionaries based on the value of a specified field
    # using the quicksort algorithm.
    # The sorting order (ascending or descending) is determined by the
    # SORT_TYPE variable.
    def quicksort(self, data):
        # Base case: if the list has 0 or 1 elements, it is already sorted.
        if len(data) <= 1:
            return data

        # Choose a pivot element from the list
        pivot = data[len(data) // 2]
        pivot_value = pivot.get(SORT_FIELD)

        # Partition the list into three parts: elements less than the pivot,
        # elements equal to the pivot, and elements greater than the pivot.
        head = list()
        middle = list()
        tail = list()

        # Iterate through the list and partition the elements based on their
        # comparison with the pivot value.
        i = 0
        while i < len(data):
            item = data[i]

            # Compare the value of the SORT_FIELD in the current item with the
            # pivot value and partition accordingly.
            if item.get(SORT_FIELD) < pivot_value:
                head.append(item)
            elif item.get(SORT_FIELD) > pivot_value:
                tail.append(item)
            else:
                middle.append(item)
            i += 1

        # Recursively sort the head and tail partitions and concatenate the
        # results with the middle partition to produce the sorted list.
        if SORT_TYPE == 'ASC':
            return self.quicksort(head) + middle + self.quicksort(tail)
        elif SORT_TYPE == 'DESC':
            return self.quicksort(tail) + middle + self.quicksort(head)
        else:
            print("Sort type not supported")
            return []


if __name__ == "__main__":
    # Create an instance of the solution class.
    solution = Solution()

    # obtener filtros
    filter_data = []

    print(f"initial data --> {len(data)}")
    print(data)

    data_remaining = []

    i = 0
    while i < len(data):
        item = data[i]
        match = True

        # Aplicar todos los filtros
        j = 0
        while j < len(input_filter):
            key, operator, value = input_filter[j]
            if not solution.evaluate_comparison(
                item.get(key), operator, value
            ):
                match = False
                break
            j += 1

        if match:
            filter_data.append(item)
        else:
            data_remaining.append(item)

        i += 1

    sorted_filter_data = solution.quicksort(filter_data)
    print("Resultados filtrados ordenados")
    print(sorted_filter_data)

    final_result = sorted_filter_data + data_remaining
    print(final_result)
