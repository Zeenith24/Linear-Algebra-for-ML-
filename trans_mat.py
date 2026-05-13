def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:

    if not a:
        return []
    return [list(row) for row in zip(*a)]

print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))  
print(transpose_matrix([[1]]))                 
print(transpose_matrix([]))                    
print(transpose_matrix([[1.5, 2.5], [3.5, 4.5]])) 
print(transpose_matrix([[1, 2], [3, 4], [5, 6]])) 