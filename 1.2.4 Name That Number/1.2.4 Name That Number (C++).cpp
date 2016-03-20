/*
ID: pablomo1
PROG: namenum
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;

string
get_the_cows_number_given(const char* the_input_filename) {
  //INPUT FORMAT
  //A single line with a number from 1 through 12 digits in length.
  //SAMPLE INPUT (file namenum.in)
  //4734
  //the ifstream function can't take a C++ string as input
  ifstream fin (the_input_filename);
  string cow_number;
	fin >> cow_number;
  return cow_number;
}

std::vector<std::string>
getDictionaryGiven(const char* its_filename) {
  ifstream dictionary_input (its_filename);
  std::vector<std::string> dictionary_array;
  for (int i = 0; !dictionary_input.eof(); ++i) {
    dictionary_array.push_back("");
    getline(dictionary_input,dictionary_array[i]);
  }
  return dictionary_array;
}

std::vector<std::string>
getValidNamesGiven(string the_cows_number, std::vector<std::string> dictionary) {
  std::vector<string> possible_letter_combinations = getT9LetterCombinations(cow_number)
  std::vector<std::string> valid_names;
  for (int i = 0; i < possible_letter_combinations.size(); ++i) {
    //if i in dictionary
    if(std::find(possible_letter_combinations.begin(),
    possible_letter_combinations.end(), i) != 
    possible_letter_combinations.end()) {
      valid_names.push_back(i);
    }
  }
  return valid_names;
}

std::vector<string>
getT9LetterCombinations(string number) {
  map<string, std::vector<string>> phone;
  phone["2"] = ["A", "B", "C"];
  phone["3"] = ["D", "E", "F"];
  phone["4"] = ["G", "H", "I"];
  phone["5"] = ["J", "K", "L"];
  phone["6"] = ["M", "N", "O"];
  phone["7"] = ["P", "R", "S"];
  phone["8"] = ["T", "U", "V"];
  phone["9"] = ["W", "X", "Y"];
  std::vector<string> list_of_possibilities;
  //base case
  if (number.length == 1) {
    return phone[number]
  } else {  //recursive case
  }
}

void
output_the_answer_given(std::vector<std::string> valid_names) {
  //OUTPUT FORMAT
  //A list of valid names that can be generated from the input, one per line, in
  //ascending alphabetical order.
  //SAMPLE OUTPUT (file namenum.out)
  //GREG
  ofstream fout ("namenum.out");
  for (int i = 0;(valid_names[i].compare(" ") != 0) && 
                 (i < valid_names.size()); ++i) {
	  fout << valid_names[i] << endl;
  }
  return;
}

int
main(void) {
  const char* the_input_filename = "namenum.in";
  string the_cows_number = get_the_cows_number_given(the_input_filename);
  const char* the_dictionarys_filename = "dict.txt";
  std::vector<std::string> dictionary = getDictionaryGiven(the_dictionarys_filename);
  std::vector<std::string> valid_names = getValidNamesGiven(the_cows_number, dictionary);
  output_the_answer_given(valid_names);
  return (0);
}
