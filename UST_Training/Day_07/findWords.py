#find words starting with s

import re

def find_words(input_string):
    pattern=r'\bs\w*'
    word=re.findall(pattern,input_string,re.IGNORECASE)
    return word

#in
input_string="My name is Sanjay  sadan"
word=find_words(input_string)
print(word)