#####################################################
#####################################################
# Simple warmup problems to get started, no loops.

# Warmup-1 > sleep_in
"""
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
"""

#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True

#####
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False


#####################################################

# Warmup-1 > monkey_trouble
"""
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
"""

#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False

#####
def monkey_trouble(a_smile, b_smile):
  return (a_smile==True and b_smile==True) or (a_smile==False and b_smile==False)

# or

def monkey_trouble(a_smile, b_smile):
  if (a_smile==True and b_smile==True) or (a_smile==False and b_smile==False):
    return True
  else:
    return False


#####################################################

# Warmup-1 > sum_double
"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
"""

#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8

#####
def sum_double(a, b):
  if a==b:
    return 2*(a+b)
  else:
    return a+b


#####################################################

# Warmup-1 > diff21
"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
"""

#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

#####
def diff21(n):
  if n<=21:
    return abs(21-n)
  else:
    return 2*abs(n-21)


#####################################################

# Warmup-1 > parrot_trouble
"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
"""

#parrot_trouble(True, 6) → True
#parrot_trouble(True, 7) → False
#parrot_trouble(False, 6) → False

#####
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))
  # Need extra parenthesis around the or clause
  # since and binds more tightly than or.
  # and is like arithmetic *, or is like arithmetic +

# or

def parrot_trouble(talking, hour):
  return (talking==True and (hour<7 or hour>20))

# or

def parrot_trouble(talking, hour):
  if (talking==True and (hour < 7 or hour > 20)):
    return True
  else:
    return False


#####################################################

# Warmup-1 > makes10
"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
"""

#makes10(9, 10) → True
#makes10(9, 9) → False
#makes10(1, 9) → True

#####
def makes10(a, b):
  return ((a==10) or (b==10) or (a+b==10))


#####################################################

# Warmup-1 > near_hundred
"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
"""

#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False

#####
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

# or

def near_hundred(n):
  if (abs(100-n) <= 10) or (abs(200-n) <=10):
    return True
  else:
    return False


#####################################################

# Warmup-1 > pos_neg
"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
"""

#pos_neg(1, -1, False) → True
#pos_neg(-1, 1, False) → True
#pos_neg(-4, -5, True) → True

#####
def pos_neg(a, b, negative):
  if negative:
    return (a<0 and b<0)
  else:
    return ((a<0 and b>0) or (a>0 and b<0))
       
    
#####################################################

# Warmup-1 > not_string
"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
"""

#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'

#####
def not_string(str):
  #if split(str)[0]!='not':
  #  return 'not '+str
  #else:
  #  return str
  if str[0:3] != 'not':
    return 'not '+str
  else:
    return str


#####################################################

# Warmup-1 > missing_char
"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
"""

#missing_char('kitten', 1) → 'ktten'
#missing_char('kitten', 0) → 'itten'
#missing_char('kitten', 4) → 'kittn'

#####
def missing_char(str, n):
  return str[0:n] + str[n+1:]


#####################################################

# Warmup-1 > front_back
"""
Given a string, return a new string where the first and last chars have been exchanged.
"""

#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'

#####
def front_back(str):
  #if len(str) == 2:
    #return str[-1] + str[0]
  if len(str) > 1:  
    return str[-1] + str[1:-1] + str[0]
  else:
    return str

# or 

def front_back(str):
  if len(str) <= 1:
    return str
  mid = str[1:len(str)-1]  # str[1:-1]
  # last + mid + first
  return str[len(str)-1] + mid + str[0]


#####################################################

# Warmup-1 > front3
"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
"""

#front3('Java') → 'JavJavJav'
#front3('Chocolate') → 'ChoChoCho'
#front3('abc') → 'abcabcabc'

#####
def front3(str):
  if len(str) < 3:
    return 3*str
  else:
    return 3*str[0:3]


#####################################################
#####################################################
# Medium warmup string/list problems with loops.

# Warmup-2 > string_times
"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
"""

#string_times('Hi', 2) → 'HiHi'
#string_times('Hi', 3) → 'HiHiHi'
#string_times('Hi', 1) → 'Hi'

#####
def string_times(str, n):
  return n*str


#####################################################

