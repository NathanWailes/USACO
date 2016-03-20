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
#PROG: namenum
#LANG: Python

##TASK
##Among the large Wisconsin cattle ranchers, it is customary to brand cows
##with serial numbers to please the Accounting Department. The cow hands don't
##appreciate the advantage of this filing system, though, and wish to call the
##members of their herd by a pleasing name rather than saying, "C'mon, #4734,
##get along."
##
##Help the poor cowhands out by writing a program that will translate the brand
##serial number of a cow into possible names uniquely associated with that
##serial number. Since the cow hands all have cellular saddle phones these
##days, use the standard Touch-Tone(R) telephone keypad mapping to get from
##numbers to letters (except for "Q" and "Z"):
##
##          2: A,B,C     5: J,K,L    8: T,U,V
##          3: D,E,F     6: M,N,O    9: W,X,Y
##          4: G,H,I     7: P,R,S
##Acceptable names for cattle are provided to you in a file named "dict.txt",
##which contains a list of fewer than 5,000 acceptable cattle names (all
##letters capitalized). Take a cow's brand number and report which of all the
##possible words to which that number maps are in the given dictionary which is
##supplied as dict.txt in the grading environment (and is sorted into ascending
##order).
##
##For instance, the brand number 4734 produces all the following names:
##
##GPDG GPDH GPDI GPEG GPEH GPEI GPFG GPFH GPFI GRDG GRDH GRDI
##GREG GREH GREI GRFG GRFH GRFI GSDG GSDH GSDI GSEG GSEH GSEI
##GSFG GSFH GSFI HPDG HPDH HPDI HPEG HPEH HPEI HPFG HPFH HPFI
##HRDG HRDH HRDI HREG HREH HREI HRFG HRFH HRFI HSDG HSDH HSDI
##HSEG HSEH HSEI HSFG HSFH HSFI IPDG IPDH IPDI IPEG IPEH IPEI
##IPFG IPFH IPFI IRDG IRDH IRDI IREG IREH IREI IRFG IRFH IRFI
##ISDG ISDH ISDI ISEG ISEH ISEI ISFG ISFH ISFI
##As it happens, the only one of these 81 names that is in the list of valid
##names is "GREG".
##
##Write a program that is given the brand number of a cow and prints all the
##valid names that can be generated from that brand number or "NONE" if there
##are no valid names. Serial numbers can be as many as a dozen digits long.
##
##PROGRAM NAME: namenum
##
##INPUT FORMAT
##A single line with a number from 1 through 12 digits in length.
##SAMPLE INPUT (file namenum.in)
##4734
##
##OUTPUT FORMAT
##A list of valid names that can be generated from the input, one per line, in
##ascending alphabetical order.
##SAMPLE OUTPUT (file namenum.out)
##GREG

def main():
    the_input_filename = 'namenum.in'
    the_cows_number = get_the_cows_number_given(the_input_filename)
    
    the_dictionarys_filename = 'dict.txt'
    dictionary = get_dictionary_given(the_dictionarys_filename)

    the_list_of_names = get_the_list_of_names_given(the_cows_number, dictionary)
    output_the_answer_given(the_list_of_names)

def get_the_cows_number_given(the_input_filename):
    ##INPUT FORMAT
    ##A single line with a number from 1 through 12 digits in length.
    ##SAMPLE INPUT (file namenum.in)
    ##4734
    input_file = open(the_input_filename, 'r')
    the_cows_number = int(input_file.readline())
    return the_cows_number

def get_dictionary_given(its_filename):
    dict_file = open(its_filename, 'r')
    dictionary = []
    for line in dict_file.read().split('\n'):
        dictionary.append(line)
    dict_file.close()
    return dictionary

def get_the_list_of_names_given(cow_number, dictionary):
    possible_letter_combinations = get_T9_letter_combinations(cow_number)
    valid_names = []
    for p in possible_letter_combinations:
        if p in dictionary:
            valid_names.append(p)
    return valid_names

def get_T9_letter_combinations(number):
    """use recursion to come up with every possible combination"""
    phone = {1: "", 2: "A B C", 3: "D E F", 4: "G H I", 5: "J K L", \
             6: "M N O", 7: "P R S", 8: "T U V", 9: "W X Y"}
    list_of_possibilities = []
    #base case
    if len(str(number)) == 1:
        return phone[number].split()
    else: #recursive case
        current_digit = int(str(number)[0])
        later_digits = int(str(number)[1:])
        current_digit_possible_letters = phone[current_digit].split()
        current_digit_possibilities = []
        later_digit_possibilities = get_T9_letter_combinations(later_digits)
        for l in range(len(current_digit_possible_letters)):
            for p in range(len(later_digit_possibilities)):
                current_digit_possibilities.append( \
                    current_digit_possible_letters[l] + \
                    later_digit_possibilities[p])
        return current_digit_possibilities

def output_the_answer_given(valid_names):
    ##OUTPUT FORMAT
    ##A list of valid names that can be generated from the input, one per line,
    ##in ascending alphabetical order.
    ##SAMPLE OUTPUT (file namenum.out)
    ##GREG
    output_file = open('namenum.out', 'w')
    if (len(valid_names) == 0):
        output_file.write("NONE")
    else:
        for n in valid_names:
            output_file.write("%s\n" % (n))

if __name__ == '__main__':
    main()
#########################THIS LINE IS 80 CHARACTERS LONG########################
#########################THIS LINE IS 80 CHARACTERS LONG########################
