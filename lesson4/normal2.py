"""The matrix module."""

from random import randrange


def make_random_matrix(size):
    """Make a quadratic matrix of a given size with random elements, where
       there is a single random position containing zero.

       size -- the size of the matrix
    """
    if size < 0:
        raise ValueError('Size must be positive.')
    matrix = []
    for i in range(size):
        matrix.append(_make_random_row(size))
    return matrix


def _make_random_row(size):
    if size == 1:
        return [0]
    row = []
    for i in range(size):
        row.append(randrange(1, size))
    row[randrange(size)] = 0
    return row


if __name__ == '__main__':
    from sys import argv
    size = int(argv[1])
    matrix = make_random_matrix(size)
    print(matrix)
