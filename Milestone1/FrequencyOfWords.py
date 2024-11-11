# Create a program to read a file which contains large set of some text file.
# Get the frequencies of all words in the file and finally show the frequencies
# for each word in a pandas dataframe.

import pandas as pd
import re
from collections import Counter


def Filter_words(data):
    # Function to filter words.
    return re.findall(r"\b[\w’-]+\b", data.lower())


def Count_words(data):
    #Function to get each word count."""
    return Counter(data)


try:
    with open("Cristiano.txt", "r", encoding="utf8") as file:
        file_content = file.read()
except FileNotFoundError:
    print("'Cristiano.txt' file not found.")

file_content = Filter_words(file_content)
word_frequencies = Count_words(file_content)

# Final dataframe
print(pd.DataFrame(list(word_frequencies.items()), columns=["Word", "Count"]))
      