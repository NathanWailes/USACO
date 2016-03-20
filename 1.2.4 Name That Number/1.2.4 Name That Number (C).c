#include <stdio.h>
#include <string.h>

const char* get_the_cows_number_given(const char* the_input_filename) {
    //INPUT FORMAT
    //A single line with a number from 1 through 12 digits in length.
    //SAMPLE INPUT (file namenum.in)
    //4734
    FILE *the_input_file;
    the_input_file = fopen("namenum.in", "r");
    const char* the_cows_number[13];
    int i = 0;
    char next_character_in_file;
    while ((next_character_in_file = fgetc(the_input_file)) != '\n') {
        the_cows_number[i] = "f";
        printf("hi\n");
    }

/*
    //    the_cows_number
*/
    fclose(the_input_file);
    return(the_input_filename);
}

int main()
{
    const char* the_input_filename = "namenum.in";

    const char* the_cows_number = get_the_cows_number_given(the_input_filename);

    /*
    const char* the_dictionarys_filename = "dict.txt";
    get_dictionary_given(the_dictionarys_filename);

*/
    printf(the_cows_number);
    return(0);
}


/*

    int day, year;
    char weekday[20], month[20], dtm[100];

    strcpy( dtm, "Saturday March 25 1989" );
    sscanf( dtm, "%s %s %d %d", weekday, month, &day, &year );

    printf("%s %d, %d = %s\n", month, day, year, weekday );
*/