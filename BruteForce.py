""""""


from Cryptic import decrypt
from Scanner import Scanner


class Brute:
    """"""

    def __init__(self, possible, size=4) -> None:
        self.amount = len(possible)**size
        self.possible_elements = possible
        self.size = size

    def _crack(self, size):
        """"""
        if size == 1:
            for i in self.possible_elements:
                yield str(i)
        else:
            for i in self.possible_elements:
                for j in self._crack(size - 1):
                    yield str(i) + j

    def start(self):
        """"""
        if self.amount > 25:
            print("There are {} possiblities".format(self.amount))
            print("This will take about {} seconds".format(self.amount // 10))
        return self._crack(self.size)


class Force:
    """"""

    def __init__(self, brute: Brute, scanner: Scanner = Scanner()) -> None:
        self.brute = brute
        self.scanner = scanner
        self.key = ""
        self.score = 0

    def start(self, encrypted_text: str):
        """"""
        passwords = self.brute.start()
        if passwords is not None:
            for password in passwords:
                decrypted_text = decrypt(password, encrypted_text)
                found_words = self.scanner.check(decrypted_text)
                if found_words > self.score:
                    self.key = password
                    self.score = found_words
        return self.key
