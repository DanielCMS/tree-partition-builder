class TreePartition:
    def __init__(self, nodes):
        self._nodes = nodes
        self._node_dic = { node.id: node for node in nodes }

    def build_partition(self):
        self.clear_visit_status()

        stack = []
        partition_counter = 0

        if not len(self._nodes):
            return

        stack.append(self._nodes[0])

        while len(stack):
            tmp_node = stack.pop()

            to_push = []

            if tmp_node.visited:
                for neighbor in tmp_node.non_parent_neighbors:
                    tmp_node.mark_partition_label(neighbor.partition_label)
            else:
                stack.push(tmp_node)
                tmp_node.mark_partition_label(partition_counter)
                tmp_node.mark_as_visited()
                partition_counter += 1

                for neighbor in tmp_node.non_visited_neighbors:
                    neighbor.parent = tmp_node
                    to_push.append(neighbor)

            stack.extend(to_push)

    @property
    def nodes(self):
        return [node in self._nodes]

    def get_node_by_id(self, id):
        return self._node_dic.get(id)

    def clear_visit_status(self):
        for node in self._nodes:
            node.reset_visit_status()

    def get_partition_size(self):
        size_dic = {}

        for node in self._nodes:
            label = node.partition_label
            size_dic[label] = size_dic.get(label, 0) + 1

        size_array = size_dic.values()
        size_array.sort(reverse=True)

        return size_array
