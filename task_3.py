class Letter:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f"{repr(self.value)}"

    __repr__ = __str__

    def all_neighbor(self, letters):
        self.neighbors.extend(letters)

    def need_neighbors(self, need):
        """

        :return: right neighbor
        """
        output = []
        for k in self.neighbors:
            if need == k.value:
                output.append(k)
        return output


class Board:
    def __init__(self, values, m, n):
        self.m = m
        self.n = n
        self.letters = []
        for line in values:
            for letter in line:
                self.letters.append(Letter(letter))

        for i in range(self.m):
            for j in range(self.n):
                neighbors = []
                k = i * self.n + j
                if j - 1 >= 0:
                    neighbors.append(self.letters[k - 1])
                if i - 1 >= 0:
                    neighbors.append(self.letters[k - self.n])
                if j + 1 < self.n:
                    neighbors.append(self.letters[k + 1])
                if i + 1 < self.m:
                    neighbors.append(self.letters[k + self.n])

                self.letters[k].all_neighbor(neighbors)

    def check(self, need_word):
        if len(need_word) == 0:
            return True
        elif len(need_word) == 1:
            for letter in self.letters:
                if letter.value == need_word:
                    return True
                else:
                    return False
        else:
            answers = list()
            for letter in self.letters:
                i = 0  # Счётчик букв в нужном слове
                if letter.value == need_word[i]:
                    answer = []
                    seen = set()
                    stack = list()
                    stack.append(letter)
                    while stack:
                        node = stack.pop()
                        answer.append(node.value)
                        if len(answer) == len(need_word):
                            break
                        i = len(answer)
                        if node in seen:
                            continue
                        else:
                            seen.add(node)

                        m = node.need_neighbors(need_word[i])

                        for need_neighbor in m:
                            stack.append(need_neighbor)
                    answers.append(answer)

            for ans in answers:
                s = ""
                if s.join(ans) == need_word:
                    return True
            return False


def main():
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"],
             ]
    m = len(board)
    n = len(board[0])
    word = "ABCCED"
    b = Board(board, m, n)
    print(b.check(word))


main()
