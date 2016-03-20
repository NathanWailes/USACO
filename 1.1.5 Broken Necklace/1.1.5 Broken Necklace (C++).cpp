/*
ID: pablomo1
PROG: beads
LANG: C++
*/
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
// PROG: beads
// LANG: C++
// 
// TASK:
// You have a necklace of N red, white, or blue beads (3<=N<=350) some of which 
// are red, others blue, and others white, arranged at random. Suppose you are 
// to break the necklace at some point, lay it out straight, and then collect 
// beads of the same color from one end until you reach a bead of a different 
// color, and do the same for the other end (which might not be of the same 
// color as the beads collected before this). Write a program to determine the 
// largest number of beads that can be collected from a supplied necklace. 
//
// Note: When collecting beads, a white bead that is encountered may be treated 
// as either red or blue and then painted with the desired color. The string 
// that represents this configuration will include the three symbols r, b and w.

// Thoughts on solving this:
//
// The key is to break the problem into smaller pieces. So ignore the white
// beads at first; they're an added complication. And ignore the fact that the
// beads are connected in a circle; imagine there's just a single line of beads.
// And start off with a small number of beads, say 3; ignore the fact that the
// final solution will need to be able to handle up to 350 beads.
//
// After thinking about this for a few minutes, a seemingly obvious solution
// came to me that for some reason wasn't obvious before: loop through each bead
// in the string, and calculate a "score" for that bead, ie the number of beads
// you'd be able to collect by splitting the string before/after that bead. Then
// just save the "best" score in a variable as you go through the whole string,
// replacing it if a bead you've just encountered has a better score. Handling
// the fact that the string is connected in a circle, handling white beads, and 
// handling large numbers of beads should be easy with this method.

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int beads_takeable(string beads, int start_bead, string direction);
int increment_bead(string beads, int current_bead, string direction);

int
main(void)
{

  // INPUT FORMAT:

  // Line 1: N, the number of beads
  ifstream fin ("beads.in");
  int number_of_beads;
	fin >> number_of_beads;

  // Line 2: a string of N characters, each of which is r, b, or w
  string string_of_beads;
  fin >> string_of_beads;

  // Initializing
  int max_beads_takeable = 0;

  // This loops through every bead in the string of beads to calculate a score
  // for each bead. It only saves the top score it's found so far, which it 
  // passes to the Output.
  for (int b = 0; b < number_of_beads; ++b) {
    
    int current_beads_score = 2; // you can always get at least two beads
    
    // Count in both directions and add that to the score
    int forward_score = beads_takeable(string_of_beads, b, "right");
    //cout << forward_score << endl;
    int backward_bead = increment_bead(string_of_beads, b, "left");
    //cout << "\nBackward bead: " << backward_bead << endl;
    int backward_score = beads_takeable(string_of_beads, backward_bead, "left");
    current_beads_score += (forward_score + backward_score);

    //cout <<"Bead: " << b;
    //cout << "\nForward score: ";
    //cout << forward_score;
    //cout << "\nBackward score: ";
    //cout << backward_score;
    //cout << "\nCurrent bead's score: ";
    //cout << current_beads_score;
    //cout << "\n\n" ;

    // saves the current bead's score if it's the highest score found so far
    if (current_beads_score > max_beads_takeable) {
      max_beads_takeable = current_beads_score;
    }
  }
  if (max_beads_takeable > number_of_beads) {
    max_beads_takeable = number_of_beads;
  }

  //cout << "\n\nMax beads: " << max_beads_takeable;
  //cin.get();

  // OUTPUT FORMAT:
  // A single line containing the maximum of number of beads that can be
  // collected from the supplied necklace.
  ofstream fout ("beads.out");
	fout << max_beads_takeable << endl;

  return (0);
}


int
beads_takeable(string beads, int start_bead, string direction)
{
  // Initializing
  int i = 0;
  int score = 0;

  // sets the first bead to check based on the direction we'll be moving in
  i = increment_bead(beads, start_bead, direction);
  //cout << "\ni = " << i << endl;
  // checking the initial bead's color
  char color_to_match = beads[start_bead];

  // If the initial bead is white, we need to find the first nonwhite bead
  for (int j = start_bead; color_to_match == 'w';) {
    
    // Setting the color to match to the next bead in the direction we're going
    color_to_match = beads[j];

    // Incrementing in the correct direction
    j = increment_bead(beads, j, direction);
    if (j == start_bead) {
      break;
    }
  }

  // This loops through the beads in whichever direction we chose above.
  while (true) {
    //cout << "\nInner loop: examining bead: " << i << endl;
    // First, the condition to check: This breaks us out of the loop once we hit
    // a nonmatching bead.
    if (
        (beads[i] != color_to_match) &&
        (beads[i] != 'w')
       )
    { break; }
    ++score; // Statement to execute
    i = increment_bead(beads, i, direction); // Increment

    // This handles situations where all the beads can be removed
    if (i == start_bead) {
      score = beads.size();
      // The problem is that when I'm considering whether to break the chain of
      // beads at a particular point, I calculate a score by looking at both 
      // ends of the broken chain and then adding them together.  So if ALL the 
      // beads can be collected, I'm going to get two returned scores of the
      // entire size of the chain.  My solution is to just arbitrarily pick one
      // of the sides to return the size of the chain, with the other one
      // returning zero (which makes the checking a waste of time to begin with,
      // but it would take more time to figure out how to turn it off). I need
      // to subtract two to compensate for the fact that I initialize the score
      // to 2 before I run these checks.
      if (direction == "right") {
        return score - 2;
      }
      else {
        return 0;
      }
    }
  }
  return score;
}

int
increment_bead(string beads, int current_bead, string direction)
{
  int next_bead = 0; // initializing to zero
  //cout << beads << current_bead << direction;
  if (direction == "right") {
    next_bead = current_bead + 1;
  }
  else {
    next_bead = current_bead - 1;
    //cout << next_bead;
  }

  int last_bead = (beads.size() - 1);
  if (next_bead > last_bead) {
    //cout << "next_bead: " << next_bead << endl;
    //cout << "Ibeads.size() - 1: " << (beads.size() - 1) << endl;
    next_bead = 0;
  }
  if (next_bead < 0) {
    //cout << "\nnext_bead < 0\n";
    next_bead = last_bead;
  }
  //cout << "\n" << next_bead << "\n";
  return next_bead;
}
