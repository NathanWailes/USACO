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
// PROG: friday
// LANG: C++
// 
// TASK
// Is Friday the 13th really an unusual event?
// 
// That is, does the 13th of the month land on a Friday less often than on any
// other day of the week? To answer this question, write a program that will
// compute the frequency that the 13th of each month lands on Sunday, Monday,
// Tuesday, Wednesday, Thursday, Friday, and Saturday over a given period of N
// years. The time period to test will be from January 1, 1900 to December 31,
// 1900+N-1 for a given number of years, N. N is non-negative and will not
// exceed 400.

#include <iostream>
#include <fstream>
#include <string>

int is_leap_year(int);

int
main(void)
{
  using namespace std;

  // INPUT: The number of years to calculate for. The number is an integer,
  // non-negative, and will not exceed 400.
  ifstream fin ("friday.in");
  int number_of_years;
	fin >> number_of_years;

  // INITIALIZING
  // I use this_weekday to track the day of the week over time. I use the 
  // convention given in the question, so 0 = Sat, 1 = Sun, 2 = Mon, etc.
  // 
  int thirteens_per_weekday[7] = {0}; // '={0}' sets all values to 0
  int this_weekday = 2;
  int number_of_days;

  // this loops through each of the years.
  for (int y = 0; y < number_of_years; y++) {

    int this_year = 1900 + y;

    // this loops through the months
    for (int m = 1; m <= 12; m++) {
    
      if (m == 1) { number_of_days = 31; }
      if (m == 2) { 
        if (is_leap_year(this_year)) { number_of_days = 29; }
        else {number_of_days = 28; }
      }
      if (m == 3) { number_of_days = 31; }
      if (m == 4) { number_of_days = 30; }
      if (m == 5) { number_of_days = 31; }
      if (m == 6) { number_of_days = 30; }
      if (m == 7) { number_of_days = 31; }
      if (m == 8) { number_of_days = 31; }
      if (m == 9) { number_of_days = 30; }
      if (m == 10) { number_of_days = 31; }
      if (m == 11) { number_of_days = 30; }
      if (m == 12) { number_of_days = 31; }
      
      // this loops through the days
      for (int d = 1; d <= number_of_days; d++) {

        if (d == 13) {
          thirteens_per_weekday[this_weekday]++;
        }
        if (this_weekday < 6) { this_weekday++; }
        else {this_weekday = 0;}

      }
    }

  }

  // OUTPUT: Seven space separated integers on one line. These integers
  // represent the number of times the 13th falls on Saturday, Sunday, Monday,
  // Tuesday, ..., Friday.
  ofstream fout ("friday.out");
	for (int d = 0; d < 7; d++) {
	  fout << thirteens_per_weekday[d];
    if (d < 6) {
    fout << " ";
    }
    else { fout << endl;}
	}


  return (0);
}


int
is_leap_year(int year) {
  if ((year % 4) != 0) { // All leap years are evenly divisible by 4, so if the 
    return 0; // given year isn't evenly divisible by 4, it isn't a leap year.
  }
  if (((year % 100) == 0) && ((year % 400) != 0)) { // Once the previous test is
    return 0; // passed, the only way to not be a leap year is to be a century
  } // year that isn't evenly divisble by 400 (eg 2100).
  return 1;
}
