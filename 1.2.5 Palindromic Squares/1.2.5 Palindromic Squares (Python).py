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
#PROG: palsquare
#LANG: Python

##TASK
##Palindromes are numbers that read the same forwards as backwards. The
##number 12321 is a typical palindrome.
##
##Given a number base B (2 <= B <= 20 base 10), print all the integers
##N (1 <= N <= 300 base 10) such that the square of N is palindromic when
##expressed in base B; also print the value of that palindromic square.
##Use the letters 'A', 'B', and so on to represent the digits 10, 11,
##and so on.
##
##Print both the number and its square in base B.
##
##PROGRAM NAME: palsquare
##
##INPUT FORMAT
##A single line with B, the base (specified in base 10).
##SAMPLE INPUT (file palsquare.in)
##10
##
##OUTPUT FORMAT
##Lines with two integers represented in base B. The first integer is
##the number whose square is palindromic; the second integer is the square
##itself.
##SAMPLE OUTPUT (file palsquare.out)
##1 1
##2 4
##3 9
##11 121
##22 484
##26 676
##101 10201
##111 12321
##121 14641
##202 40804
##212 44944
##264 69696


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
        
    if remainder == 0: #if the remainder's 0, tack on any needed 0s for places
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
    ##A single line with B, the base (specified in base 10).
    ##SAMPLE INPUT (file palsquare.in)
    ##10
    input_file = open('palsquare.in', 'r')
    goal_base = int(input_file.readline())

    list_of_palindromes = ""

    #I need to go through all the numbers from 1 to 300, and for each one I
    #need to first square it, then switch it to the goal base,
    #then take the squared value and
    #switch its base to the goal base, and then after I've
    #switched it I need to check if its a palindrome.  If it is, I need to add
    #the switched versions of both numbers to my list to be outputted.
    i = 1
    while i <= 300:
        i_squared = pow(i, 2)

        #switch i^2 to goal base
        i_squared_in_goal_base = switch_base(i_squared, 10, goal_base)

        #if the switched i^2 is a palindrome, add i and i_squared to the string
        #to be outputted
        #
        if its_a_palindrome(str(i_squared_in_goal_base)):
            list_of_palindromes += str(i) + " " + str(i_squared_in_goal_base) \
            + "\n"
        i += 1

    print list_of_palindromes

    ##OUTPUT FORMAT
    ##Lines with two integers represented in base B. The first integer is
    ##the number whose square is palindromic; the second integer is the square
    ##itself.
    output_file = open('palsquare.out', 'w')
    output_file.write(list_of_palindromes)


if __name__ == '__main__':
    main()
#########################THIS LINE IS 80 CHARACTERS LONG########################

#########################THIS LINE IS 80 CHARACTERS LONG########################
