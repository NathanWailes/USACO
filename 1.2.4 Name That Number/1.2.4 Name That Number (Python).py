def main():
    the_input_filename = 'namenum.in'
    the_cows_number = get_the_cows_number_given(the_input_filename)

    the_dictionarys_filename = 'dict.txt'
    dictionary = get_dictionary_given(the_dictionarys_filename)

    the_list_of_valid_names = get_the_list_of_valid_names_given(the_cows_number, dictionary)
    output_the_answer_given(the_list_of_valid_names)


def get_the_cows_number_given(the_input_filename):
    """INPUT FORMAT
    A single line with a number from 1 through 12 digits in length.
    SAMPLE INPUT (file namenum.in)
    4734
    :param the_input_filename: """
    with open(the_input_filename, 'r') as input_file:
        the_cows_number = int(input_file.readline())
    return the_cows_number


def get_dictionary_given(its_filename):
    with open(its_filename, 'r') as dict_file:
        dictionary = []
        for line in dict_file.read().split('\n'):
            dictionary.append(line)
    return dictionary


def get_the_list_of_valid_names_given(the_cows_number, dictionary):
    possible_letter_combinations = get_t9_letter_combinations(the_cows_number)
    valid_names = []
    for p in possible_letter_combinations:
        if p in dictionary:
            valid_names.append(p)
    return valid_names


def get_t9_letter_combinations(the_cows_number):
    """use recursion to come up with every possible combination"""
    phone = {1: "", 2: "A B C", 3: "D E F", 4: "G H I", 5: "J K L", \
             6: "M N O", 7: "P R S", 8: "T U V", 9: "W X Y"}

    if len(str(the_cows_number)) == 1:  # base case
        return phone[the_cows_number].split()
    else:  # recursive case
        current_digit = int(str(the_cows_number)[0])
        later_digits = int(str(the_cows_number)[1:])
        current_digit_possible_letters = phone[current_digit].split()
        later_digit_possibilities = get_t9_letter_combinations(later_digits)
        current_digit_possibilities = get_current_digit_possibilities_given(current_digit_possible_letters,
                                                                            later_digit_possibilities)
        return current_digit_possibilities


def get_current_digit_possibilities_given(current_digit_possible_letters, later_digit_possibilities):
    """ """
    current_digit_possibilities = []
    for l in range(len(current_digit_possible_letters)):
        for p in range(len(later_digit_possibilities)):
            current_digit_possibilities.append(current_digit_possible_letters[l] + later_digit_possibilities[p])
    return current_digit_possibilities


def output_the_answer_given(valid_names):
    """OUTPUT FORMAT
    A list of valid names that can be generated from the input, one per line,
    in ascending alphabetical order.
    SAMPLE OUTPUT (file namenum.out)
    GREG"""
    with open('namenum.out', 'w') as output_file:
        if not valid_names:
            output_file.write("NONE")
        else:
            for n in valid_names:
                output_file.write("%s\n" % (n))


if __name__ == '__main__':
    main()
