class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.char < other.char


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b,
    with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    if a.char < b.char:
        Node = HuffmanNode(a.char, a.freq + b.freq)
    else:
        Node = HuffmanNode(b.char, a.freq + b.freq)
    Node.left = a
    Node.right = b
    return Node


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    fp = open(filename, 'r')
    List = [0] * 256
    for i in "".join(fp.readlines()):
        List[ord(i)] += 1
    fp.close()
    return List


def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    if sum(char_freq) == 0:
        return None
    Nodes = []
    for i in range(256):
        if char_freq[i] != 0:
            Nodes.append(HuffmanNode(i, char_freq[i]))
    Nodes = sorted(Nodes, key=lambda Node: Node.freq)[::-1]
    while 1 < len(Nodes):
        new = combine(Nodes.pop(), Nodes.pop())
        if len(Nodes) != 0 and new < Nodes[-1]:
            Nodes.append(new)
        else:
            try:
                n = -1
                temp = Nodes[n]
                while temp < new:
                    n -= 1
                    temp = Nodes[n]
                Nodes.insert(n + 1, new)
            except IndexError:
                Nodes.insert(0, new)
    return Nodes[0]


def create_code(node):
    """Returns an array (Python list) of Huffman codes. 
    For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman 
    code for that character stored at that location"""
    if node == None:
        return None
    codes = [""] * 256
    for i in get_codes([(node, "")], []):
        codes[i[0]] = i[1]
    return codes


def get_codes(branches, codes):
    if len(branches) == 0:
        return codes
    new = []
    for i in branches:
        if i[0].left != None:
            new.append((i[0].left, i[1] + '0'))
        if i[0].right != None:
            new.append((i[0].right, i[1] + '1'))
        if i[0].left == None and i[0].right == None:
            codes.append((i[0].char, i[1]))
    return get_codes(new, codes)


def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    head = []
    for i in range(256):
        if freqs[i] != 0:
            head.append(str(i))
            head.append(str(freqs[i]))
    return " ".join(head)


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input 
    file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    fp = open(in_file, 'r')
    fp2 = open(out_file, 'w')
    freq_list = cnt_freq(in_file)
    fp2.write(create_header(freq_list))
    codes = create_code(create_huff_tree(freq_list))
    fp2.write('\n')
    for i in "".join(fp.readlines()):
        fp2.write(codes[ord(i)])
    fp.close()
    fp2.close()


def parse_header(header_string):
    List = [0]*256
    header_string = header_string.split()
    for i in range(0, len(header_string), 2):
        List[int(header_string[i])] = int(header_string[i + 1])
    return List


def huffman_decode(encoded_file, decode_file):
    fp = open(encoded_file, 'r')
    temp = tree = create_huff_tree(parse_header(fp.readline()))
    bits = fp.readline()
    fp2 = open(decode_file, 'w')
    if len(bits) == 0 and tree != None:
        for i in range(tree.freq):
            fp2.write(chr(temp.char))
    for i in bits:
        if i == '0':
            temp = temp.left
        else:
            temp = temp.right
        if temp.right == None and temp.left == None:
            fp2.write(chr(temp.char))
            temp = tree
    fp.close()
    fp2.close()