# Warmup-2 > front_times
"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
"""

#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc'

#####
def front_times(str, n):
  if len(str) < 3:
    return n*str
  else:
    return n*str[:3]


#####################################################

# Warmup-2 > string_bits
"""
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
"""

#string_bits('Hello') → 'Hlo'
#string_bits('Hi') → 'H'
#string_bits('Heeololeo') → 'Hello'

#####
def string_bits(str):
  result = ""
  # Many ways to do this. This uses the standard loop of i on every char,
  # and inside the loop skips the odd index values.
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result


#####################################################

# Warmup-2 > string_splosion
"""
Given a non-empty string like "Code" return a string like "CCoCodCode".
"""

#string_splosion('Code') → 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'

#####
def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result


#####################################################

# Warmup-2 > last2
"""
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
"""

#last2('hixxhi') → 1
#last2('xaxxaxaxx') → 1
#last2('axxxaaxx') → 2

#####
def last2(str):
  # Avoid too short strings
  if len(str) < 2:
    return 0
  # last 2 chars (ie, str[len(str)-2:] )
  last2 = str[-2:]
  count = 0
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1
  return count


#####################################################

# Warmup-2 > array_count9
"""
Given an array of ints, return the number of 9's in the array.
"""

#array_count9([1, 2, 9]) → 1
#array_count9([1, 9, 9]) → 2
#array_count9([1, 9, 9, 3, 9]) → 3

#####
def array_count9(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count += 1
  return count
  
# or
 
def array_count9(nums):
  count = 0
  # Check each value
  for num in nums:
    if num == 9:
      count = count + 1
  return count


#####################################################

# Warmup-2 > array_front9
"""
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
"""

#array_front9([1, 2, 9, 3, 4]) → True
#array_front9([1, 2, 3, 4, 9]) → False
#array_front9([1, 2, 3, 4, 5]) → False

#####
def array_front9(nums):
  first4 = nums[0:4]
  for i in range(len(first4)):
    if nums[i] == 9:
      return True
  return False

# or

def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4  
  for i in range(end):  # loop over [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False
  
  
#####################################################

# Warmup-2 > array123
"""
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
"""

#array123([1, 1, 2, 3, 1]) → True
#array123([1, 1, 2, 4, 1]) → False
#array123([1, 1, 2, 1, 2, 3]) → True

#####
def array123(nums):
  seq123 = [1, 2, 3]
  for i in range(len(nums)-2):
    sub = nums[i:i+3]
    if sub == seq123:
      return True
  return False    
  
  
#####################################################

# Warmup-2 > string_match
"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
"""

#string_match('xxcaazz', 'xxbaaz') → 3
#string_match('abc', 'abc') → 2
#string_match('abc', 'axc') → 0

#####
def string_match(a, b):
  a_len = len(a)
  b_len = len(b)
  shorter = min(a_len, b_len)
  count = 0
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1
  return count      

# or

def string_match(a, b):
  # Check which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  # Loop i over every substring starting spot.
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count += 1
  return count


#####################################################
#####################################################
# Basic python string problems -- no loops. Use + to combine strings, len(str) is the number of chars in a String, str[i:j] extracts the substring starting at index i and running up to but not including index j.

# String-1 > hello_name
"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
"""

#hello_name('Bob') → 'Hello Bob!'
#hello_name('Alice') → 'Hello Alice!'
#hello_name('X') → 'Hello X!'

#####
def hello_name(name):
  return 'Hello '+name+'!'


#####################################################

# String-1 > make_abba
"""
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
"""

#make_abba('Hi', 'Bye') → 'HiByeByeHi'
#make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
#make_abba('What', 'Up') → 'WhatUpUpWhat'

#####
def make_abba(a, b):
  return a+b+b+a


#####################################################

# String-1 > make_tags
"""
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
"""

#make_tags('i', 'Yay') → '<i>Yay</i>'
#make_tags('i', 'Hello') → '<i>Hello</i>'
#make_tags('cite', 'Yay') → '<cite>Yay</cite>'

#####
def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>' 
  
  
#####################################################  

# String-1 > make_out_word
"""
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
"""

#make_out_word('<<>>', 'Yay') → '<<Yay>>'
#make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
#make_out_word('[[]]', 'word') → '[[word]]'

#####
def make_out_word(out, word):
  return out[0:2]+word+out[-2:]


#####################################################

# String-1 > extra_end
"""
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
"""

#extra_end('Hello') → 'lololo'
#extra_end('ab') → 'ababab'
#extra_end('Hi') → 'HiHiHi'

#####
def extra_end(str):
  last2 = str[-2:]
  return 3*last2


#####################################################

# String-1 > first_two
"""
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
"""

#first_two('Hello') → 'He'
#first_two('abcdefg') → 'ab'
#first_two('ab') → 'ab'

#####
def first_two(str):
  if str >=2:
    return str[0:2]
  else:
    return str


#####################################################

# String-1 > first_half
"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
"""

