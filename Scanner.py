""""""


class Scanner:
    """"""

    def __init__(self, dictionary="./wordlist.txt") -> None:
        self.dictionary = dictionary
        self.load()

    def load(self):
        """"""
        self.wordlist = []
        with open(self.dictionary) as wordlist:
            for word in wordlist:
                self.wordlist.append(word[:-1].upper())

    def check(self, text):
        """"""
        words_in_text = []
        for word in self.wordlist:
            if word in text:
                words_in_text.append(word)
        return len(words_in_text)
