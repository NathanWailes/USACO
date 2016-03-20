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
#PROG: dualpal
#LANG: Python

##A number that reads the same from right to left as when read from left to
##right is called a palindrome. The number 12321 is a palindrome; the number
##77778 is not. Of course, palindromes have neither leading nor trailing
##zeroes, so 0220 is not a palindrome.
##
##The number 21 (base 10) is not palindrome in base 10, but the number 21
##(base 10) is, in fact, a palindrome in base 2 (10101).
##
##Write a program that reads two numbers (expressed in base 10):
##
##N (1 <= N <= 15)
##S (0 < S < 10000)
##and then finds and prints (in base 10) the first N numbers strictly greater
##than S that are palindromic when written in two or more number bases
##(2 <= base <= 10).
##Solutions to this problem do not require manipulating integers larger than
##the standard 32 bits.
##
##PROGRAM NAME: dualpal
##
##INPUT FORMAT
##A single line with space separated integers N and S.
##
##SAMPLE INPUT (file dualpal.in)
##3 25
##
##OUTPUT FORMAT
##N lines, each with a base 10 number that is palindromic when expressed in
##at least two of the bases 2..10. The numbers should be listed in order from
##smallest to largest.
##
##SAMPLE OUTPUT (file dualpal.out)
##26
##27
##28


def switch_base(original_number, starting_base = 10, ending_base = 10):

    #To use base 10 as an example, in this section I'm finding what tens-place
    #is the highest tens-place needed to represent the number I've been given.
    #I do it by trying higher exponents of the base (b^0, b^1, b^2, etc) until I
    #get one that won't divide into the number.  When you find one that won't, 
    #set the current exponent to one less than that number.  It's like testing a
    #bridge by driving bigger and bigger trucks across it until it breaks.
    exponent = 0 #this is the variable I'm trying to set
    i = 0
    while True:
        test_value = pow(ending_base, i) #make a truck, and...
        if (original_number / test_value) < 1: #if it breaks the bridge...
            exponent = i - 1
            break
        i += 1

    #Now I need to find the coefficient.  For example, in the last section I
    #found the highest-tens-place needed, but what digit goes there? 1? 3? 7?
    base_place_value = pow(ending_base, exponent) #eg 16 = 2^4
    coefficient = original_number / base_place_value #eg 1 = 20 / 16 (w/ ints)

    #Here I'm starting to construct the new number (in the destination base)
    new_number = ""
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", \
              "D", "E", "F", "G", "H", "I", "J"]
    new_number += digits[coefficient] #eg if coef is 9, new num is "9".

    #Here I'm figuring out if I need to tack anything else onto the end of the
    #new number:
    total_value = coefficient * base_place_value
    remainder = original_number - total_value
    if remainder > 0:

        tack_on_number = switch_base(remainder, starting_base, ending_base)

        #this bit handles 0s in between other digits
        i = exponent - len(tack_on_number)
        while i>0:
            new_number += "0"
            i -= 1

        #once I've taken care of intermediate 0s I can tack on the rest
        new_number += tack_on_number

    #if the remainder's 0, tack on any needed 0s for places.  For example, I
    #want "900" (base 10) to be represented as "900", not "9".  I need to add on
    #the 0s using the current base-exponent as a clue as to how many I need. For
    #example, if I'm dealing with "9" and that digit should be in the hundreds-
    #place (base 10), then the value of my "exponent" variable will be 2 (from
    #the above code): (9 * 10^2) + (0 * 10^1) + (0 * 10^0).
    if remainder == 0: 
        i = 0
        while True:
            if exponent > i:
                new_number += "0"
                i += 1
            else:
                break

    return new_number


def its_a_palindrome(number):

    num_length = len(number)

    if num_length == 1:
        return True
    if (num_length == 2) and (number[0]==number[1]):
        return True
    if num_length >= 3:
        #I need to check if the middle of the number is a palindrome
        middle_number = number[1:(num_length - 1)]
        if number[0]==number[num_length - 1] and \
        (its_a_palindrome(middle_number)):
            return True

    return False


def main():

    ##INPUT FORMAT
    ##A single line with space separated integers N and S.
    ##SAMPLE INPUT (file dualpal.in)
    ##3 25
    input_file = open('dualpal.in', 'r')
    input_string = input_file.readline()
    number_of_palindromes_to_find = 3 #need to fix this
    starting_number = 1987 #need to fix this

    list_of_palindromes = ""

    #find and print (in base 10) the first N numbers strictly(?) greater
    #than S that are palindromic when written in two or more number bases
    #(2 <= base <= 10).
    found_palindromes = 0
    current_number_to_consider = starting_number + 1
    while found_palindromes < number_of_palindromes_to_find:

        palindrome_confirmed = False
        
        #I need to check whether the current number is a palindrome in the
        #various different bases (2-10)
        current_base = 2
        while current_base <= 10:
                
            #switch the currently-considered number to the currently-considered
            #base
            number_in_current_base = switch_base(current_number_to_consider \
                                                 , 10, current_base)

            #if the switched number is a palindrome, add the base-10 version to the
            #string to be outputted and break out of the loop
            if its_a_palindrome(number_in_current_base):
                list_of_palindromes += str(current_number_to_consider) + "\n"
                found_palindromes += 1
                break
            current_base += 1
        current_number_to_consider += 1

    print list_of_palindromes

    ##OUTPUT FORMAT:
    ##N lines, each with a base 10 number that is palindromic when expressed in
    ##at least two of the bases 2..10. The numbers should be listed in order
    ##from smallest to largest.
    ##SAMPLE OUTPUT (file dualpal.out):
    ##26
    ##27
    ##28
    output_file = open('dualpal.out', 'w')
    output_file.write(list_of_palindromes)


if __name__ == '__main__':
    main()
#########################THIS LINE IS 80 CHARACTERS LONG########################

#########################THIS LINE IS 80 CHARACTERS LONG########################
