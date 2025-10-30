class Node:
    """
    This is a Node or binary Tree- A Huffman Tree
    """

    def __init__(self, byte, frequency):
        self.frequency = frequency
        self.byte = byte
        self.left = None
        self.right = None

    def __str__(self):
        return self.frequency

    def __lt__(self, other):
        self.frequency < other.frequency
