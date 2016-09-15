# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
Q1.Define a function max() that takes two numbers as arguments and returns 
the largest of them.Use the if-then-else construct available in Python.
"""
 
def print_max(a, b):
    #define a function called max that use two parameters called a and b.  
   # compare 3 situations:a>b;a=b;a<b and use if else  
    if(a > b):
        print (a, 'is maximum' )
    elif a == b :
        print (a, 'is equal to',b)
    else: 
        print (b, 'is maximun')
        
        
print_max (6, 7)
print_max (4, 40)

"""
Q2. Define a function max_of_three() that takes three numbers as arguments and 
returns the largest of them.
"""
#def a function called max_of_three that use 3 parameters 

def max_of_three (a,b,c):
    #The if statement is used to check a condition
    if a >= b:
    #compare a and b firstly
        if a >=c:
          print (a,'is maximum')
        else: 
          print (c, 'is maximum')
    else :   
   #compare a<=b
        if b >= c:
           print (b,'is maximum')
        else :
           print (c,'is maximum')
max_of_three (3,6,8)


"""
Q3. Define a function that computes the length of a given list or string.
"""
#define a funtion called length that have one parameter:sentence 
def length(sentence):
#return the numbers of the length of the parameter 
  count = 0 #initialize count 
  for i in sentence:
  #The for..in statement is another looping statement which iterates 
  #over a sequence of objects. i go through each item in a the 'sentence'.  
   count = count+1
   #for every i in the sentence plus 1 in the count 
  return count 
   #return count in here to get the count 
length ('hello')
length (' hello ')


"""
Q4.Write a function that takes a character (i.e. a string of length 1) and 
returns True if it is a vowel, False otherwise.
"""
def vowel(char):
    #define a funtion called vowel that have a parameter 
    if (char == "a" or char == "A" or
      char == "e" or char == "E" or              
      char == "i" or char == "I" or
      char == "o" or char == "O" or
      char == "u" or char == "U"):
      return "True"
      # if else loop in here:consider capital letter and lower case 
    else:
       return "False"

vowel('e')

 
"""
Q5. Write a function translate() that will translate a text into "rovarspraket" 
(Swedish for "robber's language").That is, double every consonant and place an 
occurrence of "o" in between.
"""
def translate(text):
#define a funtion called translate that takes one parameter 
  consonants = 'bcdfghjklmnpqrstvwxyz'  
  #define what is the consonants  
  a=''
  #declare a new empty variable a 
  for i in text:
  #i go through each item in a the 'text'.   
      if i in consonants:
          #if i in 'bcdfghjklmnpqrstvwxyz'
          a =  a + i +'o'+i
      else:
          #if i is not in consonants
          a = a + i
  return  a 
translate ('this is fun')

"""
Q6. Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of
numbers. 
"""
def sum(numbers):
#define a funtion called sum 
    totalSum = 0 #initialize totalSum  
    for i in numbers:
#go through each iteam in numbers (or list )
        totalSum = totalSum + i
#plus every number in  'numbers'       
    return totalSum
     
sum ([1,2,3,4,5])

def multiply(numbers):
#define a function called multiply 
    total = 1 #intialize totalSum (cannot be zero because of *) 
    for i in numbers:
        total = total * i 
#multiply every number in the 'numbers' 
    return total
 
multiply ([1,2,3,4,5])
  
"""
Q7.Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".
parameter: A string
Returns: the reverse of a string
I write 2 solutions  
"""
def reverse(string):
#define a function  
#get the length of the string and suntract 1
#we know that string are indexed from 0
    end_string = len(string)-1
    revS = '' #initialize the revserse string 
    for i in string:
    #start at the end of the string and work back to the beginning to build
    #the reverse string 
      revS = revS + string[end_string]
      end_string = end_string -1
    return revS
reverse('I am testing')



def reverse(str):   
    return str[::-1]
# [::-1] reverse the str from the first item to the last item  
#-1 go back
reverse('testing')  

a='I am testing'
reverse (a)

"""
Q8. Define a function is_palindrome() that recognizes palindromes .
"""
def is_palindrome(string=""):
    #string:any word with alphabetic characters 
    # also need to concern the "space"
    palindrome = False
    string = string.upper()#take care of mixed case by upper casing the word
    string = string.replace (" ","")#take care of spaces delete the space  
    if not string.isalpha():# return flase if there are any numbers
                            #in the word
       return palindrome   
    if reverse(string) == string:
        palindrome = True 
    
    return palindrome 
    
is_palindrome ('Radar')
is_palindrome ('R adar')
is_palindrome ('Radar raDAr')
is_palindrome ("")


"""
Q9. Write a function is_member() that takes a value (i.e. a number, string, etc) x 
and a list of values a, and returns True if x is a member of a, False otherwise. 
"""
def is_member(x,a):
#define a function called is_member that takes 2 parameters 
    for i in a:
 #for every item in a        
        if x ==  i:
#if x is  one member of i 
            return True
    return False 
is_member('a','aaa')

is_member('abc',['abc','dhskde'])

"""
Q10. Define a function overlapping()that takes two lists and returns True if
they have at least one member in common, False otherwise. 
"""
#define for i in the range of length of List 1 and list 2 
#if the element i in list  1 is equal to element in list 2
#then we will return true, otherwise return false.

def overlapping(List1, List2):
 #define a function that has 2 parameters 
    for i in range (len(List1)):
#i in the range of the length of list1:every item in List 1 
        for j in range (len(List2)):
            if List1[i]== List2[j]:
#the item in list1= the item in list2    
                return True 
    return False 
overlapping(['a','b','v','g'],['a','d','c','h'])
overlapping ([1,2,4,5],[2,6,7,8,9])



"""
Q11: Define a function generate_n_chars()that takes an integer nand a
character cand returns a string, ncharacters long, consisting only of
c:s.
"""
def generate_n_chars(n, char):
#def a function that has 2 parameters, n and char  
    outputstring='' #initialize the outputstring 
    for i in range(n):
# for in loop: i in the range of (number n)
        outputstring = outputstring + char 
#outputstring plus char (n times ) 
    return outputstring 
    
generate_n_chars(2 , 'g')
generate_n_chars(5,'ff')

"""
Q12: Define a procedure histogram()that takes a list of integers and prints
a histogram to the screen. 
"""
def histogram(numbers):
    for i in range(len(numbers)):
#i in the range of the length of numbers     
        print (numbers[i]*'*')
# i in the list of numbers multiply *
numbers = [3,4,9,7]
histogram(numbers)

a=[6,7,8,10,2]
histogram(a)

"""
Q13: Write a function max_in_list()that takes a list of numbers and
returns the largest one. 
"""

def max_in_list(List):
#def a function called max_in_list 
    max = 0 #initialize max 
    for n in List: #for loop 
        if n > max:  
            max = n
    return max
    
a=(2,3,4,5,6)
max_in_list(a)
b=(12,6,9,10000)
max_in_list(b)
                  
"""
Q14:Write a program that maps a list of words into a list of integers
representing the lengths of the correponding words.
""" 
def map_list(words):
    lengths = []    #A new empty list
    for i in range (len(words)):
       lengths.append (len(words[i]))
       #use append in here,updates existing list 
       #Add a single member, at the end of the list
    return lengths 
        
a  = ['hello','word']
map_list(a)
b=['wwwwhat','uuuuup']
map_list(b)

"""
Q15 Write a function find_longest_word()that takes a list of words and
returns the length of the longest one. 
"""
#import Q14 in to our question return the max number 
def find_longest_word(words):
#return the max of (mmap_list(words))   
    return max(map_list(words))
       
a=['hello','word']
find_longest_word(a)

"""
Q16 Write a function filter_long_words()that takes a list of words and an
integer n and returns the list of words that are longer than n.
"""
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