#first_half('WooHoo') → 'Woo'
#first_half('HelloThere') → 'Hello'
#first_half('abcdef') → 'abc'

#####
def first_half(str):
  half_len = int(len(str)/2)
  return str[0:half_len]


#####################################################

# String-1 > without_end
"""
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
"""

#without_end('Hello') → 'ell'
#without_end('java') → 'av'
#without_end('coding') → 'odin'

#####
def without_end(str):
  return str[1:-1]


#####################################################

# String-1 > combo_string
"""
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
"""

#combo_string('Hello', 'hi') → 'hiHellohi'
#combo_string('hi', 'Hello') → 'hiHellohi'
#combo_string('aaa', 'b') → 'baaab'

#####
def combo_string(a, b):
  str_sho = min(a, b, key=len)	# min(str1, str2, key=len)
  str_lon = max(a, b, key=len)
  return str_sho+str_lon+str_sho


#####################################################

# String-1 > non_start
"""
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
"""

#non_start('Hello', 'There') → 'ellohere'
#non_start('java', 'code') → 'avaode'
#non_start('shotl', 'java') → 'hotlava'

#####
def non_start(a, b):
  return a[1:]+b[1:]


#####################################################

# String-1 > left2
"""
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
"""

#left2('Hello') → 'lloHe'
#left2('java') → 'vaja'
#left2('Hi') → 'Hi'

#####
def left2(str):
  if len(str) > 2:
    return str[2:]+str[0:2]
  else:
    return str
       

#####################################################
#####################################################
# Basic python list problems -- no loops.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.

# List-1 > first_last6
"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
"""

#first_last6([1, 2, 6]) → True
#first_last6([6, 1, 2, 3]) → True
#first_last6([13, 6, 1, 2, 3]) → False

#####
def first_last6(nums):
  if (nums[0]==6 or nums[-1]==6):	# nums[len(nums) - 1].
    return True
  else:
    return False


#####################################################

# List-1 > same_first_last
"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
"""

#same_first_last([1, 2, 3]) → False
#same_first_last([1, 2, 3, 1]) → True
#same_first_last([1, 2, 1]) → True

#####
def same_first_last(nums):
  if (len(nums) >= 1) and (nums[0]==nums[-1]):
    return True
  else:
    return False
       

#####################################################

# List-1 > make_pi
"""
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
"""
#make_pi() → [3, 1, 4]

#####
def make_pi():
  return ([3, 1, 4])


#####################################################

# List-1 > common_end
"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
"""

#common_end([1, 2, 3], [7, 3]) → True
#common_end([1, 2, 3], [7, 3, 2]) → False
#common_end([1, 2, 3], [1, 3]) → True

#####
def common_end(a, b):
  return ((a[0]==b[0]) or (a[-1]==b[-1]))


#####################################################

# List-1 > sum3
"""
Given an array of ints length 3, return the sum of all the elements.
"""

#sum3([1, 2, 3]) → 6
#sum3([5, 11, 2]) → 18
#sum3([7, 0, 0]) → 7

#####
def sum3(nums):
  return sum(nums)


#####################################################

# List-1 > rotate_left3
"""
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
"""

#rotate_left3([1, 2, 3]) → [2, 3, 1]
#rotate_left3([5, 11, 9]) → [11, 9, 5]
#rotate_left3([7, 0, 0]) → [0, 0, 7]

#####
def rotate_left3(nums):
  return ([nums[1], nums[2], nums[0]]) 
  

#####################################################

# List-1 > reverse3
"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
"""

#reverse3([1, 2, 3]) → [3, 2, 1]
#reverse3([5, 11, 9]) → [9, 11, 5]
#reverse3([7, 0, 0]) → [0, 0, 7]

