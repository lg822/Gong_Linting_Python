# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:13:20 2016

@author: lintinggong
"""
#Overall Commnet: Please refer to professor G's format, once you correct the format, I am more than happy to give back your
#                 grades. If you have problem with the format, please feel free to email me. For the content, your logic is
#                 effective and efficient, but there is still some details you need to pay attention.
'''
Q1:write a function translate()that takes a list of English words and
returns a list of Swedish words. 
'''
        
def dictionary(inputWord):
    dictionary={"merry":"god", "christmas":"jul", "and":"och", 
                 "happy":"gott", "new":"nytt", "year":"ar"}
#define what is in the dictionary 
#if word is not in the dictionary, return the original word
    if inputWord in dictionary:  
             return dictionary.get(inputWord)
    else:
             return inputWord

def translate(inputText):
#here we define the funtion translate in order to translate the words
# parameters: words in english 
        words = inputText.split( );
        #split word in here 
        new = " "#initialize new 
        for i in words:#every i in the words 
                new = new + dictionary(i) + " "
        #new = new plus the meaning in dictionary + " " 
        return new

translate("merry christmas and happy new year")
translate("merry christmas plus happy new year")

#Comment: There are some detail about the space you need to adjust. The output of the first example is ' god jul och gott nytt ar '
#         so that you can see there are unnecessary space in front and at the end of the string.
'''
Q2 "Write a function char_freq() that takes a string and builds a frequency
listing of the characters contained in it. Represent the frequency listing
as a Python dictionary. 
'''
def char_freq(String):
#def a function called char_freq
#space number and character look same in here 
    dictionary = {} #start off with an empty  dictionary
    for i in String:
    #for in loop : the item i in String 
        dictionary[i] = dictionary.get(i,0)+1
        # use dictionary.get(i,0) to look for the [i].
        #if it is not found returns 0.Have [i] add 1, if not return 0
    return dictionary    

char_freq("hhhhhuysekhdk")
char_freq("bababbbbbbchar")
char_freq("12345hhhhh")
char_freq("nn234 kgeod") 

'''
Q3 Your task in this exercise is to implement an
encoder/decoder of ROT-13.
'''
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}   
#This step it used to  built a dictionary(key step to translate the code )
def ROT_13(code): 
#Function:Define our decoder to transalte the text from the coded language into
#the English 
#Parameter: the characters are translated in the  key 
    newcode=''   # Initial a new code inhere 
    for i in code:   # We take every i (character) in the string separately
        if i in key:  
    #If else loop used in here: 2 situations  
    # When the character belongs to the dictionary(key)
            newcode+=key[i]   
    # Add and translate the characgter to newcode
        else:
            newcode+=i  
    # Otherwise directly add the character to newcode
    return newcode

ROT_13('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')        



'''
Q4  Define a simple "spelling correction" function correct()that takes a
   string and sees to it that 1) two or more occurrences of the space 
   character is compressed into one, and 2) inserts an extra space
   after a period if the period is directly followed by a letter.
'''
    
def correct(string):
# Define a correcting funtion to fix spacing issues
#inserts an extra space after a period if the period is directly followed 
#by a letter.
#parameter: the function will only affect the spaces
#return the correct sentence  
   import re
   #we use the import Regular expression operations to fix the mistake 
   correction = re.sub(' +',' ',string)
   #we remove the extra space from the input 
   finalcorrection = re.sub('\.','. ',correction)
   #insert a space after period
   print(finalcorrection)
#we then print the corrected sentence that combines both of the correcting
#definitions 
correct("This  is    very funny and cool.Indeed!")

'''
Q5  Define a function changing an infinitive verb to its third person singular 
form
'''
def make_3sg_form(verb):
# Define a funtion changes a verb and make it the third person singular form
#parameters: input needs to be an infinitive verb 
    if verb.endswith('y'): # if the verb ends in y
        newWord = verb[:-1]+'ies' #the output remove y and add ies
    elif verb.endswith(('o','ch','s','sh','x','z')):
        newWord = verb + 'es' # add es
    # if the verb ends in o ch s sh x z 
    else: # all other endings
        newWord = verb + 's' # add s
    return newWord 
    #return the new verb created using the above rules 
    
make_3sg_form('try')
make_3sg_form('brush')
make_3sg_form('run')
make_3sg_form('fix')

'''
Q7 Using the higher order function reduce(), write a function
max_in_list()that takes a list of numbers and returns the largest
one. 
'''

import functools 
# We import the tool so that we can use reduce 

def max_in_list(numbers):
#Define a funtion that takes a list of numbers and returns the largest
#of those numbers 
#parameters: a list of numbers   
   return functools.reduce(max, numbers) 
#when given the function max_in_list, 
#we want it to call the function reduce, 
#in which it reduces the list of numbers inputted to only the maximum one
max_in_list([3,10,8,9,12,5])
max_in_list([5,77,88,99,10000])

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
    #Common applications are to create a subsequence of those
    #elements that satisfy a certain condition.
    #we want get the return of the lengths in the words so we combine 
    #2 funtions in here . 

words = ["Hello", "word"]

list_comprehension(words)

'''
Q9 Write a function find_longest_word()that takes a list of words and
returns the length of the longest one. 
'''
def find_longest_word(string):
#deifne a function that will return the longest length 
#parameters: a list of characters 
    return max(list(map(len,string)))
#using the above len() to map the length of the list 
#of words into a list of integers, then using the max() function to find 
#greatest number

find_longest_word(['math', 'statistics', 'world'])

'''
Q10 Write a function filter_long_words()that takes a list of words and an
integer n and returns the list of words that are longer than n.
'''
def filter_long_words(words, n):
    Listwords=[] # A new empty list
    for i in range(len(words)):# the item in the words 
        if len(words[i])>n:#if the length of i is longer than n 
            Listwords.append(words[i])# add word[i]into the list              
    return Listwords# return the Listwords 
a=["hello","words","maxxxx"]

filter_long_words(a,7)

b=["car","bussss"]
filter_long_words(b,4)

'''
Q11 Use the higher order function map()to write
a function translate() that takes a list of English words and
returns a list of Swedish words. 
'''
lex_dic = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott",
           "new":"nytt", "year":"år"}
# define all the Swedish words as English words 
def translate(inputWords):
# Define a function to translate the input English words.
#parameters: input english words 
    return list(map(lambda x: lex_dic[x.lower()], inputWords))
    # map the English words to a list of Swedish words by the rules in the 
    # lex dictionary to the swidsh word 
translate(["merry", "christmas", "and", "happy", "new","year"])

'''
Q12 Question 12: Implement the higher order functions map(), filter() and 
reduce()
'''
def mapfunc(mapf,iterablemap):
#Define a function that does what the map function does 
#parameters: a function is given first for mapf, and then a string or list is given
     mapfunc = [] #initialize an empty set
     for i in iterablemap:# for each item in the iterablemap
        mapping = mapf(i) #mapping euqal the function to the iterable 
        mapfunc.append(mapping)
 #for each function applied to each element in iterable,
 #we add the solution to the list of final answers
     return mapfunc 
# return the final answer 

numbers = [1, 5, 3, 9, 10]
print(mapfunc(lambda x: x * 2, numbers))


def filterf(funcfilter,iterablefilter):

#Define a funtion that does what the filter function does
#parameter:a function is given in the first, and filter to the iterable    
     filterfunc = [] #initialize an empty set
     for j in iterablefilter: #for each item in the iterablefilter
        if funcfilter(j) == True: 
        # if the j is true under the function
           filterfunc.append (j)
        # add the item to the list of the answer
    
     return filterfunc 
     
numbers = [1, 5, 3, 9, 10]
print(filter(lambda x: x > 3, numbers))
     
     
def reducefct(funcreduce, sequencereduce, initial=None):
#Define a function that does waht reduce function does
#Parameters: function reduce, a string or listfor sequencereduce,
#the initial value is none
     
    ansreduce = initial if initial else sequencereduce[0] 
    #the answer is the initial value in the list given in sequencereduce
    for k in sequencereduce: 
    #for each element k in sequencereduce
        ansreduce = funcreduce(ansreduce, k)
    #the answer applies that element to the function and compares it to the previous answer (or 0 if there is no previous answer)
    return ansreduce 
    #the element that best fits the function after all iterations is kept and produced    
     
numbers = [1, 5, 3, 9, 10]
print(reducefct(lambda x, y: x + y, numbers))
