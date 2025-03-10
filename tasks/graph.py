from typing import TypeVar, Generic
from collections import deque

__all__ = ("Node", "Graph")

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

        self.outbound: list[Node] = []
        self.inbound: list[Node] = []

    @property
    def value(self) -> T:
        return self._value

    def point_to(self, other: "Node") -> None:
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self) -> str:
        return f"Node({repr(self._value)})"

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node) -> None:
        self._root = root

    def dfs(self) -> list[Node]:
        visited_nodes = []

        def dfs_node(node: Node) -> None:
            if node not in visited_nodes:
                visited_nodes.append(node)
                for child in node.outbound:
                    dfs_node(child)

        dfs_node(self._root)
        return visited_nodes

    def bfs(self) -> list[Node]:
        visited_nodes = []
        queue = deque()

        current_node = self._root
        while current_node:
            if current_node not in visited_nodes:
                visited_nodes.append(current_node)
                queue.append((current_node,))
                for child in current_node.outbound:
                    queue.append((child,))
            try:
                current_node = queue.popleft()[0]
            except IndexError:
                break

        return visited_nodes