#####
def reverse3(nums):
  return nums[::-1]	# with slicing


#####################################################

# List-1 > max_end3
"""
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
"""

#max_end3([1, 2, 3]) → [3, 3, 3]
#max_end3([11, 5, 9]) → [11, 11, 11]
#max_end3([2, 11, 3]) → [3, 3, 3]

#####
def max_end3(nums):
  nums_hi = max(nums[0], nums[-1])
  return ([nums_hi, nums_hi, nums_hi])


#####################################################

# List-1 > sum2
"""
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
"""

#sum2([1, 2, 3]) → 3
#sum2([1, 1]) → 2
#sum2([1, 1, 1, 1]) → 2

#####
def sum2(nums):
  if len(nums) < 2:
    return sum(nums)
  else:  
    return sum(nums[0:2])


#####################################################

# List-1 > middle_way
"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
"""

#middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
#middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
#middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

#####
def middle_way(a, b):
  return ([a[1], b[1]])


#####################################################

# List-1 > make_ends
"""
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
"""

#make_ends([1, 2, 3]) → [1, 3]
#make_ends([1, 2, 3, 4]) → [1, 4]
#make_ends([7, 4, 6, 2]) → [7, 2]

#####
def make_ends(nums):
  return ([nums[0], nums[-1]])


#####################################################

# List-1 > has23
"""
Given an int array length 2, return True if it contains a 2 or a 3.
"""
#has23([2, 5]) → True
#has23([4, 3]) → True
#has23([4, 5]) → False

#####
def has23(nums):
  return ((nums[0]==2) or (nums[0]==3) or (nums[1]==2) or (nums[1]==3))


#####################################################
#####################################################
# Basic boolean logic puzzles -- if else and or not

# Logic-1 > cigar_party
"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
"""

#cigar_party(30, False) → False
#cigar_party(50, False) → True
#cigar_party(70, True) → True

#####
def cigar_party(cigars, is_weekend):
  if is_weekend == False:
    return ((cigars >= 40) and (cigars <= 60))
  if is_weekend == True:
    return (cigars >= 40)
  else:
    False

# or

def cigar_party(cigars, is_weekend):
    if ( (is_weekend and cigars >= 40) or (cigars >= 40 and cigars <= 60) ):
        return True
    return False


#####################################################

# Logic-1 > date_fashion
"""
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
"""

#date_fashion(5, 10) → 2
#date_fashion(5, 2) → 0
#date_fashion(5, 5) → 1

#####
def date_fashion(you, date):
  no = 0
  maybe = 1
  yes = 2
  if (you <=2) or (date<=2):     
    return no
  if (you >=8) or (date>=8): 
    return yes
  else:
    return maybe


#####################################################

# Logic-1 > squirrel_play
"""
The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
"""

#squirrel_play(70, False) → True
#squirrel_play(95, False) → False
#squirrel_play(95, True) → True

#####
def squirrel_play(temp, is_summer):
  if is_summer == False: 
    return ((temp >= 60) and (temp <= 90))
  if is_summer == True:
    return ((temp >= 60) and (temp <= 100))
  else:
    return False
       
    
#####################################################    

# Logic-1 > caught_speeding
"""
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
"""

#caught_speeding(60, False) → 0
#caught_speeding(65, False) → 1
#caught_speeding(65, True) → 0

#####
def caught_speeding(speed, is_birthday):
  no_ticket = 0
  small_ticket = 1
  big_ticket = 2
  if is_birthday == False:
    if speed <= 60:
      return no_ticket
    if (speed >= 61) and (speed <=80):
      return small_ticket
    if speed >= 81:
      return big_ticket
  if is_birthday == True:
    if speed <= 65:
      return no_ticket
    if (speed >= 66) and (speed <=85):
      return small_ticket
    if speed >= 86:
      return big_ticket
    

#####################################################

# Logic-1 > sorta_sum
"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
"""

#sorta_sum(3, 4) → 7
#sorta_sum(9, 4) → 20
#sorta_sum(10, 11) → 21

#####
def sorta_sum(a, b):
  ab_sum = a + b				# not sum(a, b), these are ints
  if (ab_sum >= 10) and (ab_sum <= 19):
    return 20
  else:
    return a + b


#####################################################

# Logic-1 > alarm_clock
"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
"""

