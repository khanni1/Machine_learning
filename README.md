# Khanjan Matrix Functions
(khanjan_matfunc.py)

A collection of fundamental matrix operations implemented in pure Python, designed for building matrices from scratch without external dependencies.

## Overview

`khanjan_matfunc.py` provides essential linear algebra functions for matrix manipulation and calculations. These functions work with Python lists of lists as matrix representations, making them ideal for educational purposes and custom matrix operations.

---

## Functions

### 1. `scalar_mul(A: list, s)`
Multiplies all elements of a matrix by a scalar value.

**Parameters:**
- `A` (list): Input matrix (list of lists)
- `s` (numeric): Scalar value to multiply

**Returns:** 
- New matrix with all elements multiplied by `s`, rounded to 5 decimal places

**Example:**
```python
A = [[1, 2], [3, 4]]
result = scalar_mul(A, 2)
# Result: [[2, 4], [6, 8]]
```

---

### 2. `pretty_print_2D(A)`
Prints a matrix in a readable 2D format.

**Parameters:**
- `A` (list): Matrix to print

**Returns:** 
- None (prints to console)

**Example:**
```python
A = [[1, 2, 3], [4, 5, 6]]
pretty_print_2D(A)
# Output:
# [1, 2, 3]
# [4, 5, 6]
```

---

### 3. `mat_create_ini(rows, cols)`
Creates an empty matrix initialized with zeros.

**Parameters:**
- `rows` (int): Number of rows
- `cols` (int): Number of columns

**Returns:** 
- Matrix of size `rows × cols` filled with zeros

**Example:**
```python
matrix = mat_create_ini(3, 2)
# Result: [[0, 0], [0, 0], [0, 0]]
```

---

### 4. `is_square_mat(A)`
Checks if a matrix is square (rows == columns) and not jagged.

**Parameters:**
- `A` (list): Matrix to check

**Returns:** 
- `True` if matrix is square and valid, `False` otherwise

**Example:**
```python
A = [[1, 2], [3, 4]]
print(is_square_mat(A))  # True

B = [[1, 2, 3], [4, 5, 6]]
print(is_square_mat(B))  # False
```

---

### 5. `isnt_jagged(A)`
Checks if all rows in a matrix have the same length (not jagged).

**Parameters:**
- `A` (list): Matrix to check

**Returns:** 
- `True` if matrix is not jagged, `False` if jagged

**Example:**
```python
A = [[1, 2], [3, 4]]
print(isnt_jagged(A))  # True

B = [[1, 2], [3, 4, 5]]  # Jagged
print(isnt_jagged(B))  # False
```

---

### 6. `Minor(A, x, y)`
Computes the minor matrix by removing row `x` and column `y`.

**Parameters:**
- `A` (list): Input matrix
- `x` (int): Row index to remove
- `y` (int): Column index to remove

**Returns:** 
- New matrix with row `x` and column `y` removed
- `(False, "jagged matrix error")` if matrix is jagged

**Example:**
```python
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
minor = Minor(A, 0, 1)
# Result: [[4, 6], [7, 9]]
```

---

### 7. `det(A)`
Calculates the determinant of a square matrix using recursive cofactor expansion.

**Parameters:**
- `A` (list): Square matrix

**Returns:** 
- Determinant value (numeric)
- `(False, "Not a square matrix")` if matrix is not square

**Special Cases:**
- 1×1 matrix: Returns the single element
- 2×2 matrix: Returns `A[0][0]*A[1][1] - A[0][1]*A[1][0]`
- n×n matrix: Uses cofactor expansion

**Example:**
```python
A = [[1, 2], [3, 4]]
determinant = det(A)
# Result: -2
```

---

### 8. `mat_mul(A, B)`
Multiplies two matrices using the standard matrix multiplication algorithm.

**Parameters:**
- `A` (list): First matrix (m × n)
- `B` (list): Second matrix (n × p)

**Returns:** 
- Product matrix of size m × p
- `(False, "conditions not suitable for multiplication")` if dimensions don't match or matrices are jagged

**Requirements:**
- Both matrices must not be jagged
- Number of columns in `A` must equal number of rows in `B`

**Example:**
```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
product = mat_mul(A, B)
# Result: [[19, 22], [43, 50]]
```

---

### 9. `transpose(A)`
Transposes a matrix (swaps rows and columns).

**Parameters:**
- `A` (list): Input matrix

**Returns:** 
- Transposed matrix of size cols × rows
- `False` if matrix is jagged

**Example:**
```python
A = [[1, 2, 3], [4, 5, 6]]
transposed = transpose(A)
# Result: [[1, 4], [2, 5], [3, 6]]
```

---

## Quick Start

### Import the Module
```python
from khanjan_matfunc import *
```

### Basic Usage
```python
# Create a matrix
X = [[1, 2, 4], [5, 6, 6], [5, 6, 8]]

# Print it
pretty_print_2D(X)

# Multiply by scalar
result = scalar_mul(X, 0.5)
pretty_print_2D(result)

# Calculate determinant
determinant = det(X)
print(f"Determinant: {determinant}")

# Transpose
transposed = transpose(X)
pretty_print_2D(transposed)

# Matrix multiplication
A1 = [[3, 2], [1, 5], [3, 2]]
A2 = [[10, 20], [30, 40]]
product = mat_mul(A1, A2)
pretty_print_2D(product)
```

---

## Use Cases

✅ Educational purposes - learn matrix operations from scratch  
✅ Custom matrix calculations without NumPy/SciPy dependencies  
✅ Algorithm implementation and testing  
✅ Small-scale matrix computations  

⚠️ **Note:** For production or large-scale applications, use **NumPy** for better performance and numerical stability.

---

## Important Notes

- Matrices are represented as Python lists of lists
- All matrix operations check for jagged matrices and return errors accordingly
- The determinant calculation uses cofactor expansion (recursive), which can be slow for large matrices
- Results are rounded to 5 decimal places in scalar multiplication
---

## Requirements

- Python 3.x
- No external dependencies

---

## Author

**Khanjan Chokshi**

---

## License

Feel free to use and modify these functions as needed.
