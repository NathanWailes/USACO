/*
ID: pablomo1
PROG: ride
LANG: C++
*/

#include <iostream>
#include <string>
#include <fstream>


int
ConvertANameToTheProductOfItsLettersNumberEquivalents(string Name) {
  int NameProduct = 1;
  int i = 0;
  char Alphabet [26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
  while (i < Name.length()) {
    char LetterInQuestion = Name[i];
    int LetterNumberEquivalent = 1;
    int j = 0;
    while (j < sizeof Alphabet) {
      if (LetterInQuestion == Alphabet[j]) {
        LetterNumberEquivalent = j + 1;
        break;
      }
      else {
        j = j + 1;
      }
    }
    NameProduct = NameProduct * LetterNumberEquivalent;
    i = i + 1;
  }
  return NameProduct;
}

int
main(void) {

  using namespace std;

  ofstream fout ("ride.out");
  ifstream fin ("ride.in");

  string CometName;
  string GroupName;
  fin >> CometName >> GroupName;

  int CometNameProduct = ConvertANameToTheProductOfItsLettersNumberEquivalents (CometName);
  int GroupNameProduct = ConvertANameToTheProductOfItsLettersNumberEquivalents (GroupName);

  if ((CometNameProduct%47) == (GroupNameProduct%47)) {
    fout << "GO" << endl;
  }
  else {
    fout << "STAY" << endl;
  }
  return 0;
}
