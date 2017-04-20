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
        self.command = sys.argv[1:]
        if len(self.args) == 0:
            print("python most_common_word.py [source]")
        elif len(sys.argv) == 1 :
            print ("No source provided")
        elif len(self.command) == 2 and self.command[0] == 'most_common_word.py':
            self.most_common_word(self.command[0], self.command[1])

    def most_common_word(self, program, source):
        try:
            source_file = open(source, mode='r')
            file_content = source_file.read()
            self.total = []
            count = 0
            for word in file_content:
                if word == word:
                    count += 1
            self.total.sort()
            self.total.reverse()
            source_file.close()
            a = self.total[0]
            return a
        except FileNotFoundError:
            print('No such file was found')

count_that = WordCounter()
count_that.most_common_word("most_common_word.py", "filetoread.txt")
