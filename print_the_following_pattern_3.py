size=int(input())
def print_n_pattern(size):
    for i in range(size):
        for j in range(size):
            if j == 0 or j == size - 1 or i == j:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

# Example usage
print_n_pattern(size)
