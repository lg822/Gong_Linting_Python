# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:33:35 2016

@author: lintinggong
"""
'''
Q2 "Write a function char_freq() that takes a string and builds a frequency
listing of the characters contained in it. Represent the frequency listing
as a Python dictionary. 
'''
def char_freq(String):
#def a function called char_freq
#space number and character looks same in here 
    dictionary = {} #start off with an empty  dictionary
    for i in String:
    #for in loop : the the item i in here loop 
        dictionary[i] = dictionary.get(i,0)+1
        # use dictionary.get(i,0) to look for the [i].
        #if it is not found returns0.Have [i] add 1, if not return 0
    return dictionary    

char_freq("hhhhhuysekhdk")
char_freq("bababbbbbbchar")
char_freq("12345hhhhh")
char_freq("nn234 kgeod")   
    
''' 
Q8 Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words. Write it in
three different ways: 1) using a for-loop, 2) using the higher order
function map(), and 3) using list comprehensions. 
'''

def map_list(words):
    lengths = [] #A new empty list
    for i in words:
        lengths.append(len(i))
        #use append in here,updates existing list 
        #Add a single member, at the end of the list
        #get the length of the words 
    return lengths

a  = ['hello','word']
map_list(a)
b=['wwwwhat','uuuuup']
map_list(b)



def map_Highorder(words):
    #words: list of words,
    #returns a list of integers - the lengths of the corresponding words
    return list(map(len, words))
    #map (map takes the first parameter and then an iterable containing 
    #data)we map lengthes of different words in here 
    #list() we use list fct. to covert the # lengths into the list.
words = ["Hello", "word"]

map_Highorder(words)



def list_comprehension(words):
    return [len(i) for i in words]
    #List comprehensions provide a concise way to create lists.
    #Common applications are tocreate a subsequence of those
    #elements that satisfy a certain condition.
    #we want get the return of the lengths in the words so we combine 
    #2 funtions in here . 

words = ["Hello", "word"]

list_comprehension(words)







   
    
