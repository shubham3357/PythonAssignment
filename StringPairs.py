from itertools import combinations


class StringPairs:
    stringPairCombo = []

    def string_pairs(self):
        charList = list(self)
        StringPairs.stringPairCombo = list(combinations(charList, 2))

    def print_pairs(self):
        for x in range(len(self)):
            print(self[x], end=" ")

    string_pairs("Hello")
