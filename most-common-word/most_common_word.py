# This should be a simple word counter which give us the most common word in a file
# If ran from the command line without arguments it should print out the usage:
# python most_common_word.py [source]
# When no argument is provided print out
# No source provided
# When the argument provided and the source is a file
# count all words in the given file and print the most common
# ("cat", "CAT", "cat," "cat." are different words )

import sys
from collections import Counter

class WordCounter():
    def __init__(self):
        self.args = sys.argv
        self.command = sys.argv[1:]
        if len(self.args) == 1:
            print("python most_common_word.py [source]")
        elif len(sys.argv) == 2 :
            print ("No source provided")
        elif len(self.command) == 3 and self.command[0] == 'python':
                self.read_write(self.command[1], self.command[2])

    def MostCommonWord(self, program, source):
        try:
            source_file = open(source, mode='r')
            file_content = source_file.read()
            source_file.close()
            words_to_count = []
            for w in file_content:
                if w not in words_to_count:
                    words_to_count.append(w)
            for word in words_to_count:
                count = 0
                if word == word:
                    count += 1
            return count
        except FileNotFoundError:
            print('No such file was found')

count = WordCounter()
count.MostCommonWord("most_common_word.py", "filetoread.txt")
