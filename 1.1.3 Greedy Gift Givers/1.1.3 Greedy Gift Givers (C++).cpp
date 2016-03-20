// Copyright (c) 2012 Nathan Wailes
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
// 
// Author(s): Nathan Wailes
// 
// ID: pablomo1
// PROG: gift1
// LANG: C++
// 
// TASK
// Given a group of friends, no one of whom has a name longer than 14
// characters, the money each person in the group spends on gifts, and a
// (sub)list of friends to whom each person gives gifts, determine how much more
// (or less) each person in the group gives than they receive.
//
// More in-depth overview
// Look at the first number; then add those names to the output array in the
// order they're given (it HAS to be in that order). Then go to the first name 
// after the initial list and check who it is against our list and calculate
// whether they'll have any money left over (get the amount of money they start
// with modulus the number of people they're giving to) save that amount to
// another array that's in the same order as the first array
//
// The code below creates a list of people that I can use later.  The input data
// doesn't necessarily order the data consistently, eg you may have Nathan
// listed before Alice in the initial list but then have Alice's gift-giving 
// behavior described before Nathan's. To handle this we'll check each name 
// later on against this list to see who we're talking about. We'll track each 
// person's money in a separate array.
// 
// I think the best way to do this is as a giant loop, where the program handles
// each person one at a time.
// 
// So, the pseudocode would be:
// 1. Get the number of people
// 2. OUTER LOOP: For each person, get their initial amount of money and figure 
//    out the remainder after they've given out gifts.
// 3. INNER LOOP: Then do a sub-loop through the other people and find out which
//    of the other people will be giving this person money.
// 4. Then use all that to calculate the final value for the first person and 
//    save it to an output array.
// 5. Repeat the outer loop for the next person.

#include <iostream>
#include <fstream>
#include <string>

int
main(void)
{
  using namespace std;

  // INPUT
  ifstream fin ("gift1.in");
	
  // Line 1: The single integer, NP (NumberOfPeople)
  int number_of_people;
	fin >> number_of_people;
	
  // Lines 2..NP+1: 	Each line contains the name of a group member
  // This loop populates the list_of_names array and creates default values
  // of 0 for the change_in_money array.
  string list_of_names[number_of_people];
	int change_in_money[number_of_people] = {0}; // everyone starts at 0
	for (int p = 0; p < number_of_people; p++) {
    fin >> list_of_names[p];
	}

// Lines NP+2..end: NP groups of lines organized like this:
// The first line in the group tells the person's name who will be giving gifts.
// The second line in the group contains two numbers: The initial amount of
// money (in the range 0..2000) to be divided up into gifts by the giver and 
// then the number of people to whom the giver will give gifts, NGi
// (0 <= NGi <= NP-1).

  // This huge loop populates the change_in_money array.
  for (int i = 0; i < number_of_people; i++) {
    
    string giver_name;
    int total_amount_given, number_of_recipients;
    fin >> giver_name >> total_amount_given >> number_of_recipients;

    if (total_amount_given > 0) {
    
      // Determining the change in money for the GIVER
      int giver_index = 0;
      for (int k = 0; k < number_of_people; k++) {
        if (giver_name == list_of_names[k]) {
          giver_index = k;
        }
      }
      int amount_after_gifts = total_amount_given % number_of_recipients;
      change_in_money[giver_index] -= (total_amount_given - amount_after_gifts);

      // Determining the change in money for the giver's RECIPIENTS
      for (int j = 0; j < number_of_recipients; j++) {
        string recipient_name;
        fin >> recipient_name;
        for (int k = 0; k < number_of_people; k++) {
          if (recipient_name == list_of_names[k]) {
            change_in_money[k] += (total_amount_given / number_of_recipients);
          }
        }
      }
    }
  }

// OUTPUT
// The output is NP lines, each with the name of a person followed by a single
// blank followed by the net gain or loss (final_money_value - 
// initial_money_value) for that person. The names should be printed in the same
// order they appear on line 2 of the input.

  ofstream fout ("gift1.out");
	for (int p = 0; p < number_of_people; p++) {
	  fout << list_of_names[p] << " " << change_in_money[p] << endl;
	}


  return (0);
}
