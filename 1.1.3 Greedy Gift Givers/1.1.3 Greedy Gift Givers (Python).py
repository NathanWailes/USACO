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
#PROG: gift1
#LANG: Python

# TASK
# Given a group of friends, no one of whom has a name longer than 14 characters,
# the money each person in the group spends on gifts, and a (sub)list of friends
# to whom each person gives gifts, determine how much more (or less) each person
# in the group gives than they receive.

# More in-depth overview
# Look at the first number; then add those names to the output array in the
# order they're given (it HAS to be in that order). Then go to the first name 
# after the initial list and check who it is against our list and calculate
# whether they'll have any money left over (get the amount of money they start
# with modulus the number of people they're giving to) save that amount to
# another array that's in the same order as the first array


# The code below creates a list of people that I can use later.  The input data
# doesn't necessarily order the data consistently, eg you may have Nathan listed
# before Alice in the initial list but then have Alice's gift-giving behavior
# described before Nathan's. To handle this we'll check each name later on
# against this list to see who we're talking about. We'll track each person's
# money in a separate array.


# Initializing variables

def main():

    input_data = [5, "dave", "laura", "owen", "vick", "amr", "dave", 200, 3,
                  "laura", "owen", "vick", "owen", 500, 1, "dave", "amr", 150,
                  2, "vick", "owen", "laura", 0, 2, "amr", "vick", "vick", 0, 0]

    number_of_people = input_data[0]
    list_of_names = []
    change_in_money = []


    # This loop populates the list_of_names variable and creates default values
    # of 0 for the change_in_money array.
    for i in range(number_of_people):
        current_person_name = input_data[i+1]
        list_of_names.append(current_person_name)
        change_in_money.append(0)


    # This huge loop populates the change_in_money variable.
    index_of_current_gift_givers_name = number_of_people + 1
    for i in range(number_of_people):

        giver_name = input_data[index_of_current_gift_givers_name]
        total_amount_given = input_data[index_of_current_gift_givers_name+1]
        number_of_recipients = input_data[index_of_current_gift_givers_name+2]

        if (total_amount_given > 0):

            # Determining the change in money for the GIVER
            giver_index = 0
            for k in range(number_of_people):
                if giver_name == list_of_names[k]:
                    giver_index = k
            amount_after_gifts = total_amount_given % number_of_recipients
            change_in_money[giver_index] -= (total_amount_given - amount_after_gifts)

            # Determining the change in money for the giver's RECIPIENTS
            for j in range(number_of_recipients):
                current_gift_recipient = input_data[(index_of_current_gift_givers_name+3)+j]
                for k in range(number_of_people):
                    if (current_gift_recipient == list_of_names[k]):
                        change_in_money[k] += (total_amount_given / number_of_recipients)

        # Incrementing for the next loop
        index_of_current_gift_givers_name += (number_of_recipients + 3)


    # Outputting the values I calculated
    for i in range(number_of_people):
        print list_of_names[i] + " " + str(change_in_money[i])


if __name__ == '__main__':
    main()
