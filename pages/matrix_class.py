import random as r
import numpy as np
import math as m
class MatrixError(Exception):
    pass
class IncorrectDimentionsInitilizationError(MatrixError):
    def __init__(self):
        super().__init__(f"The data entered into the matrix is not a 2 dimentional numpy array")
class MultiplicationDimentionError(MatrixError):
    def __init__(self):
        super().__init__("The matrexes that you're trying to multiply dont have valid dimentions")
class DotProductListLengthError(MatrixError):
    def __int__(self):
        super().__init__("The lengths of the lists that you entered into _dot are not the same length")
class ParsingError(Exception):
    pass
class InvalidCharacter(ParsingError):
    def __init__(self, char:str):
        super().__init__(f"The character, '{char}' is not a valid character")
class NeglectedInput(ParsingError):
    def __init__(self,neglected_input:str):
        super().__init__(f"The {neglected_input} input was neglected")

class Matrix:

    def __init__(self, data:np.array):
        if data.ndim != 2:
            raise IncorrectDimentionsInitilizationError()
        self.data = data
        self.row = len(data)
        self.col = len(data[0])
    
    def __str__(self):
        return_list = []
        for row in self.data:
            return_list.append(row)
        return_string = ''
        for i in return_list:
            return_string += str(i)
            return_string += '\n'
        return return_string

    def _checkDimentions(self,other_matrix):
        return self.row == other_matrix.row and self.col == other_matrix.col
    
    def add(self,other_matrix):
        if self._checkDimentions(other_matrix): 
            resulting_matrix_data_as_list = []
            for row in range(self.row):
                resulting_matrix_row = []
                for col in range(self.col):
                    resulting_matrix_row.append((self.data[row,col])+(other_matrix.data[row,col]))
                resulting_matrix_data_as_list.append(resulting_matrix_row)
            return Matrix(np.array([row for row in resulting_matrix_data_as_list]))
        else:
            return None
    
    def subtract(self,other_matrix):
        if self._checkDimentions(other_matrix): 
            resulting_matrix_data_as_list = []
            for row in range(self.row):
                resulting_matrix_row = []
                for col in range(self.col):
                    resulting_matrix_row.append((self.data[row,col])-(other_matrix.data[row,col]))
                resulting_matrix_data_as_list.append(resulting_matrix_row)
            return Matrix(np.array([row for row in resulting_matrix_data_as_list]))
        else:
            return None


    def multiply(self,other_matrix):
        if self.row == other_matrix.col:
            resulting_matrix_data_as_list = []
            def get_col(matrix, col_num):
                col = np.array([])
                for row in matrix.data:
                    col = np.append(col,row[col_num])

                return col
            for row in range(self.row):
                self_row = self.data[row]
                row = []
                for col in range(other_matrix.col):
                    col = get_col(other_matrix,col)
                    row.append(Matrix._dot(col,self_row))
                resulting_matrix_data_as_list.append(row)
            print(resulting_matrix_data_as_list)
            return Matrix(np.array([row for row in resulting_matrix_data_as_list]))
        else:
            raise MultiplicationDimentionError()
    
    def shape(self):
        return (self.row,self.col)

    def scalar_multiply(self, scalar):
        data_as_list = []
        for row in self.data:
            new_row = []
            for point in row:
                new_row.append(point)
            data_as_list.append(new_row)
        return Matrix(np.array([row for row in data_as_list]))
    
    def is_equal(self, other_matrix):
        if self.shape() == other_matrix.shape():
            for row in range(len(self.data)):
                for item in range(len(self.data[row])):

                    if self.data[row][item] != other_matrix.data[row][item]:
                        return False
            return True
        else:
            return False

    def copy(self):
        return Matrix(self.data.copy())
    @staticmethod
    def _dot(list1,list2):
        if len(list1) == len(list2):
            list_of_products = []
            for i in range(len(list1)):
                list_of_products.append(list1[i]*list2[i])
            dot_product = sum(list_of_products,0)
            return dot_product
        else:
            return False

    def zero_matrix(row,col):
        data_as_list = []
        for i in range(row):
            row = []
            for j in range(col):
                row.append(0)
            data_as_list.append(row)
        return Matrix(np.array([row for row in data_as_list]))

def parse_shape(shape:str) -> tuple:
    """
    Returns:\n
    a tuple (row x col)\n
    0 if an invalid character appered\n
    1 if col was neglected
    """
    dimentions = ()
    row = ''
    col = ''
    before_x = True
    for char in shape:

        if char.isdigit():
            if before_x:
                row += char
            else:
                col += char
        else:
            if char.isalpha() and char.lower() == 'x':
                before_x = False
            elif char !=' ':
                return 0
    if col == '':
        return 1
    dimentions = (row , col)
    return dimentions