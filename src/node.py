import math
import uuid

class Node:
    def __init__(self):
        self._label = math.inf
        self._visited = False
        self._neighbors = []
        self._parent = None
        self._id = uuid.uuid4()

    def add_neighbor(self, node):
        self._neighbors.append(node)

    def mark_as_visited(self):
        self._visited = True

    def reset_visit_status(self):
        self._visited = False

    @property
    def id(self):
        return str(self._id)

    @property
    def visited(self):
        return self._visited

    @property
    def parent(self):
        return self._parent

    @parent.setter(self, parent):
        self._parent = parent

    @property
    def partition_label(self):
        return self._label

    @partition_label.setter
    def partition_label(self, new_label):
        self._label = min(self._label, new_label)

    @property
    def neighbors(self):
        return [node for node in self._neighbors]

    @property
    def non_parent_neighbors(self):
        return [node for node in self._neighbors if node is not self.parent]

    @property
    def non_visited_neighbors(self):
        return [node for node in self._neighbors if not node.visited]
