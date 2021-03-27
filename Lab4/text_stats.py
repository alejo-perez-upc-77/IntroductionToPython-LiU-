#!/usr/bin/env python3 

## answers to the additional questions:
# 1. all words are lowercase and kept only symbols a-z
# 2. most common structure was list, for 2d array used numpy array as its easier to filter,
#    also list of tuples as it was returned by counter.

import re, collections, sys 
import numpy as np


N_FOLLOWING_WORDS = 3
N_MOST_COMMON_WORDS = 5

def read_file(name):
    # return list of words and list of characters
    with open(name,'r',encoding="utf8") as file: 
        words = [re.sub('[^a-z]+', '', word.lower()) for line in file for word in line.split() ]
    letters = [char for word in words for char in word]

    return words, letters


def count_frequencies(string_list):
    elements_count = collections.Counter(string_list)
    return elements_count.most_common()

def print_frequencies(tuple_list):
    for key, value in tuple_list:
        print(f"{key}: {value}")
    return ""

def unique_values(string_list):
    unique_list = list(set(string_list))
    return unique_list

def get_array_with_following_words(words):
    ## array: collumn 1 - words; column2 - following words
    word_shifted = words[1:]
    word_shifted.append("")
    words_with_following = np.column_stack((words, word_shifted))
    return words_with_following

def get_most_common_following_words(word,words_flw):
    ## extract word we are interested in 
    word_list = words_flw[(words_flw[:,0]==word), 1]
    ## count
    ordered_frequencies = count_frequencies(word_list)
    return ordered_frequencies


def print_N_most_common_following_words(word, words_flw, N):
    ordered_frequencies = get_most_common_following_words(word,words_flw)
    iterations = lambda x: N if (len(x) > N) else len(x)
    for i in range(iterations(ordered_frequencies)):
        point = ordered_frequencies[i]
        print(f"----\"{point[0]}\": {point[1]}")
    return ""

def print_N_most_common_words(words, n_common, n_following):
    ## count frequencies of word
    ordered_word_freq = count_frequencies(words)
    words_flw = get_array_with_following_words(words)
    for i in range(n_common):
        point = ordered_word_freq[i]
        print(f"\n{point[0]}: {point[1]}")
        print_N_most_common_following_words(point[0], words_flw, n_following) 
    return ""

def print_output(file_name,n_most_common_words,n_following_words):
        try:
            words, letters = read_file(file_name)
        except:
            print("this file does not exist!")  
        else:
            print("letter frequencies: \n")
            print_frequencies(count_frequencies(letters))

            print("\n number of words:", len(words))
            print("\n number of unique words:", len(unique_values(words)))

            print_N_most_common_words(words,n_most_common_words,n_following_words)
            return ""


if __name__ == "__main__":
    
    try:
        infile = sys.argv[1]
    except:
        print("Please provide a text file name")
    else:    
        if len(sys.argv)==3:
            with open(sys.argv[2], 'w') as f:
                original_stdout = sys.stdout
                sys.stdout = f # Change the standard output to the file we created.
                print_output(infile,N_MOST_COMMON_WORDS, N_FOLLOWING_WORDS)
                    

                sys.stdout = original_stdout # Reset the standard output to its original value
        else:
            print_output(infile,N_MOST_COMMON_WORDS, N_FOLLOWING_WORDS)

        