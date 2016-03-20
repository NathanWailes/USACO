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
#PROG: transform
#LANG: Python

##TASK
##A square pattern of size N x N (1 <= N <= 10) black and white square
##tiles is transformed into another square pattern. Write a program that
##will recognize the minimum transformation that has been applied to the
##original pattern given the following list of possible transformations:
##
###1: 90 Degree Rotation: The pattern was rotated clockwise 90 degrees.
###2: 180 Degree Rotation: The pattern was rotated clockwise 180 degrees.
###3: 270 Degree Rotation: The pattern was rotated clockwise 270 degrees.
###4: Reflection: The pattern was reflected horizontally (turned into a
##    mirror image of itself by reflecting around a vertical line in the
##    middle of the image).
###5: Combination: The pattern was reflected horizontally and then
##    subjected to one of the rotations (#1-#3).
###6: No Change: The original pattern was not changed.
###7: Invalid Transformation: The new pattern was not obtained by any of
##    the above methods.
##In the case that more than one transform could have been used, choose
##the one with the minimum number above.
##
##PROGRAM NAME: transform
##
##INPUT FORMAT
##
##Line 1:	 A single integer, N
##Line 2..N+1:	 N lines of N characters (each either `@' or `-'); this
##               is the square before transformation
##Line N+2..2*N+1: N lines of N characters (each either `@' or `-');
##                 this is the square after transformation
##SAMPLE INPUT (file transform.in)
##
##3
##@-@
##---
##@@-
##@-@
##@--
##--@
##OUTPUT FORMAT
##
##A single line containing the the number from 1 through 7 (described above)
##that categorizes the transformation required to change from the `before'
##representation to the `after' representation.
##SAMPLE OUTPUT (file transform.out)
##1


def main():

    ##INPUT FORMAT
    ##
    ##Line 1:	 A single integer, N
    ##Line 2..N+1:	 N lines of N characters (each either `@' or `-'); this
    ##               is the square before transformation
    ##Line N+2..2*N+1: N lines of N characters (each either `@' or `-');
    ##                 this is the square after transformation
    ##SAMPLE INPUT (file transform.in)
    ##3
    ##@-@
    ##---
    ##@@-
    ##@-@
    ##@--
    ##--@
    input_file = open('transform.in', 'r')

    side_length = int(input_file.readline())

    #this creates empty arrays of the correct size; I'm going to copy the input
    #data into these
    input_square = [None] * side_length
    transformed_square = [None] * side_length
    reflected_square = [None] * side_length
    for i in range(side_length):
        input_square[i] = [None] * side_length
        transformed_square[i] = [None] * side_length
        reflected_square[i] = [None] * side_length

    #below I'm filling the arrays I just created with the input from
    #transform.in

    #filling in the original square
    for r in range(side_length):
        current_row = input_file.readline()
        for c in range(side_length):
            input_square[r][c] = current_row[c]

    #filling in the transformed version of the square from input
    for r in range(side_length):
        current_row = input_file.readline()
        for c in range(side_length):
            transformed_square[r][c] = current_row[c]

    #filling in a reflected version of the original square
    for r in range(side_length):
        for c in range(side_length):
            reflected_square[r][c] = input_square[r][side_length - 1 - c]

    #below I'm checking the original square against the transformed version
    #in various ways to check which of the transformations is happening.
    possible_manipulations = [1, 2, 3, 4, 5, 6, 7]
    for r in range(side_length):
        for c in range(side_length):

            #1 - 90 deg rotation
            if 1 in possible_manipulations and \
               (input_square[r][c] != \
                transformed_square[c][side_length - 1 - r]):
                possible_manipulations.pop(possible_manipulations.index(1))

            #2 - 180 deg rotation
            if 2 in possible_manipulations and \
               (input_square[r][c] != \
                transformed_square[side_length - 1 - r][side_length - 1 - c]):
                possible_manipulations.pop(possible_manipulations.index(2))  

            #3 - 270 deg rotation
            if 3 in possible_manipulations and \
               (input_square[r][c] != \
                transformed_square[side_length - 1 - c][r]):
                possible_manipulations.pop(possible_manipulations.index(3))

            #4 - reflection
            if 4 in possible_manipulations and \
               (input_square[r][c] != \
                transformed_square[r][side_length - 1 - c]):
                possible_manipulations.pop(possible_manipulations.index(4))  

            #6 - no change
            if 6 in possible_manipulations and \
               (input_square[r][c] != transformed_square[r][c]):
                possible_manipulations.pop(possible_manipulations.index(6))

            c += 1 # go to the next column
        r += 1 # go to the next row

    #if there was a combination, then i'll need to check if any of the three
    #possible rotations were performed on the reflection.  If the only number
    #remaining in the array at the end of this check is "4", then I know it
    #wasn't a combination.
    reflected_manipulations = [1, 2, 3, 4]

    for r in range(side_length):
        for c in range(side_length):
            #5-1 - 90 deg rotation
            if 1 in reflected_manipulations and \
               (reflected_square[r][c] != \
                transformed_square[c][side_length - 1 - r]):
                reflected_manipulations.pop(reflected_manipulations.index(1))

            #5-2 - 180 deg rotation
            if 2 in reflected_manipulations and \
               (reflected_square[r][c] != \
                transformed_square[side_length - 1 - r][side_length - 1 - c]):
                reflected_manipulations.pop(reflected_manipulations.index(2)) 

            #5-3 - 270 deg rotation
            if 3 in reflected_manipulations and \
               (reflected_square[r][c] != \
                transformed_square[side_length - 1 - c][r]):
                reflected_manipulations.pop(reflected_manipulations.index(3))

            c += 1 # go to the next column
        r += 1 # go to the next row

    #if all of the reflected manipulations were eliminated as possibilities,
    #then eliminate "combination" as a possible transformation
    if reflected_manipulations[0] == 4:
        possible_manipulations.pop(possible_manipulations.index(5))

    #output the first type of manipulation that could match the data
    print possible_manipulations[0]
    output_file = open('transform.out', 'w')
    output_file.write("%d\n" % (possible_manipulations[0]))


if __name__ == '__main__':
    main()
#########################THIS LINE IS 80 CHARACTERS LONG########################

#########################THIS LINE IS 80 CHARACTERS LONG########################