#alarm_clock(1, False) → '7:00'
#alarm_clock(5, False) → '7:00'
#alarm_clock(0, False) → '10:00'

#####
def alarm_clock(day, vacation):
  #Sun = 0
  #Mon = 1
  #Tue = 2
  #Wed = 3
  #Thu = 4
  #Fri = 5
  #Sat = 6
  if vacation == False:
    if day >=1 and day <= 5:
      return '7:00'
    if (day == 0) or (day == 6):
      return '10:00'
  if vacation == True:
    if day >=1 and day <= 5:
      return '10:00'
    if (day == 0) or (day == 6):
      return 'off'
      

#####################################################

# Logic-1 > love6
"""
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
"""

#love6(6, 4) → True
#love6(4, 5) → False
#love6(1, 5) → True

#####
def love6(a, b):
  return ((a==6) or (b==6) or ((a+b)==6) or ((a-b)==6) or ((b-a)==6))


#####################################################

# Logic-1 > in1to10
"""
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
"""

#in1to10(5, False) → True
#in1to10(11, False) → False
#in1to10(11, True) → True

#####
def in1to10(n, outside_mode):
  if outside_mode == False:
    if (n >= 1) and (n <= 10):
      return True
    else:
      return False
  if outside_mode == True:
    if (n <= 1) or (n >= 10):
      return True
    else:
      return False
  

#####################################################

# Logic-1 > near_ten
"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
"""

#near_ten(12) → True
#near_ten(17) → False
#near_ten(19) → True

#####
def near_ten(num):
  remain = num % 10
  return ((remain <= 2) or (remain >= 8))


#####################################################
#####################################################
# Medium python string problems -- 1 loop.. Use + to combine strings, len(str) is the number of chars in a String, str[i:j] extracts the substring starting at index i and running up to but not including index j.

# String-2 > double_char
"""
Given a string, return a string where for every char in the original, there are two chars.
"""

#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'

#####
def double_char(str):
  double = ""
  for i in range(len(str)):
    double = double + 2*str[i]
  return double


#####################################################

# String-2 > count_hi
"""
Return the number of times that the string "hi" appears anywhere in the given string.
"""

#count_hi('abc hi ho') → 1
#count_hi('ABChi hi') → 2
#count_hi('hihi') → 2

#####
def count_hi(str):
  count = 0
  for i in range(len(str)): 
    sub = str[i:i+2]
    if sub == 'hi':
      count = count + 1
  return count   
  
  
#####################################################

# String-2 > cat_dog
"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""

#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True

#####
def cat_dog(str):
  count_cat = 0
  count_dog = 0
  if len(str) >=3: 
    for i in range(len(str)):
      sub = str[i:i+3]
      if sub == 'cat':
        count_cat = count_cat + 1
      if sub == 'dog':
        count_dog = count_dog + 1
  if count_cat == count_dog:		
    return True   
  else:
    return False
    

#####################################################

# String-2 > count_code
"""
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
"""

#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2

#####
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    subCO = str[i:i+2]
    subE = str[i+3]
    if (subCO == 'co') and (subE == 'e'):	# wildcards ? or . were not working (sub == 'co?e')
      count = count + 1
  return count
 

#####################################################

# String-2 > end_other
"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
"""

#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True

#####
def end_other(a, b):
  if len(a) != len(b):
    str_sho = min(a, b, key=len)
    str_lon = max(a, b, key=len)
    sub = str_lon[-len(str_sho):]
    if sub.lower() == str_sho.lower():
      return True
    else:
      return False      
  if (len(a) == len(b)) and (a ==b):
    return True
  else:
    return False


#####################################################

# String-2 > xyz_there
"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
"""

#xyz_there('abcxyz') → True
#xyz_there('abc.xyz') → False
#xyz_there('xyz.abc') → True

#####
def xyz_there(str):
  if str[0:3] == 'xyz':
    return True
  if len(str) >= 4:
    for i in range(len(str)-3):
      sub = str[i+1:i+4] # 'xyz'
      subDot = str[i]
      if (sub == 'xyz') and (subDot+sub != '.xyz'):
        return True
    else:
      return False
  else:
    return False


#####################################################
#####################################################
# Medium python list problems -- 1 loop.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.

# List-2 > count_evens
"""
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
"""
#count_evens([2, 1, 2, 3, 4]) → 3
#count_evens([2, 2, 0]) → 3
#count_evens([1, 3, 5]) → 0

#####
def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    remain = nums[i] % 2
    if remain == 0:
      count += 1
  return count
   
 
#####################################################

# List-2 > big_diff
"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
"""

