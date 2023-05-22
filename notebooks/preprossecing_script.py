import numpy as np  # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re # regular expression
from langdetect import detect_langs # language detection
import nltk # natural language processing
from nltk.corpus import stopwords # stopwords
import matplotlib.pyplot as plt # visualization


def remove_english_language(text):
  pattern = r"[a-zA-Z\s]+"
  regex_pattern = re.compile(pattern)
  text = re.sub(regex_pattern," ",text)
  return text


def remove_numbers(text):
  pattern = r'\d+'
  regex_pattern = re.compile(pattern)
  text = re.sub(regex_pattern," ",text)
  return text

def remove_puncituation(text):
  pattern = r"[^\w\s]"
  regex_pattern = re.compile(pattern)
  text = re.sub(regex_pattern," ",text)
  return text


def remove_uderScore(text):
  pattern = r"_"
  regex_pattern = re.compile(pattern)
  text = re.sub(regex_pattern," ",text)
  return text


def remove_Tifinagh_characters(text): 
  ''' Tifinagh characters are used in Tamazight 
  like ⴰ ⴱ ⵛ ⴷ ⴹ ⴻ ⴼ ⴳ ⵀ ⵃ ⵉ ⵊ ⴽ ⵍ ⵎ ⵏ ⵓ ⵔ ⵕ ⵙ ⵜ ⵡ ⵅ ⵢ ⵣ ⵥ ⵄ ⵅ
  '''
  pattern = r'[\u2D30-\u2D7F]+'
  regex_pattern = re.compile(pattern)
  text = re.sub(regex_pattern," ",text)
  return text


def remove_additional_space(text):
  pattern = r"\s{2,}"
  regex_pattern = re.compile(pattern)
  text = re.sub(regex_pattern," ",text)
  return text

nltk.download('stopwords')
list_of_stop_words = stopwords.words('arabic')
type(list_of_stop_words)


modified_list_stop_words = []
for word in list_of_stop_words:
    pattern = re.compile(r'\b[إ,أ]')
    # replace the first letter of each word with a dash (-) using re.sub()
    new_word = re.sub(pattern, 'ا', word)
    modified_list_stop_words.append(new_word)
    
    
def remove_stop_words(text):
    '''
    This function removes stop words from a sentence
    args:
        text: a string of text
    '''
    # define the regex pattern to match words to remove
    pattern = re.compile(r'\b(' + '|'.join(modified_list_stop_words) + r')\b')
    # remove words from the sentence that appear in the words_to_remove list using re.sub()
    clean_sentence = re.sub(pattern, '', text)
    # print the resulting clean sentence
    return clean_sentence

def remove_repeated_characters(text):
    '''
    This function removes repeated characters from a sentence
    if a character is repeated more than twice
    
    args:
        text: a string of text
    '''
    pattern = r'(.)\1{2,}'
    regex_pattern = re.compile(pattern)
    text = re.sub(regex_pattern,r'\1',text)
    return text


def NFD(text):
    '''NFD stands for Normalization Form Decomposition
    using unicodedata.normalize() to normalize the text'''
    text = re.sub(r'[\u064B-\u0652]', "", text)
    return text


def all_cleaning(text):
    '''
    This function is used to clean the text
    
    '''
    text = remove_english_language(text)
    text = remove_puncituation(text)
    text = remove_numbers(text)
    text = remove_uderScore(text)
    text = remove_Tifinagh_characters(text)
    text = remove_stop_words(text)
    text = remove_additional_space(text)
    text = remove_repeated_characters(text)
    text = NFD(text)
    return text