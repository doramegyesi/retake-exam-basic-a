# This should be a simple word counter which give us the most common word in a file
# If ran from the command line without arguments it should print out the usage:
# python most_common_word.py [source]
# When no argument is provided print out
# No source provided
# When the argument provided and the source is a file
# count all words in the given file and print the most common
# ("cat", "CAT", "cat," "cat." are different words )

import sys

class WordCounter():
    def __init__(self):
        self.args = sys.argv
        if len(self.args) == 1:
            print("No source provided")
        elif len(sys.argv) == 2 :
            print ('python most_common_word.py [source]')
