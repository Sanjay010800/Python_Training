import re

test_string="H1 W0rld"
pattern=r'\d'
numbers=re.findall(pattern,test_string)
print(numbers)