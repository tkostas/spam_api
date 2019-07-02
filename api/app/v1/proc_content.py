import os
import string

import joblib
import nltk
import pandas as pd
from nltk import WordNetLemmatizer


class SpamModel:
    def __init__(self):
        self._wn = WordNetLemmatizer()
        self._en_stopwords = nltk.corpus.stopwords.words('english')
        full_path = os.path.join('app', 'pkl', 'spam_model_v1.joblib')
        self._model_v1 = joblib.load(full_path)
        self._text = ''

    def set_text(self, text):
        self._text = text

    def predict(self):
        clean_text = pd.Series(self._text).apply(self._clean_msg)
        resp = {"value": list(self._model_v1.predict(clean_text))}
        return resp

    def _clean_msg(self, msg):
        msg_no_punc = ''.join([c for c in msg if c not in string.punctuation])
        tokens = nltk.word_tokenize(msg_no_punc)
        tokens_non_stop = [tkn.lower() for tkn in tokens if tkn not in self._en_stopwords]
        lemmatized = []
        for word in tokens_non_stop:
            try:
                lemmatized.append(self._wn.lemmatize(word))
            except:
                lemmatized.append(word)
        return ' '.join(lemmatized)
