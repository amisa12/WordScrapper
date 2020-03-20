import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable

words = []
word_count_type = {}


# Get the url from a user as input
url = str(input('Enter a url and press ENTER: '))

# Get content of the url
response = requests.get(url)


def get_tokens(url_response):
    """

    :param url_response:
    :return: a list of words from the url:
    """
    soup = BeautifulSoup(url_response.text, "html.parser")

    # Get all text
    all_text = soup.get_text()

    # Remove words that contain digit from the text
    text_only = ' '.join(s for s in all_text.split() if not any(c.isdigit() for c in s))

    print(text_only)
    # remove numbers
    text_no_num = re.sub(r'\d+', '', text_only)

    # Define a tokenizer
    tokenizer = RegexpTokenizer('\w+')

    # Get all token as specified in the regex from the soup
    tokens = tokenizer.tokenize(text_no_num)

    return tokens


returned_tokens = get_tokens(response)


# Create a word_count_type dictionary that consists of word as key and a list of value containing frequency and Type
def word_count_type_dict(tokens):
    """

    :param tokens:
    :end_result: creates a word_count_type dictionary
    """
    # Get word count frequency
    word_count = Counter(tokens)

    dict_word_count = dict(word_count)
    # Get word type
    words_type = nltk.pos_tag(tokens)
    dict_word_type = dict(words_type)

    for k in dict_word_count:
        word_count_type[k] = [dict_word_count[k], dict_word_type.get(k)]


word_count_type_dict(returned_tokens)


def print_table():
    """

    :return: a table of word, Type , Frequency
    """
    table = PrettyTable(['Word', 'Type', 'Frequency'])

    counter = 0

    for i in word_count_type:
        if counter > 100:
            break
        else:
            if word_count_type[i][1] == 'NN':
                type = 'Noun'
            elif word_count_type[i][1] == 'VBP':
                type = 'Verb'
            else:
                type = 'other'
            table.add_row([i, type, word_count_type[i][0]])
            counter += 1
    return table


print(print_table())

# Add lowercase tokens to word
for word in returned_tokens:
    words.append(word.lower())


def draw_graph():
    """
    Draw a graph of words against count
    """
    sns.set()

    # Create freq dist
    frequency_dist = nltk.FreqDist(words)

    # Plot the graph
    frequency_dist.plot(10)

    plt.show()


draw_graph()
