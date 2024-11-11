#find date(yyyy-mm-dd) from string

import re

def find_words(input_string):
    pattern=r'\b(\d{2,4}[/-]\d{2}[/-]\d{2})\b'
    date1=re.findall(pattern,input_string,re.IGNORECASE)
    return date1

#in
input_string="I have work on 2024-02-03 and 2024/02/04 and 24-02-03"
date1=find_words(input_string)
print(date1)