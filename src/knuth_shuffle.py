from random import randint, random
from math import floor

#
# From Wikipedia:
#
# the Knuth Shuffle is an algorithm to generate a random 
# permutation of a finite sequence. In simple terms, the
# algorithm shuffles the sequence.

def knuth_shuffle(input_list):
    # find the length of the input list to be permuted. 
    # generate a list which has the numbers from 0 to that number minus 1.
    list_range = range(0, len(input_list))

    for first_index in list_range:
        second_index = randint(list_range[0], list_range[-1])
        swap = input_list[first_index]
        input_list[second_index] = input_list[first_index]
        input_list[first_index] = swap
    return input_list

#
# code downloaded from the Internet
# cannot find the source
#
# DEVNOTE: found the source
# URL: https://gist.github.com/JenkinsDev/1e4bff898c72ec55df6f
def knuth_shuffle_improved(input_list):
    amnt_to_shuffle = len(input_list)

    while amnt_to_shuffle > 1:

        i = int(floor(random() * amnt_to_shuffle))

        amnt_to_shuffle -= 1

        input_list[i], input_list[amnt_to_shuffle] = input_list[amnt_to_shuffle], input_list[i]
    return input_list
