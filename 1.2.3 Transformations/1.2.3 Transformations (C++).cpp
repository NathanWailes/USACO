/*
ID: pablomo1
PROG: transform
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int
main(void) {
  //INPUT FORMAT
  //
  //Line 1:	 A single integer, N
  //Line 2..N+1:	 N lines of N characters (each either `@' or `-'); this
  //               is the square before transformation
  //Line N+2..2*N+1: N lines of N characters (each either `@' or `-');
  //                 this is the square after transformation
  //SAMPLE INPUT (file transform.in)
  //3
  //@-@
  //---
  //@@-
  //@-@
  //@--
  //--@
  ifstream fin ("transform.in");
  int side_length;
	fin >> side_length;
	//create empty arrays of the correct size so I can copy the input into them
	char input_square [side_length][side_length];
	char transformed_square [side_length][side_length];
	char reflected_square [side_length][side_length];
	
  //below I'm filling the arrays I just created with the input from
  //transform.in
  
  //filling in the original square
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      fin >> input_square[r][c];
    }
  }
  //filling in the transformed square
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      fin >> transformed_square[r][c];
    }
  }
  //filling in a reflected version of the original square
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      reflected_square[r][c] = input_square[r][side_length - 1 - c];
    }
  }
  //below I'm checking the original square against the transformed version
  //in various ways to check which of the transformations is happening.
  int possible_manipulations [] = {1, 2, 3, 4, 5, 6, 7};
  //1 - check for a 90 degree rotation
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      if (input_square[r][c] != transformed_square[c][side_length - 1 - r]){
        possible_manipulations[0] = 0;
      }
    }
  }  
  //2 - check for a 180 degree rotation
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      if (input_square[r][c] != 
      transformed_square[side_length - 1 - r][side_length - 1 - c]){
        possible_manipulations[1] = 0;
      }
    }
  }
  //3 - check for a 270 degree rotation
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      if (input_square[r][c] != 
      transformed_square[side_length - 1 - c][r]){
        possible_manipulations[2] = 0;
      }
    }
  }
  //4 - check for a horizontal reflection
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      if (input_square[r][c] != 
      transformed_square[r][side_length - 1 - c]){
        possible_manipulations[3] = 0;
      }
    }
  }
  //5 - if there was a combination, then i'll need to check if any of the three
  //possible rotations were performed on the reflection.  If the only number
  //remaining in the array at the end of this check is "4", then I know it
  //wasn't a combination.
  int reflected_manipulations [] = {1, 2, 3, 4};
  //5-1 - check for a reflection-then-90-degree-rotation
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      if (reflected_square[r][c] != 
      transformed_square[c][side_length - 1 - r]){
        reflected_manipulations[0] = 0;
      }
    }
  }
  //5-2 - check for a reflection-then-180-degree-rotation
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      if (reflected_square[r][c] != 
      transformed_square[side_length - 1 - r][side_length - 1 - c]){
        reflected_manipulations[1] = 0;
      }
    }
  }
  //5-3 - check for a reflection-then-270-degree-rotation
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      if (reflected_square[r][c] != 
      transformed_square[side_length - 1 - c][r]){
        reflected_manipulations[2] = 0;
      }
    }
  }
  //5 - if all of the reflected manipulations were eliminated as possibilities,
  //then eliminate "combination" as a possible transformation
  if (reflected_manipulations[0] == 0 &&
      reflected_manipulations[1] == 0 &&
      reflected_manipulations[2] == 0){
    possible_manipulations[4] = 0;
  }
  //6 - checking for no change
  for (int r = 0; r < side_length; ++r){
    for (int c = 0; c < side_length; ++c){
      if (input_square[r][c] != transformed_square[r][c]){
        possible_manipulations[5] = 0;
      }
    }
  }
  //OUTPUT FORMAT
  //A single line containing the the number from 1 through 7 (described above)
  //that categorizes the transformation required to change from the `before'
  //representation to the `after' representation.
  //SAMPLE OUTPUT (file transform.out)
  //1
  int output_manipulation;
  if (possible_manipulations[0] != 0) {
     output_manipulation = 1;
  } else if (possible_manipulations[1] != 0) {
     output_manipulation = 2;
  } else if (possible_manipulations[2] != 0) {
     output_manipulation = 3;
  } else if (possible_manipulations[3] != 0) {
     output_manipulation = 4;
  } else if (possible_manipulations[4] != 0) {
     output_manipulation = 5;
  } else if (possible_manipulations[5] != 0) {
     output_manipulation = 6;
  } else {
     output_manipulation = 7;
  }
  ofstream fout ("transform.out");
	fout << output_manipulation << endl;
  return (0);
}
