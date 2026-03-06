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


if __name__ == "__main__":
    # Create an instance of the solution class.
    solution = Solution()

    # obtener filtros
    filter_data = []

    print(f"initial data --> {len(data)}")
    print(data)

    i = 0
    while i < len(data):
        item = data[i]

        # Aplicar todos los filtros
        j = 0
        while j < len(input_filter):
            key, operator, value = input_filter[j]
            match = True
            if not solution.evaluate_comparison(
                item.get(key), operator, value
            ):
                match = False
                break

            # if all filters match, add the item to the filtered data list.
            if match:
                filter_data.append(item)
            j += 1
        i += 1

    print(f"filtered data --> {len(filter_data)}")
    print(filter_data)