#big_diff([10, 3, 5, 6]) → 7
#big_diff([7, 2, 10, 9]) → 8
#big_diff([2, 10, 7, 2]) → 8

#####
def big_diff(nums):
  nums_min = min(nums)
  nums_max = max(nums)
  if nums_min != nums_max:
    return nums_max - nums_min
  else:
    return 0
    
       
#####################################################   

# List-2 > centered_average
"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
"""

#centered_average([1, 2, 3, 4, 100]) → 3
#centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
#centered_average([-10, -4, -2, -4, -2, 0]) → -3

#####
def centered_average(nums):
  nums_len = len(nums) 
  nums_min = min(nums) 
  nums_max = max(nums) 
  total = sum(nums) 
  return (total - nums_min - nums_max) / (nums_len-2)


#####################################################

# List-2 > sum13
"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""

#sum13([1, 2, 2, 1]) → 6
#sum13([1, 1]) → 2
#sum13([1, 2, 2, 1, 13]) → 6

#####				
def sum13(nums):
  if len(nums) == 0:
    return 0
  else:
    tot = 0
    for i in range(len(nums)):
      n = nums[i]
      if n == 13:
        tot = tot
        if (i != (len(nums) - 1)) and (nums[i+1] != 13):
          tot = tot - nums[i+1] 
      else:
        tot += n
    return tot  
    

#####################################################

# List-2 > sum67
"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
"""

#sum67([1, 2, 2]) → 5
#sum67([1, 2, 2, 6, 99, 99, 7]) → 5
#sum67([1, 1, 6, 7, 2]) → 4

#####                                       
def sum67(nums):
  while 6 in nums: 
    print('nums.index(6): ', nums.index(6))
    print('nums.index(7): ', nums.index(7))
    print('nums.index(7, nums.index(6)) + 1: ',  nums.index(7, nums.index(6)) + 1)
    del nums[nums.index(6) : nums.index(7, nums.index(6)) + 1]
  return sum(nums)

sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])	# 2

# or

def sum67(nums):
    tot_sum = 0
    skip_flag = False
    for number in nums:
        if number == 6:
            skip_flag = True 
            continue # skip this iter
        if number == 7 and skip_flag == True:
            skip_flag = False # sum afterwards
            continue 
        if skip_flag == False:
            tot_sum += number 
    return tot_sum

sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])	# 2


#####################################################

