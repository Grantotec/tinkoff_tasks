class Letter:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f"{repr(self.value)}"

    __repr__ = __str__

    def all_neighbor(self, letters):
        self.neighbors.extend(letters)

    def need_neighbor(self, need):
        """

        :return: right neighbor
        """
        output = []
        for k in self.neighbors:
            if need == k.value:
                output.append(k)
        return output




class Board:
    def __init__(self, values, lines, rows):
        self.m = lines
        self.n = rows
        self.letters = []
        for line in values:
            for letter in line:
                self.letters.append(Letter(letter))

        for i in range(len(self.letters)):
            neighbors = []
            if i - 1 >= 0:
                neighbors.append(self.letters[i - 1])
            if i - self.n >= 0:
                neighbors.append(self.letters[i - 4])
            if i + 1 < 12:
                neighbors.append(self.letters[i + 1])
            if i + self.n < 12:
                neighbors.append(self.letters[i + 4])

            self.letters[i].all_neighbor(neighbors)


    def check(self, need_word):
        if len(need_word) == 0:
            return True
        elif len(need_word) == 1:
            for letter in self.letters:
                if letter.value == need_word:
                    return True

        for letter in self.letters:
            if letter.value == need_word[0]:
                need_word = need_word[1:]
                seen = set()
                seen.add(letter)
                start = letter
                need_letter = need_word[0]








def main():
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"],
             ]
    m = len(board)
    n = len(board[0])
    word = "ABCCED"
    b = Board(board, m, n)
    b.check(word)




    """for i in letters:
        if i.value == word[0]:
            a = i.neighbor(word[1])
            for j in a:
                b = j.neighbor(word[2])
                for l in b:
                    c = l.neighbor(word[3])
                    for v in c:
                        d = v.neighbor(word[4])
                        for m in d:
                            print("true")"""


main()