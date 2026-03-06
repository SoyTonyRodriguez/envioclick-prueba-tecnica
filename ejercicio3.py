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
    # Initializes the number of rows and columns in the sheet, and creates a
    # sheet represented as a 2D list where each cell is initialized to None.
    def __init__(self, filas=5, columnas=10):
        self.filas = filas
        self.columnas = columnas
        self.hoja = list()

        # Create a 2D list to represent the sheet, where each cell is
        # initialized to None.
        i = 0
        while i < self.filas:
            list_columnas = list()
            j = 0
            while j < self.columnas:
                list_columnas.append(None)
                j += 1

            self.hoja.append(list_columnas)
            i += 1

    # Check if a string can be converted to a valid number.
    def _is_valid_number(self, s):
        try:
            # Tries converting the string to a float
            float(s)
            return True
        except ValueError:
            # If a ValueError is raised, the string is not a valid number
            return False

    # Validate if the given row and column indices are within the bounds of
    # the sheet.
    def _valid_position(self, fila, columna):
        try:
            if fila < 0 or fila >= self.filas:
                return False

            if columna < 0 or columna >= self.columnas:
                return False

            return True
        except Exception:
            return False

    # Insert information into a cell specified by its row and column indices.
    def insert_info(self, fila, columna, value):
        # Validate the position of the cell and the value before inserting it
        # into the sheet.
        if not self._valid_position(fila, columna):
            print("Posición inválida")
            return

        # Validate that the value is a valid number before inserting it into
        # the sheet.
        if not self._is_valid_number(value):
            print("Se debe proporcionar un numero valido")
            return

        # Insert the value into the specified cell in the sheet after
        # converting it to a float.
        self.hoja[fila][columna] = float(value)

    # Actualizar información en una celda
    def update_data(self, fila, columna, new_value):
        # Validate the position of the cell and the value before updating it
        # in the sheet.
        if not self._valid_position(fila, columna):
            print("Posición inválida")
            return

        # Validate that the new value is a valid number before updating it in
        # the sheet.
        if not self._is_valid_number(new_value):
            print("Se debe proporcionar un numero valido")
            return

        # Check if there is existing information in the specified cell before
        # updating it. If the cell is empty (None), print a message indicating
        # that there is no information to update.
        if self.hoja[fila][columna] is None:
            print("No hay informacion para actualizar")
            return
        else:
            self.hoja[fila][columna] = float(new_value)

    # Validate if a cell specified by its row and column indices is empty.
    def is_empty(self, fila, columna):
        # Validate the position of the cell before checking if it is empty.
        if not self._valid_position(fila, columna):
            print("Posición inválida")
            return True

        if self.hoja[fila][columna] is None:
            return True
        return False

    # Show a preview of the entire sheet by printing its contents in a
    # formatted manner. Empty cells are represented with "[    ]", while cells
    # with values are displayed with their respective values enclosed in
    # brackets.
    def print_sheet(self):
        print("Sheet preview")

        # Iterate through each row and column of the sheet to print its
        # contents.
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

    # Given a row index, retrieve all the elements in that row and print the
    # sum of all the values in that row. Empty cells are ignored in the sum
    # calculation.
    def row_summary(self, fila):
        entry_fila = self.hoja[fila]
        print(f"fila {fila} --> {entry_fila}")

        # Iterate through each cell in the specified row to retrieve the
        # values and calculate the total sum of the values in that row.
        i = 0
        total = 0
        while i < self.columnas:
            if entry_fila[i] is not None:
                total += entry_fila[i]
            i += 1

        print(f"total fila --> {total}")

    # Given a column index, retrieve all the elements in that column and print
    # the sum of all the values in that column. Empty cells are ignored in the
    # sum calculation.
    def column_summary(self, column):
        entry_column = []
        total = 0

        # Iterate through each row in the specified column to retrieve the
        # values and calculate the total sum of the values in that column.
        i = 0
        while i < self.filas:
            value = self.hoja[i][column]
            entry_column.append(value)
            if value is not None:
                total += value
            i += 1
        print(f"Column: {column} --> {entry_column}")
        print(f"total column --> {total}")


if __name__ == "__main__":
    # Create an instance of the SheetExcel class
    sheet_excel = SheetExcel()

    # sheet_excel.print_sheet()

    # Insert values into specific cells in the sheet and print the sheet to
    # show the changes.
    sheet_excel.insert_info(fila=2, columna=3, value=40)
    sheet_excel.insert_info(fila=2, columna=2, value=10)

    print("After inserting values:")
    sheet_excel.print_sheet()

    # Update the value of a specific cell in the sheet and print the sheet to
    # show the changes.
    sheet_excel.update_data(fila=2, columna=1, new_value=100)
    print("After updating a value:")
    sheet_excel.print_sheet()

    # Check if a specific cell is empty and print the result.
    print("Checking if cell (1, 1) is empty:")
    print("Celda vacia" if sheet_excel.is_empty(fila=1, columna=1)
          else "Celda con valor")

    # Calculate and print the summary of a specific row and column in the
    # sheet.
    print("Row summary for specified row:")
    sheet_excel.row_summary(fila=2)
    print("Column summary for specified column:")
    sheet_excel.column_summary(column=3)
