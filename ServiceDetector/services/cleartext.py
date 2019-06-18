from pymystem3 import Mystem
import nltk
from nltk.corpus import stopwords


class ClearText(object):
    def __init__(self):
        nltk.download('stopwords')
        self.mystopwords = stopwords.words('russian') + ['это', 'наш', 'тыс', 'млн', 'млрд', 'также',  'т', 'д']
        self.m = Mystem()
        self.mystoplemmas = ['который', 'прошлый', 'сей', 'свой', 'наш', 'мочь']
        self.cText = ''
        print('Clear text ready!!!')
        
    def remove_stopwords(self, text: str) -> str:
        try:
            return " ".join([token for token in text.split() if token not in self.mystopwords])
        except:
            return ""
        
    def lemmatize(self, text: str) -> str:
        try:
            return "".join(self.m.lemmatize(text)).strip()  
        except:
            return " "
        
    def remove_stoplemmas(self, text: str) -> str:
        try:
            return " ".join([token for token in text.split() if token not in self.mystoplemmas])
        except:
            return ""
        
    def clear_text(self, text: str) ->str:
        self.cText = self.remove_stopwords(text)
        print(self.cText)
        self.cText = self.lemmatize(self.cText)
        print(self.cText)
        self.cText = self.remove_stoplemmas(self.cText)
        print(self.cText)
        return self.cText
