import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	arr = np.array(a)

	if arr.size != new_shape[0] * new_shape[1]:
		return []

	reshaped_matrix = arr.reshape(new_shape).tolist()
	return reshaped_matrix

print(reshape_matrix([[1, 2, 3], [4, 5, 6]], (3, 2))) 
print(reshape_matrix([[1, 2], [3, 4]], (1, 4)))       
print(reshape_matrix([[1, 2], [3, 4]], (3, 2)))       
print(reshape_matrix([[1.5, 2.5], [3.5, 4.5]], (4, 1)))
print(reshape_matrix([[42]], (1, 1)))