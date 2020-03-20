import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable

words = []


# Get the url from a user as input
url = str(input('Enter a url and press ENTER: '))

# Get content of the url
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Define a regex
defined_regex = '\w+'

# Get all token as specified in the regex from the soup
tokens = re.findall(defined_regex, soup.text)

# Get a list of all possible english words
english_words = set(nltk.corpus.words.words())

# Get word type
words_type = nltk.pos_tag(tokens)

table = PrettyTable(['Word', 'Type'])
for i in words_type:
    if i[1] == 'NN':
        type = 'Noun'
    elif i[1] == 'VBP':
        type == 'Verb'
    else:
        type == 'other'
    table.add_row([i[0], type])

print(table)
for word in tokens:
    if word in english_words:
        words.append(word.lower())

# Get word count
word_count = Counter(words)

# Get most common 100 words
most_common_100_words = word_count.most_common(100)
sns.set()

# Create freq dist
frequency_dist = nltk.FreqDist(words)

# Plot the graph
frequency_dist.plot(100)

plt.show()
