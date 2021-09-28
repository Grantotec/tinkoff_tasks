from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.outbound = []

    def point_to(self, other):
        self.outbound.append(other)

    def __str__(self):
        return f"Node({repr(self.value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self.root = root

    def dfs1(self) -> list[Node]:
        """
        Обход в глубину с помощью рекурсии
        :return: Порядок обхода узлов
        """
        return self.dfs1_help(self.root, set())

    def dfs1_help(self, start: Node, seen: set[Node]) -> list[Node]:
        output = []
        if start in seen:
            return output

        output.append(start)
        seen.add(start)

        for node in start.outbound:
            output.extend(self.dfs1_help(node, seen))
        return output

    def dfs2(self) -> list[Node]:
        """
        Обход в глубину с помощью цикла
        :return: Порядок обхода узлов
        """
        output = []
        stack = list()
        stack.append(self.root)
        while stack:
            node = stack.pop()
            if node in output:
                continue

            for out_node in node.outbound[::-1]:
                stack.append(out_node)
            output.append(node)
        return output

    def bfs(self) -> list[Node]:
        """
        Обход в ширину
        :return: Порядок обхода узлов
        """
        output = []
        seen = set()
        queue = deque()
        queue.append(self.root)
        while len(queue):
            node = queue.popleft()

            if node in seen:
                continue

            seen.add(node)
            output.append(node)
            for out_node in node.outbound:
                queue.append(out_node)
        return output


def make_graph(dictionary) -> Graph:
    """
    Создаем граф из входного словаря
    :param dictionary: Входной словарь
    :return: Граф с узлами
    """
    nodes = []  # список узлов
    n = 0  # счётчик узлов

    for key, values in dictionary.items():
        nodes.append(Node(str(key)))

    for values in dictionary.values():
        for value in values:
            nodes[n].point_to(nodes[value])
        n += 1

    return Graph(nodes[0])


def main():
    data = {0: [1, 2],
            1: [2],
            2: [3],
            3: [1, 2],
            }
    g = make_graph(data)

    print(g.dfs1())
    print(g.dfs2())
    print(g.bfs())


if __name__ == "__main__":
    main()
