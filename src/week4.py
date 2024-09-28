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


################################################################################
# Additional Exercises
################################################################################


def king_and_wise_man() -> None:
    """Runs the king and wise man exercise"""
    RICE_WEIGHT = 0.03  # grams
    total_rice = 0
    for i in range(64):
        rice = (2**i) * RICE_WEIGHT
        total_rice += rice
        print(f"{rice:.2f} grams for square {i+1}")

    print(f"Total rice: {total_rice:.2f} grams")
    print(f"{total_rice / 1_000_000_000_000_000:.2f} Gt (Gigatonnes) of rice")
