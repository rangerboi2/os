import threading

# Result matrix
result = []

# Worker thread class
class MultiplyThread(threading.Thread):
    def __init__(self, row, col, i, j):
        threading.Thread.__init__(self)
        self.row = row
        self.col = col
        self.i = i
        self.j = j
        self.value = 0

    def run(self):
        self.value = sum(self.row[k] * self.col[k] for k in range(len(self.col)))

    def get_value(self):
        return self.value


def get_matrix_input(name):
    r = int(input(f"Enter number of rows in {name}: "))
    c = int(input(f"Enter number of columns in {name}: "))
    print(f"Enter values for {name} row-wise:")
    matrix = []
    for i in range(r):
        row = list(map(int, input().split()))
        if len(row) != c:
            print("Incorrect number of columns! Exiting.")
            exit()
        matrix.append(row)
    return matrix, r, c


def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def matrix_multiply(A, B):
    global result
    threads = []
    result = [[0] * len(B[0]) for _ in range(len(A))]
    B_T = transpose(B)  # So we can take columns as rows
    thread_map = [[None for _ in range(len(B_T))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B_T)):
            thread = MultiplyThread(A[i], B_T[j], i, j)
            thread_map[i][j] = thread
            threads.append(thread)
            thread.start()

    for t in threads:
        t.join()

    for i in range(len(A)):
        for j in range(len(B[0])):
            result[i][j] = thread_map[i][j].get_value()

    return result


def print_matrix(mat, name):
    print(f"\n{name}:")
    for row in mat:
        print(" ".join(map(str, row)))


def main():
    A, r1, c1 = get_matrix_input("Matrix A")
    B, r2, c2 = get_matrix_input("Matrix B")

    if c1 != r2:
        print("Matrix multiplication not possible. Columns of A must match rows of B.")
        return

    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")

    result_matrix = matrix_multiply(A, B)

    print_matrix(result_matrix, "Resultant Matrix (A x B)")


if __name__ == "__main__":
    main()