# List-2 > has22
"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
"""

#has22([1, 2, 2]) → True
#has22([1, 2, 1, 2]) → False
#has22([2, 1, 2]) → False

#####
def has22(nums):
  for i in range(len(nums)):
    n = nums[i]
    if (n == 2) and (i != (len(nums) - 1)) and (nums[i+1] == 2):
      return True
  else:
    return False


#####################################################
#####################################################
# Medium boolean logic puzzles -- if else and or not

# Logic-2 > make_bricks
"""
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
"""

#make_bricks(3, 1, 8) → True
#make_bricks(3, 1, 9) → False
#make_bricks(3, 2, 10) → True

#####					
def make_bricks(small, big, goal):
  u_small = small * 1
  u_big = big * 5
  return ((goal % 5) <= u_small and (goal - u_big) <= u_small) 

# Most elegant and shortest solution. Code returns False when the two conditions are not True. 
# Left-hand condition: remainder of (goal % 5) needs to be less than or equal to small bricks 
# in order to have enough small bricks to cover less than 5 inches after we laid big bricks. 
# Right-hand condition: Goal minus all the big bricks needs to be less than or equal to small 
# bricks, again, that covers the scenario of not enough big and small bricks to meet the goal, 
# plus, this also covers the case when we can use only small bricks.


#####################################################

# Logic-2 > lone_sum
"""
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
"""

#lone_sum(1, 2, 3) → 6
#lone_sum(3, 2, 3) → 2
#lone_sum(3, 3, 3) → 0

#####
def lone_sum(a, b, c):
  sum = 0
  if (a == b) and (a == c):
    sum = sum
  if (a == b) and (a != c):
    sum = c
  if (b == c) and (b != a):  
    sum = a
  if (c == a) and (c != b): 
    sum = b
  if (a != b) and (b != c) and (c != a):
    sum = a + b + c
  return sum  
  
   
#####################################################

# Logic-2 > lucky_sum
"""
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
"""

#lucky_sum(1, 2, 3) → 6
#lucky_sum(1, 2, 13) → 3
#lucky_sum(1, 13, 3) → 1

#####					
def lucky_sum(a, b, c):
  tot = 0
  if a != 13:
    tot = a
  if a != 13 and b != 13:
    tot += b
  if a != 13 and b != 13 and c != 13:  
    tot += c
  else:
    tot = tot
  return tot 

# or

def lucky_sum(a, b, c):
  tot = 0
  for n in (a, b, c):
    if n != 13:
      tot += n	
    else:
       break
  return tot


#####################################################

# Logic-2 > no_teen_sum
"""
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
"""

#no_teen_sum(1, 2, 3) → 6
#no_teen_sum(2, 13, 1) → 3
#no_teen_sum(2, 1, 14) → 3

#####
def fix_teen(n):
  if n==13 or n==14 or n==17 or n==18 or n==19: 
    return 0
  else:
    return n

def no_teen_sum(a, b, c):
  tot = sum([fix_teen(a), fix_teen(b), fix_teen(c)])
  return tot
  

#####################################################

# Logic-2 > round_sum
"""
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().
"""

#round_sum(16, 17, 18) → 60
#round_sum(12, 13, 14) → 30
#round_sum(6, 4, 4) → 10

#####
def round10(num):
  roundNum = round(num, -1)
  return roundNum

def round_sum(a, b, c):
  roundSum = int(round10(a) + round10(b) + round10(c))  
  return roundSum


#####################################################

# Logic-2 > close_far
"""
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
"""

#close_far(1, 2, 10) → True
#close_far(1, 2, 3) → False
#close_far(4, 1, 3) → True

#####
def close_far(a, b, c):
  abDiff = abs(a - b)
  acDiff = abs(a - c)
  bcDiff = abs(b - c)
  return ( (abDiff <= 1 and acDiff >= 2 and bcDiff >= 2) or (abDiff >= 2 and bcDiff >= 2 and acDiff <= 1) )


#####################################################

# Logic-2 > make_chocolate
"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.
"""

#make_chocolate(4, 1, 9) → 4
#make_chocolate(4, 1, 10) → -1
#make_chocolate(4, 1, 7) → 2

#####
def make_chocolate(small, big, goal):
  u_small = small * 1
  u_big = big * 5
  if goal - u_big <= u_small and goal - u_big >= 0:
    return goal - u_big
  if goal - (u_big-5) <= u_small and goal - (u_big-5) >= 0:
    return goal - (u_big-5) 
  if goal - (u_big-10) <= u_small and goal - (u_big-10) >= 0:
    return goal - (u_big-10) 
  if goal - (u_big-15) <= u_small and goal - (u_big-15) >= 0:
    return goal - (u_big-15) 
  # Could be more compact, but 4 "iterations" are sufficient based on tests 
  else:
    return -1


#####################################################
#####################################################
# + 1 problem (not on CodingBat)

# "FizzBuzz"
"""
Iterate the integers from 1 to 70. For multiples of 3 print "Fizz" instead of the number and for the multiples of 5 print "Buzz". For numbers which are multiples of both 3 and 5 print "FizzBuzz".
"""

#####
for n in range(1, 71):
  if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz') 
    continue 
  if n % 3 == 0:
    print('Fizz')   
    continue
  if n % 5 == 0:
    print('Buzz')
    continue
  print(n)  
  
# or  
  
for n in range(1, 71):
  if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')    
    continue    
  elif n % 3 == 0:  
    print('Fizz')       
    continue
  elif n % 5 == 0:  
    print('Buzz')
    continue
  print(n)      
  
  
#####################################################
# + 2 problem (not on CodingBat)

"""
Returns every nth element of a list:
"""

#####
lis = list(range(20))   
nth = 3

print( lis[nth-1 : : nth] )  
  
  
