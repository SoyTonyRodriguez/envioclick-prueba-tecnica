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
    # The default number of rows is 5 and the default number of columns is 10
    def __init__(self, rows: int = 5, columns: int = 10) -> None:
        self.rows = rows
        self.columns = columns
        self.sheet = list()

        # Create a 2D list to represent the sheet, where each cell is
        # initialized to None.
        i = 0
        while i < self.rows:
            list_columns = list()
            j = 0
            while j < self.columns:
                list_columns.append(None)
                j += 1

            self.sheet.append(list_columns)
            i += 1

    # Check if a string can be converted to a valid number.
    def _is_valid_number(self, value: str) -> bool:
        try:
            # Tries converting the string to a float
            float(value)
            return True
        except ValueError:
            # If a ValueError is raised, the string is not a valid number
            return False

    # Validate if the given row and column indices are within the bounds of
    # the sheet.
    def _valid_position(self, row: int, column: int) -> bool:
        try:
            if row < 0 or row >= self.rows:
                return False

            if column < 0 or column >= self.columns:
                return False

            return True
        except Exception:
            return False

    # Convert user-friendly row and column indices (starting from 1) to
    # zero-based indices used internally in the sheet representation.
    def _user_to_index(self, row, column):
        return row - 1, column - 1

    # Insert information into a cell specified by its row and column indices.
    def insert_info(self, row: int, column: int, value: str) -> None:
        # Convert user-friendly row and column indices to zero-based indices.
        row, column = self._user_to_index(row, column)

        # Validate the position of the cell and the value before inserting it
        # into the sheet.
        if not self._valid_position(row, column):
            print("Posición inválida")
            return

        # Validate that the value is a valid number before inserting it into
        # the sheet.
        if not self._is_valid_number(value):
            print("Se debe proporcionar un numero valido")
            return

        # Insert the value into the specified cell in the sheet after
        # converting it to a float.
        self.sheet[row][column] = float(value)

    # Actualizar información en una celda
    def update_data(self, row: int, column: int, new_value: str) -> None:
        # Convert user-friendly row and column indices to zero-based indices.
        row, column = self._user_to_index(row, column)

        # Validate the position of the cell and the value before updating it
        # in the sheet.
        if not self._valid_position(row, column):
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
        if self.sheet[row][column] is None:
            print("No hay informacion para actualizar")
            return
        else:
            self.sheet[row][column] = float(new_value)

    # Validate if a cell specified by its row and column indices is empty.
    def is_empty(self, row: int, column: int) -> bool:
        # Convert user-friendly row and column indices to zero-based indices.
        row, column = self._user_to_index(row, column)

        # Validate the position of the cell before checking if it is empty.
        if not self._valid_position(row, column):
            print("Posición inválida")
            return True

        if self.sheet[row][column] is None:
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
        while i < self.rows:
            j = 0
            while j < self.columns:
                value = self.sheet[i][j]
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
    def row_summary(self, row: int) -> None:
        # Convert user-friendly row index to zero-based index.
        row, _ = self._user_to_index(row, 1)

        entry_fila = self.sheet[row]
        print(f"fila {row + 1} --> {entry_fila}")

        # Iterate through each cell in the specified row to retrieve the
        # values and calculate the total sum of the values in that row.
        i = 0
        total = 0
        while i < self.columns:
            if entry_fila[i] is not None:
                total += entry_fila[i]
            i += 1

        print(f"total fila --> {total}")

    # Given a column index, retrieve all the elements in that column and print
    # the sum of all the values in that column. Empty cells are ignored in the
    # sum calculation.
    def column_summary(self, column: int) -> None:
        # Convert user-friendly column index to zero-based index.
        column, _ = self._user_to_index(1, column)

        entry_column = []
        total = 0

        # Iterate through each row in the specified column to retrieve the
        # values and calculate the total sum of the values in that column.
        i = 0
        while i < self.rows:
            value = self.sheet[i][column]
            entry_column.append(value)
            if value is not None:
                total += value
            i += 1
        print(f"Column: {column + 1} --> {entry_column}")
        print(f"total column --> {total}")


if __name__ == "__main__":
    # Create an instance of the SheetExcel class
    sheet_excel = SheetExcel()

    # sheet_excel.print_sheet()

    # Insert values into specific cells in the sheet and print the sheet to
    # show the changes.
    sheet_excel.insert_info(row=2, column=3, value=40)
    sheet_excel.insert_info(row=2, column=2, value=10)
    sheet_excel.insert_info(row=1, column=1, value=5)

    print("After inserting values:")
    sheet_excel.print_sheet()

    # Update the value of a specific cell in the sheet and print the sheet to
    # show the changes.
    sheet_excel.update_data(row=2, column=1, new_value=100)
    print("After updating a value:")
    sheet_excel.print_sheet()

    # Check if a specific cell is empty and print the result.
    print("Checking if cell (1, 1) is empty:")
    print("Celda vacia" if sheet_excel.is_empty(row=1, column=1)
          else "Celda con valor")

    # Calculate and print the summary of a specific row and column in the
    # sheet.
    print("Row summary for specified row:")
    sheet_excel.row_summary(row=2)
    print("Column summary for specified column:")
    sheet_excel.column_summary(column=3)
