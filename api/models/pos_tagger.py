"""
POS tagger. For now, it is simply a wrapper around NLTK's POS tagger
while I'm implementing my own.
"""

import nltk
import json

def _pos_tag(req_text):
    text = nltk.word_tokenize(req_text)
    return nltk.pos_tag(text)

def pos_tag_json(req_text):
    result_list = _pos_tag(req_text)
    rs = json.dumps(dict(result_list))
    return rs
