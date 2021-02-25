#!/usr/bin/python

## answers to the additional questions:
# 1. all words are lowercase and kept only symbols a-z
# 2. most common structure was list, for 2d array used numpy array as its easier to filter,
#    also list of tuples as it was returned by counter.

import re, collections, sys 
import numpy as np

def read_file(name):
    # return list of words and list of characters
    with open(name,'r',encoding="utf8") as file: 
        words = [re.sub('[^a-z]+', '', word.lower()) for line in file for word in line.split() ]
    letters = [char for word in words for char in word]
    return words, letters


def count_frequencies(data):
    elements_count = collections.Counter(data)
    return elements_count.most_common()

def print_frequencies(data):
    for key, value in data:
        print(f"{key}: {value}")

def unique_values(data):
    unique_list = list(set(data))
    return unique_list

def get_array_with_following_words(words):
    ## array: collumn 1 - words; column2 - following words
    word_shifted = words[1:]
    word_shifted.append("")
    words_with_following = np.column_stack((words, word_shifted))
    return words_with_following

def get_most_common_following_words(word,words_flw):
    words_with_following = words_flw
    ## extract word we are interested in 
    word_list = words_with_following[(words_with_following[:,0]==word), 1]
    ## count
    ordered_frequencies = count_frequencies(word_list)
    return ordered_frequencies


def print_3_most_common_following_words(word, words_flw):
    ordered_frequencies = get_most_common_following_words(word,words_flw)
    iterations = lambda x: 3 if (len(x) > 3) else len(x)
    for i in range(iterations(ordered_frequencies)):
        point = ordered_frequencies[i]
        print(f"----\"{point[0]}\": {point[1]}")
    return ""

def print_most_common_words(words):
    ## count frequencies of word
    ordered_word_freq = count_frequencies(words)
    words_flw = get_array_with_following_words(words)
    for i in range(5):
        point = ordered_word_freq[i]
        print(f"\n{point[0]}: {point[1]}")
        print_3_most_common_following_words(point[0], words_flw) 
    return ""


if __name__ == "__main__":

    try:
        a = sys.argv[1]
        try:
            words, letters = read_file(a)
            print("letter frequencies: \n")
            print_frequencies(count_frequencies(letters))

            print("\n number of words:", len(words))
            print("\n number of unique words:", len(unique_values(words)))

            print(print_most_common_words(words))
        except:
            print("this file does not exist!")
    except:
        print("Please provide a text file name")
        