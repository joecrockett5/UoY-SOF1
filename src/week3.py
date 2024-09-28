class Week3:
    @staticmethod
    def is_palindrome(s: str):
        return s == s[::-1]

    @staticmethod
    def check_for_palindrome(s: str):
        stripped_string = "".join([c for c in s if c.isalpha()]).lower()
        palindrome = Week3.is_palindrome(stripped_string)

        print(
            f"""The string 
    "{s}" 
Is{'n\'t' if not palindrome else ''} a palindrome."""
        )

    @staticmethod
    def remove_whitespace(s: str, camel_case: bool = False):
        words = s.split()
        if camel_case:
            words = [w.title() for w in words]
        return "".join(words)

    @staticmethod
    def split_camel_case(s):
        words = []
        cur = 0
        for index, char in enumerate(s):
            if char.isupper() and index != cur:
                words.append(s[cur:index])
                cur = index
        if cur != len(s):
            words.append(s[cur:])
        return words

    @staticmethod
    def run_camel_case() -> None:
        """Runs the camel case"""
        s = input("Enter a string: ")
        words = Week3.split_camel_case(s)
        print(f"The words are: {words}")

    @staticmethod
    def caeser_cipher_encrypt(s: str, shift: int):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_str = "".join([alphabet[(alphabet.index(c) + shift) % 26] for c in s])
        print(f"The cipher is: {new_str}")

    @staticmethod
    def caeser_cipher_decrypt(s: str, shift: int):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_str = "".join([alphabet[(alphabet.index(c) - shift) % 26] for c in s])
        print(f"The original string was: {new_str}")

    ################################################################################
    # Additional Exercises
    ################################################################################

    @staticmethod
    def evens_from_series() -> None:
        """Counts the number of even numbers inputted from the series"""
        series = input("Enter a series of numbers: ")
        evens = set()
        for number in series.split():
            if int(number) % 2 == 0:
                evens.add(int(number))
        print(
            f"There are {len(evens)} distinct even numbers in the series {list(evens)}"
        )

    @staticmethod
    def create_sudoku() -> None:
        """Creates a sudoku puzzle"""
        import sys

        puzzle = []
        for _ in range(4):
            row_str = input("Enter a row: ")

            row = row_str.split()
            valid = True
            if len(row) != 4:
                valid = False
                print("Invalid row")

            for item in row:
                if item not in "0123456789":
                    valid = False
                    print("Invalid item")
                    break

                if item == "0":
                    row[row.index(item)] = " "

            if not valid:
                print("Try again")
                sys.exit()

            puzzle.append(row)

        border = "+-+-+-+-+"
        print(border)
        for row in puzzle:
            print("|" + "|".join(row) + "|")
            print(border)

    @staticmethod
    def denary_to_binary() -> None:
        """Converts a denary number to binary"""
        denary = int(input("Enter a denary number: "))
        binary = ""
        while denary > 0:
            print(f"{denary}/2 = ", end="")
            denary, remainder = divmod(denary, 2)
            print(f"{denary}, remmainder {remainder}")
            binary = f"{remainder}{binary}"
        print(f"The binary number is: {binary}")
