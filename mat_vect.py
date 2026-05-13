def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a) == 0:
		return -1
	if len(a[0]) != len(b):
		return -1

	return [sum(x * y for x,y in zip(row,b)) for row in a]


def main():
    tests = [
        # (matrix, vector, expected)
        (
            [[1, 2, 3], [4, 5, 6]],
            [1, 1, 1],
            [6, 15]
        ),
        (
            [[1.5, 2.0], [3.0, 4.5]],
            [2, 3],
            [9.0, 19.5]
        ),
        (
            [[0, -1], [2, 3], [4, 5]],
            [10, 2],
            [-2, 26, 50]
        ),
        (
            [],                 # empty matrix
            [1, 2],
            -1
        ),
        (
            [[1, 2], [3, 4]],   # column count != len(vector)
            [1, 2, 3],
            -1
        ),
    ]
    for i, (a, b, expected) in enumerate(tests, start=1):
        result = matrix_dot_vector(a, b)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        print(f"  a = {a}")
        print(f"  b = {b}")
        print(f"  expected = {expected}, got = {result}\n")
if __name__ == "__main__":
    main()