from hash_node import *

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and
        insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        fp = open(filename, 'r')
        self.stop_table = HashTable(191)
        for line in fp.readlines():
            self.stop_table.insert(line.split()[0], 0)
        fp.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and
        insert them into the concordance hash table, 
        after processing for punctuation, numbers and
        filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once,
        just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        fp = open(filename, 'r')
        self.concordance_table = HashTable(191)
        for value, line in enumerate(fp.readlines(), start=1):
            for word in set(line.split()):
                keys = []
                key = []
                for letter in word:
                    if letter.isalpha():
                        key.append(letter.lower())
                    elif letter == "-":
                        keys.append("".join(key))
                        key = []
                keys.append("".join(key))
                for key in keys: 
                    if len(key) != 0 and not self.stop_table.in_table(key):
                        self.concordance_table.insert(key, value)
        fp.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        fp = open(filename, 'w')
        words = []
        for i in self.concordance_table.hash_table:
            if i != None:
                word = []
                word.append(i.key + ":")
                for num in self.concordance_table.get_value(i.key):
                    word.append(str(num))
                words.append(" ".join(word))
        words.sort()
        for i in range(len(words) - 1):
            fp.write(words[i])
            fp.write('\n')
        fp.write(words[-1])
        fp.close()
