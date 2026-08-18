#copy-paste from ai...

class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def __repr__(self, level=0):
        ret = "  " * level + f"Node({self.node_id})\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


def build_tree(records):
    if not records:
        raise ValueError("Record list is empty")

    # Sort records by ID
    records.sort(key=lambda r: r.record_id)

    # Validate root
    if records[0].record_id != 0:
        raise ValueError("Root node must have ID 0")

    if records[0].parent_id != 0:
        raise ValueError("Root node must have parent ID equal to itself")

    nodes = {}

    for record in records:
        rid = record.record_id
        pid = record.parent_id

        # Validate ID sequence
        if rid != len(nodes):
            raise ValueError(f"Invalid record ID {rid}: IDs must be continuous starting from 0")

        # Validate parent relationship
        if rid != 0 and pid >= rid:
            raise ValueError(f"Invalid parent ID {pid} for record {rid}: parent must be less than child")

        # Create node
        node = Node(rid)
        nodes[rid] = node

        # Attach to parent
        if rid != 0:
            parent_node = nodes.get(pid)
            if parent_node is None:
                raise ValueError(f"Parent node {pid} not found for record {rid}")
            parent_node.children.append(node)

    return nodes[0]


# -----------------------------
# 🎯 Interactive Input Section
# -----------------------------

def get_user_input():
    try:
        n = int(input("Enter number of records: "))
        if n <= 0:
            raise ValueError("Number of records must be positive")

        records = []
        print("Enter records in format: <record_id> <parent_id>")

        for i in range(n):
            raw = input(f"Record {i+1}: ").strip()
            parts = raw.split()

            if len(parts) != 2:
                raise ValueError("Each record must contain exactly two integers")

            rid, pid = map(int, parts)
            records.append(Record(rid, pid))

        return records

    except ValueError as e:
        raise ValueError(f"Input error: {e}")


# -----------------------------
# 🚀 Main Execution
# -----------------------------

if __name__ == "__main__":
    try:
        records = get_user_input()
        tree_root = build_tree(records)

        print("\nConstructed Tree:")
        print(tree_root)

    except ValueError as e:
        print(f"Error: {e}")

#solution...

class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []
def BuildTree(records: list[Record]) -> Node | None:
    if not records:
        return None
    records = sorted(records, key=lambda x: x.record_id)
    root = Node(records[0].record_id)
    if (root.node_id != 0 or records[-1].record_id != len(records)-1):
        raise ValueError("Record id is invalid or out of order.")
    if records[0].parent_id != records[0].record_id:
        raise ValueError("Node parent_id should be smaller than it's record_id.")
    nodes = {0: root}
    for record in records[1:]:
        if record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")
        node = Node(record.record_id)
        if node.node_id in nodes:
            raise ValueError("Record id is invalid or out of order.")
        nodes[node.node_id] = node
        try:
            nodes[record.parent_id].children.append(node)
        except KeyError:
            raise ValueError( "Record id is invalid or out of order.")
    return root