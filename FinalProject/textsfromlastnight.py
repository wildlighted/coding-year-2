from requests_html import HTMLSession
import re
import os
import random
import markovify

def make_corpus(filename):
    session = HTMLSession()
    if not os.path.exists(os.getcwd() + '\\' + filename):
        with open (filename, 'w', encoding='utf-8') as f:
            r = session.get('http://www.textsfromlastnight.com/')
            for texts in r.html.find('div.text'):
                for text in texts.find('p'):
                    if text.text != "Send us your Text From Last Night!":
                        f.write(text.text+'\n')
            while r.html.next() != 'http://www.textsfromlastnight.com/Texts-From-Areacode-413.html':
                r = session.get(r.html.next())
                print(r.html)
                for texts in r.html.find('div.text'):
                    for text in texts.find('p'):
                        if text.text != "Send us your Text From Last Night!":
                            f.write(text.text+'\n')

def clean_corpus(filename, new_filename):
    with open (filename, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    with open (new_filename, 'w', encoding='utf-8') as f1:
        clean_text = re.sub('\(\d?-?\d{3}\):? ', '\n', raw_text)
        f1.write(clean_text)

def make_text(corpus):
    with open(corpus, 'r', encoding='utf-8') as f:
        text = f.read()
    text_model = markovify.NewlineText(text)
    return text_model.make_sentence(max_overlap_ratio=30)

def choose_text(corpus):
    with open(corpus, 'r', encoding='utf-8') as f:
        texts = f.readlines()
        return random.choice(texts)

#make_corpus('texts.txt')
#clean_corpus('texts.txt', 'clean.txt')