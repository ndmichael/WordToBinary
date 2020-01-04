"""WordToBinary Converter
This code is up for Optimization,
your contribution is welcome, coz its a means for me to learn

This code converts user inputed words to its binary equivalence
First the words are converted into  ASCII using ord()
then converted to binary which is formatted and printed

PS: incase you wanted be geekie and tell your girl
" I Love You" in binary LOL

#Written by: Micheal "BlackRose" Ukeje

"""


# Class declaration
class WordToBinary:
    def __init__(self, word):
        self.word = word
        self.word_split = self.word.split()

    # Utility method to split words
    def word_slice(self):
        self.word_sliced = []
        for wrd in self.word:
            if wrd != " ":  # this removes the spaces in d word
                self.word_sliced.append(wrd)
        # Result is passed to be converted to ASCII
        self.ord_converter(self.word_sliced)

        # ASCII converter utility method

    def ord_converter(self, word_sl):
        self.word_ord = []
        # word_length = len(self.word)
        for i in word_sl:
            self.word_ord.append(ord(i))
        # Result is passed to be converted to binary
        self.bin_converter(self.word_ord)

    # Binary converter utility method
    def bin_converter(self, wordie):
        self.wordie = wordie
        self.word_bin = []
        for bc in self.wordie:
            self.word_bin.append(bin(bc)[2:])  # remove prefix then append
        return self.word_bin

    # prints the result to the screen
    def printout(self):
        final_result = zip(self.word_sliced, self.word_bin)
        print("Binary Equivalent \t\t\t Word", end="\n\n")
        for w, b in final_result:
            print(f"{b} {w.rjust(23)}", end="\n\n")


if __name__ == "__main__":
    user_inp = input(" Enter your Word: \n")
    print(user_inp)
    print(" \n\n")
    obj = WordToBinary(user_inp)
    obj.word_slice()
    obj.printout()



