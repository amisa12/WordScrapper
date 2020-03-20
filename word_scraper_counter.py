import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import nltk
import matplotlib.pyplot as plt
import seaborn as sns

words = []
# Get the url from a user as input
url = str(input('Enter a url: '))

# Get content of the url
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

defined_regex = '\w+'

tokens = re.findall(defined_regex, soup.text)

print(nltk.pos_tag(soup))
# for word in tokens:
#     words.append(word.lower())
#
# sns.set()
#
# # Create freq dist and plot
# frequency_dist = nltk.FreqDist(words)
# frequency_dist.plot(100)
#
# plt.show()
# print(Counter(token))