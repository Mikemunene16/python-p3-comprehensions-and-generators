#!/usr/bin/env python3

def return_evens(num_list):

    even_elements = [x for x in num_list if x % 2 == 0]
    
    # Check if even_elements list is empty
    if not even_elements:
        return []  # Return an empty list if there are no even elements
    else:
        return even_elements  # Return the list of even elements

def make_exclamation(sentence_list):
    exclaimed_sentence_list = [sentence + '!' for sentence in sentence_list]
    return exclaimed_sentence_list