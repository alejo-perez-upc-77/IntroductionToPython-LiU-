#!/usr/bin/python

## some comments: 
#  we havent made that generating 2000 words would be similar to 500, 
#  as to make this it would require to generate frequencies of following words for every unique word, 
#  and in shakespeare.txt there are 30897 of them. 

import sys
import text_stats as ts
from random import choices
import time



def write_to_file(sentence, file_name):
    # Writing to file 
    with open(file_name, "w") as file1: 
        # Writing data to a file 
        file1.writelines(sentence)

def Convert(tup): 
    list1 = []
    list2 = []
    for a, b in tup: 
        list1.append(a) 
        list2.append(b)
    return list1, list2


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        starting_word = sys.argv[2]
        max_words = int(sys.argv[3])
        start = time.time()
    except:
        print("Please provide all arguments correctly")
    else:
        try:
            words, letters = ts.read_file(file_name)
        except:
            print("this file does not exist!")
        else:
            ordered_words  = Convert(ts.count_frequencies(words))[0]
            
            word_flw = ts.get_array_with_following_words(words)
            word_sequence = [starting_word]
            Stop = True
            i = 0
            new_word = starting_word
            word_dictionary = {}
            while (i<max_words) & Stop:
                if new_word in ordered_words:
                    if new_word in word_dictionary:
                        new_word = choices(word_dictionary[new_word][0],word_dictionary[new_word][1],k=1)[0]
                        word_sequence.append(new_word)
                    else:
                        following_words, weights  =  Convert(ts.get_most_common_following_words(new_word,word_flw))
                        word_dictionary[new_word] = (following_words, weights)

                        if len(following_words) != 0:
                            new_word = choices(following_words, weights, k=1)[0]
                            word_sequence.append(new_word)
                        else:
                            Stop = False
                else:
                    print(f"word {new_word} does not exist!")
                    Stop = False
                i+=1
            write_to_file(" ".join(word_sequence), "_".join(("new",file_name.split(".")[0])))
            end = time.time()
            print((end - start)/max_words)
            


        
