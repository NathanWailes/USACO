/* 2016.03.20 - I finally got the function 'get_the_cows_number_given()' working.
Next step: implement one of the other functions found in the Python solution (which works). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* get_the_cows_number_given(const char* the_input_filename) {
    /* 2016.03.20 - This function should be good-to-go. */
    FILE *the_input_file;
    the_input_file = fopen("namenum.in", "r");
    char* the_cows_number = malloc(13);
    int i = 0;
    char next_character_in_file;
    while ((next_character_in_file = fgetc(the_input_file)) != '\n') {
        the_cows_number[i] = next_character_in_file;
        putchar(next_character_in_file);
    }

    fclose(the_input_file);
    return(the_cows_number);
}

int main()
{
    const char* the_input_filename = "namenum.in";
    const char* the_cows_number = get_the_cows_number_given(the_input_filename);

    printf(the_cows_number);
    return(0);
}
