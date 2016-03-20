# Copyright (c) 2012 Nathan Wailes

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Author(s): Nathan Wailes

#ID: pablomo1
#PROG: ride
#LANG: Python

def ConvertANameToTheProductOfItsLettersNumberEquivalents(Name):
    NameProduct = 1
    i = 0
    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    while i < len(Name):
        LetterInQuestion = Name[i]
        LetterNumberEquivalent = 1
        j = 0
        while j < len(Alphabet):
            if LetterInQuestion == Alphabet[j]:
                LetterNumberEquivalent = j + 1
                break
            else:
                j = j + 1
        NameProduct = NameProduct * LetterNumberEquivalent
        i = i + 1

    return NameProduct


def main():
    CometName = "COMETQ"
    GroupName = "HVNGAT"

    CometNameProduct = ConvertANameToTheProductOfItsLettersNumberEquivalents(CometName)
    GroupNameProduct = ConvertANameToTheProductOfItsLettersNumberEquivalents(GroupName)

    if CometNameProduct%47 == GroupNameProduct%47:
        print "GO"

    else:
        print "STAY"


if __name__ == '__main__':
    main()
