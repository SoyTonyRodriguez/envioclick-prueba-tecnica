# Envíoclick Backend Technical Test

This repository contains the solution to a backend technical challenge implemented in **Python 3.13**.

The objective of the challenge is to solve three algorithmic problems while respecting specific constraints defined in the test.

## Constraints

The implementation follows the rules specified in the challenge:

- Python **3.13**
- **No external libraries**
- Avoid using built-in helper methods such as:
  - `sort`
  - `find`
  - `index`
  - `in`
  - `contains`
  - `refind`
- Follow **PEP8 coding standards**

---

# Repository Structure

```
envioclick-prueba-tecnica
│
├── python_test/
│   └── input.py
│
├── ejercicio1.py
├── ejercicio2.py
├── ejercicio3.py
│
├── .gitignore
└── README.md
```

Each script can be executed independently.

---

# Requirements

Python version required:

```
Python 3.13
```

No additional dependencies are required.

---

# Exercise 1 — Text Occurrence Counter

## Description

This script counts how many times a given word appears inside a paragraph.

The algorithm processes the paragraph **character by character**, avoiding the use of built-in search functions.

### Implementation Details

The solution includes:

- Accent normalization
- Uppercase to lowercase normalization
- Manual word detection
- Alphanumeric validation

The text is converted into a normalized list of characters to ensure accurate comparisons.

### Example

Input paragraph:

```
"La logística Digital es un concepto que surge de la integración entre la logística tradicional..."
```

Search text:

```
"logística"
```

Output:

```
4 ocurrencias encontradas
```

### Run

```
python ejercicio1.py
```

---

# Exercise 2 — Dynamic Filter and Priority Sorting

## Description

This script processes a list of dictionaries and performs the following operations:

1. Applies **dynamic filters**
2. Selects only elements that satisfy all filters
3. Sorts the filtered elements by **priority**
4. Supports **ascending or descending sorting**
5. Keeps the remaining elements in their **original order**

The filtered and sorted results appear **first**, followed by the remaining elements.

### Example Data Element

```
{
"id": 12340,
"weight": 1,
"width": 1,
"height": 1,
"length": 1,
"cost": 125,
"priority": 2
}
```

### Example Filter

```
[
('weight', '=', 3),
('width', '>', 2)
]
```

### Sorting Options

```
ASC
DESC
```

### Algorithm


The solution for Exercise 2 is divided into three main stages:

1. **Filtering the dataset**
2. **Sorting the filtered elements**
3. **Building the final result**

This approach ensures that only the elements matching the filters are sorted, while the rest of the elements preserve their original order.

---

Sorting is implemented using a **custom QuickSort algorithm** instead of Python's built-in sorting methods.

### Run

```
python ejercicio2.py
```

Input data is defined in:

```
python_test/input.py
```

---

# Exercise 3 — Basic Excel Sheet Representation

## Description

This exercise implements a **basic spreadsheet simulation** using a 2D list structure.

Rows and columns represent spreadsheet cells.

### Features

The sheet supports the following operations:

### Insert information into a cell

```
insert_info(row, column, value)
```

### Update cell information

```
update_data(row, column, new_value)
```

### Validate if a cell is empty

```
is_empty(row, column)
```

### Show sheet preview

```
print_sheet()
```

### Row summary

Returns the sum of all values in a given row.

```
row_summary(row)
```

### Column summary

Returns the sum of all values in a given column.

```
column_summary(column)
```

### Run

```
python ejercicio3.py
```

---

# Design Decisions

Key design choices in this implementation include:

- Avoiding built-in helper methods as required by the challenge
- Manual implementation of algorithms
- Character normalization using ASCII manipulation
- Custom QuickSort implementation
- Validation of user inputs for spreadsheet operations

---

# Author

Antonio Rodríguez  
Backend Developer

GitHub  
https://github.com/SoyTonyRodriguez