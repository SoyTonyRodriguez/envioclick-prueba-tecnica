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


class Solution:
    # Class constructor.
    def __init__(self, sort_field='priority', sort_type=sort_type):
        self.sort_field = sort_field
        self.sort_type = sort_type

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
        pivot_value = pivot.get(self.sort_field)

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
            if item.get(self.sort_field) < pivot_value:
                head.append(item)
            elif item.get(self.sort_field) > pivot_value:
                tail.append(item)
            else:
                middle.append(item)
            i += 1

        # Recursively sort the head and tail partitions and concatenate the
        # results with the middle partition to produce the sorted list.
        if self.sort_type == 'ASC':
            return self.quicksort(head) + middle + self.quicksort(tail)
        elif self.sort_type == 'DESC':
            return self.quicksort(tail) + middle + self.quicksort(head)
        else:
            print("Sort type not supported")
            return data


if __name__ == "__main__":
    # Create an instance of the solution class.
    solution = Solution()

    # List to store the filtered data that meets the criteria specified
    filter_data = []

    print(f"initial data --> {len(data)}")
    print(data)

    # List to store the remaining data that does not meet the filter criteria
    data_remaining = []

    # Iterate through the input data and apply the filters specified in the
    # input_filter list. Each item is evaluated against all filters, and if it
    # meets all criteria, it is added to the filter_data list; otherwise, it
    # is added to the data_remaining list.
    i = 0
    while i < len(data):
        item = data[i]
        match = True

        # Apply all filters to the current item. If any filter is not
        # satisfied, the item is marked as not matching and the loop breaks.
        j = 0
        while j < len(input_filter):

            # Extract the key, operator, and value from the current filter.
            key, operator, value = input_filter[j]

            # If the item does not have the key specified in the filter,
            # it cannot match the filter criteria, so it is marked as not
            # matching and the loop breaks.
            if item.get(key) is None:
                match = False
                break

            # Evaluate the comparison between the item's value for the key and
            # the filter's comparison value using the specified operator. If
            # the comparison fails, the item is marked as not matching and the
            # loop breaks.
            if not solution.evaluate_comparison(
                item.get(key), operator, value
            ):
                match = False
                break
            j += 1

        # If the item matches all filters, it is added to the filter_data list;
        # otherwise, it is added to the data_remaining list.
        if match:
            filter_data.append(item)
        else:
            data_remaining.append(item)

        i += 1

    # Sort the filtered data using the quicksort method.
    # The sorting is based on the field specified in the sort_field attribute
    sorted_filter_data = solution.quicksort(filter_data)
    # print("Sorted filter data")
    # print(sorted_filter_data)

    # Combine the sorted filtered data with the remaining data to produce the
    # final result. The sorted filtered data is placed at the beginning of the
    # list, followed by the remaining data in its original order.
    final_result = sorted_filter_data + data_remaining
    print(final_result)
