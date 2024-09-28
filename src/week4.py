def sum_digits(n: int) -> int:
    return sum([int(d) for d in str(n)])


def pairwise_digits(number_a: int, number_b: int) -> str:
    out = ""
    nA, nB = str(number_a), str(number_b)
    if len(nA) != len(nB):
        return "The numbers are not the same length"
    for i in range(len(nA)):
        out += "1" if nA[i] == nB[i] else "0"
    return out


def binary_triangle(rows: int) -> None:
    """Prints a binary triangle"""
    for row in range(rows):
        for col in range(row + 1):
            print(f"{(row+col+1) % 2}", end="")
        print()


def sum_lists(list_2d: list[list[int]]) -> list[int]:
    """Sums a list of lists"""
    return [sum(row) for row in list_2d]
