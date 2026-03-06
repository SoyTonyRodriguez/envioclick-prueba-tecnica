# Ejercicio 3
# Crear una representación básica de una hoja de excel, esta representación
# debe contar con celda que se representan por filas y columnas, debe haber 6
# funcionalidades basicas dentro de esta hoja
#  - Insertar información en una celda
#  - Actualizar información en una celda
#  - Validar si una celda tiene información dentro
#  - Mostrar un preview de la hoja entera
#  - Dada una fila recuperar todos los elementos e imprimir la suma de todos
#       los valores dados
#  - Dada una columna recuperar todos los elementos e imprimir la suma de todos
#       los valores dados

class SheetExcel():
    # Class constructor
    def __init__(self, filas=5, columnas=10):
        self.filas = filas
        self.columnas = columnas
        self.hoja = list()
        i = 0
        while i < self.filas:
            list_columnas = list()
            j = 0
            while j < self.columnas:
                list_columnas.append(None)
                j += 1

            self.hoja.append(list_columnas)
            i += 1

    def is_valid_number(self, s):
        try:
            # Tries converting the string to a float
            float(s)
            return True
        except ValueError:
            # If a ValueError is raised, the string is not a valid number
            return False

    # Validate if the given row and column indices are within the bounds of
    # the sheet.
    def valid_position(self, fila, columna):
        if fila < 0 or fila >= self.filas:
            return False

        if columna < 0 or columna >= self.columnas:
            return False

        return True

    # Insertar información en una celda
    def insert_info(self, fila, columna, value):
        if not self.valid_position(fila, columna):
            print("Posición inválida")
            return

        if not self.is_valid_number(value):
            print("Se debe proporcionar un numero valido")
            return

        self.hoja[fila][columna] = float(value)

    # Actualizar información en una celda
    def update_data(self, fila, columna, new_value):
        if not self.valid_position(fila, columna):
            print("Posición inválida")
            return

        if not self.is_valid_number(new_value):
            print("Se debe proporcionar un numero valido")
            return

        if self.hoja[fila][columna] is None:
            print("No hay informacion para actualizar")
            return
        else:
            self.hoja[fila][columna] = float(new_value)

    # Validar si una celda tiene información dentro
    def is_empty(self, fila, columna):
        if not self.valid_position(fila, columna):
            print("Posición inválida")
            return True
        if self.hoja[fila][columna] is None:
            return True
        return False

    # Mostrar un preview de la hoja entera
    def print_sheet(self):
        print("Sheet prevew")
        i = 0
        while i < self.filas:
            j = 0
            while j < self.columnas:
                value = self.hoja[i][j]
                if value is None:
                    print("[    ]", end=" ")
                else:
                    print(f"[{value}]", end=" ")
                j += 1
            print()
            i += 1

    # Dada una fila recuperar todos los elementos e imprimir la suma de todos
    # los valores dados
    def row_summary(self, fila):
        entry_fila = self.hoja[fila]
        print(f"fila {fila} --> {entry_fila}")
        i = 0
        total = 0
        while i < self.columnas:
            if entry_fila[i] is not None:
                total += entry_fila[i]
            i += 1

        print(f"total fila --> {total}")

    # Dada una columna recuperar todos los elementos e imprimir la suma de
    # todos los valores dados
    def column_summary(self, column):
        entry_column = []
        total = 0
        i = 0
        while i < self.filas:
            value = self.hoja[i][column]
            entry_column.append(value)
            if value is not None:
                total += value
            i += 1
        print(f"Columan {column} --> {entry_column}")
        print(f"total columna --> {total}")


if __name__ == "__main__":
    sheet_excel = SheetExcel()

    # sheet_excel.print_sheet()

    sheet_excel.insert_info(fila=2, columna=3, value=40)
    sheet_excel.insert_info(fila=2, columna=2, value=10)

    sheet_excel.print_sheet()

    sheet_excel.update_data(fila=2, columna=1, new_value=100)
    # sheet_excel.print_sheet()

    # print("Celda vacia" if sheet_excel.is_empty(fila=1, columna=1) else "Celda con valor")

    # sheet_excel.row_summary(fila=2)
    sheet_excel.column_summary(column=3)
