#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
num_list =[0,1,3,5,7,8,9]
result = return_evens(num_list)


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
sentences = ["Hello", "I'm doing great", "Python is fun"]
exclamation_sentences = make_exclamation(sentences)